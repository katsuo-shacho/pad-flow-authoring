#!/usr/bin/env python3
"""
robin_to_mermaid.py — Robin テキストから独自デザインのフローチャート（Mermaid）を作る

使い方: python3 robin_to_mermaid.py flow.robin > flow.mmd
        python3 robin_to_mermaid.py flow.robin --html > flow.html   # ブラウザーで開ける単体 HTML

見た目は PAD のデザイナーを模倣しない（一般的なフローチャート記法: 角丸=処理, ひし形=分岐,
二重枠=ループ, 破線=エラー経路）。ラベルはアクション名と主要引数だけに丸める。
"""
import sys, re, html, pathlib

ID_RE = re.compile(r"([A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+)")
KEY_ARGS = ("File","Folder","Url","Path","Text","Title","Message","Instance","BrowserInstance","Excel instance","SubflowName")

def strip_strings(s):
    return re.sub(r"\$'''.*?'''", lambda m: "“" + m.group(0)[4:-3][:18] + ("…" if len(m.group(0)) > 25 else "") + "”", s, flags=re.S)

def esc(t):
    t = t.replace('"', "'").replace("\n", " ")
    return t[:60] + ("…" if len(t) > 60 else "")

def label_action(s):
    m = ID_RE.match(s)
    aid = m.group(1) if m else s.split(" ")[0]
    parts = aid.split(".")
    name = parts[-1] if len(parts) > 2 else ".".join(parts[-2:])
    name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)
    rest = strip_strings(s[len(aid):])
    key = ""
    for k in KEY_ARGS:
        mm = re.search(r"\b" + re.escape(k) + r":\s*(\S+)", rest)
        if mm: key = f" ({mm.group(1)})"; break
    out = re.search(r"(\w+)=>\s*(\w+)", rest)
    if out: key += f" → {out.group(2)}"
    return esc(f"{parts[0]}: {name}{key}")

def convert(text):
    lines = [l.rstrip() for l in text.split("\n")]
    nodes, edges = [], []
    n = 0
    def new(label, shape="proc"):
        nonlocal n; n += 1; nid = f"n{n}"
        nodes.append((nid, label, shape)); return nid
    start = new("開始", "term"); prev = [start]
    stack = []  # frames: dict(kind, cond_node, done(list), pending_else, loop_node, handler_of)
    i = 0; in_str = False
    while i < len(lines):
        s = lines[i].strip(); i += 1
        if not s: continue
        # multi-line string skip (rough)
        if s.count("$'''") % 2 == 1 and s.count("'''") % 2 == 1: in_str = not in_str;
        if in_str: continue
        if s.startswith("#") or s.startswith("/#") or s.startswith("**") or s.startswith("@@") or s.startswith("# [ControlRepository]"): continue
        if s.startswith("# [ControlRepository]"): break
        up = s.upper()
        if up.startswith("IF "):
            c = new(esc("条件: " + strip_strings(s[3:].rsplit(" THEN", 1)[0])), "dec")
            for p in prev: edges.append((p, c, ""))
            stack.append({"kind": "IF", "cond": c, "done": [], "label": "はい"}); prev = [c]; continue
        if up.startswith("ELSE IF "):
            f = stack[-1]; f["done"] += prev
            c = new(esc("条件: " + strip_strings(s[8:].rsplit(" THEN", 1)[0])), "dec")
            edges.append((f["cond"], c, "いいえ")); f["cond"] = c; prev = [c]; f["label"] = "はい"; continue
        if up == "ELSE":
            f = stack[-1]; f["done"] += prev; prev = [f["cond"]]; f["label"] = "いいえ"; f["else"] = True; continue
        if up.startswith("SWITCH "):
            c = new(esc("分岐: " + strip_strings(s[7:])), "dec");
            for p in prev: edges.append((p, c, ""))
            stack.append({"kind": "SWITCH", "cond": c, "done": [], "label": ""}); prev = []; continue
        if up.startswith("CASE ") or up == "DEFAULT":
            f = stack[-1]; f["done"] += prev; prev = [f["cond"]]; f["label"] = esc(s); continue
        if up.startswith("LOOP "):
            l = new(esc("ループ: " + strip_strings(s[5:])), "loop")
            for p in prev: edges.append((p, l, ""))
            stack.append({"kind": "LOOP", "cond": l, "done": [], "label": "各要素"}); prev = [l]; continue
        if up.startswith("BLOCK "):
            b = new(esc("ブロック " + s[6:]), "sub")
            for p in prev: edges.append((p, b, ""))
            stack.append({"kind": "BLOCK", "cond": b, "done": [], "label": ""}); prev = [b]; continue
        if up.startswith("ON BLOCK ERROR") or up.startswith("ON ERROR"):
            if stack and stack[-1]["kind"] == "HANDLER":
                h = new(esc(s), "err"); edges.append((stack[-1]["src"], h, "error")); prev = [h]; continue
            src = stack[-1]["cond"] if (stack and up.startswith("ON BLOCK")) else (prev[-1] if prev else start)
            h = new(esc(s), "err"); edges.append((src, h, "error"))
            stack.append({"kind": "HANDLER", "src": src, "resume": prev, "done": []}); prev = [h]; continue
        if up == "END":
            if not stack: continue
            f = stack.pop()
            if f["kind"] == "HANDLER":
                f["done"] += prev; prev = f["resume"] + f["done"]; continue
            if f["kind"] == "LOOP":
                for p in prev: edges.append((p, f["cond"], "次へ"))
                prev = [f["cond"]]; continue
            if f["kind"] in ("IF", "SWITCH"):
                f["done"] += prev
                if f["kind"] == "IF" and not f.get("else"): f["done"].append(f["cond"])
                prev = f["done"]; continue
            prev = f["done"] + prev; continue
        if up.startswith("EXIT LOOP") or up.startswith("NEXT LOOP") or up.startswith("GOTO ") or up.startswith("EXIT"):
            x = new(esc(s), "term");
            for p in prev: edges.append((p, x, ""));
            prev = []; continue
        if up.startswith("LABEL "):
            x = new(esc(s), "term");
            for p in prev: edges.append((p, x, ""));
            prev = [x]; continue
        if up.startswith("SET ") or up.startswith("CALL ") or up.startswith("WAIT"):
            x = new(esc(strip_strings(s)), "proc")
        else:
            x = new(label_action(s), "proc")
        for p in prev:
            lab = ""
            if stack and p == stack[-1].get("cond") and stack[-1]["kind"] in ("IF", "SWITCH", "LOOP"):
                lab = stack[-1]["label"]
            edges.append((p, x, lab))
        prev = [x]
    end = new("終了", "term")
    for p in prev: edges.append((p, end, ""))
    out = ["flowchart TD"]
    for nid, label, shape in nodes:
        l = f'"{label}"'
        if shape == "dec": out.append(f"  {nid}{{{l}}}")
        elif shape == "term": out.append(f"  {nid}([{l}])")
        elif shape == "loop": out.append(f"  {nid}[[{l}]]")
        elif shape == "err": out.append(f"  {nid}>{l}]")
        elif shape == "sub": out.append(f"  {nid}[/{l}/]")
        else: out.append(f"  {nid}[{l}]")
    seen = set()
    for a, b, lab in edges:
        if (a, b, lab) in seen: continue
        seen.add((a, b, lab))
        if lab == "error": out.append(f"  {a} -.->|エラー| {b}")
        elif lab: out.append(f"  {a} -->|{lab}| {b}")
        else: out.append(f"  {a} --> {b}")
    out += ["  classDef dec fill:#fff4d6,stroke:#b8860b;", "  classDef err fill:#fde8e8,stroke:#c0392b;",
            "  classDef loop fill:#e8f0fe,stroke:#2b5fd9;", "  classDef term fill:#eef7ee,stroke:#2e7d32;"]
    for nid, _, shape in nodes:
        if shape in ("dec", "err", "loop", "term"): out.append(f"  class {nid} {shape};")
    return "\n".join(out)

HTML = """<!doctype html><html><head><meta charset="utf-8"><title>Flow chart</title>
<style>body{{font-family:system-ui,sans-serif;margin:16px}} .mermaid{{max-width:100%}}</style></head><body>
<h3>{title}</h3><pre class="mermaid">{code}</pre>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true, flowchart:{{curve:'basis'}}}});</script></body></html>"""

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    text = pathlib.Path(args[0]).read_text(encoding="utf-8")
    mmd = convert(text)
    if "--html" in sys.argv:
        print(HTML.format(title=html.escape(pathlib.Path(args[0]).name), code=html.escape(mmd)))
    else:
        print(mmd)
