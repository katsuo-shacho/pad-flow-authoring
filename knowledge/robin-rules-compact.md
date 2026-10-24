# Robin 規則・圧縮版（貼付が無言で捨てられる原因の上位。全文は robin-rules.md）
出典: JoeG592/pad-robin-action-kb (CC BY 4.0) 要約
V3  `%…%` は文字列 `$'''…'''` の内側だけ。式は裸: `SET X TO N + 1`, `IF Files.Count = 0 THEN`
V1  文字列 `$'''v'''`、空 `$''''''`、真偽 True/False、数値は裸。出力 `Name=> Var`
V4  enum は完全修飾 `Module.EnumType.Value`、KB の許可値のみ
S6  文字列内の `'` は `\'`（SQL/XPath/JS 注意）。`%…%` 式内の `'` はそのままで可
S7  変数の直前と閉じ引用符直前の `\` は二重: `$'''C:\Dir\\%Name%'''`, `$'''C:\Tmp\\'''`。`\%` は書かない
S8  UNC は `\\\\server\share`。S9 リテラル % は `%%`
N11 予約語を変数名・プロパティ名に使わない（From To Step End In Then If Else Loop Set Wait Next Exit Label Goto Call Case Default Switch Block Error On Not And Or Mod True False Global Disable Function Throw）→ `Mail['From']`
N12 変数は英字始まり。N13 使う変数は SET／出力／ループ変数のどこかで定義する
T15 1行1文。T16 IF…THEN/ELSE IF…THEN/ELSE/END、SWITCH/CASE = 1/DEFAULT/END、LOOP FOREACH x IN l/END、LOOP i FROM a TO b STEP 1/END、LOOP WHILE (A) < (B)/END、EXIT LOOP、NEXT LOOP、LABEL/GOTO、WAIT n、EXIT Code: 0
T18 CASE は比較のみ。T19 条件アクションは `IF (Action …) THEN`。`ELSE IF (Action…)` 不可 → ELSE 内に IF を入れ子
T20 エラー処理: アクション直後に `ON ERROR REPEAT n TIMES WAIT s` → `ON ERROR <Name>` → `ON ERROR` → 1つの END。ハンドラー内は SET/CALL/GOTO/THROW ERROR のみ（IF 不可）。群は `BLOCK Name` / `ON BLOCK ERROR` … `END` … `END`
T21 ON ERROR は KB で「ON ERROR可」のアクションだけ、例外名は宣言済みのみ。不可なら BLOCK で囲む。WAIT (…) は常に可
T22 コメント `# …` `/# … #/`、領域 `**REGION`/`**ENDREGION`、無効化は行頭 `DISABLE `
T23 ヘッダー（@@…, IMPORT, @SENSITIVE）とサブフロー定義（FUNCTION…END FUNCTION）は貼らない。サブフローは Designer で作り本体だけ貼る。CALL に引数は付けられない
T24 裸の `Database.Connect` / `Scripting.RunPythonScript` は削除済み。セレクター付き ID を使う
型: String/DateTime/FileObject/FolderObject → `$'''…'''`。Int/Decimal → 裸。*InstanceHandle/List/DataTable/CustomObject → 裸の変数名。WebControl/UIControl → `$'''selector'''` か `appmask['Window \'T\'']['Button \'OK\'']`
