# 設計: csv-to-excel

処理順
1. 一括取得: `Folder.GetFiles`（FileFilter *.csv、名前順）。`Files.Count = 0` なら `EXIT Code: 0`（早期終了）
2. 移動先フォルダーが無ければ作る（`Folder.IfFolderExists.DoesNotExist` → `Folder.Create`）
3. ループ（残るループ）: `File.ReadFromCSVFile.ReadCSV`（1行目=列名）→ 1件目は `SET Combined TO CSVTable`、2件目以降は `Variables.MergeDataTables`。再試行はこの読取1行だけに `ON ERROR REPEAT 2 TIMES WAIT 2`、失敗はフラグ `ReadOk` と件数に記録して続行（ハンドラー内に IF/NEXT LOOP は書けない）
4. 一括書込み: `Excel.LaunchExcel.Launch`（非表示）→ `Excel.WriteToExcel.WriteCell`（A1 にテーブルを1回）→ `Excel.CloseExcel.CloseAndSaveAs`
5. 一括移動: `File.Move`（上書き）→ `Logging.LogMessage` → `DebugMode = False` のときだけ完了ダイアログ

操作手段の選定表
| 操作 | 候補 | 採用 | 理由 |
|---|---|---|---|
| CSV 読取 | 専用アクション / PowerShell | 専用アクション | 列名行の扱いと区切りが引数で済む |
| 結合 | MergeDataTables / PowerShell で一括 | MergeDataTables | 件数 50 以下なら十分。500 超なら PowerShell 一括に切替 |
| Excel 出力 | 専用アクション / COM | 専用アクション | テーブルを1回で書ける |
| 利用者通知 | ShowMessage | ShowMessage | 入力は無いのでカスタムフォーム不要 |
UI 要素依存: 0 行

堅牢性: 0件 → 早期終了。読取失敗 → 件数に記録して続行。列不一致 → AddExtraColumns。
速度: ループ本体 2 操作＋フラグ。WAIT なし。ループ内の `SET ReadOk TO True` は毎回のリセットに必要（lint の ADVICE は理由付きで不採用）。
