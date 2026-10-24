#!/usr/bin/env python3
"""
JoeG592/pad-robin-action-kb（CC BY 4.0, Joe Green）の PAD_Robin_ActionKB.json から
knowledge/robin/<module>.md と knowledge/robin-index.md（1行1アクション）を生成する。

使い方:
  curl -L -o kb.json https://raw.githubusercontent.com/JoeG592/pad-robin-action-kb/main/PAD_Robin_ActionKB.json
  python3 build_robin.py kb.json <skill_dir>/knowledge [--powerfx]
"""
import json, re, sys, pathlib
from collections import defaultdict

SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
FX = "--powerfx" in sys.argv
SUB = "robin-powerfx" if FX else "robin"
ATTR = ("出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) "
        "https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/\n"
        "ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。")

d = json.loads(SRC.read_text(encoding="utf-8"))
recs = d["actions"]
meta = f"KB {d.get('version')} / PAD {d.get('pad_build')} / {d.get('date')}"

def slug(m): return re.sub(r"[^a-z0-9]+", "-", m.lower()).strip("-")

def short_type(t):
    t = t.replace("`1", "")
    return t

bym = defaultdict(list)
for r in recs: bym[r["module"]].append(r)

(OUT / SUB).mkdir(parents=True, exist_ok=True)
index = [f"# Robin ID 索引（{'Power Fx' if FX else 'Classic'}）", "", ATTR, meta, "",
         "1行＝1 Robin ID。貼る前に必ず `" + SUB + "/<module>.md` で引数・enum・エラー名を確認する。",
         "kind: A=Action, C=Condition（IF (...) THEN）, W=Wait（WAIT (...)）, L=While（LOOP WHILE (...)）。",
         "UI=録画したUI要素/画像が必要（例はプレースホルダー）。", ""]
kinds = {"Action": "A", "Condition": "C", "Wait": "W", "While": "L"}
for mod in sorted(bym):
    rows = bym[mod]
    index.append(f"## {mod} → {SUB}/{slug(mod)}.md ({len(rows)})")
    out = [f"# Robin: {mod}", "", ATTR, meta, "",
           "各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行", ""]
    fam_seen = set()
    for r in sorted(rows, key=lambda x: x["actionId"]):
        fam = ".".join(r["actionId"].split(".")[:2])
        if r.get("sibling_selectors") and fam not in fam_seen:
            fam_seen.add(fam)
            sels = sorted({r["actionId"]} | set(r["sibling_selectors"]))
            out.append(f"### {fam} のセレクター: " + ", ".join(x.split(".")[-1] for x in sels))
            out.append("")
        k = kinds.get(r["kind"], r["kind"][:1])
        ui = " UI" if r.get("needs_ui_selector") else ""
        index.append(f"- {r['actionId']} [{k}{ui}]")
        out.append(f"## {r['actionId']} [{k}{ui}]")
        out.append("```")
        out.append(r["golden_example"])
        out.append("```")
        ins = []
        for p in r.get("input_params", []):
            s = f"{p['name']}:{short_type(p['type'])}"
            if p.get("required"): s = "!" + s
            if p.get("enumValues"): s += "{" + ",".join(p["enumValues"]) + "}"
            ins.append(s)
        if ins: out.append("入力: " + " ".join(ins))
        outs = [f"{p['name']}:{short_type(p['type'])}=>{p.get('defaultVariable','')}" for p in r.get("output_params", [])]
        if outs: out.append("出力: " + " ".join(outs))
        eh = r.get("error_handling", {})
        if eh.get("on_error"):
            out.append("ON ERROR可: " + (", ".join(eh.get("errors", [])) or "(名前なし)"))
        else:
            out.append("ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）")
        if r.get("constraints"):
            out.append("固定: " + ", ".join(f"{a}={b}" for a, b in r["constraints"].items()))
        out.append("")
    (OUT / SUB / f"{slug(mod)}.md").write_text("\n".join(out), encoding="utf-8")
    index.append("")
(OUT / (SUB + "-index.md")).write_text("\n".join(index), encoding="utf-8")
print(len(recs), "records,", len(bym), "modules")
