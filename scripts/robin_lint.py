#!/usr/bin/env python3
"""
robin_lint.py — PAD 貼付前チェッカー兼 静的レビュー（エージェント環境用）

使い方:
  python3 robin_lint.py flow.robin [--kb PAD_Robin_ActionKB.json] [--json] [--no-advice]
  KB が無ければ構文規則だけ。KB があれば ID・引数・enum・ON ERROR も検査する。

出力の重み:
  FATAL  貼付全体が無言で捨てられる違反（robin-rules.md の silent）
  ERROR  貼れるが行にエラーが付く／クラウド起動で拒否される違反
  WARN   貼れるが意図と違う値になる、または未確認
  ADVICE 開発原則（03-principles.md）に照らした改善提案（ループ内の WAIT/SET、まとめられる処理 など）
終了コード: 0=なし, 1=WARN/ADVICE のみ, 2=FATAL/ERROR あり
規則は knowledge/robin-rules.md（JoeG592/pad-robin-action-kb, CC BY 4.0）に基づく。
"""
import sys, re, json, pathlib

KEYWORDS = {"from","to","step","end","in","then","if","else","loop","foreach","while","set","wait",
            "next","exit","label","goto","call","case","default","switch","block","error","on","not",
            "and","or","mod","true","false","global","disable","function","throw"}
HANDLER_OK = ("SET ", "CALL ", "GOTO ", "THROW ERROR")
ID_RE = re.compile(r"([A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+)")
ARG_RE = re.compile(r"(?<![\w.])([A-Za-z][A-Za-z0-9]*):(?!:)\s")
OUT_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9]*)=>\s*([^\W\d_][\w]*)")
ENUM_RE = re.compile(r"(?<![\w.$'])([A-Za-z][A-Za-z0-9]*)\.([A-Za-z][A-Za-z0-9]*)\.([A-Za-z0-9]+)(?![\w.(])")
IDENT = r"[^\W\d_][\w]*"

class Issue:
    def __init__(self, sev, line, rule, msg):
        self.sev, self.line, self.rule, self.msg = sev, line, rule, msg
    def __str__(self):
        return f"{self.sev:6} L{self.line:<4} [{self.rule}] {self.msg}"

def load_kb(path):
    if not path: return None
    d = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    return {r["actionId"].lower(): r for r in d["actions"]}

def split_statements(text):
    """行に分割。$'''...''' と /# ... #/ の中の改行は同じ文に属する。"""
    out, cur, cur_start = [], [], 1
    in_str = in_cmt = False
    for ln_no, ln in enumerate(text.split("\n"), 1):
        if not cur: cur_start = ln_no
        cur.append(ln)
        j = 0
        while True:
            if in_cmt:
                k = ln.find("#/", j)
                if k < 0: break
                in_cmt = False; j = k + 2; continue
            if not in_str:
                k1 = ln.find("$'''", j); k2 = ln.find("/#", j)
                if k2 >= 0 and (k1 < 0 or k2 < k1) and ln[:k2].strip() == "":
                    in_cmt = True; j = k2 + 2; continue
                if k1 < 0: break
                in_str = True; j = k1 + 4
            else:
                k = ln.find("'''", j)
                if k < 0: break
                in_str = False; j = k + 3
        if not in_str and not in_cmt:
            out.append((cur_start, "\n".join(cur))); cur = []
    if cur: out.append((cur_start, "\n".join(cur)))
    return out

def strings_and_code(stmt):
    parts, i = [], 0
    while True:
        k = stmt.find("$'''", i)
        if k < 0:
            parts.append(("code", stmt[i:])); break
        parts.append(("code", stmt[i:k]))
        e = stmt.find("'''", k + 4)
        if e < 0:
            parts.append(("str", stmt[k+4:])); parts.append(("unterminated", "")); break
        parts.append(("str", stmt[k+4:e])); i = e + 3
    return parts

def find_expr_end(s, j):
    n = len(s); q = False
    while j < n:
        c = s[j]
        if c == "'": q = not q
        elif c == "%" and not q: return j
        j += 1
    return -1

def check_string(s, line, issues, exprs):
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            if i + 1 < n and s[i+1] == "%":
                issues.append(Issue("WARN", line, "S7", r"文字列内の \% は % が消える（%% を使う）"))
            if i + 1 < n and s[i+1] == "\\":
                i += 2; continue
            if i + 1 >= n:
                issues.append(Issue("FATAL", line, "S7", "閉じ引用符の直前のバックスラッシュは二重にする（\\\\'''）"))
            i += 2 if i + 1 < n else 1
            continue
        if c == "%":
            if i + 1 < n and s[i+1] == "%":
                i += 2; continue
            e = find_expr_end(s, i + 1)
            if e < 0:
                issues.append(Issue("FATAL", line, "S9", "文字列内に対になっていない % がある（リテラルは %%）")); return
            if i > 0 and s[i-1] == "\\" and not (i > 1 and s[i-2] == "\\"):
                issues.append(Issue("FATAL", line, "S7", "変数 %...% の直前のバックスラッシュは二重にする（\\\\%Var%）"))
            exprs.append(s[i+1:e]); i = e + 1; continue
        if c == "'":
            issues.append(Issue("FATAL", line, "S6", "文字列内のアポストロフィは \\' にエスケープする")); i += 1; continue
        i += 1

def expr_idents(expr):
    """式中の識別子（先頭のもの）を返す。文字列リテラル '...' は除外。"""
    expr = re.sub(r"'[^']*'", "''", expr)
    out = []
    for m in re.finditer(r"(?<![\w.])(" + IDENT + r")", expr):
        out.append(m.group(1))
    return out

def keyword_props(expr):
    return [m.group(1) for m in re.finditer(r"\.(" + IDENT + r")", expr) if m.group(1).lower() in KEYWORDS]

def kb_lookup(kb, aid):
    return kb.get(aid.lower()) if kb else None

def lint(text, kb=None, advice=True):
    issues = []
    stmts = split_statements(text)
    # ---- pass 1: definitions anywhere in the flow
    defined = set()
    for line, stmt in stmts:
        s = stmt.strip()
        if s.startswith("DISABLE "): s = s[8:]
        if s.startswith("# [ControlRepository]"): break
        m = re.match(r"SET\s+(" + IDENT + r")\s+TO\s", s, re.I)
        if m: defined.add(m.group(1).lower())
        m = re.match(r"LOOP\s+FOREACH\s+(" + IDENT + r")\s+IN\s", s, re.I)
        if m: defined.add(m.group(1).lower())
        m = re.match(r"LOOP\s+(" + IDENT + r")\s+FROM\s", s, re.I)
        if m: defined.add(m.group(1).lower())
        m = re.match(r"ERROR\s*=>\s*(" + IDENT + r")", s, re.I)
        if m: defined.add(m.group(1).lower())
        code = " ".join(p for k, p in strings_and_code(s) if k == "code")
        for _, var in OUT_RE.findall(code): defined.add(var.lower())
        m = re.search(r"\bList:\s*(" + IDENT + r")", code)  # in-place list actions define too
        if m and re.match(r"Variables\.AddItemToList", s): defined.add(m.group(1).lower())
    # ---- pass 2
    stack = []; handler = None  # handler: dict(kind, saw_plain, line)
    pending_meta = None
    prev_action = None
    loop_depth = 0; loop_stats = []  # per loop: (line, actions, waits, sets)
    seen_ids = {}
    for line, stmt in stmts:
        s = stmt.strip()
        if not s: continue
        if s.startswith("# [ControlRepository]"): break   # 以降は UI 要素リポジトリ JSON
        if s.startswith("DISABLE "): s = s[8:].strip()
        up = s.upper()
        parts = strings_and_code(s)
        if any(k == "unterminated" for k, _ in parts):
            issues.append(Issue("FATAL", line, "S1", "閉じていない $''' 文字列")); continue
        code = " ".join(p for k, p in parts if k == "code")
        exprs = []
        for k, p in parts:
            if k == "str": check_string(p, line, issues, exprs)
        if pending_meta is not None and not (ID_RE.match(s) or up.startswith(("SET ","IF ","LOOP ","WAIT","CALL ","BLOCK ","SWITCH ","LABEL ","GOTO "))):
            issues.append(Issue("FATAL", pending_meta, "T23", "@@copilotGeneratedAction はアクション行の直前にだけ置ける（コメント/REGION の前は不可）"))
        if pending_meta is not None and (ID_RE.match(s) or up.startswith(("SET ","IF ","LOOP ","WAIT","CALL ","BLOCK ","SWITCH ","LABEL ","GOTO "))): pending_meta = None
        if s.startswith("#") or s.startswith("/#"): continue
        if s.startswith("**REGION") or s.startswith("**ENDREGION"): continue
        if up.startswith("REGION") or up.startswith("END REGION"):
            issues.append(Issue("FATAL", line, "T22", "領域は **REGION / **ENDREGION と書く")); continue
        if s.startswith("@@copilotGeneratedAction"):
            pending_meta = line; continue
        if s.startswith("@@"):
            issues.append(Issue("FATAL", line, "T23", "@@ ヘッダー行は貼らない")); continue
        if up.startswith(("IMPORT ", "@SENSITIVE", "FUNCTION ", "END FUNCTION", "EXIT FUNCTION")):
            issues.append(Issue("FATAL", line, "T23", "ヘッダー/サブフロー定義/EXIT FUNCTION は貼らない")); continue
        if "%" in code:
            issues.append(Issue("FATAL", line, "V3", "%...% は文字列の内側だけ。式は裸で書く（SET X TO N + 1）"))
        # keyword properties and undefined vars in string expressions
        for ex in exprs:
            for kw in keyword_props(ex):
                issues.append(Issue("FATAL", line, "N11", f"予約語をプロパティ名に使えない: .{kw} → ['{kw}']"))
            for ident in expr_idents(ex):
                if ident.lower() not in defined and ident.lower() not in KEYWORDS and not re.match(r"^(IsEmpty|IsNotEmpty|Contains|NotContains|StartsWith|EndsWith)$", ident):
                    issues.append(Issue("FATAL", line, "N13", f"文字列内の %{ident}% が未定義（変数か、%% のつもりか）"))
        for kw in keyword_props(code):
            issues.append(Issue("FATAL", line, "N11", f"予約語をプロパティ名に使えない: .{kw} → ['{kw}']"))
        # handler body restriction
        if handler and not (up.startswith("ON ERROR") or up.startswith("ON BLOCK ERROR") or up == "END"):
            if not up.startswith(HANDLER_OK):
                issues.append(Issue("FATAL" if up.startswith("IF") else "ERROR", line, "T20",
                                    "ON ERROR ハンドラー内は SET/CALL/GOTO/THROW ERROR のみ"))
        # ---- statements
        if up.startswith("SET "):
            m = re.match(r"SET\s+(\S+)\s+TO\s+(.*)$", s, re.I | re.S)
            if not m:
                issues.append(Issue("FATAL", line, "T16", "SET x TO value の形になっていない"))
            else:
                name, val = m.group(1), m.group(2)
                if name.lower() in KEYWORDS: issues.append(Issue("FATAL", line, "N11", f"予約語 {name} は変数名に使えない"))
                if not re.match(r"^" + IDENT + r"$", name): issues.append(Issue("FATAL", line, "N12", f"変数名は英字始まり: {name}"))
                vcode = " ".join(p for k, p in strings_and_code(val) if k == "code")
                if re.search(r"\sSET\s+\S+\s+TO\s", vcode, re.I):
                    issues.append(Issue("FATAL", line, "T15", "1行に2文（SET が2つ）"))
                mm = ID_RE.match(vcode.strip())
                if mm and kb_lookup(kb, mm.group(1)):
                    issues.append(Issue("FATAL", line, "T16", "SET X TO (アクション) は不可。アクションの出力 Name=> X を使う"))
                if loop_depth and advice and loop_stats:
                    loop_stats[-1]["sets"] += 1
                    if not expr_idents(vcode) and "'''" not in val or re.match(r"^\s*(\d+|True|False)\s*$", val):
                        issues.append(Issue("ADVICE", line, "P2", f"ループ内の定数 SET {name}: ループ外へ出せないか"))
            prev_action = None; continue
        if up.startswith("IF ") or up.startswith("ELSE IF "):
            if up.startswith("ELSE IF ") and re.search(r"ELSE IF\s*\(\s*[A-Za-z][A-Za-z0-9]*\.", s, re.I):
                issues.append(Issue("FATAL", line, "T19", "ELSE IF (アクション) は不可。ELSE の中に IF (...) THEN を入れ子にする"))
            if not up.rstrip().endswith("THEN"):
                issues.append(Issue("FATAL", line, "T16", "IF 行は THEN で終わる"))
            if up.startswith("IF "): stack.append(("IF", line))
            m = re.search(r"\(\s*" + ID_RE.pattern + r"\s", s)
            if m:
                rec = kb_lookup(kb, m.group(1))
                if kb is not None and rec is None: issues.append(Issue("FATAL", line, "K1", f"KB に無いアクション ID: {m.group(1)}"))
                if rec: check_args(s, rec, line, issues)
                prev_action = (line, rec, "cond")
            else:
                prev_action = None
            continue
        if up == "ELSE": prev_action = None; continue
        if up.startswith("SWITCH "): stack.append(("SWITCH", line)); prev_action = None; continue
        if up.startswith("CASE "):
            if not re.match(r"CASE\s*(=|<>|>=|<=|>|<)\s", s, re.I):
                issues.append(Issue("FATAL", line, "T18", "CASE は比較演算子のみ（CASE = 1 / CASE > 5）"))
            prev_action = None; continue
        if up == "DEFAULT": prev_action = None; continue
        if up.startswith("LOOP "):
            stack.append(("LOOP", line)); loop_depth += 1
            loop_stats.append({"line": line, "actions": 0, "waits": 0, "sets": 0})
            m3 = re.match(r"LOOP\s+WHILE\s*\(\s*" + ID_RE.pattern + r"\s", s, re.I)
            if m3:
                rec = kb_lookup(kb, m3.group(1))
                if kb is not None and rec is None: issues.append(Issue("FATAL", line, "K1", f"KB に無いアクション ID: {m3.group(1)}"))
                prev_action = (line, rec, "while")
            else:
                if up.startswith("LOOP WHILE") and advice:
                    issues.append(Issue("ADVICE", line, "P3", "LOOP WHILE: 脱出条件とセーフティカウンター（上限）があるか確認"))
                prev_action = None
            continue
        if up.startswith("BLOCK "): stack.append(("BLOCK", line)); prev_action = None; continue
        if up.startswith("ON BLOCK ERROR"):
            if "REPEAT" in up: issues.append(Issue("FATAL", line, "T20", "REPEAT はアクションの ON ERROR のみ（ON BLOCK ERROR には付けられない）"))
            if handler is None: handler = {"kind": "block", "plain": False, "line": line}; stack.append(("HANDLER", line))
            if re.match(r"ON BLOCK ERROR\s*$", s, re.I): handler["plain"] = True
            elif "IsUserDefinedErrorCode" not in s and not re.match(r"ON BLOCK ERROR\s+all\s*$", s, re.I):
                issues.append(Issue("ERROR", line, "T20", "名前付き ON BLOCK ERROR はカスタムエラー用（... IsUserDefinedErrorCode: True）。宣言済み例外名はアクションの ON ERROR で受ける"))
            elif handler["plain"]: issues.append(Issue("FATAL", line, "T20", "無名 ON BLOCK ERROR の後に名前付きは置けない"))
            continue
        if up.startswith("ON ERROR"):
            m = re.match(r"ON ERROR\s+(" + IDENT + r")\b", s, re.I)
            named = m.group(1) if m and m.group(1).upper() != "REPEAT" else None
            is_repeat = up.startswith("ON ERROR REPEAT")
            if handler is None:
                if prev_action is None:
                    issues.append(Issue("ERROR", line, "T20", "ON ERROR の直前にアクションが無い"))
                elif prev_action[1] and prev_action[2] != "wait" and not prev_action[1].get("error_handling", {}).get("on_error", True):
                    issues.append(Issue("ERROR", line, "T21", f"{prev_action[1]['actionId']} は ON ERROR 不可（BLOCK ... ON BLOCK ERROR で囲む）"))
                handler = {"kind": "action", "plain": False, "line": line, "rec": prev_action[1] if prev_action else None}
                stack.append(("HANDLER", line))
            else:
                if is_repeat: issues.append(Issue("FATAL", line, "T20", "REPEAT は最初の ON ERROR 行に1回だけ"))
                if handler.get("kind") == "block": issues.append(Issue("FATAL", line, "T20", "ON BLOCK ERROR 群の中に ON ERROR は置けない"))
            if named:
                if handler.get("plain"): issues.append(Issue("FATAL", line, "T20", "無名 ON ERROR の後に名前付き ON ERROR は置けない"))
                rec = handler.get("rec")
                if rec is not None:
                    errs = rec.get("error_handling", {}).get("errors", [])
                    if named not in errs:
                        issues.append(Issue("ERROR", line, "T21", f"宣言されていない例外名: {named}（宣言: {', '.join(errs) or 'なし'}）"))
            elif not is_repeat:
                handler["plain"] = True
            continue
        if up == "END":
            if not stack: issues.append(Issue("FATAL", line, "T16", "対応する開始行の無い END")); continue
            kind, l = stack.pop()
            if kind == "HANDLER": handler = None
            if kind == "LOOP":
                loop_depth -= 1
                st = loop_stats.pop()
                if advice:
                    if st["waits"]: issues.append(Issue("ADVICE", st["line"], "P1", f"ループ内に固定 WAIT が {st['waits']} 個: 条件付き待機（WAIT (...) FOR n）に置換"))
                    if st["actions"] >= 8: issues.append(Issue("ADVICE", st["line"], "P2", f"ループ本体 {st['actions']} アクション: スクリプト1ブロック（JS/PowerShell/VBScript）や一括アクションにまとめられないか"))
            prev_action = None; continue
        if up.startswith("WAIT"):
            m = re.match(r"WAIT\s*\(\s*" + ID_RE.pattern + r"\s", s, re.I)
            if m:
                rec = kb_lookup(kb, m.group(1))
                if kb is not None and rec is None: issues.append(Issue("FATAL", line, "K1", f"KB に無いアクション ID: {m.group(1)}"))
                if rec: check_args(s, rec, line, issues)
                prev_action = (line, rec, "wait")
                if advice and not re.search(r"\)\s*FOR\s+\S+", s, re.I):
                    issues.append(Issue("ADVICE", line, "P1", "条件付き WAIT に FOR <秒> の上限が無い"))
            else:
                prev_action = None
                if loop_depth and loop_stats: loop_stats[-1]["waits"] += 1
                elif advice: issues.append(Issue("ADVICE", line, "P1", "固定 WAIT: 状態確認＋再試行、または条件付き待機に置換できないか"))
            continue
        if up.startswith("ERROR =>") or up.startswith("ERROR=>"): prev_action = None; continue
        if up.startswith("CALL "):
            if re.search(r"CALL\s+\S+\s+\S+:", s, re.I): issues.append(Issue("FATAL", line, "T16", "CALL に引数は付けられない（変数で渡す）"))
            prev_action = None; continue
        if up.startswith(("LABEL ", "GOTO ", "EXIT LOOP", "NEXT LOOP", "EXIT", "THROW ERROR")):
            prev_action = None; continue
        # ---- action line
        m = ID_RE.match(s)
        if not m or not (len(s) == m.end() or s[m.end()].isspace()):
            issues.append(Issue("FATAL", line, "T15", f"文として解釈できない行: {s[:60]}")); prev_action = None; continue
        aid = m.group(1)
        if aid.lower() in ("database.connect", "scripting.runpythonscript"):
            issues.append(Issue("FATAL", line, "T24", f"{aid} は 2.72 で削除。セレクター付きの ID を使う"))
        rec = kb_lookup(kb, aid)
        if kb is not None and rec is None:
            issues.append(Issue("FATAL", line, "K1", f"KB に無いアクション ID: {aid}（兄弟セレクター違いか綴り）"))
        if rec: check_args(s, rec, line, issues)
        # duplicate args
        names = [a.lower() for a in ARG_RE.findall(code)]
        dups = {a for a in names if names.count(a) > 1}
        if dups: issues.append(Issue("FATAL", line, "T15", f"引数が重複: {', '.join(dups)}"))
        # undefined bare identifiers as argument values
        for am in re.finditer(r"(?<![\w.])(" + IDENT + r"):\s+(" + IDENT + r")(?=\s|$)", code):
            val = am.group(2)
            if val.lower() in ("true", "false") or val.lower() in defined: continue
            if ENUM_RE.search(code[am.start(2):am.start(2)+80]) and "." in code[am.start(2):am.start(2)+80].split(" ")[0]: continue
            if "." in code[am.start(2):].split(" ")[0]: continue
            issues.append(Issue("FATAL", line, "N13", f"引数 {am.group(1)} の値 {val} が未定義の変数"))
        if loop_depth and loop_stats: loop_stats[-1]["actions"] += 1
        prev_action = (line, rec, "action")
        # advice: consecutive single-cell Excel writes etc.
        if advice:
            fam = ".".join(aid.split(".")[:2]).lower()
            if fam in ("excel.writetoexcel", "excel.writeexcel") and loop_depth:
                issues.append(Issue("ADVICE", line, "P2", "ループ内のセル書込み: データテーブルを作って1回で書く"))
            if fam == "excel.readfromexcel" and loop_depth:
                issues.append(Issue("ADVICE", line, "P2", "ループ内のセル読込み: 範囲を1回で読んでテーブルを回す"))
            if "appmask[" in s or re.search(r"\b(Control|Element|UIElement|Image):", code):
                if ":eq(" in s or re.search(r"\bImage:", code):
                    issues.append(Issue("ADVICE", line, "P5", "UI要素が位置（:eq）や画像に依存。id/name/AutomationId で一意に取れるセレクターか、UI を使わない方法に置換"))
                else:
                    issues.append(Issue("ADVICE", line, "P5", "UI要素を使用: 何で一意に取れるか（AutomationId/id/name/data-*）を設計に明記。可能なら JS/HTTP/COM へ"))
            if fam.startswith("mouseandkeyboard.sendmouseclick") and "ClickAt" in aid:
                issues.append(Issue("ADVICE", line, "P4", "座標クリックは環境依存。UI要素クリックか JS に置換できないか"))
    for kind, l in stack:
        issues.append(Issue("FATAL", l, "T16", f"{kind} が END で閉じられていない"))
    return issues

def check_args(s, rec, line, issues):
    code = " ".join(p for k, p in strings_and_code(s) if k == "code")
    given = {a.lower(): a for a in ARG_RE.findall(code)}
    allowed = {p["name"].lower(): p for p in rec.get("input_params", [])}
    outs = {p["name"].lower() for p in rec.get("output_params", [])}
    for a_l, a in given.items():
        if a_l not in allowed and a_l not in outs:
            sibs = ", ".join(x.split(".")[-1] for x in rec.get("sibling_selectors", [])) or "なし"
            issues.append(Issue("ERROR", line, "K2", f"{rec['actionId']} に無い引数: {a}（兄弟セレクター: {sibs}）"))
    for a_l, p in allowed.items():
        if p.get("required") and a_l not in given:
            issues.append(Issue("WARN", line, "K3", f"{rec['actionId']} の KB 上の必須引数が無い: {p['name']}（省略可の場合あり）"))
    enum_params = [p for p in rec.get("input_params", []) if p.get("enumValues")]
    for mod, typ, val in ENUM_RE.findall(code):
        for p in enum_params:
            if p["type"].split(".")[-1].lower() == typ.lower():
                if val.lower() not in [v.lower() for v in p["enumValues"]]:
                    issues.append(Issue("ERROR", line, "V4", f"enum 値 {mod}.{typ}.{val} は許可値に無い: {', '.join(p['enumValues'])}"))
    for p in enum_params:
        m = re.search(r"(?<![\w.])" + re.escape(p["name"]) + r":\s+(" + IDENT + r")(?=\s|$)", code)
        if m and m.group(1).lower() in [v.lower() for v in p["enumValues"]]:
            issues.append(Issue("ERROR", line, "V4", f"enum は完全修飾で書く: {p['name']}: Module.{p['type'].split('.')[-1]}.{m.group(1)}"))

def main():
    args = sys.argv[1:]
    if not args: print(__doc__); sys.exit(0)
    kb_path = None; as_json = False; advice = True; files = []
    i = 0
    while i < len(args):
        if args[i] == "--kb": kb_path = args[i+1]; i += 2; continue
        if args[i] == "--json": as_json = True; i += 1; continue
        if args[i] == "--no-advice": advice = False; i += 1; continue
        files.append(args[i]); i += 1
    kb = load_kb(kb_path)
    worst = 0
    for f in files:
        issues = lint(pathlib.Path(f).read_text(encoding="utf-8"), kb, advice)
        issues.sort(key=lambda x: x.line)
        if as_json:
            print(json.dumps([vars(x) for x in issues], ensure_ascii=False, indent=1))
        else:
            print(f"== {f}: {len(issues)} issue(s)" + ("" if kb else "（KB なし: 構文のみ）"))
            for x in issues: print("  " + str(x))
        for x in issues: worst = max(worst, 2 if x.sev in ("FATAL", "ERROR") else 1)
    sys.exit(worst)

if __name__ == "__main__":
    main()
