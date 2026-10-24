# Agent モード キックオフ（自宅の PC で、Claude が PAD の画面を操作できるとき）

最初に1回だけ聞く: 「対話で進めますか、いきなり作りますか。無人で回してよい範囲（時間・回数・触ってよいフォルダー／アプリ・禁止事項）は？」
返事がなければ: いきなり作る／3時間・10周／送信系は無効化／本番フローは触らない。

以後は SKILL.md の手順 1→8 と workflow/04-environments.md「B」、無人なら workflow/06-autonomous-loop.md に従い、
検証用フロー `ZZ_Verify_*` に貼って実行し、利用者操作はエミュレートし、止まったら自分で止め、
時間は粗→細・待機除外で測り、改善を優先度つきで報告する。本番取り込みは承認後。
貼付前に `python3 scripts/robin_lint.py flow.robin --kb <KB json>` を FATAL/ERROR 0 にする。
