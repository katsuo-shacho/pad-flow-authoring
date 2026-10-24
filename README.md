# pad-flow-authoring

**v0.1.0 (experimental)** — A Claude skill (also usable as a prompt pack for any chat assistant) for building Power Automate Desktop flows systematically:
plan → design → look up a paste-validated Robin dictionary (1,086 action IDs, Classic and Power Fx) → compose → self-check against the paste rules → verify → improve.
The knowledge layer is an **unofficial description of the product's observed behaviour** (see LEGAL.md), built on Microsoft's CC BY 4.0 documentation and Joe Green's CC BY 4.0 PAD Robin Action Knowledge Base. Not affiliated with Microsoft. Repository: https://github.com/katsuo-shacho/pad-flow-authoring
Japanese documentation below; English README to follow.


License: docs CC BY 4.0 / scripts MIT（LICENSE）。第三者素材の出典は THIRD_PARTY_NOTICES.md。法的な位置づけは LEGAL.md（製品の挙動の記述であり製品の複製ではない。Microsoft とは無関係の非公式プロジェクト）。投稿ルールは CONTRIBUTING.md。

Claude 用スキル。Power Automate Desktop（PAD）のフロー作成・改修・検証を、公式リファレンスと有志公開の貼付コードを階層的に引きながら行う。

構成（辞書を核に、進め方と引き出しを足した三層）:
- SKILL.md — 手順（計画→設計→引く→組む→AI内検査→検証→取り込み→育てる）
- knowledge/ — 辞書。catalog.md（公式群一覧＋自分の memo）→ robin-index.md / robin/<module>.md / robin-powerfx/（1,086 Robin ID の貼付検証済み例・引数・enum・エラー名。JoeG592/pad-robin-action-kb, CC BY 4.0）→ robin-rules.md（構文規則）→ actions/, howto-index.md, official-guides.md（公式要約・索引）→ paste-format.md（貼付テキストの構造・互換性）→ snippets/, patterns-*.md（公開実例・定石）。knowledge/README.md が引く順の索引
- workflow/ — 00-modes（Chat／Interactive／Autonomous の使い分け、承認ゲート、plan/design/tasks の spec）/ 01-plan（要件・見積もり・GO）/ 02-design（アルゴリズム設計）/ 03-principles / 04-environments（AI内で完結・Copilotのみ・エージェント）/ 05-verify / 06-autonomous-loop
- prompts/ — モード別キックオフ（chat-kickoff / interactive-kickoff / agent-kickoff）と chat-lookup-protocol（チャットで「必要なファイルだけ読む」を再現する手順）
- scripts/ — robin_lint.py（貼付前検査。KB 付属プローブ 456 件で検証: 無言却下 107/107、エラー 23/27 を検出、誤検出 0/322）、robin_to_mermaid.py（独自デザインのフローチャート）、analyze_timing.py（粗→細・待機除外の時間解析）、make_prompt_pack.py（Copilot 用貼付パック）、build_catalog.py / build_robin.py（辞書の再生成）

更新: 公式リポジトリを sparse clone して `python3 scripts/build_catalog.py <docs>/articles/desktop-flows knowledge`。

Robin 参照の更新:
```
curl -L -o kb.json https://raw.githubusercontent.com/JoeG592/pad-robin-action-kb/main/PAD_Robin_ActionKB.json
curl -L -o kbfx.json https://raw.githubusercontent.com/JoeG592/pad-robin-action-kb/main/PAD_Robin_ActionKB_PowerFx.json
python3 scripts/build_robin.py kb.json knowledge && python3 scripts/build_robin.py kbfx.json knowledge --powerfx
```
クレジット: Robin データは Joe Green「PAD Robin Action Knowledge Base」（CC BY 4.0）を要約・再構成したもの。公式要約は Microsoft Docs（CC BY 4.0）。
