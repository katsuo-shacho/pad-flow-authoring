---
name: pad-flow-authoring
description: Power Automate Desktop（PAD）のフローを、計画→設計→Robin組立→検査→検証→改善の順で作る。公式アクション一覧を入口に、貼付検証済みの Robin 辞書（1,086 ID）を引いて貼付テキストを自動生成し、AI 内の模擬貼付テストで貼る前にほぼ100点にする。エージェント環境では実機検証・時間解析・自走改善まで行う。クラウドフローだけの作業には使用しない。
---

# PAD Flow Authoring

**核**: 製品の挙動をまとめた非公式ドキュメント（knowledge/）から推論して、貼って通る Robin を出す。
**進め方**: まず workflow/00-modes.md でモード（Chat／Interactive／Autonomous）を決め、01→06 の順。利用者とは「計画で GO」「設計で1回確認」「本番取り込み前」の3点だけ往復し、あとは進める。モードをまたぐ成果物は plan.md / design.md / tasks.md。
**原則**: 動く > 戻せる > 少ない > 速い（workflow/03-principles.md）。用意されたアクション／コネクタを第一選択、次にキーボード ショートカット、UI 要素は「何で一意に取れるか」を書けるときだけ・最後の手段。

## 構成
- `knowledge/` 辞書。公式群カタログ（catalog.md、自分の memo 行つき）→ Robin ID 辞書（robin-index.md → robin/<module>.md、Power Fx は robin-powerfx/）→ 構文規則（robin-rules.md）→ 公式仕様・how-to・方法論の索引（actions/、howto-index.md、official-guides.md）→ 貼付テキストの構造と互換性（paste-format.md）→ 公開フローの実例と定石（snippets/、patterns-*.md）。
- `workflow/` 進め方。00-modes（対話／自走／プロンプトだけ の使い分けと承認ゲート）、01-plan（要件・見積もり・GO）、02-design（アルゴリズム設計）、03-principles（開発原則）、04-environments（AI 内で完結する層／Copilot だけ／エージェント）、05-verify（デバッグ入口・本番入口・テスト）、06-autonomous-loop（無人で回す）。
- `prompts/` モード別キックオフ（chat / interactive / agent）と、チャットでフックを再現する手順（chat-lookup-protocol）。
- `examples/` 01→05 を通した見本（csv-to-excel）。書式に迷ったらこれを真似る。
- `scripts/` 引き出し。robin_lint.py（貼付前検査＋静的レビュー）、robin_to_mermaid.py（フローチャート）、analyze_timing.py（時間解析）、make_prompt_pack.py（Copilot 用の貼付パック）、build_catalog.py / build_robin.py（辞書の再生成）。

## 手順

0. **モード** workflow/00-modes.md。環境から Chat／Interactive／Autonomous を決め、prompts/<mode>-kickoff.md の最初の質問（対話で進めるか、いきなり作るか）を1回だけする。
1. **計画** workflow/01-plan.md。要件カードを埋め、方針・見積もり・検証方法を1枚にして GO を取る。末尾で「PAD でなくてよいのでは」を1回だけ判定し、Excel マクロ／VBScript／ブックマークレットが明確に向くときだけ「技術選定メモ」を短く添える（手段・何がどう楽になるか・前提、3文まで。Python／.NET は「もしインストールできるなら」の条件付きで弱く）。実装中には出さない。主導権は開発者。返事が無ければ PAD 版を進め、本線を脱線させない。既存フローがあれば現行コード（手編集含む）を退避し、戻し先を確保する。
2. **設計** workflow/02-design.md。データの流れを先に決め、一括化・ループ削減・ループ内ブロック削減・再試行・チェックポイントを明記。必要なら Mermaid で分岐と繰返しだけ描く。利用者に1回確認。
3. **引く** knowledge/catalog.md を grep して群を決める → knowledge/robin-index.md で ID → knowledge/robin/<module>.md の例をコピーして値だけ差し替える（二表方式）。KB に無い ID・引数・enum は推測せず「Designer で確認」とする。仕様の意味は knowledge/actions/、やり方は howto-index.md から1本だけ読む。
4. **組む** knowledge/robin-rules.md を守って Robin を書く。利用者 UI はカスタムフォームに集約し、本番の利用者操作と DebugMode 入口を両方持たせる（workflow/05-verify.md）。
5. **AI 内で検査** workflow/04-environments.md「共通」。模擬貼付テスト（規則番号つきで1行ずつ判定）と静的レビュー（まとめられる処理・減らせるループ・ループ内の SET/WAIT）を優先度つきで出す。全行 OK になるまで直す。エージェント環境なら `python3 scripts/robin_lint.py flow.robin --kb <KB json>` で FATAL/ERROR 0 を機械的に確認。
6. **届ける／検証する** Copilot だけ・ツール無しの環境では、ここで Robin と判定表と貼り方（サブフローは Designer で作り本体だけ貼る、版の一致）を渡して終わり。エージェント環境では workflow/04-environments.md「B」に従い、検証用コードで利用者操作をエミュレートして実行・判定し、時間は粗→細・待機除外で計測し（scripts/analyze_timing.py）、改善を優先度つきで提案。無人で回すなら workflow/06-autonomous-loop.md。
7. **取り込む** 現行に新しい手編集がないか確認してから検証済み差分を貼り、保存完了を確認し、ネイティブコードを再採取して照合。本番入口（利用者操作あり）の最終確認は利用者に残す。
8. **育てる** 動いた部品は knowledge/snippets/own-*.md に確認版つきで、コツは catalog.md の群に `  - memo:` で追記。KB に無い ID が判明したら robin-syntax.md の表へ。

## Robin を出す前の反射チェック（毎回・省略不可）
Robin を1行でも出力する直前に、knowledge/robin-rules-compact.md の次の8点を**全行**に当て、結果を「行 | 判定 | 根拠」の表で添える。1つでも NG なら直してから出す。
1. `%…%` が `$'''…'''` の外に無い（式は裸）
2. 文字列内の `'` は `\'`、変数直前と末尾の `\` は二重、リテラル % は `%%`
3. enum は `Module.Type.Value` 完全修飾で、参照の許可値にある
4. ID・引数名が参照（robin/<module>.md）の例と一致。無いものは「Designer で確認」と書き、推測しない
5. 変数は SET／出力／ループ変数で定義済み。予約語を変数名・プロパティ名に使っていない（`Mail['From']`）
6. IF/LOOP/SWITCH/BLOCK と END が対応し、1行1文。`ELSE IF (アクション)` を使っていない
7. ON ERROR は「ON ERROR可」のアクションだけ、例外名は宣言済み、ハンドラー内は SET/CALL/GOTO/THROW のみ
8. ヘッダー行・FUNCTION を含めず、サブフローは「Designer で先に作る」と明記
エージェント環境では加えて `scripts/robin_lint.py --kb` を FATAL/ERROR 0 にする。
静的レビューの末尾で、計画時と同じ基準で「PAD でなくてよいのでは」を再判定する（出来上がりの大半がスクリプト1ブロック／UI 操作が結局無い等）。該当があれば「技術選定メモ」（手段・具体的な理由・前提、3文まで）を添える。

## 出力ゲート（ハーネス。チャットでも同じ）
Robin のコードブロックは、**その直前に判定表と判定行がある場合にだけ**出力してよい。順序は固定:
1. 判定表（全行、行 | 判定 | 根拠）
2. 判定行 `GATE: PASS 8/8` または `GATE: FAIL <NG の規則番号>`
3. FAIL のときは Robin を出さず、修正点だけを書いて直し、再判定してから出す（PASS になるまで繰り返す）
Robin を1文字でも変更したら、必ず判定表と判定行を作り直す。判定表の無い Robin、`GATE: FAIL` の後の Robin は出力違反。

## コピーできる形式（出力の既定）
- Robin は ``` で囲んだ1ブロック＝1サブフロー。ブロック内はコード行だけ（説明・番号・省略記号 `...`・「以下同様」を入れない）。
- ブロック1行目は `# <フロー名>/<サブフロー名>  PAD <版>  <Classic|PowerFx>  <日付>` のコメント。差し替えが要る値は、ブロック先頭に `# TODO: <変数名> を実際の値に` のコメント行で列挙し、本文には貼って通るダミー値を置く（`<<…>>` のような無効な印を本文に書かない）。
- 文字列は常に `$'''…'''`、パスは `C:\Work\…` のようなダミー、宛先は `example.com`。
- サブフローは「Main」から順に、Designer で作る順に並べる。CALL 先は先に出す。

## 守ること
- 利用可能なツール／スキルの許可範囲を守る。GUI が難しくても私有内部状態の直接書換えや未許可の UI 手段へ迂回しない。
- 送信系（メール送信・外部投稿・削除）は検証用コードではダミー宛先か無効化。本番データ・本番フローを検証に使わない。
- 実ログ、認証情報、個人設定、テスト専用フローを配布へ混ぜない。

## 報告
変更／ソース反映／実PAD取り込み／保存／検証済み範囲／未確認・入力待ち／戻し先を区別する。質問や中間報告を完了としない。限定試験を全工程の保証へ拡張しない。最適化は同条件の実測差分（待機除外）に限定し、改善提案は優先度と期待効果・リスク・戻し方を添える。
