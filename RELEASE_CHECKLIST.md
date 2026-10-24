# Release checklist（リリースのたびに実行。v0.1.0 の結果つき）

| # | 項目 | 方法 | v0.1.0 |
|---|---|---|---|
| 1 | 構成が三層（knowledge / workflow / scripts）＋ prompts / examples になっている | `find` で目視 | OK |
| 2 | SKILL.md の frontmatter（name / description）が有効、本文 10KB 以下 | スクリプト | OK（9.9KB） |
| 3 | Markdown 内の相対参照がすべて実在する | スクリプト | OK（0 件） |
| 4 | scripts がすべてコンパイル・実行できる（lint / mermaid / timing / prompt pack） | smoke test | OK |
| 5 | lint が KB プローブ corpus で誤検出 0 / 無言却下 107/107 | corpus test | OK |
| 6 | 生成ファイル全部に出典・ライセンス・「挙動の記録」の一文 | grep '出典:' | OK（actions 52 / robin 46 / robin-powerfx 46 / catalog 2） |
| 7 | 転載した第三者テキストが THIRD_PARTY_NOTICES に全部ある（MIT は全文） | 目視 | OK |
| 8 | GPL／ライセンス未記載素材の本文が混入していない | 固有語 grep | OK |
| 9 | 画像・ロゴ・スクリーンショット・バイナリを含まない | find | OK |
| 10 | 「公式」「Microsoft 認定」等の誤認表現がない。README 冒頭に非公式・無関係の明記 | grep | OK |
| 11 | 個人情報・認証情報・社内ホスト名・勤務先固有語がない | grep | OK |
| 12 | scripts に eval / exec / subprocess / ネットワーク呼び出しがない（build_* の curl は README の手順のみ） | grep | OK |
| 13 | 外部読込は CDN の mermaid（フローチャート HTML）だけ。オフラインでは .mmd を使う | grep | OK |
| 14 | .gitignore に work/ と __pycache__ | 目視 | OK |
| 15 | CHANGELOG と README の版が一致 | 目視 | OK |
