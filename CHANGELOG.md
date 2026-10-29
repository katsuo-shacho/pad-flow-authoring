# Changelog

## 0.2.0 — 2026-10-29
- knowledge: patterns-browser-fetch.md（現行の取得定石: ページ内 fetch → base64 → PowerShell 保存、window 台帳、JSON 受け渡し、実時間の待ち、状態判定、最終照合）と silent-kills.md（無言拒否・貼付失敗の実例と検査手順）を新設。patterns-download-pipeline.md を「旧方式」と明記。SKILL.md に書くときの決まり2行。

## 0.1.2 — 2026-10-29
- .github/workflows/release.yml: main への push で CHANGELOG の版を読み、未公開ならタグ・Release・portable zip を自動作成（releases/latest/download の固定 URL）。
- scripts/make_portable.py: OneDrive／ローカルに置いて辞書的に参照するポータブル版 zip（START_HERE.md 入り）。README の導入表に追加。

## 0.1.1 — 2026-10-29
- knowledge: patterns-config-object.md（環境依存の値を REGION 00/01/02 のカスタムオブジェクトに集約。本番では 00 の JSON だけ書き換える）。patterns-download-pipeline.md に自前検証からの一般則を追記（fetch/click の2方式、ログイン判定、data-* に頼らないサイト適合、VBScript を土台にしない、貼付で実際に起きた失敗 等）。
- workflow: 02-design / 03-principles に設定集約の規則、06-autonomous-loop に本番への引き渡し手順。
- GitHub Pages: knowledge/ と prompts/ をそのまま公開する workflow（.github/workflows/pages.yml）と、index.json / robin-ids.json を作る scripts/build_site_index.py。目次のある Web サイトとして辞書を URL で引ける。
- README: 環境別の導入手順、有効化の3問チェック、開発→本番の持っていき方。

## 0.1.0 — 2026-10-25
- 初版（実験的）。三層構造: knowledge（辞書）/ workflow（00-06）/ scripts（引き出し）/ prompts（モード別キックオフ）。
- knowledge: 公式アクション群 52 群 460 項目の要約カタログ、Robin ID 1,086 件（Classic / Power Fx）、構文規則（全文・圧縮版）、公式 how-to 64 本の索引、貼付テキストの構造、公開実例。
- scripts: robin_lint.py（KB 付属プローブ 456 件で検証: 無言却下 107/107・エラー 23/27 検出・誤検出 0/322）、robin_to_mermaid.py、analyze_timing.py、make_prompt_pack.py、build_catalog.py、build_robin.py。
- workflow: モード（Chat / Interactive / Autonomous）、計画→GO、アルゴリズム設計、操作手段の選定（コネクタ→ショートカット→UI要素）、出力ゲート（判定表→GATE→Robin）、検証、自走ループ。
- examples/csv-to-excel: 01→05 を通した見本。
- LICENSE（docs CC BY 4.0 / scripts MIT）、THIRD_PARTY_NOTICES、LEGAL、CONTRIBUTING。
