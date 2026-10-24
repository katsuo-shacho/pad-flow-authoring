# Robin 構文規則（貼付検証済み）

出典: PAD Robin Action Knowledge Base, Joe Green, CC BY 4.0, https://github.com/JoeG592/pad-robin-action-kb
（README「Syntax rules PAD enforces」を日本語に要約。PAD 2.72/2.73 で 443+13 件の貼付プローブにより確認されたもの。）
**失敗の大半は無言**：1行でも違反すると貼付全体が捨てられ、キャンバスは空のまま。エラーも出ない。

## 使い方（二表方式）
Robin を「書く」のではなく、`robin/<module>.md` の検証済み例をコピーして値だけ差し替える。
値の書き方は下の型表に従う。これで初回貼付の成功率が大きく上がる（作者の実測: 1/5 → ほぼ毎回）。

## 値
1. 文字列 `$'''value'''`、空文字 `$''''''`。真偽は裸の `True`/`False`、数値も裸。
2. 変数参照は裸の名前 `Instance: ExcelInstance`。式も裸: `SET Total TO Price * Qty`、`IF Files.Count = 0 THEN`、`Items[-1]`、`Row['Amount']`、`Obj.a.b`。
3. **`%...%` は文字列の内側だけ**: `$'''Saved %Count% files'''`。`SET X TO %N + 1%` や `IF %N% = 5` は全体却下。
4. enum は `Module.EnumType.Value` と完全修飾（型を持つモジュールで）。値は KB の enumValues にあるものだけ。
5. 出力は `Name=> Variable`。

## 文字列の内側
6. `\` はエスケープ。**アポストロフィは必ず `\'`**（SQL・XPath・JS に注意）。`%...%` 式の中の `'` はそのままでよい。
7. **変数の直前・閉じ引用符の直前のバックスラッシュは二重に**: `$'''C:\Reports\\%Month%'''`、`$'''C:\Temp\\'''`。通常の文字の前は1つでよい。`\%` は書かない。
8. UNC パスは `$'''\\\\server\share'''`（4つ）。
9. リテラルの `%` は `%%`。
10. 文字列は複数行可（`END` や `#` で始まる行があっても可）。

## 名前
11. 予約語は変数名・プロパティ名に使えない: From, To, Step, End, In, Then, If, Else, Loop, Foreach, While, Set, Wait, Next, Exit, Label, Goto, Call, Case, Default, Switch, Block, Error, On, Not, And, Or, Mod, True, False, Global, Disable, Function, Throw。メールは `Mail['From']` と書く（`Mail.From` は不可）。
12. 変数名は英字（Unicode 可）始まり。
13. 変数は SET／アクション出力／ループ／リスト追加のどこかで必ず定義されていること。
14. 変数名・キーワード・ID・enum・引数名は大文字小文字を区別しない。

## 文
15. 1行1文。インデントは見た目だけ。行末の `# note` は独立したコメント行になる。
16. 組込み文:
    - `SET x TO value`
    - `IF c THEN` / `ELSE IF c THEN` / `ELSE` / `END`
    - `SWITCH x` / `CASE = 1` / `CASE > 5` / `DEFAULT` / `END`（CASE は比較のみ）
    - `LOOP FOREACH item IN list` / `END`
    - `LOOP i FROM 0 TO n - 1 STEP 1` / `END`
    - `LOOP WHILE (A) < (B)` / `END`
    - `EXIT LOOP`, `NEXT LOOP`, `LABEL Name` / `GOTO Name`, `WAIT 5`, `EXIT Code: 0`
17. 条件: `=`, `<>`, `>`, `<`, `>=`, `<=`, `AND`, `OR`, `NOT(...)`, `IsEmpty(x)`, `IsNotEmpty(x)`, `Contains(x, $'''y''', False)`, `NotContains`, `StartsWith`, `EndsWith`。
18. `CASE` は比較だけ（`CASE Contains ...` は却下）。
19. 条件アクション（kind C）は `IF (Action ...) THEN`。`ELSE IF (Action ...)` は不可 → `ELSE` の中に `IF (...) THEN ... END` を入れ子にする。
20. エラー処理:
    ```
    BLOCK ReadFiles
    ON BLOCK ERROR
        SET Failed TO True
    END
        ...actions...
    END

    Text.ToNumber Text: Raw Number=> Amount
    ON ERROR REPEAT 2 TIMES WAIT 5
    ON ERROR TextNotValidNumberError
        SET Amount TO 0
    ON ERROR
        SET Failed TO True
    END
    ```
    順序は REPEAT → 名前付き ON ERROR → 無名 ON ERROR → 1つの END。ハンドラー内に書けるのは `SET`/`CALL`/`GOTO`/`THROW ERROR` だけ（IF は全体却下）。フラグを立てて後で分岐する。`REPEAT` はアクションの ON ERROR のみ（`RetryType: RetryType.Exponential MinInterval: 1 MaxInterval: 10` も可）。`ERROR => LastError` で直前のエラー取得。
21. `ON ERROR` は KB で `on_error: true` のアクションにだけ付ける。名前は KB の errors から。違反すると Designer 上は警告付きで貼れ、コンソール実行はできるが、**クラウド起動時にフロー全体が拒否される**。エラーを出さないアクションは `BLOCK ... ON BLOCK ERROR` で囲む。`WAIT (...)` はタイムアウトし得るので常に ON ERROR 可。
22. コメント `# text` / `/# ... #/`。領域は `**REGION Name` / `**ENDREGION`。行頭 `DISABLE ` で無効化。
23. ファイルヘッダー（`@@ConnectionString`, `IMPORT`, `@SENSITIVE`）やサブフロー定義（`FUNCTION ... END FUNCTION`）は貼らない。サブフローは Designer で作り、本体だけ貼る。
24. 2.72 で消えた ID は「Unknown action」: 裸の `Database.Connect`（→ `.Connect`/`.ConnectOracle`）、裸の `Scripting.RunPythonScript`（→ `.RunPythonScript`/`.RunPythonScript34`/`.RunPythonScriptCPython`）。

## 型の書き方（Type Reference 要約、44型）
- String / DateTime(`$'''YYYY-MM-DD'''`) / FileObject(フルパス) / FolderObject / FileName / CustomErrorCode / WorkQueue(キュー名) / FtpFileObject(`/path/file`) → `$'''...'''`
- Int32 / Int64 / Decimal / Double → 裸の数値。Boolean → `True`/`False`
- 各種 *InstanceHandle（Excel, Word, WebBrowser, Access, Outlook, Cmd, Sap, Terminal, PowerPoint…）、List、DataTable、CustomObject、BinaryObject、Image、OCREngineObject、XmlNodeObject、WorkQueueItem、OutlookMailMessage → **裸の変数名**（先行アクションの出力）
- WebControl / UIControl → `$'''selector'''` またはリポジトリ参照 `appmask['Window \'Title\'']['Button \'OK\'']`
- enum → `Module.EnumType.Value`

## Power Fx フローの場合
`references/robin-powerfx/` を使う。文字列は `$fx'...'` で、Classic の例をそのまま貼ってはいけない（混在不可）。詳細は KB の PROMPT_PowerFx.md。

## 貼付前チェック（KB 付属ツール）
KB リポジトリの `marketing/video/tools/check-flows.js`（Node）は上記規則と KB に照らしてスクリプトを検査する。Node が使える環境ならこれを通してから貼る。
