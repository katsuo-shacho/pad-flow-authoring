# ブラウザー取得・OneDrive・Excel入力

（自分の環境での実測知見はここに追記する。以下は公式 how-to の要点と、原則の適用例。）

## ブラウザーからのダウンロード
- まず `Web.DownloadFromWeb.DownloadToFile`（HTTP直接）で済むか確認する。認証が必要なら、ブラウザーを起動してセッションを持った状態で、ダウンロードURLをJSで取り出し（`ExecuteJavascript` → Result）、保存はブラウザーに任せる。
- ブラウザーの「名前を付けて保存」ダイアログは UI オートメーション対象（公式 how-to/automate-browser-prompts、kinuasa の保存ダイアログ例）。ファイル名は `Send keys` で入れるより、ダウンロード先フォルダーを固定して後からリネームする方が安定。
- 完了待ちは固定 WAIT ではなく `Wait for file`（存在）＋ 一時ファイル（`.crdownload`/`.partial`）の消失確認。
- 公式 how-to: handle-iframes, click-elements-list-links, get-coordinates-size-web-element, automate-browser-prompts。

## OneDrive / SharePoint 同期フォルダー
- ローカル同期パスを使う場合、同期遅延があるので「書いた直後に別プロセスが読む」構造を避ける。書込み→`Wait for file`→読込。
- パスは入力変数または設定ファイル（`tests/` と分離）から読み、ユーザー名を含むパスをハードコードしない（`%USERPROFILE%` 相当は `Get environment variable`）。
- クラウド側に直接書く必要があるなら SharePoint アクション群（actions/sharepoint.md）か、クラウドフロー連携を検討。

## Excel 入力
- 1セルずつ書かない。データテーブルを作って `Write to Excel worksheet` に一括で渡す（データテーブルは範囲に展開される）。
- 読むときも範囲を1回で読む（`Read from Excel worksheet`、「範囲の最初の行を列名として」オプション）。ループで行を読まない。
- 書式・列幅・PDF出力など Excel 固有の操作は VBScript で一括（公式 how-to/autofit-excel-columns-vbscript, convert-excel-pdf-vbscript）。
- 起動は `Launch Excel`（既存プロセス下で開く変種あり）、終わりは必ず `Close Excel`（保存指定）。利用者が同じブックを開いている可能性があるときは `Attach to running Excel` を先に試す。
- CSV→Excel は公式 how-to/convert-csv-excel。

## 入力フォーム
- 複数項目の入力は `Display custom form` に集約（03-principles.md）。ファイル選択は File input 要素、フォルダーは `Display select folder dialog`。
- 利用者が途中でキャンセルしたら `ButtonPressed` を見てフローを安全に終える（開いたExcel/ブラウザーを閉じる）。
