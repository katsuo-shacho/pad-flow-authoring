#!/usr/bin/env python3
"""
make_prompt_pack.py — Copilot だけの環境向けに、会話へ貼る1本のテキストを作る（トークン最小化）

使い方:
  python3 make_prompt_pack.py --modules excel,file                 # モジュール丸ごと
  python3 make_prompt_pack.py --families Excel.LaunchExcel,Excel.ReadFromExcel,File.GetFiles   # 必要な家族だけ（推奨）
  オプション: --powerfx  --full-rules（既定は圧縮版規則）  --max-chars 60000
内容: prompts/chat-kickoff.md + 規則（圧縮版）+ 原則（要点）+ 指定した Robin 参照
"""
import sys, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
def opt(name, default=None):
    return args[args.index(name)+1] if name in args else default
mods = (opt("--modules") or "").split(",") if opt("--modules") else []
fams = (opt("--families") or "").split(",") if opt("--families") else []
fx = "--powerfx" in args; maxc = int(opt("--max-chars", "60000"))
sub = "robin-powerfx" if fx else "robin"
rules = "robin-rules.md" if "--full-rules" in args else "robin-rules-compact.md"
parts = [(root/"prompts"/"chat-kickoff.md").read_text(encoding="utf-8"),
         (root/"knowledge"/rules).read_text(encoding="utf-8")]
pr = (root/"workflow"/"03-principles.md").read_text(encoding="utf-8")
parts.append(pr.split("## Flow Checker")[0])   # 原則の本体だけ（規則一覧は省く）
def records(modfile):
    txt = modfile.read_text(encoding="utf-8")
    head, *recs = re.split(r"\n(?=## |### )", txt)
    return head, recs
for m in mods:
    f = root/"knowledge"/sub/f"{m.strip().lower()}.md"
    if f.exists(): parts.append(f.read_text(encoding="utf-8"))
    else: sys.stderr.write(f"missing module: {f}\n")
if fams:
    want = [x.strip().lower() for x in fams]
    picked = ["# Robin 参照（抜粋）  出典: JoeG592/pad-robin-action-kb CC BY 4.0"]
    for f in sorted((root/"knowledge"/sub).glob("*.md")):
        head, recs = records(f)
        for r in recs:
            first = r.split("\n",1)[0].lower()
            if any(first.startswith("## "+w) or first.startswith("### "+w) for w in want):
                picked.append(r)
    parts.append("\n\n".join(picked))
out = "\n\n---\n\n".join(parts)
sys.stderr.write(f"{len(out)} chars\n")
if len(out) > maxc: sys.stderr.write(f"warning: > {maxc}; --families で絞るか --max-chars を上げる\n")
print(out)
