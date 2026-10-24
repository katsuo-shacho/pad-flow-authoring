# 自己テスト表（模擬貼付）と GATE

| 行 | 内容 | 判定 | 根拠 |
|---|---|---|---|
| 1-3 | コメント | OK | T22 |
| 4-8 | SET 定数 | OK | V1, N12, 予約語なし |
| 9 | Folder.GetFiles | OK | K1 robin/folder.md、enum Folder.SortBy.* 完全修飾 V4 |
| 10-13 | IF Files.Count = 0 … EXIT | OK | V3（% は文字列内のみ）、T16 |
| 14-16 | IF (Folder.IfFolderExists.DoesNotExist …) | OK | T19 条件アクションは IF (…) THEN |
| 17-18 | SET Idx / LOOP FOREACH | OK | T16、CurrentFile 定義 N13 |
| 19-25 | ReadCSV + ON ERROR REPEAT → ON ERROR → END | OK | T20 順序、ハンドラー内は SET のみ、T21 ReadCSV は ON ERROR 可 |
| 26-33 | IF ReadOk / IF Idx = 0 / Merge / END | OK | T16 END 対応、enum Variables.MergeMode.AddExtraColumns V4 |
| 35-37 | Excel Launch / WriteCell / CloseAndSaveAs | OK | K2 引数名一致（XmlMapName は空文字 `$''''''` V1） |
| 38-39 | File.Move / LogMessage | OK | enum File.IfExists.Overwrite、`%Idx%` は文字列内 V3 |
| 40-43 | IF DebugMode = False → ShowMessage | OK | 複数行文字列 T16、`'` なし S6 |

GATE: PASS 8/8

## エージェント環境の lint 結果（KB 3.4.0 / PAD 2.73）
```
== examples/csv-to-excel/Main.robin: 2 issue(s)
  ADVICE L19 [P2] ループ内の定数 SET ReadOk: ループ外へ出せないか   → 不採用（毎回のリセットが必要）
  ADVICE L23 [P2] 同上
exit=1（FATAL/ERROR なし）
```
初稿では `ON ERROR` ハンドラー内に `NEXT LOOP` を書いて ERROR T20 が出た。フラグ方式に直して PASS。

## 実機テスト計画（利用者）
1. `ZZ_Paste_Test` に貼る。空になれば V3/S6/S7 の順に疑う（この例では該当なし）
2. テスト CSV 3 件（うち1件は列が1つ多い）を `C:\Work\csv-in` に置き、`DebugMode` を True にして実行
3. 期待値: `combined.xlsx` の行数 = 3 件の行数合計、列は和集合、`csv-done` に 3 件、ログ末尾「完了: 3 件結合, 失敗 0 件」
4. `DebugMode` を False に戻し、本番入口（完了ダイアログあり）で1回
