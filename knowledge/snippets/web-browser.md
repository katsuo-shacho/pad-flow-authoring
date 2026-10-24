# スニペット: ブラウザー自動化

## Chrome を確実に起動して接続する（サブフロー化推奨）
出典: https://github.com/pnp/powerplatform-snippets/tree/main/power-automate-desktop/launch-browser-chrome （MIT、PAD 2.42.317.24061 以降で確認）
狙い: 拡張機能の読込失敗で「新しいChromeを起動」が失敗する問題を、Run application で起動→ウィンドウ待ち→既存インスタンスに接続、で回避する。

```
SET URL TO $'''https://www.someurl.com'''
System.RunApplication.RunApplication ApplicationPath: $'''chrome''' CommandLineArguments: $'''www.google.com''' WorkingDirectory: '' WindowStyle: System.ProcessWindowStyle.Maximized ProcessId=> AppProcessId
WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''Google*''' Class: $'''Chrome_WidgetWin_1''' FocusWindow: True) FOR 30
WebAutomation.LaunchChrome.AttachToChromeByTitle TabTitle: $'''Google''' AttachTimeout: 5 BrowserInstance=> BrowserMain
ON ERROR REPEAT 5 TIMES WAIT 3
END
WebAutomation.GoToWebPage.GoToWebPageNoWait BrowserInstance: BrowserMain Url: URL
```
使い方: サブフロー `LaunchBrowser` に貼り、Main から `CALL LaunchBrowser`。`BrowserMain` を以後の Web アクションの BrowserInstance に使う。
構文メモ: `WAIT (条件アクション) FOR 秒` が条件付き待機の形。

## ページ一覧→各ページへ遷移→保存（2段ループ・正規表現抽出）
出典: https://github.com/ronan-deshays/power-automate-desktop-utility-flows （MIT、2023、Firefox・フランス語UI）
狙い: HTMLソースを `GetDetailsOfWebPage(DetailsType: Source)` で取り、`Text.ParseText.RegexParse` でURL一覧を作ってループ。UI要素を使う部分（appmask）は環境依存なので、JS や「名前を付けて保存」ダイアログの UI要素取得で置き換える。

```
WebAutomation.LaunchFirefox.AttachToFirefoxByUrl TabUrl: $'''https://example.com/''' AttachTimeout: 5 BrowserInstance=> Browser
WebAutomation.GoToWebPage.GoToWebPage BrowserInstance: Browser Url: $'''https://example.com/''' WaitForPageToLoadTimeout: 60
SET regexp_category_URL TO $'''https://example.com/article-categories/[\\w-]*/*'''
WebAutomation.GetDetailsOfWebPage BrowserInstance: Browser DetailsType: WebAutomation.DetailsType.Source Details=> homepage_HTML
Text.ParseText.RegexParse Text: homepage_HTML TextToFind: regexp_category_URL StartingPosition: 0 IgnoreCase: False Matches=> categories_URL
LOOP FOREACH category_URL IN categories_URL
    WebAutomation.GoToWebPage.GoToWebPage BrowserInstance: Browser Url: category_URL WaitForPageToLoadTimeout: 60
    WebAutomation.GetDetailsOfWebPage BrowserInstance: Browser DetailsType: WebAutomation.DetailsType.Source Details=> categorypage_HTML
    Text.ParseText.RegexParse Text: categorypage_HTML TextToFind: regexp_category_URL StartingPosition: 0 IgnoreCase: False Matches=> articles_URL
    LOOP FOREACH article_URL IN articles_URL
        WebAutomation.GoToWebPage.GoToWebPage BrowserInstance: Browser Url: article_URL WaitForPageToLoadTimeout: 60
        # ここに保存処理（原本は UIAutomation.PressButton + appmask、環境依存のため省略）
    END
END
```
原本の注意点: 録画したアクションには `@@source: 'Recorder'` 行と `appmask[...]` 参照が付き、貼付テキスト末尾に `# [ControlRepository][PowerAutomateDesktop]` + JSON（UI要素/画像リポジトリ）が続く（→ knowledge/paste-format.md）。

## JS で一括処理する（原則: ループ内を薄くする）
出典の技法: DwayneSelsig/Power-Automate-Desktop-Scripts（GPL-3.0 のため本文は転載しない。形だけ）
- `WebAutomation.ExecuteJavascript BrowserInstance: Browser Javascript: $'''function ExecuteScript() { return document.body.scrollHeight; }''' Result=> H` のように **戻り値を Result で受ける**。数値にするには `Text.ToNumber`。
- 遅延読込ページは、JS でスクロール（`window.scrollTo(0, %Idx%)`）を `LOOP Idx FROM 1 TO H - W STEP W / 4` で回すより、JS側でループと待機まで済ませて1回の呼び出しにする方が軽い（原則）。
- クリックは `document.querySelector(\"#id\").click();`（文字列内のダブルクォートは `\"`）。
