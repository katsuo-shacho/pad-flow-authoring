# 互換性: 貼付テキスト・埋込コード・コミュニティ部品

（自分の環境での実測知見はこのファイルに追記する。以下は公開情報から確認済みの事項。）

## 貼付テキストの正体
- Designerで選択→コピーすると、クリップボードには「アクション行（Robin）」＋ UI要素・画像があれば末尾に
  `# [ControlRepository][PowerAutomateDesktop]` 行と JSON（`ControlRepositorySymbols`/`ImageRepositorySymbol`/`ConnectionReferences`）が付く。
  この JSON があるとサイズが数百KBになることがある。差分比較では JSON 部を分けて扱う。
- UI要素は `appmask['Window \'...\'']['Button \'...\'']` の形で参照され、録画由来の行には `@@source: 'Recorder'` が付く。
  appmask を含む行は、リポジトリ JSON ごと貼らないと「UI要素が見つからない」になる。
- 公式注記: コピー元とコピー先の PAD は同じ版にする。版が違うとアクションやUI要素が認識されないことがある。
- 貼付先は Designer の作業領域（Main または任意サブフロー）。サブフロー名は貼付テキストに含まれないので、`CALL X` を使う部品は X を先に作る。

## Classic と Power Fx
- Power Fx 有効フローでは式が `=` 始まりになり、`%...%` 記法や関数名が異なる。部品はどちら向けか明記する。混ぜない。
- 既存フローの種別は Designer のフロー プロパティで確認（公式 power-fx）。

## 埋込コード（スクリプト アクション）
- 公式のスクリプト アクション: Run DOS command / Run VBScript / Run JavaScript / Run PowerShell script（出力 `PowershellOutput`、既定タイムアウト10秒） / Run Python script（Python 2.7 または 3.4、出力 `PythonScriptOutput`） / Run .NET script。エラーは `ScriptError`。
  値を返すには PowerShell は `Write-Output`、Python は `print`（公式 scripting「Working with variables」）。
  スクリプト本文は `$'''...'''` に入り、`%Var%` はスクリプト実行前に展開されるので、スクリプト内のリテラル `%` は `%%` と書く。Robin名は観測済みの `Scripting.RunVBScript.RunVBScript` 以外は Designer コピーで確認。
- `WebAutomation.ExecuteJavascript` は `function ExecuteScript() { ... }` の形が必須。return 値が Result。
- VBScript で Excel COM を触るときは、PADのExcelインスタンスと別プロセスにならないよう `LaunchAndOpenUnderExistingProcess` や GetObject で合わせる（公式 how-to/convert-excel-pdf-vbscript, autofit-excel-columns-vbscript）。

## コミュニティ部品を取り込むとき
- 出典・ライセンス・確認版を snippets/index.md に記録する。
- 環境依存（言語別のウィンドウタイトル、座標クリック `MouseAndKeyboard.SendMouseClick.ClickAt X: Y:`、固定パス）は貼る前に置換する。
- 未知のアクション名・enum・引数は Designer で最小例を作ってコピーし、名前を照合してから採用する。推測で補わない。

## 差分比較の約束
- 比較対象は「アクション行」のみを正規化（前後空白・改行コードは正規化してよい。文字列リテラル内部は触らない）。
- リポジトリ JSON は別ファイルに切り出し、UI要素の増減だけを見る。
- Designer が保存時に並べ替える既知の差（パラメータ順・既定値の省略）は版ごとに記録し、それ以外の差は差分として報告する。
