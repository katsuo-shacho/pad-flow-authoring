# 開発原則

優先順: 動く > 戻せる > 少ない > 速い。改修は「同条件の実測差分」でのみ正当化する。

## ステップ数を増やさない
- 1アクションで済むものを複数アクションに分解しない。アクション数は実行時間・ログ量・保守コストに直結する。
- まとまった処理（文字列整形、集計、ファイル一括処理、DOM操作）は **1ブロックのスクリプトで完結させる**：
  - Web: `WebAutomation.ExecuteJavascript`（`function ExecuteScript(){ ... return x; }` → `Result=>`）。クリック・スクロール・値取得をJS側で一度にやる。
  - OS/ファイル/データ変換: `Scripting.RunPowershellScript`（公式 how-to/convert-data-powershell）、`Scripting.RunVBScript`（Excel/COM）。
  - 判定: 1つの `IF` に条件式をまとめる（`AND`/`OR`、`IsEmpty()`, `Contains()`）。
- スクリプトに寄せる判断基準: PAD側で3アクション以上になり、かつUI要素に触らない → スクリプト化を検討。UI要素操作はPADアクションのまま。

## ループを軽くする
- ループ本体のアクション数を最小にする。**ループ内で変数設定（SET）や型変換を繰り返さない**：ループ外で一度だけ作る、または不要なら作らない。
- ループ前に対象を絞る（`Folder.GetFiles` の FileFilter、データテーブルの検索、リストの重複除去）。
- ループ自体をブロック処理で置換できないか先に検討する（テーブル一括書込み、PowerShellでの一括リネーム、JSでの一括抽出）。
- ループ内の `WAIT` は原則禁止。待機は条件付き（UI要素の出現待ち、ファイル存在待ち）にし、上限回数/時間を付ける。
- `LOOP WHILE` には必ず脱出条件とセーフティカウンター（上限）を付ける。

## 待機
- 固定 `WAIT` は手段として最後。使うなら最短値で、合計10個未満・600秒未満（Flow Checker）。
- 待ちは「状態の確認＋再試行（`ON ERROR REPEAT n TIMES WAIT s`）」で表現する。

## 変数
- 環境依存の値（URL・セレクター・パス・フロー ID・待機上限）はフロー冒頭のカスタムオブジェクト（REGION 00/01/02）に集約し、本体にリテラルを書かない。移植は REGION 00 の JSON を書き換えるだけにする。
- 名前は40文字以内、入出力変数は25個以内、既定値を必ず設定（Flow Checker）。
- 一時変数はサブフロー内のスコープ変数（scoped-variables）に寄せ、Mainを汚さない。
- 機密は「機密としてマーク」または暗号化入力。平文のパスワードを貼付テキストに残さない。

## 構造
- サブフローは「再利用される」または「単体で検証したい」単位でだけ切る。数アクションだけのサブフローは作らない（Flow Checker: Not needed subflow）。
- `IF` は5段を超えてネストしない。空のIF/Elseだけの IF を残さない。
- `GOTO`/`LABEL` は再試行や早期終了にだけ使い、通常制御に使わない。
- 到達不能なアクション・無効化したままのアクションを配布版に残さない。
- サブフロー間の相互再帰を作らない。

## エラー処理
- 失敗しうるアクションにはアクション単位の「エラー発生時」で再試行または代替を設定する。ブロックエラーを置くなら中身を必ず書く（空のブロックエラー禁止）。
- 利用者向けの失敗通知は1か所（Mainの末尾 or 専用サブフロー）に集約する。

## UI 要素は最後の手段
環境（画面解像度、言語、ウィンドウタイトル、DOM の変更、拡張機能の状態）で壊れるのは UI 要素依存の部分なので、順位を決めて選ぶ。
1. **用意されたアクション／コネクタで済ませる**（第一選択）: Excel・Word・Outlook・Exchange・SharePoint・データベース・ファイル／フォルダー・PDF・圧縮の専用アクション、クラウド コネクタ アクション群（catalog.md の Cloud connectors）、HTTP（Web.* / Invoke web service）。次点でブラウザー内 JS（ExecuteJavascript で DOM を直接読む・押す）、PowerShell／VBScript／COM。
2. **キーボード ショートカット**: アプリにショートカットがあるなら、UI 要素を取るより `Send keys`（例 `{Control}({S})`）で操作する。ウィンドウのフォーカスを `Focus window` で確実にしてから送る（公式 how-to/automate-applications-keyboard-shortcuts, ensure-windows-become-focused）。文言・位置に依存しないので UI 要素より安定。
3. **確実に取れる UI 要素だけ使う**: 変わらない識別子を持つもの。デスクトップは AutomationId／Name／ClassName が固定の要素、Web は `id`・`name`・`data-*` 属性で一意に取れる要素。カスタムセレクターにしてその属性だけで書く（build-custom-selectors）。
4. **避ける指定**: 位置・順序（`:eq(n)`、兄弟の何番目）、表示文字列（ローカライズ・動的文言）、座標クリック（`ClickAt X: Y:`）、ウィンドウタイトル全文（部分一致＋ワイルドカード `*` にする）、画像認識／OCR（最終手段、解像度依存）。
5. **使うときの作法**: UI 要素を使う行は少数に集約（1サブフロー）し、`WAIT (UIAutomation.WaitForWindow… / Wait for web page content) FOR n` で出現を待ち、失敗時は `ON ERROR` で再試行→利用者通知。貼付テキストには UI 要素リポジトリの JSON が付くので（paste-format.md）、UI 要素付きの部品は版・環境を明記して配布する。
6. 設計時に「この UI 要素は何で一意か」を1行書けないなら、1 の方法に戻す。

## 利用者UI
- 複数入力は `Display custom form`（Adaptive Cards）に集約し、`ButtonPressed` で分岐する。入力ダイアログの連打より速く、キャンセル処理も1か所で済む。
- フォームのアクション（ボタン）は末尾にしか置けない。要素IDは英字始まり・一意。
- 本番フローには利用者操作（開始確認、途中確認、完了通知）を入れる。デバッグ用入口では省略できるように作る（→ 05-verify.md）。

## Flow Checker（公式静的解析）ルール一覧
出典: static-analysis.md。Designer右の Flow Checker が同じ指摘をする。
- Unsafe password security（Security）: 平文パスワード → 暗号化入力/機密変数/Get Credential
- Recursion between two subflows（Design）
- Variable length exceeded（40文字）
- Input variable default values（入出力変数に既定値）
- Threshold on number of input and output variables（25個）
- Empty on block error action（空のブロックエラー）
- Nested if clauses（5段超）
- Incomplete if（中身のないIF / Elseのみ）
- Infinite loop（終了条件のないループ）
- Misuse of wait actions（WAIT 10個超）
- Immense wait time（固定WAIT合計600秒超）
- Unreached actions（到達不能）
- Not needed subflow（空・無効化のみ・数アクションのサブフロー）
