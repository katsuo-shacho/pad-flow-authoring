# knowledge/ — PAD の挙動を体系化した辞書（非公式ドキュメント）

引く順番（上から。必要な層だけ読む）:

| 層 | 問い | ファイル | 出典 |
|---|---|---|---|
| 1 一覧 | 何ができるか | catalog.md（コア群）/ catalog-extended.md | 公式 actions-reference 要約 ＋ 自分の `- memo:` |
| 2 ID | 貼付テキストではどう書くか | robin-index.md → robin/<module>.md（Power Fx: robin-powerfx/） | JoeG592 KB（貼付検証済み） |
| 3 規則 | 何をすると貼付が無言で失敗するか | robin-rules.md | 同上 |
| 4 仕様 | 引数は何を意味し既定値は何か | actions/<group>.md | 公式 actions-reference 要約 |
| 5 やり方 | 公式はどう勧めているか | howto-index.md / official-guides.md（→ 1本だけ WebFetch） | 公式 how-to・方法論 |
| 6 貼付の構造 | コピーした文字列には何が入っているか、版・Classic/Power Fx・埋込スクリプトの互換性 | paste-format.md | 公開フローの観察 ＋ 公式注記 |
| 7 実例・定石 | 実運用ではどう組まれているか | snippets/index.md → snippets/<category>.md、patterns-*.md、robin-syntax.md | 公開フロー（ライセンス明示分のみ本文） |

- 1 は自分で育てる層（memo 行は再生成でも保持）。2〜5 は scripts/ で元データから再生成する。6〜7 は観察で増やす。
- どの層も「製品の挙動の記録」であり Microsoft の見解ではない（../LEGAL.md）。
