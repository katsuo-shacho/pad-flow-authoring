#!/usr/bin/env python3
"""
make_portable.py — OneDrive／ローカルに置いて「辞書的に参照する」ためのポータブル版 zip を作る

使い方: python3 scripts/make_portable.py [--out pad-flow-authoring-portable.zip] [--no-powerfx] [--no-scripts]
既定はフルに近い構成（.git と __pycache__ だけ除外）。先頭に START_HERE.md（入口・有効化の3問・読ませる順）を入れる。
"""
import sys, zipfile, pathlib, datetime
root = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
out = pathlib.Path(args[args.index("--out")+1]) if "--out" in args else root.parent / "pad-flow-authoring-portable.zip"
skip_fx = "--no-powerfx" in args; skip_scripts = "--no-scripts" in args
ver = (root / "CHANGELOG.md").read_text(encoding="utf-8").split("## ")[1].split("\n")[0].strip()
start = f"""# START HERE — pad-flow-authoring ポータブル版（{ver}、{datetime.date.today()}）

このフォルダーは Power Automate Desktop の**挙動辞書＋作業手順**。ネット接続もコード実行も要らない。AI にはファイルを「参照」させるだけ。
出典・ライセンスは LICENSE / THIRD_PARTY_NOTICES.md / LEGAL.md（docs CC BY 4.0、非公式、Microsoft と無関係）。

## AI に最初に読ませる2本（毎回）
1. `prompts/chat-kickoff.md` — 進め方と出力ゲート（判定表 → GATE: PASS 8/8 → Robin）
2. `knowledge/robin-rules-compact.md` — 貼付が無言で失敗する規則（2.5KB）

## 作る内容に応じて追加で読ませる
- できること一覧: `knowledge/catalog.md`（群を決める）
- 貼付用の正本: `knowledge/robin/<module>.md`（例: excel.md, file.md, folder.md, text.md, variables.md, display.md, system.md）。Power Fx フローは `knowledge/robin-powerfx/`
- 設計の定石: `knowledge/patterns-config-object.md`（環境依存の値は REGION 00/01/02 に集約）、`patterns-download-pipeline.md`
- 手順の詳細: `workflow/01-plan.md` → `02-design.md` → `03-principles.md` → `05-verify.md`
- 見本: `examples/csv-to-excel/`

## 有効になっているか（3問）
1. 「Robin を出す前に必ずやることは？」→ 8点の反射チェックと判定表、GATE: PASS 8/8 の後にだけ Robin
2. 「`SET X TO %N + 1%` は貼れる？」→ 貼れない（% は文字列の内側だけ）
3. 「環境依存の値はどこに置く？」→ 冒頭のカスタムオブジェクト REGION 00/01/02

## 自分のノウハウの足し方
- `knowledge/catalog.md` の群の末尾に `  - memo: …`
- 動作確認した部品は `knowledge/snippets/own-*.md`（確認した PAD の版を書く）
- 会社固有の値（URL・セレクター・パス）はここではなく、別ファイル（REGION 00 だけ）に置く
"""
n = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("pad-flow-authoring/START_HERE.md", start)
    for p in sorted(root.rglob("*")):
        if not p.is_file(): continue
        rel = p.relative_to(root)
        s = str(rel)
        if s.startswith(".git") or "__pycache__" in s or s.endswith(".pyc") or s.endswith(".zip"): continue
        if skip_fx and "robin-powerfx" in s: continue
        if skip_scripts and s.startswith("scripts/"): continue
        z.write(p, f"pad-flow-authoring/{s}"); n += 1
print(f"{out}  files={n+1}  bytes={out.stat().st_size}")
