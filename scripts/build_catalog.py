#!/usr/bin/env python3
"""
公式ドキュメント（MicrosoftDocs/power-automate-docs, CC BY 4.0）の
articles/desktop-flows/actions-reference/*.md から、トークン節約型の
knowledge/catalog.md と knowledge/actions/<group>.md を再生成する。

使い方:
  git clone --depth 1 --filter=blob:none --sparse https://github.com/MicrosoftDocs/power-automate-docs.git
  cd power-automate-docs && git sparse-checkout set articles/desktop-flows && cd ..
  python3 build_catalog.py power-automate-docs/articles/desktop-flows <skill_dir>/knowledge
"""
import re, sys, pathlib

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
LEARN = "https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/"

LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
IMG = re.compile(r":::image[^\n]*:::")
ANCHOR = re.compile(r'<a name="([^"]+)"></a>\s*')

def clean(s: str) -> str:
    s = LINK.sub(r"\1", s)
    s = s.replace("**", "")
    return re.sub(r"\s+", " ", s).strip()

def parse_table(lines):
    rows = []
    for ln in lines:
        if not ln.startswith("|") or set(ln.strip()) <= {"|", "-"}:
            continue
        cells = [clean(c) for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    return rows[1:] if rows else []  # drop header

def parse_group(path: pathlib.Path):
    text = IMG.sub("", path.read_text(encoding="utf-8"))
    # frontmatter title
    fm = re.search(r"^title:\s*(.+)$", text, re.M)
    title = clean(fm.group(1)) if fm else path.stem
    body = text.split("\n---\n", 1)[-1] if text.startswith("---") else text
    intro = []
    actions = []
    cur = None
    section = None
    for ln in body.split("\n"):
        if ln.startswith("## "):
            if cur: actions.append(cur)
            h = ln[3:]
            m = ANCHOR.search(h)
            anchor = m.group(1) if m else ""
            cur = {"name": clean(ANCHOR.sub("", h)), "anchor": anchor,
                   "desc": "", "params": [], "outputs": [], "exc": []}
            section = "desc"
            continue
        if ln.startswith("# ") and cur is None:
            continue
        if cur is None:
            if ln.strip() and not ln.startswith("#") and not ln.startswith(">"):
                intro.append(clean(ln))
            continue
        if ln.startswith("### "):
            h = ln.lower()
            section = ("params" if "input" in h else "outputs" if "produced" in h
                       else "exc" if "exception" in h else "other")
            continue
        if section == "desc":
            if ln.strip() and not ln.startswith(">") and not cur["desc"]:
                cur["desc"] = clean(ln)
        elif section in ("params", "outputs", "exc"):
            if ln.startswith("|"):
                cur[section + "_raw"] = cur.get(section + "_raw", []) + [ln]
            elif ln.strip() and "doesn't produce" in ln:
                cur["outputs"] = []
    if cur: actions.append(cur)
    # 非アクションの見出し（概要・既知の制限など: アンカーもパラメータ表も無い）を除く
    filtered = [a for a in actions if a["anchor"] or a.get("params_raw") or a.get("outputs_raw") or a.get("exc_raw")]
    actions = filtered or actions   # 説明だけの群（Cloud connectors, SharePoint 等）は見出しをそのまま残す
    for a in actions:
        for k in ("params", "outputs", "exc"):
            a[k] = parse_table(a.pop(k + "_raw", []))
    return title, intro, actions

def fmt_group(stem, title, intro, actions):
    out = [f"# {title}", "",
           f"出典: {LEARN}{stem} （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）", ""]
    if intro:
        out.append("概要: " + " ".join(intro)[:600])
        out.append("")
    for a in actions:
        out.append(f"## {a['name']}" + (f"  `#{a['anchor']}`" if a['anchor'] else ""))
        if a["desc"]:
            out.append(a["desc"])
        if a["params"]:
            out.append("入力:")
            for r in a["params"]:
                # Argument|Optional|Accepts|Default|Description
                r += [""] * (5 - len(r))
                arg, opt, acc, dflt, d = r[:5]
                flag = "(任意)" if opt.lower().startswith("y") else ""
                dd = f" = {dflt}" if dflt else ""
                out.append(f"- {arg}{flag}: {acc}{dd} — {d}")
        if a["outputs"]:
            out.append("出力:")
            for r in a["outputs"]:
                r += [""] * (3 - len(r))
                out.append(f"- {r[0]}: {r[1]} — {r[2]}")
        if a["exc"]:
            out.append("例外: " + "; ".join(r[0] for r in a["exc"]))
        out.append("")
    return "\n".join(out)

CORE = {"variables","conditionals","loops","flowcontrol","runflow","display","file","folder",
        "text","datetime","excel","word","pdf","compression","clipboard","mouseandkeyboard",
        "uiautomation","webautomation","web","scripting","cmd","system","workstation","services",
        "email","outlook","office365outlook","logging","testing","xml","database","ocr",
        "powerautomateenvironment","cloudconnectors","workqueues"}

# 公式グループ → Robin KB モジュールファイル（knowledge/robin/<file>.md）
ROBIN = {"access":"access","activedirectory":"activedirectory","aws":"aws","azure":"azure",
 "clipboard":"clipboard","cmd":"cmd","compression":"compression","cryptography":"cryptography, pgp",
 "cyberark":"cyberark","database":"database","datetime":"datetime","display":"display","email":"email",
 "excel":"excel","exchange":"exchange","file":"file","flowcontrol":"flowcontrol（IF/LOOP/BLOCK等の組込み文は robin-rules.md）",
 "folder":"folder","ftp":"ftp","googlecognitive":"cognitive-google","ibmcognitive":"cognitive-ibm",
 "logging":"logging","loops":"（組込み文: robin-rules.md）","conditionals":"（組込み文: robin-rules.md）",
 "microsoftcognitive":"cognitive-microsoft","mouseandkeyboard":"mouseandkeyboard","ocr":"ocr",
 "outlook":"outlook","pdf":"pdf","powerautomateenvironment":"powerautomateenvironment","sap":"sap",
 "scripting":"system（Scripting.* はここ）","services":"services","system":"system",
 "terminalemulation":"terminalemulation","testing":"testing","text":"text","uiautomation":"uiautomation",
 "variables":"variables","web":"web","webautomation":"webautomation","word":"word",
 "workqueues":"workqueues","workstation":"system（Workstation.* はここ）","xml":"xml"}

def load_memos():
    """既存カタログの `  - memo:` 行（ユーザーのノウハウ）を群見出しごとに回収し、再生成後も保持する。"""
    memos = {}
    for name in ("catalog.md", "catalog-extended.md"):
        f = OUT / name
        if not f.exists(): continue
        cur = None
        for ln in f.read_text(encoding="utf-8").split("\n"):
            if ln.startswith("## "): cur = ln.split(" → ")[0]
            elif ln.startswith("  - memo:") and cur: memos.setdefault(cur, []).append(ln)
    return memos

def main():
    memos = load_memos()
    (OUT / "actions").mkdir(parents=True, exist_ok=True)
    header = ["出典: Microsoft Power Automate documentation (MicrosoftDocs/power-automate-docs, CC BY 4.0 "
              "https://creativecommons.org/licenses/by/4.0/) の actions-reference を本プロジェクトが要約・圧縮したもの。Microsoft の見解ではない（LEGAL.md）。",
              "1行＝1アクション。",
              "詳細（引数・既定値・例外）は `actions/<group>.md` を読む。",
              "Robin（貼付テキスト）上の正式名はDesignerからのコピーで確認する（ここには無い）。", ""]
    catalog = ["# PAD アクション カタログ（第1層・コア）", ""] + header + [
        "業務でまず使う群。クラウド/AD/SAP/認知サービス等は catalog-extended.md。",
        "各群の `Robin:` 行が貼付用 ID の置き場（knowledge/robin/）。KB だけにある群: powerpoint, triggers, computeruse, llm。",
        "自分のノウハウ（使い方のコツ・はまりどころ）は各群の末尾に `  - memo:` 行で足してよい。再生成時は scripts/ の MEMO を参照。", ""]
    extended = ["# PAD アクション カタログ（第1層・拡張）", ""] + header
    groups = []
    for p in sorted(SRC.glob("actions-reference/*.md")):
        title, intro, actions = parse_group(p)
        if not actions:
            continue
        groups.append((p.stem, title, len(actions)))
        (OUT / "actions" / f"{p.stem}.md").write_text(
            fmt_group(p.stem, title, intro, actions), encoding="utf-8")
        dest = catalog if p.stem in CORE else extended
        dest.append(f"## {title} → actions/{p.stem}.md ({len(actions)})")
        rb = ROBIN.get(p.stem)
        dest.append("Robin: " + (f"robin/{rb}.md" if rb and "（" not in rb and "," not in rb else (rb or "KB未収録（Designerコピーで確認）")))
        for a in actions:
            d = a["desc"]
            if len(d) > 90: d = d[:87] + "..."
            dest.append(f"- {a['name']}: {d}")
        dest.extend(memos.get(f"## {title}", []))
        dest.append("")
    (OUT / "catalog.md").write_text("\n".join(catalog), encoding="utf-8")
    (OUT / "catalog-extended.md").write_text("\n".join(extended), encoding="utf-8")
    print(f"{len(groups)} groups, {sum(g[2] for g in groups)} actions")

if __name__ == "__main__":
    main()
