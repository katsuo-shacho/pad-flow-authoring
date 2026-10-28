#!/usr/bin/env python3
"""
build_site_index.py — Pages 公開用の索引を作る（辞書を「API っぽく」URL で引くための入口）

出力:
  <site>/index.html        人が読む入口（各ファイルへのリンク）
  <site>/index.json        AI が読む入口: { "robin": {"Excel": "knowledge/robin/excel.md", ...}, "catalog": ..., "rules": ... }
  <site>/robin-ids.json    Robin ID → ファイルパス（1,086 件）。AI は ID で引ける
使い方: python3 build_site_index.py <site_dir>
"""
import sys, re, json, pathlib, html
site = pathlib.Path(sys.argv[1])
k = site / "knowledge"
idx = {"name": "pad-flow-authoring dictionary", "license": "docs CC BY 4.0; see LICENSE / THIRD_PARTY_NOTICES.md",
       "entry": {"skill": "SKILL.md", "rules_compact": "knowledge/robin-rules-compact.md", "rules_full": "knowledge/robin-rules.md",
                 "catalog": "knowledge/catalog.md", "catalog_extended": "knowledge/catalog-extended.md",
                 "robin_index": "knowledge/robin-index.md", "chat_kickoff": "prompts/chat-kickoff.md",
                 "lookup_protocol": "prompts/chat-lookup-protocol.md"},
       "robin": {}, "robin_powerfx": {}, "actions": {}, "patterns": {}}
for sub, key in (("robin", "robin"), ("robin-powerfx", "robin_powerfx"), ("actions", "actions")):
    for p in sorted((k / sub).glob("*.md")):
        idx[key][p.stem] = f"knowledge/{sub}/{p.name}"
for p in sorted(k.glob("patterns-*.md")):
    idx["patterns"][p.stem.replace("patterns-", "")] = f"knowledge/{p.name}"
(site / "index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
ids = {}
for p in sorted((k / "robin").glob("*.md")):
    for m in re.finditer(r"^## ([A-Za-z][\w.]+) \[", p.read_text(encoding="utf-8"), re.M):
        ids[m.group(1)] = f"knowledge/robin/{p.name}"
(site / "robin-ids.json").write_text(json.dumps(ids, ensure_ascii=False, indent=0), encoding="utf-8")
rows = []
def sec(title, d):
    rows.append(f"<h2>{html.escape(title)}</h2><ul>" + "".join(f'<li><a href="{v}">{html.escape(k_)}</a></li>' for k_, v in d.items()) + "</ul>")
rows.append("<h2>入口</h2><ul>" + "".join(f'<li><a href="{v}">{html.escape(k_)}</a> — {v}</li>' for k_, v in idx["entry"].items()) + "</ul>")
rows.append('<p>機械向け: <a href="index.json">index.json</a> / <a href="robin-ids.json">robin-ids.json</a>（Robin ID → ファイル）</p>')
sec("Robin（Classic）", idx["robin"]); sec("Robin（Power Fx）", idx["robin_powerfx"]); sec("公式アクション要約", idx["actions"]); sec("定石", idx["patterns"])
(site / "index.html").write_text("""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>pad-flow-authoring dictionary</title>
<style>body{font-family:system-ui,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;line-height:1.5}ul{columns:3;-webkit-columns:3}li{break-inside:avoid}</style></head><body>
<h1>pad-flow-authoring — PAD 挙動辞書（非公式）</h1>
<p>Power Automate Desktop の観察された挙動の記録。Microsoft とは無関係。docs CC BY 4.0（<a href="LICENSE">LICENSE</a> / <a href="THIRD_PARTY_NOTICES.md">THIRD_PARTY_NOTICES</a> / <a href="LEGAL.md">LEGAL</a>）。
AI に読ませるときは「この URL のファイルを参照して」と渡す。まず <a href="knowledge/robin-rules-compact.md">規則（圧縮版）</a> と該当モジュール1本だけ。</p>
""" + "\n".join(rows) + "</body></html>", encoding="utf-8")
print(f"index: {sum(len(v) for v in (idx['robin'], idx['robin_powerfx'], idx['actions'], idx['patterns']))} files, {len(ids)} robin ids")
