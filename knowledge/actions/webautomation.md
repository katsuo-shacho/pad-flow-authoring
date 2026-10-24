# Browser automation actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/webautomation （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Browser automation actions enable you to interact with web applications and components through UI elements. Web UI elements, also called web elements, uniquely describe the web components that the action handles. To perform web automation, first create a new browser instance by using one of the Launch Browser actions. These actions support Microsoft Edge, Google Chrome, Mozilla Firefox, and Internet Explorer. For web automation to function correctly, you must have either the appropriate browser extension or a compatible WebDriver installed, depending on the interaction method you select. You c

## Extract data from web page  `#extractdata`
Extract data from specific parts of a web page as single values, lists, rows, or tables.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on the web page to extract data from.
- Extraction parameters: Datatable — The parameters to use when extracting data. Depending on the extraction mode, this parameter accepts different data.
- Max web pages to process: Numeric value — This is the maximum number of web pages to process.
- Send physical click for next page: Boolean value = False — Specify whether to physically move the mouse cursor over the page prior to clicking. A physical click is required for cases where emulated clicks to the page don't perform the intentional action on the element. As this option requires the browser window to be focused, it automatically brings it to the foreground.
- Page CSS selector: Text value — This is the page CSS selector.
- Extraction mode: <ul><li>Undefined</li><li>Single value</li><li>Handpicked values</li><li>List</li><li>Table</li><li>Entire HTML table</li></ul> = Single value — Specify what to extract from the web page.
- Use paging: Boolean value = False — Specify whether to use paging.
- Get all web pages: Boolean value = False — Specify whether to get all web pages.
- Process data upon extraction: Boolean value = False — Specify whether to process extracted data to present them exactly as displayed in the webpage. Processing of extracted data includes displaying of the information nested in iframes and filtering through hidden or visible elements. For larger datasets, having this option enabled isn't recommended as it will increase the extraction time.
- Timeout(任意): Numeric value = 60 — Set the time in seconds that you want to wait for the extraction to complete before the action fails.
- Store data mode: <ul><li>Variable</li><li>Excel spreadsheet</li></ul> = Variable — Specify whether to store the extracted data in a variable or an Excel spreadsheet.
出力:
- `ExcelInstance`: Excel instance — The Excel instance with the extracted data. Use this instance to manipulate the spreadsheet (or save and close it) by using the dedicated Excel actions.
- `DataFromWebPage`: Datatable — The extracted data as a single value, list, data row, or data table.
例外: Failed to extract data.; Failed to launch Excel instance.; Failed to write values to Excel.

## Get details of web page  `#getdetailsofwebpage`
Get a property of a web page, such as its title or its source text.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- Get: <ul><li>Web page description</li><li>Web page meta keywords</li><li>Web page title</li><li>Web page text</li><li>Web page source</li><li>Web browser's current URL address</li></ul> = Web page description — Select the information to retrieve from the web page.
出力:
- `WebPageProperty`: Text value — The details retrieved from the web page.
例外: Failed to get details of web page.

## Get details of element on web page  `#getdetailsofelement`
Get the value of an element's attribute on a web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on the web page to get details from.
- Attribute name: Text value = Own Text — Enter or select the attribute whose value to retrieve.
出力:
- `AttributeValue`: Text value — It's the value of the web element's attribute.
例外: Failed to retrieve attribute of UI element on web page.

## Take screenshot of web page  `#takescreenshotbase`
Takes a screenshot of the web page (or an element of the web page) currently displayed in the browser and saves the image to a file or the clipboard.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- Capture: <ul><li>Entire web page</li><li>Specific element</li></ul> = Entire web page — Specify whether to capture the entire web page or only a specific element of it.
- UI element: UI element — Select the UI element on the web page to capture.
- Save mode: <ul><li>Clipboard</li><li>File</li></ul> = Clipboard — Specify whether to save the image into a file or store it into the clipboard.
- Image file: File — Set the full path for the file to save the image capture.
- File format: <ul><li>BMP</li><li>EMF</li><li>EXIF</li><li>GIF</li><li>JPG</li><li>PNG</li><li>TIFF</li><li>WMF</li></ul> = BMP — Select the format of the image file.
例外: Element with specified CSS selector not found.; Failed to save file.; Failed to save in the clipboard.; Failed to take screenshot.

## Focus text field on web page  `#focusbase`
Set the focus on an input element of a web page and scroll it into view.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on the web page to focus.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to set input focus on web page text field.

## Populate text field on web page  `#populatetextfieldbase`
Fill a text field in a web page with the specified text.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the text field to populate.
- Text: <ul><li>Direct encrypted input</li><li>Text value</li></ul> — Enter the text to fill in the text field.
- If field isn't empty(任意): <ul><li>Replace text</li><li>Append text</li></ul> = Replace text — Specify whether to replace existing content, or to append.
- Populate text using physical keystrokes: Boolean value = False — Emulate using physical keystrokes when populating text to UI text field elements. Physical keystrokes are required for cases that emulated text population doesn't perform the intentional action on the element. As this option requires the browser window to be focused, it automatically brings it in the foreground.
- Emulate typing: Boolean value = True — Specify whether to fill the text field at once by setting the value of the text box, or emulate a user typing by sending characters one by one. The latter method is slower, but required in some complex web pages.
- Unfocus text box after filling it: Boolean value = False — Choose whether to unfocus the text box right after this action fills it with the specified text. If scraping autocompletion lists, set this parameter to False.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after populating the text field.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after populating the text field.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to write on text field.

## Set check box state on web page  `#setcheckboxstatebase`
Check or uncheck a check box in a web form.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the check box to set the *state of*.
- Check box state: <ul><li>Checked</li><li>Unchecked</li></ul> = Checked — Select the check box *state*.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after setting the check box state.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after setting the check box state.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to set the state of the checkbox.

## Select radio button on web page  `#selectradiobuttonbase`
Select a radio button on the web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — The radio button to select.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after selecting the radio button.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after selecting the radio button.
- Dialog button to press(任意): Text value = OK — The dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found; Failed to select radio button

## Set drop-down list value on web page  `#setdropdownlistvaluebase`
Set or clear the selected options for a drop-down list in a web form.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the drop-down list to set its value.
- Operation: <ul><li>Clear all options</li><li>Select options by name</li><li>Select options by index</li></ul> = Clear all options — Select whether to select a value or clear the selected value of the drop-down list.
- Option names: List of Text values — Enter an option or a list of options to be selected in the drop-down list. Multiple options make sense only when working with multi-selection lists. If the list is single-selection, then only the first option of the list specified is used.
- Use regular expressions: Boolean value = False — Specify whether the option names values to interpret as a regular expression.
- Option indices: List of Numeric values — Enter an index or a list of indices to be selected in the drop-down list. Multiple options make sense only when working with multi-selection lists. If the list is single-selection, then only the first option of the list specified is used.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after setting the drop-down list value.
- Timeout for webpage load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after setting the drop-down list value.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to set the selected option.

## Press button on web page  `#pressbuttonbase`
Press a web page button.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the button to press.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after pressing the button.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after pressing the button.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to click on web page button.

## If web page contains  `#ifwebpagecontainsaction`
Mark the beginning of a conditional block of actions, depending on whether a specific piece of text or element exists in a web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- Check if web page: <ul><li>Contains element</li><li>Doesn't contain element</li><li>Contains text</li><li>Doesn't contain text</li></ul> = Contains element — Check whether a specific text or web page element exists in a web page.
- UI element: UI element — Select the UI element on web page to check for.
- Text: Text value — Enter the text on web page to check for.
例外: Failed to communicate with the browser.

## Wait for web page content  `#waitforwebpagecontentaction`
Suspend the flow until a specific piece of text or web page element appears or disappears from a web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- Wait for web page to: <ul><li>Contain element</li><li>Not contain element</li><li>Contain text</li><li>Not contain text</li></ul> = Contain element — Specify whether to wait for a specific text or web page element to appear or disappear in a web page.
- UI element: UI element — Select the UI element on web page to check for.
- Text: Text value — Enter the text on web page to check for.
例外: Wait for web page content failed.

## Launch new Internet Explorer  `#launchinternetexplorerbase`
Launch a new instance or attach to a running instance of Internet Explorer for automating websites and web applications.
入力:
- Launch mode: <ul><li>Launch automation browser</li><li>Launch new Internet Explorer</li><li>Attach to running Internet Explorer</li></ul> = Launch automation browser — Specify whether to launch the automation browser, a new instance of Internet Explorer, or attach to an existing one.
- Attach to Internet Explorer tab: <ul><li>By title</li><li>By URL</li><li>Use foreground window</li></ul> = By title — Specify whether to attach to an Internet Explorer tab by its title, URL, or attach to the active tab of Internet Explorer running as the foreground window.
- Initial URL: Text value — Enter the URL of the website to visit when the web browser launches.
- Tab title: Text value — Enter the title (or part of it) of the Internet Explorer tab to attach to.
- Tab URL: Text value — Enter the URL (or part of it) of the Internet Explorer tab to attach to.
- Window state: <ul><li>Normal</li><li>Maximized</li><li>Minimized</li></ul> = Normal — Specify whether to launch the browser window in normal, minimized, or maximized state.
- Target desktop: <ul><li>Local computer</li><li>Any virtual desktop that is either currently connected or has at least one UI element captured</li></ul> = Local computer — Set the connection string of the target desktop that the browser launches.
- Clear cache: Boolean value = False — Specify whether to clear the entire cache of the web browser right after launching it.
- Clear cookies: Boolean value = False — Specify whether to clear all stored cookies in the web browser right after launching it.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: Close it, Press a button, Do nothing = Do nothing — Specify what to do if a pop-up dialog appears while loading the initial web page.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
- Custom user agent string(任意): Text value — Specify the custom user agent string for the runtime web helper. If this field remains empty, the runtime web helper uses by default the user agent string of Internet Explorer installed on the machine.
出力:
- `InternetExplorer`: Web browser instance — The Internet Explorer instance to use with browser automation actions.
例外: Failed to launch Internet Explorer.; Invalid URL

## Launch new Firefox  `#launchfirefoxbase`
Launch a new instance or attach to a running instance of Firefox for automating websites and web applications.
入力:
- Launch mode: <ul><li>Launch new Instance </li><li> Attach to running instance</li></ul> = Launch new Instance — Specify whether to launch a new instance of Firefox or attach to an existing one.
- Attach to Firefox tab: <ul><li>By title</li><li>By URL</li><li>Use foreground window</li></ul> = By title — Specify whether to attach to a Firefox tab by its title, URL, or attach to the active tab of Firefox running as the foreground window
- Initial URL: Text value — Enter the URL of the website to visit when the web browser launches.
- Tab title: Text value — Enter the title (or part of it) of the Firefox tab to attach to
- Tab URL: Text value — Enter the URL (or part of it) of the Firefox tab to attach to
- Window state: <ul><li>Normal</li><li>Maximized</li><li>Minimized</li></ul> = Normal — Specify whether to launch the browser window in normal, minimized, or maximized state.
- Target desktop: <ul><li>Local computer</li><li>Any virtual desktop that is either currently connected or has at least one UI element captured</li></ul> = Local computer — Set the connection string of the target desktop that the browser launches.
- Browser interaction method: <ul><li>Browser extension</li><li>WebDriver</li></ul> = Browser extension — Set how Power Automate for desktop communicates with the browser during web automation
- Clear cache: Boolean value = False — Specify whether to clear the entire cache of the web browser right after launching it.
- Clear cookies: Boolean value = False — Specify whether to clear all stored cookies in the web browser right after launching it.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears while loading the initial web page.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
- Timeout: Numeric value = 60 — Set the time in seconds that you want to wait for the browser to be launched before the action fails
- User data folder: <ul><li>Picture-in-Picture default</li><li>Browser default</li><li>Custom</li></ul> = Picture-in-Picture default — Specify the user data folder the browser uses when the flow runs in Picture-in-Picture. If Browser default is selected, the browser can't be opened on both the desktop and in Picture-in-Picture at the same time. Learn more
- User data folder path: Folder — Specify the path of the user data folder the browser uses when the flow runs in Picture-in-Picture. Learn more
出力:
- Browser: Web browser instance — The Firefox instance to use with browser automation actions
例外: Failed to launch Firefox.; Invalid URL

## Launch new Chrome  `#launchchromebase`
Launch a new instance or attach to a running instance of Chrome for automating websites and web applications.
入力:
- Launch mode: <ul><li>Launch new Instance</li><li>Attach to running instance</li></ul> = Launch new Instance — Specify whether to launch a new instance of Chrome or attach to an existing one
- Attach to Chrome tab: <ul><li>By title</li><li>By URL</li><li>Use foreground window</li></ul> = By title — Specify whether to attach to a Chrome tab by its title, URL, or attach to the active tab of Chrome running as the foreground window
- Initial URL: Text value — Enter the URL of the website to visit when the web browser launches.
- Tab title: Text value — Enter the title (or part of it) of the Chrome tab to attach to
- Tab URL: Text value — Enter the URL (or part of it) of the Chrome tab to attach to
- Window state: <ul><li>Normal</li><li>Maximized</li><li>Minimized</li></ul> = Normal — Specify whether to launch the browser window in normal, minimized, or maximized state.
- Target desktop: <ul><li>Local computer</li><li>Any virtual desktop that is either currently connected or has at least one UI element captured</li></ul> = Local computer — Set the connection string of the target desktop that the browser launches.
- Browser interaction method: <ul><li>Browser extension</li><li>WebDriver</li></ul> = Browser extension — Set how Power Automate for desktop communicates with the browser during web automation
- Clear cache: Boolean value = False — Specify whether to clear the entire cache of the web browser right after launching it.
- Clear cookies: Boolean value = False — Specify whether to clear all stored cookies in the web browser right after launching it.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears while loading the initial web page.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
- Timeout: Numeric value = 60 — Set the time in seconds that you want to wait for the browser to be opened before the action fails
- User data folder: <ul><li>Picture-in-Picture default</li><li>Browser default</li><li>Custom</li></ul> = Picture-in-Picture default — Specify the user data folder the browser uses when the flow runs in Picture-in-Picture. If Browser default is selected, the browser can't be opened on both the desktop and in Picture-in-Picture at the same time. Learn more
- User data folder path: Folder — Specify the path of the user data folder the browser uses when the flow runs in Picture-in-Picture. Learn more
出力:
- Browser: Web browser instance — The Chrome instance to use with browser automation actions
例外: Failed to launch Chrome; Invalid URL

## Launch new Microsoft Edge
Launch a new instance or attach to a running instance of Microsoft Edge for automating websites and web applications.
入力:
- Launch mode: <ul><li>Launch new Instance</li><li>Attach to running instance</li></ul> = Launch new Instance — Specify whether to launch a new instance of Microsoft Edge or attach to an existing one
- Attach to Microsoft Edge tab: <ul><li>By title</li><li>By URL</li><li>Use foreground window</li></ul> = By title — Specify whether to attach to a Microsoft Edge tab by its title, URL, or attach to the active tab of Microsoft Edge running as the foreground window
- Initial URL: Text value — Enter the URL of the website to visit when the web browser launches.
- Tab title: Text value — Enter the title (or part of it) of the Microsoft Edge tab to attach to
- Tab URL: Text value — Enter the URL (or part of it) of the Microsoft Edge tab to attach to
- Window state: <ul><li>Normal</li><li>Maximized</li><li>Minimized</li></ul> = Normal — Specify whether to launch the browser window in normal, minimized, or maximized state.
- Target desktop: <ul><li>Local computer</li><li>Any virtual desktop that is either currently connected or has at least one UI element captured</li></ul> = Local computer — Set the connection string of the target desktop that the browser launches.
- Browser interaction method: <ul><li>Browser extension</li><li>WebDriver</li></ul> = Browser extension — Set how Power Automate for desktop communicates with the browser during web automation
- Clear cache: Boolean value = False — Specify whether to clear the entire cache of the web browser right after launching it.
- Clear cookies: Boolean value = False — Specify whether to clear all stored cookies in the web browser right after launching it.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears while loading the initial web page.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
- Timeout: Numeric value = 60 — Set the time in seconds that you want to wait for the browser to be launched before the action fails
- User data folder: <ul><li>Picture-in-Picture default</li><li>Browser default</li><li>Custom</li></ul> = Picture-in-Picture default — Specify the user data folder the browser uses when the flow runs in Picture-in-Picture. If Browser default is selected, the browser can't be opened on both the desktop and in Picture-in-Picture at the same time. Learn more
- User data folder path: Folder — Specify the path of the user data folder the browser uses when the flow runs in Picture-in-Picture. Learn more
出力:
- Browser: Web browser instance — The Microsoft Edge instance to use with browser automation actions
例外: Failed to launch Microsoft Edge.; Invalid URL

## Create new tab  `#createnewtabbase`
Create a new tab and go to the given URL (supported in Microsoft Edge, Chrome, and Firefox).
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with
- URL to go to: Text value — Enter the URL, or a variable containing the URL, to go to
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely before proceeding.
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears while loading the web page
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
出力:
- `NewBrowser`: Web browser instance — The new web browser instance to use with browser automation actions.
例外: Invalid URL; Failed to create a new tab.

## Go to web page  `#gotowebpagebase`
Navigate the web browser to a new page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with
- Navigate: <ul><li>To URL</li><li>Back</li><li>Forward</li><li>Reload web page</li></ul> = To URL — Specify where to navigate to
- URL: Text value — Enter the URL to navigate to
- Wait for page to load: Boolean value = True — Specify whether to wait for the web page to load completely before proceeding
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears while loading the web page
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Failed to navigate to web page.; Invalid URL

## Click link on web page  `#clickbase`
Click on a link or any other element of a web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on web page to click.
- Click type: <ul><li>Left click</li><li>Right click</li><li>Double click</li><li>Left button down</li><li>Left button up</li><li>Right button down</li><li>Right button up</li><li>Middle click</li></ul> = Left click — The kind of click to perform
- Send physical click: Boolean value = False — Specify whether to physically move the mouse cursor over the element prior to clicking. A physical click is required for cases where emulated clicks don't perform the intentional action on the element. As this option requires the browser window to be focused, it automatically brings it to the foreground.
- Wait for page to load: Boolean value = True — Specify whether to wait for the new web page to load completely after clicking the link
- Timeout for webpage to load: Numeric value = 60 — Set the time in seconds for page to load before the action throws an error.
- If a pop-up dialog appears: <ul><li>Close it</li><li>Press a button</li><li>Do nothing</li></ul> = Do nothing — Specify what to do if a pop-up dialog appears after clicking the link.
- Dialog button to press(任意): Text value = OK — Enter the dialog button to press if a pop-up dialog appears.
例外: Element with specified CSS selector not found.; Failed to click UI element.

## Click download link on web page  `#clickdownloadlink`
Select a link in a web page that results in downloading a file.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on web page to click.
- Destination folder: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to save the downloaded file to.
出力:
- `DownloadedFile`: File — The file on the disk where the download is saved. This value is a filepath that consists of the download folder as specified earlier plus the name of the file as provided by the web server.
例外: Failed to download file.; Element with specified CSS selector not found.; Failed to click UI element.; Failed to save file.

## Run JavaScript function on web page  `#executejavascript`
Run a JavaScript function on the web page and get the returned result.
出力:
- `Result`: Text value — The result of the :::no-loc text="JavaScript"::: function that ran.
例外: Failed to run :::no-loc text="JavaScript":::.

## Hover mouse over element on web page  `#hoveroverelement`
Hover the mouse over an element of a web page.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to work with.
- UI element: UI element — Select the UI element on web page to hover.
- Move mouse to hover: Boolean value = False — Specify whether to physically move the mouse cursor over the element in order to hover the UI element. A physical hover is required for cases where emulated hover doesn't perform the intentional action on the element. As this option requires the browser window to be focused, it automatically brings it to the foreground.
例外: Failed to hover over element.

## Close web browser  `#closewebbrowser`
Closes a web browser window.
入力:
- Web browser instance: Web browser instance — Enter or choose the variable that contains the web browser instance to close.
例外: Failed to close the web browser.
