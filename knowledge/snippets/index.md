# 有志公開の貼付コード 辞書（第3層）

公開されている Robin 形式のフロー。**ライセンスのあるものだけ本文を取り込める**。
ライセンス不明（gist 等）は URL と技法の要約のみ持ち、必要時に WebFetch で読む。
PAD版は公開時点のもの。貼付前に自環境の版と差を疑う。

書式: `- 名前 | 出典URL | ライセンス | 確認版 | 使っている主な技法/Robin名`

## 最重要: Robin アクション KB（取り込み済み → knowledge/robin/, robin-powerfx/, robin-rules.md）
- JoeG592/pad-robin-action-kb | https://github.com/JoeG592/pad-robin-action-kb | CC BY 4.0 | PAD 2.72/2.73 | 1,086 Robin ID（46モジュール）の貼付検証済み例・引数型・enum・エラー名・兄弟セレクター、Classic と Power Fx 両版、構文規則24項、Deployment KB（クラウド配布）。更新は `scripts/build_robin.py` で raw JSON から再生成。

## 取り込み済み（ライセンス明示）
- pnp/powerplatform-snippets: launch-browser-chrome | https://github.com/pnp/powerplatform-snippets/tree/main/power-automate-desktop/launch-browser-chrome | MIT | – | Chrome起動をサブフロー化し、起動済みなら AttachToChromeByTitle、無ければ LaunchChrome。再利用パターンの見本 → snippets/web-browser.md
- ronan-deshays/power-automate-desktop-utility-flows | https://github.com/ronan-deshays/power-automate-desktop-utility-flows | MIT | 2023 | サイトの全記事をPDF保存。ExtractData.ExtractTable で一覧→LOOP FOREACH→ExecuteJavascript、ON ERROR REPEAT → snippets/web-browser.md

## リンクのみ（GPL / ライセンス未記載）
- chriskyfung/Rename-Bank-eStatement-PDFs | https://github.com/chriskyfung/Rename-Bank-eStatement-PDFs-with-PowerAutomateDesktop | GPL-3.0 | – | PDF先頭ページ抽出→正規表現で勘定番号・日付→リネーム。CreateNewDatatable のリテラル、サブフローへの CALL、`/# #/` ヘッダー、InputDialog/SelectFolder の ButtonPressed 確認
- DwayneSelsig/Power-Automate-Desktop-Scripts | https://github.com/DwayneSelsig/Power-Automate-Desktop-Scripts | GPL-3.0 | – | ブラウザー選択→LABEL/GOTO 再試行、ExecuteJavascript でスクロール/クリック/高さ取得、LOOP FROM..TO..STEP、ExtractTable のカスタムセレクター、WriteCSV
- cravelweb: ヒット＆ブロー | https://github.com/cravelweb/robin-hit-and-blow-game-for-power-automate-desktop | 未記載 | – | 基本アクション（Text.Random, リスト, ループ, ダイアログ）だけのゲーム。教材向け
- kinuasa: PDF処理サンプル | https://gist.github.com/kinuasa/86af4f027da2f5f672af3c59e42bf744 | 未記載 | 2.47 | Pdf.ExtractText/ExtractTables/ExtractImages/ExtractPages/MergeFiles、Word→PDF（CloseAndSaveAs）、Excel→PDF（RunVBScript + ExportAsFixedFormat）、ON ERROR で最終ページ検出→EXIT LOOP、**REGION
- kinuasa: 和暦表示 | https://gist.github.com/kinuasa/0395c95de26f16110da5a26c1d30fefb | 未記載 | – | 日時→和暦（令和対応）
- kinuasa: 直近の平日 | https://gist.github.com/kinuasa/b7560aa9b1fb3d844406b89152fd6751 | 未記載 | 2.41 | 日付計算
- kinuasa: 名前を付けて保存ダイアログ | https://gist.github.com/kinuasa/bd147fe3e15b4f75c3bdaea23773c44b | 未記載 | – | UIオートメーションでダイアログ操作
- kinuasa: 電卓ボタン順クリック | https://gist.github.com/kinuasa/a28010619fca56d6cedb946c6876141f | 未記載 | – | UI要素をループでクリック
- kinuasa: PA4d教室 vol.1 | https://gist.github.com/kinuasa/8cf7b203f4be1add3a35e7e01fc7df2c | 未記載 | – | 入門フロー
- kinuasa: 実行中フロー名取得スクリプト / VBAから実行 / PowerShellから実行 | https://gist.github.com/kinuasa | 未記載 | – | 外部からのPAD起動（ms-powerautomate: スキーム周辺）

## 辞書の増やし方
1. 出典・ライセンス・確認版を必ず書く。本文を取り込むのは MIT/Apache/BSD/CC-BY 等の明示があるものだけ。
2. 本文は「そのまま貼れる最小単位」に切り、先頭に `# 出典: URL` コメントを付けて `snippets/<category>.md` に置く。
3. 自分で作って動作確認した部品は `snippets/own-*.md` に、確認したPAD版を添えて置く（これが最も信頼できる辞書になる）。
4. 取り込んだら robin-syntax.md の Robin名表に新しい名前を追記する。

## 探し方
- GitHub: `Power Automate Desktop robin`, `.robin`, `PAD flow copy paste`, 日本語は `Power Automate for desktop フロー コピー`。
- 日本語圏は gist（kinuasa / ka-net.org）、Qiita、各ブログ記事内のコードブロック。
