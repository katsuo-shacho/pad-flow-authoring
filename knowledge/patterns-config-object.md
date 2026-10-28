# 定石: 環境依存の値をカスタムオブジェクトに集約する（REGION 00/01/02 方式）

出典: 本プロジェクトの自前検証（模擬サイトでの PAD フロー改修、PAD 2.73 / Classic）から整理した設計知見。実サイトでの全工程は未検証。

## なぜ
- 開発環境（模擬サイト・ダミーデータ・高性能 AI）と本番環境（会社の PC・安いモデルか AI 無し）が違うとき、**本番で触るのは冒頭の JSON だけ**にできる。コード本体は一切変えない。
- 本番側では、AI が無くても人が手で JSON を書き換えれば動く。AI があっても「このオブジェクトの値だけ直して」と頼むだけで済み、安いモデルでも間違えにくい。
- 会社固有の値（URL・セレクター・パス・フロー ID）を**ファイル1か所**に閉じ込められるので、公開リポジトリには模擬用の値だけを置き、会社用の REGION 00 は社内の OneDrive に別ファイルで持てる。

## 3つに分ける
フロー冒頭に `Variables.ConvertJsonToCustomObject` を3回置く（貼付検証済み）。

| REGION | 中身 | 本番で触るか | 例 |
|---|---|---|---|
| **00 環境設定** | 接続先 URL、検索欄・ボタンの CSS セレクター、保存先、連携先フロー ID、取得方式の切替 | **触る**（環境ごとに必ず） | `BaseUrl`, `SearchInputSelector`, `SearchButtonSelector`, `BrowserDownloadFolder`, `NextFlowId` |
| **01 文言と初期値** | 画面タイトル・ボタン名・ログ各行のテンプレート（`{ID}` `{日時}` `{名前}` `{理由}` 等の置換子）、フォームの初期値 | 文言を変えたいときだけ | `初期_ID`, `画面_入力タイトル`, `ログ_成功行` |
| **02 固定値** | 待機上限・ポーリング間隔・並列数・バッファ上限・一致パターン・「結果が出た印」「失敗の印」のセレクター | 普通は触らない（サイトの挙動が違うときだけ） | `ResultWaitSeconds`, `StableSeconds`, `MaxParallelFetch`, `LinkMustMatch`, `ArrivalText`, `FailedSelector` |

```
**REGION 00 環境設定（本番ではここだけ書き換える）
#  BaseUrl              : 検索画面の URL
#  SearchInputSelector  : 検索欄の CSS セレクター（F12 → 要素を右クリック → Copy selector）
#  SearchButtonSelector : 検索ボタンのセレクター。空なら検索欄で Enter
Variables.ConvertJsonToCustomObject Json: $'''{
  "BaseUrl": "http://127.0.0.1:8765/",
  "SearchInputSelector": "#searchInput",
  "SearchButtonSelector": "#searchButton",
  "NextFlowId": ""
}''' CustomObject=> Env
**ENDREGION
```
各キーの意味は JSON の直前に `#` コメントで1行ずつ書く。本番で触る人はこのコメントだけ読めばよい。

## 作法
- **参照は `Env['BaseUrl']` / `%Env['BaseUrl']%`**。コード本体に URL や パスのリテラルを書かない。grep で `http` `C:\` が REGION 00 以外に出たら設計違反。
- **JSON 内の `'` は `\'`**、`\` は `\\`（robin-rules S6/S7）。セレクターに `'` を含むときは特に注意。
- **模擬用の初期値を入れたまま配布**し、「初期値は模擬用。本番では REGION 00 の n 項目を変える」と README と画面の両方に書く。会社用の値は初期値に混ぜない。
- **設定の表示**: 入力フォームの先頭に接続先（BaseUrl 等）を編集不可で小さく出す。利用者が「どこに繋いでいるか」を実行前に目で確認できる。
- **リストはそのまま JSON 化できない**ことがある。カスタムオブジェクトに包んで `ConvertCustomObjectToJson` で変換する。
- **JS / PowerShell へは JSON のまま渡す**。PAD 側で項目ごとに変数へ展開しない（アクション数が増える）。スクリプト側で `JSON.parse` / `ConvertFrom-Json` する。
- **環境ごとの差分は REGION 00 の JSON だけを diff** すれば分かる。移植時のレビューはそこだけ見る。

## AI への頼み方（本番側）
「REGION 00 の JSON だけを、次の値に書き換えて。他の行は触らない: BaseUrl=…, SearchInputSelector=…」。安いモデルには「JSON の値だけ」「キーは増やさない」「`'` は `\'`」の3点を添える。出力は REGION 00 のブロックだけでよい（貼付は Designer でそのブロックを選択して置換）。

## 関連
- 受付と完了確認の分離: patterns-download-pipeline.md
- 貼付テキストの構造: paste-format.md
