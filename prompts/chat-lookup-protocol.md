# Chat モードでの「フック」の再現（ツール無しのチャットに、必要な知識だけ読ませる）

エージェントでは SKILL.md が「必要なファイルだけ開く」フックになる。チャットではそれを**二段構え**で真似る。

## 段1: 小さな索引を先に渡し、モデルに「次に必要なファイル」を言わせる
1. 会話の先頭に `prompts/chat-kickoff.md` ＋ `knowledge/robin-rules-compact.md` ＋ `knowledge/catalog.md` の該当群だけ（grep して5〜10行）を貼る。
2. 計画・設計まで作らせたら、「この設計に必要な Robin の家族（Module.Action）を列挙して」と頼む。
3. その家族だけで `python3 scripts/make_prompt_pack.py --families …` を作って貼る（自宅で作っておけるよう、よく使う家族のパックを数本用意しておく）。
   例: Excel 読み書き用、ファイル整理用、Web 抽出用、Outlook 用。各 1〜2 万字。

## 段2: 知識ファイルを「参照できる場所」に置き、チャットに読みに行かせる
チャット製品ごとにできることが違うので、使えるものから順に:
- **OneDrive / SharePoint に knowledge/ を置き、チャットでファイル参照する**（M365 Copilot の "/" でのファイル指定、添付）。モデルが「robin/excel.md が要る」と言ったら、そのファイルを参照に加える。最もフックに近く、社内データとして扱えるので安全。
- **Copilot Studio のエージェント（宣言型エージェント）に、そのフォルダーを知識源として登録する**。以後は「Excel の読込みの Robin は？」と聞くだけで該当ファイルを引く。社内で複数人が使うならこれが本命。
- **公開 URL を読ませる**（GitHub Pages に knowledge/ を公開し、チャットの Web 参照で開かせる）。組織設定で Web 参照が許可されているときだけ。raw.githubusercontent は読めないことが多いので、Pages（HTML）にする。
いずれも、索引（robin-index.md / catalog.md）→ 該当モジュール1本、の順に読ませるのは段1と同じ。

## ルール（kickoff に含める一文）
「必要な参照が手元に無いときは推測せず、『knowledge/robin/<module>.md の <家族> を参照に追加してください』と要求して止まる。」
これで、チャットでも「無い知識で書かない」が守られる。

## 自宅での下準備
- `scripts/make_prompt_pack.py` で用途別パックを作り、OneDrive の `pad-flow-authoring/packs/` に置く。
- `knowledge/` 全体も同じ場所へ（ZIP ではなく展開して置くと、ファイル単位で参照できる）。
- 公開するなら GitHub Pages を有効化し、`knowledge/` をそのまま配信する（Markdown は Pages が HTML 化する）。
