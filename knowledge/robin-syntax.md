# Robin（貼付テキスト）メモ — 公開サンプルからの観測

**規則の正本は references/robin-rules.md、ID・引数・enum・エラー名の正本は references/robin-index.md → robin/<module>.md**
（JoeG592/pad-robin-action-kb, CC BY 4.0, PAD 2.73 で貼付検証済み）。
このファイルは、公開フロー（実運用の例）で見た「使われ方」の補足。規則と食い違う場合は robin-rules.md を優先する。


PADのDesignerで「コピー」したアクションはテキストとして貼り付け可能（公式 designer-workspace）。版が違うと貼れないことがある（公式注記：コピー元とコピー先のDesignerは同じ版にする）。

## 行の形

```
Module.Action[.Variant] Param1: value Param2: value Output=> VarName Output2=> Var2
```
- 1アクション＝1行（複数行文字列は `$'''...'''` 内で改行できる）。
- 入力は `Name: value`、出力は `Name=> Var`。パラメータ名・順序はDesignerコピーに合わせる。
- enum は `Module.EnumType.Value` で書く（例 `Display.Icon.Information`, `Folder.SortBy.Name`, `File.IfExists.DoNothing`）。
- 真偽は `True`/`False`、数値は裸で書く。

## 値・式
- 文字列: `$'''text'''`。内部に `%Var%` で変数展開。`\"` でダブルクォート、正規表現の `\\d` のようにバックスラッシュは二重。
- 変数参照（式位置）: 裸の `VarName`。文字列中は `%VarName%`。
- プロパティ/添字: `DataTableMatches[0]['Row']`、`%CurrentFile.FullName%`、`List[0]`。
- 関数: `IsEmpty(X)`, `NotContains(Text, $'''x''', True)` などは条件式で使える（名前は観測分のみ）。
- リスト/テーブル リテラル: `{ ^['Col1','Col2'], [$'''a''', $'''b'''] }`（`^[...]` がヘッダー行）。
  `Variables.CreateNewDatatable InputTable: {...} DataTable=> T`

## 制御構文
```
SET X TO $'''value'''
SET N TO 0
IF A <> $'''OK''' THEN ... ELSE IF ... THEN ... ELSE ... END
IF (WebAutomation.IfWebPageContains.WebPageContainsText BrowserInstance: Browser Text: T) THEN ... END   # 条件アクションを括弧で
LOOP FOREACH Item IN List ... END
LOOP Idx FROM 1 TO N STEP 1 ... END          # STEP は式も可
LOOP WHILE (Cond) ... END
EXIT LOOP                                   # NEXT LOOP 等の他形はDesignerで確認
LABEL Name   /  GOTO Name
CALL SubflowName
WAIT 2       /  WAIT 0.1
```
- ブロックはインデント＋ `END` で閉じる。ネストは `END` を対応させる。

## エラー処理
アクション行の直後、1段インデントして:
```
    ON ERROR REPEAT 3 TIMES WAIT 5
    ON ERROR
        ...  # 失敗時に実行する行
    END
```
- 「エラー発生時」設定はアクションごと。ブロック単位（BLOCK / ON BLOCK ERROR）の貼付形は観測未確認→Designerで確認。
- 特定例外名での分岐（例 `ON ERROR PageOutOfBoundsError`）は公開例あり。例外名は actions/<group>.md の「例外」欄が手掛かりだが、Robin上の識別子は別物なのでDesignerで確認。

## コメント・領域
```
# 1行コメント（Designerでは「コメント」アクションになる）
/# 複数行
   コメント #/
**REGION 名前
...
**ENDREGION
```

## 公開フローで実際に使われていた Robin アクション名
Designer表示名 ↔ Robin名は同一ではない。網羅は robin-index.md。ここは「実運用でよく出る組合せ」の目安。

| Robin名 | 用途 |
|---|---|
| Display.ShowMessageDialog.ShowMessage / .ShowMessageWithTimeout | メッセージ表示（ButtonPressed=>） |
| Display.InputDialog | 入力ダイアログ（UserInput=>, ButtonPressed=>） |
| Display.SelectFolder / Display.SelectFromListDialog.SelectFromList | フォルダー選択 / リスト選択 |
| Variables.CreateNewList / .AddItemToList / .RemoveDuplicateItemsFromList | リスト |
| Variables.CreateNewDatatable / .AddRowToDataTable.AppendRowToDataTable / .DeleteRowFromDataTable | データテーブル |
| Variables.RetrieveDataTableColumnIntoList / .FindOrReplaceInDataTable.FindItemInDataTableByColumnIndex | テーブル列→リスト / 検索 |
| Variables.IncreaseVariable | カウンター |
| Text.ToNumber / Text.Random / Text.Join / Text.JoinText.JoinWithCustomDelimiter | 変換・結合 |
| Text.SplitText.SplitWithDelimiter / Text.ParseText.RegexParseForFirstOccurrence | 分割 / 正規表現 |
| Text.ConvertTextToDateTime.ToDateTime / Text.ConvertDateTimeToText.FromCustomDateTime | 日時変換 |
| Folder.GetFiles | ファイル列挙（SortBy1..3） |
| File.WriteText / File.RenameFiles.Rename / File.WriteToCSVFile.WriteCSV / File.GetPathPart | ファイル |
| Pdf.ExtractTextFromPDF.ExtractText / .ExtractTextFromPageRange / Pdf.ExtractTablesFromPDF.ExtractTablesFromPage / Pdf.ExtractImagesFromPDF.ExtractImages / Pdf.ExtractPages / Pdf.MergeFiles | PDF |
| Word.LaunchWord.LaunchAndOpen / Word.CloseWord.CloseAndSaveAs | Word |
| Excel.LaunchExcel.LaunchAndOpenUnderExistingProcess / Excel.CloseExcel.Close | Excel |
| Scripting.RunVBScript.RunVBScript | VBScript（Excel の ExportAsFixedFormat 等） |
| System.RunApplication.RunApplication | アプリ起動 |
| Web.DownloadFromWeb.DownloadToFile | HTTPダウンロード |
| WebAutomation.LaunchChrome.LaunchChrome / .AttachToChromeByTitle / LaunchEdge.LaunchEdge / LaunchFirefox.LaunchFirefox | ブラウザー起動 |
| WebAutomation.GoToWebPage.GoToWebPage / .GoToWebPageNoWait / WebAutomation.CloseWebBrowser | 遷移 |
| WebAutomation.GetDetailsOfWebPage（DetailsType: WebAutomation.DetailsType.URLAddress） | ページ情報 |
| WebAutomation.ExecuteJavascript（Javascript: `function ExecuteScript() {...}` / Result=>） | JS実行 |
| WebAutomation.ExtractData.ExtractTable（ExtractionParameters: {[selector, $'''Own Text''', ..., name], ...}） | テーブル抽出 |
| WebAutomation.IfWebPageContains.WebPageContainsText | 条件アクション |

出典: references/snippets/index.md を参照。
