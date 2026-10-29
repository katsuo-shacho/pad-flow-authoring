# 無言拒否・貼付失敗の実例集（自前検証で実際に起きたもの）

出典: 本プロジェクトの自前検証（PAD 2.73 / Classic）。規則の正本は robin-rules.md（KB 由来）。ここは「実際に踏んだもの」を、検査手順つきで蓄積する。
追記のルール: 1件＝「症状 → 原因 → 直し方 → 検査方法」。実例は会社固有の値を伏せる。

## 貼り付けが「無言で消える」もの（キャンバスが空のまま、エラーなし）
1. **予約語を変数名・ループ変数・ラベルに使う**（実例: `CustomObject=> Wait`）。
   検査: `=> Name` / `SET Name` / `LOOP Name` / `LOOP FOREACH Name` / `LABEL Name` の Name を次と照合（大文字小文字無視）:
   From To Step End In Then If Else Loop Set Wait Next Exit Label Goto Call Case Default Switch Block Error On Not And Or Mod True False Global Disable Function Throw
2. 文字列 `$'''…'''` と `'''{…}'''` の外に `%` がある（V3）。
3. `ON ERROR` 〜 `END` の中に GOTO/SET/CALL/THROW ERROR 以外（実例: `EXIT Code: 0` →「このステートメントは例外処理内に置けません」）。
4. `@@statistics_…` などヘッダー行を貼る（T23）。

## 貼れるが赤くなる・動かないもの
5. アクション ID の版差（実例: `Text.Replace` → 正しくは `Text.Replace.ReplaceText`、`ComparisonType` 必須）。辞書 `knowledge/robin/*.md` を `grep -A6 "^## <ID> \[A\]"` で引いて署名を写す。記憶で引数名・enum を書かない。
6. `$'''…'''` の中の `\"` は JSON に通らない（実例: CSS セレクター `[attr=""]` が壊れた）。引用符が要るときは `\'` を使う。
7. PowerShell 5.1 の `ConvertFrom-Json` は JSON 配列を1個の入れ子にして返す。`@(… | ConvertFrom-Json)` は要素が配列のまま foreach に入る。代入してから `@()` で包む。
8. `$'''…'''` 内の `\` は、変数の直前と閉じ引用符の直前は二重、正規表現の `\d` も `\\d`。`%` のリテラルは書かない（PS は `[char]37`、JS は `String.fromCharCode(37)`）。

## 検査の手順（lint が回せない環境でも）
- 1〜4 は正規表現で機械的に検査してから渡す。結果を一言報告する（「予約語なし／% は文字列内のみ／ハンドラー内は SET と GOTO のみ／ヘッダー行なし」）。
- 5 は使うアクションごとに辞書を引く。
- エージェント環境では `python3 scripts/robin_lint.py flow.robin --kb <KB json>`（1〜4 と 5 を機械検査）。
