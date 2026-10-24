# Legal notice / 法的な位置づけ

Project: https://github.com/katsuo-shacho/pad-flow-authoring

## English

**This project describes the observable behaviour of a product. It does not reproduce the product.**

- Power Automate, Power Automate Desktop and Robin are trademarks of Microsoft Corporation. This project is not affiliated with, endorsed by, or supported by Microsoft. Trademarks are used only to identify the product being described (nominative use). No trademark rights are granted.
- The action identifiers, argument names, enum values, error names and paste syntax recorded here are facts about how Power Automate Desktop behaves when text is pasted into its designer. They are recorded the same way, and on the same footing, as the PAD Robin Action Knowledge Base by Joe Green (CC BY 4.0), which this project builds on. Interface specifications and functional behaviour of this kind are not reproduced from any proprietary source; they were observed or taken from Microsoft's own documentation, which Microsoft publishes under CC BY 4.0.
- No Microsoft binaries, decompiled code, internal schemas, screenshots, icons, logos or non-public material are included.
- Every third-party text that is reproduced (rather than summarized) is listed in THIRD_PARTY_NOTICES.md with its license and copyright holder. Material without an explicit license is referenced by link only and never reproduced.
- Summaries of Microsoft documentation are our own paraphrases, marked as such in each file header, and must not be read as Microsoft's statements. Always confirm against the linked official page.
- Nothing here is a warranty. Paste validation claims come from the cited knowledge base and apply to the PAD builds it names; your build may differ. Verify in your own designer before relying on anything.
- Do not contribute content copied from sources without a permissive license, credentials, personal data, or anything belonging to your employer. See CONTRIBUTING.md.

## Scope of what this project does — and does not do

- It never runs, modifies, or bypasses any part of Power Automate Desktop. Everything it describes is done through the product's own documented features: copying and pasting actions as text in the designer, running flows from the console or designer, reading the run log. No API that Microsoft does not expose is used, no file format is reverse-engineered, no license check is circumvented.
- "Autonomous" mode in workflow/06 means an AI assistant operating the designer the way a signed-in user would, on that user's own machine, under that user's own license, with the user's prior consent on scope. Whether such operation (including overnight runs under a signed-in session) is permitted is governed by the user's Microsoft license terms and their organization's policies, not by this project; the project does not decide that and asks the user to confirm it first.
- Microsoft's documentation describes *unattended* desktop flows as cloud-triggered runs on a machine with all users signed out, requiring the Power Automate Process plan; attended runs happen in the user's own signed-in session. Users should check which applies to how they intend to use this project.

## 日本語

**このプロジェクトは製品の観察可能な挙動を記述するものであり、製品そのものを複製するものではない。**

- Power Automate、Power Automate Desktop、Robin は Microsoft Corporation の商標です。本プロジェクトは Microsoft と無関係で、承認も支援も受けていません。商標は記述対象の製品を指すためだけに使用しています（指示的使用）。商標権の許諾は一切含みません。
- ここに記録したアクション ID・引数名・enum 値・エラー名・貼付構文は、Power Automate Desktop のデザイナーにテキストを貼り付けたときの挙動という「事実」です。土台とした Joe Green 氏の PAD Robin Action Knowledge Base（CC BY 4.0）と同じ方法・同じ立場で記録しています。この種のインターフェース仕様・機能的挙動は、非公開の素材から複製したものではなく、観察するか、Microsoft 自身が CC BY 4.0 で公開している文書から取ったものです。
- Microsoft のバイナリ、逆コンパイルしたコード、内部スキーマ、スクリーンショット、アイコン、ロゴ、非公開資料は含みません。
- 要約ではなく転載している第三者テキストは、すべて THIRD_PARTY_NOTICES.md にライセンスと著作権者を明記しています。ライセンス表示のない素材はリンクのみで、本文は転載しません。
- Microsoft 文書の要約は本プロジェクト独自の言い換えであり、各ファイル先頭にその旨を記し、Microsoft の見解として読まないでください。必ずリンク先の公式ページで確認してください。
- 一切の保証はありません。貼付検証の記述は引用元 KB のものであり、そこに記された PAD ビルドに限られます。使用前に自分のデザイナーで確認してください。
- 許諾のない素材のコピー、認証情報、個人情報、勤務先のデータは投稿しないでください。CONTRIBUTING.md を参照。

### このプロジェクトがやること・やらないこと
- Power Automate Desktop を改変・迂回・解析しません。使うのは製品が公式に提供している機能だけです（デザイナーでのアクションのテキストとしてのコピー＆貼付、コンソール／デザイナーからの実行、実行ログの閲覧）。非公開 API、ファイル形式の逆解析、ライセンス確認の回避は一切ありません。
- workflow/06 の「自走」は、サインイン済みの利用者と同じ操作を、利用者自身の PC・ライセンスの下で、範囲について利用者の事前同意を得たうえで AI が行うことを指します。それが許されるか（サインイン済みセッションでの夜間実行を含む）は利用者の Microsoft ライセンス条件と所属組織の方針が決めることであり、本プロジェクトは判断せず、最初に確認を求めます。
- Microsoft の文書では「無人（unattended）」デスクトップフローは、全ユーザーがサインアウトした機械でクラウドから起動する実行を指し、Power Automate Process プランが必要です。有人（attended）は利用者自身のサインイン済みセッションでの実行です。自分の使い方がどちらに当たるかは利用者が確認してください。
