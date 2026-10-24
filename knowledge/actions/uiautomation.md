# UI automation actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/uiautomation （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate provides various UI automation actions to enable users to interact with Windows and desktop applications. Some UI automation actions require you to set UI elements in their properties to indicate the element you want to handle. To add a new UI element, select Add UI element through the deployed UI automation action or the UI elements pane of the flow designer. All UI elements consist of selectors that pinpoint the hierarchical structure of the components. Selectors use the > notation to indicate that each element is contained within the element on its left. When you create a UI 

## Get details of window  `#getwindowdetails`
Gets a property of a window such as its title or its source text.
入力:
- Window: UI element — The window to get details from
- Window property: Get window title, Get window text, Get window location and size, Get process name = Get window title — Choose which property of the window to extract
- Bring to front: Boolean value = True — Specify whether the window containing the UI element will be brought to the front during execution. If this option is disabled, the action is executed in the background. Note that not all UI elements are compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- WindowProperty: General value — The retrieved information of the window
例外: Failed to retrieve property of window

## Get details of a UI element in window  `#getelementdetails`
Gets the value of a UI element's attribute in a window.
入力:
- UI element: UI element — The UI element to get details from
- Attribute name(任意): Text value = Own Text — The attribute whose value will be retrieved
- Bring to front: Boolean value = True — Specify whether the window containing the UI element will be brought to the front during execution. If this option is disabled, the action is executed in the background. Note that not all UI elements are compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- AttributeValue: Text value — The value of the UI element's text
例外: Failed to retrieve attribute of UI element

## Get selected checkboxes in window  `#getselectedcheckboxesinwindow`
Retrieves the names of the selected checkboxes in a checkbox group or the state of a specific checkbox.
入力:
- UI element: UI element — The checkbox or checkbox group
- Operation: Get names of selected checkboxes in group, Get state of checkbox = Get names of selected checkboxes in group — Specify whether to retrieve the state of multiple selected checkboxes or just one
- Bring to front: Boolean value = True — Specify whether the window containing the UI element should be brought to the front during execution. If this option is disabled, the action will be executed in the background. Note that not all UI elements might be compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- IsChecked: Boolean value — The state of the selected checkbox
- SelectedCheckboxes: List of Text values — The names of selected checkboxes inside the specified checkbox group
例外: Failed to retrieve checkbox state(s)

## Get selected radio button in window  `#getselectedradiobuttoninwindow`
Retrieves the names of the selected radio button in a radio button group or the state of a specific radio button.
入力:
- UI element: UI element — The radio button or radio button group
- Operation: Get selected radio button name in group, Get state of radio button = Get selected radio button name in group — Specify whether to retrieve the name of the radio button that's selected inside a group of radio buttons or just the state of a single radio button
- Bring to front: Boolean value = True — Specify whether the window containing the UI element will be brought to the front during execution. If this option is disabled, the action is executed in the background. Note that not all UI elements are compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- IsSelected: Boolean value — The state of the selected radio button
- SelectedRadiobutton: Text value — The selected radio button inside the specified radio group
例外: Failed to retrieve radio button state

## Extract data from window  `#extractdatafromwindow`
Extracts data from specific parts of a window in the form of single values, lists, or tables.
入力:
- Window: UI element — The window to extract data from
- Store extracted data in: an Excel spreadsheet, A variable = an Excel spreadsheet — Specify where to store the extracted data
- Bring to front: Boolean value = True — Specify whether the window containing the UI element will be brought to the front during execution. If this option is disabled, the action is executed in the background. Note that not all UI elements are compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- ExcelInstance: Excel instance — The Excel instance with the extracted data. Use this instance to manipulate the spreadsheet (or save and close it) by using the dedicated Excel actions.
- DataFromWindow: General value — The extracted data in the form of a datatable
例外: Extraction failed

## Extract data from table  `#extractdatafromtable`
Extracts data from a table in the form of a datatable.
入力:
- Table: UI element — The table or grid to extract data from
- Store extracted data in: an Excel spreadsheet, A variable = an Excel spreadsheet — Specify where to store the extracted data
- Bring to front: Boolean value = True — Specify whether the window containing the UI element is brought to the front during execution. If this option is disabled, the action is executed in the background. Not all UI elements are compatible with having the option disabled. Additionally, if execution of the action requires scrolling, disabling this option might not extract all elements.
出力:
- ExcelInstance: Excel instance — The Excel instance with the extracted data. Use this instance to manipulate the spreadsheet (or save and close it) by using the dedicated Excel actions.
- DataFromTable: General value — The extracted data in the form of a datatable
例外: Extraction failed

## Take screenshot of UI element  `#takescreenshot`
Takes a screenshot of a UI element in window.
入力:
- UI element: UI element — The UI element in the window to capture as screenshot
- Save mode: Clipboard, File = Clipboard — Specify whether to save the image into a file or store it into the clipboard
- Image file path: File — Set the full path for the file to be saved
- File format: BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF = BMP — The file format of the image file
出力:
- ImageFile: File — The file path of the generated screenshot image file
例外: Failed to retrieve UI element; Failed to save image; Failed to take screenshot of UI element

## Focus text field in window  `#focustextfield`
Sets the focus on a text box of a window and scrolls it into view.
入力:
- Text field: UI element — The text box to focus
例外: Failed to set input focus in window text box

## Populate text field in window  `#populatetextfield`
Fills a text box in a window with the specified text.
入力:
- Text box: UI element — The text box to populate
- Text to fill in: Direct encrypted input or Text value — The text to fill in the text field
- Simulate action: Boolean value = False — Simulate the keystrokes programmatically when populating text to UI text field elements. This option doesn't require the UI element's screen to be focused, it will not automatically bring it to the foreground. Note this option can be applied only to left-click action and it might not be applicable to every UI element.
- If field isn't empty(任意): Replace text, Append text = Replace text — Specify whether to replace existing content, or to append.
- Click before populating(任意): Left-click, Double-click, No = Left-click — Specify whether a left mouse click is performed before populating the text field or not.
例外: Failed to write in textbox

## Press button in window  `#pressbutton`
Presses a window button.
入力:
- UI element: UI element — The button to press
例外: Failed to press button

## Select radio button in window  `#selectradiobutton`
Selects a radio button on a window.
例外: Failed to select radio button UI element

## Set checkbox state in window  `#setcheckboxstate`
Checks or unchecks a checkbox in a window form.
入力:
- Checkbox: UI element — The checkbox to set the state of
- Set checkbox state to: Checked, Unchecked = Checked — Specify whether the checkbox will become checked or unchecked
例外: Failed to set checkbox state

## Set drop-down list value in window  `#setdropdownlistvalueinwindow`
Sets or clears the selected options for a drop-down list in a window form.
入力:
- Drop-down list: UI element — The drop-down list whose value to set
- Operation: Clear selected options, Select options by name, Select options by index = Clear selected options — Specify whether you want to select a value by name or by ordinal position (1 2 3 ...) or clear the selected value of the drop-down list
- Option names: List of Text values — Enter an option or a list of options to be selected in the drop-down list. Multiple options make sense only when working with multi-selection lists. If the list is single-selection, then only the first option of the list specified will be used.
- Use regular expressions: Boolean value = False — Specify whether the option names values to interpret as a regular expression
- Options indices: List of Numeric values — Enter an index or a list of indices to be selected in the drop-down list. Multiple options make sense only when working with multi-selection lists. If the list is single-selection, then only the first option of the list specified will be used.
例外: Failed to select the specified options in the drop-down list

## Get window  `#getwindowbase`
Gets a running window, for automating desktop applications.
入力:
- Get window: Specific window, Foreground window = Specific window — Specify whether to look using a selector or the foreground window
- UI element: UI element — The selector of the window to get
- Bring window to front: Boolean value = False — Specify whether to bring the window to the foreground automatically upon acquiring it
- Fail if window isn't found: Boolean value = True — Specify whether to wait indefinitely for the window to appear or to fail if the window doesn't show up within a set time period
- Timeout: Numeric value — The timeout to wait in seconds
出力:
- WindowTitle: Text value — The title of the foreground window
- AutomationWindow: Window instance — The specific window instance for use with later UI Automation actions
例外: Failed to get window

## Focus window  `#focuswindowbase`
Activates and brings to the foreground a specific window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to focus
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to use.
例外: Window wasn't found; Can't focus window; Can't perform window-related action in noninteractive mode

## Set window state  `#setwindowstatebase`
Restores, maximizes or minimizes a specific window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to set the state of
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to use.
- Window state: Restored, Maximized, Minimized = Restored — Choose in which state to display the window
例外: Window wasn't found; Can't set window state; Can't perform window-related action in noninteractive mode

## Set window visibility  `#setwindowvisibilitybase`
Shows a hidden window or hides a visible window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to set the visibility of
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to use.
- Visibility: Visible, Hidden = Hidden — Choose in which state to set the window visibility to
例外: Window wasn't found; Can't set window visibility; Can't perform window-related action in noninteractive mode

## Move window  `#movewindowbase`
Sets the position of a specific window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the Window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to move
- Window class(任意): Text value — If you have two windows with the same title, Window Class might help differentiate between them. In this case, enter the class of the window to use.
- Position X: Numeric value — The X position of the window
- Position Y: Numeric value — The Y position of the window
例外: Window wasn't found; Can't move window; Can't perform window-related action in noninteractive mode

## Resize window  `#resizewindowbase`
Sets the size of a specific window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to resize
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to use
- Width: Numeric value — The new width, in pixels
- Height: Numeric value — The new height, in pixels
例外: Window wasn't found; Can't resize window; Can't perform window-related action in noninteractive mode

## Close window  `#closewindowbase`
Closes a specific window.
入力:
- Find window mode: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window: UI element — The window UI element
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window instance: Numeric value — The instance or handle of the window to close
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to use.
例外: Window wasn't found; Can't close window; Can't perform window-related action in noninteractive mode

## If window contains  `#ifwindowcontainsaction`
Marks the beginning of a conditional block of actions depending on whether a specific piece of text or UI element exists in a window.
入力:
- Check if window: Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text = Contains UI element — Check whether a specific text or UI element exists in a window
- Check UI element state: Boolean value = False — Check whether a specific UI element is enabled or disabled
- Text: Text value — The text to check for
- UI element: UI element — The UI element to check for
- Window: UI element — The window to check if the text exists on
- State: Enabled, Disabled = Enabled — The UI element state to check for

## Wait for window content  `#waitforwindowcontentaction`
Suspends the execution of the automation until a specific piece of text or UI element appears or disappears from a Window.
入力:
- Wait until window: Contains UI element, Doesn't contain UI element, Contains text, Doesn't contain text = Contains UI element — Whether to wait for a specific text or UI element to appear in a window
- Check UI element state: Boolean value = False — Check whether a specific UI element is enabled or disabled
- Text: Text value — The text to check for
- UI element: UI element — The UI element to check for
- Window: UI element — The window to check if the text exists on
- State: Enabled, Disabled = Enabled — The UI element state to check for
例外: Wait for window content failed

## If image  `#ifimageaction`
This action marks the beginning of a conditional block of actions depending on whether a selected image is found on the screen or not.
入力:
- If image: exists, doesn't exist = exists — Whether to check for the existence or absence of the selected image
- Image: List of Images — The image/s that the action will check if it/they exist
- Search for image on: Entire screen, Foreground window only = Entire screen — Whether to look for the specified image in the foremost window only or the entire visible screen. Neither choice will find the image if it isn't clearly visible on the screen
- Search mode: Search whole screen or foreground window, Search on specified subregion of screen or foreground window = Search whole screen or foreground window — Whether to scan the entire screen (or window) to find the supplied text or only a narrowed down subregion of it
- Find all images in the list: Boolean value = False — Check whether all images on the list exist or don't exist
- X1(任意): Numeric value — The start X coordinate of the subregion to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion to scan for the supplied text
- Y1(任意): Numeric value — The start Y coordinate of the subregion to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion to scan for the supplied text
- Tolerance(任意): Numeric value = 10 — Specify how much the image(s) searched for can differ from the originally chosen image
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
例外: Can't check image in noninteractive mode; Invalid subregion coordinates

## Use desktop  `#usedesktop`
Performs desktop and taskbar related operations.
入力:
- UI element: UI element — The UI element to perform a click on
- Click type: Left-click, Right-click, Double-click = Left-click — The kind of click to perform
- Launch new application when left-clicking on the taskbar: Boolean value = True — When this parameter is set to 'true', it ensures that a new window of an application will be created when left-clicking on its icon in the 'quick launch' bar, also known as the taskbar of Windows 7 or above. Uncheck this option to bring an already running instance of the application to the foreground.
例外: Taskbar operation failed

## Select tab in window  `#selecttab`
Selects a tab from a group of tabs.
入力:
- Tab: UI element — The tab to select
例外: Selecting tab failed

## Wait for image  `#waitforimageaction`
This action waits until a specific image appears on the screen or on the foreground window.
入力:
- Wait for image to: Appear, Disappear = Appear — Check whether to wait for the image(s) to appear or disappear
- Image to wait for: List of Images — The image/s that the action will check if it/they exist
- Search for image on: Entire screen, Foreground window only = Entire screen — Whether to look for the specified image in the foremost window only or the entire visible screen. Neither choice will find the image if it isn't clearly visible on the screen
- Search mode: Search whole screen or foreground window, Search on specified subregion of screen or foreground window = Search whole screen or foreground window — Whether to scan the entire screen (or window) to find the supplied text or only a narrowed down subregion of it
- Wait for all images: Boolean value = False — Whether to wait for all the images on the list to appear(disappear), or just one of them
- X1(任意): Numeric value — The start X coordinate of the subregion to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion to scan for the supplied text
- Y1(任意): Numeric value — The start Y coordinate of the subregion to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion to scan for the supplied text
- Tolerance(任意): Numeric value = 10 — Specify how much the image(s) searched for can differ from the originally chosen image
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
- Fail with timeout error: Boolean value = False — Specify whether you want the action to wait indefinitely or fail after a set time period
出力:
- X: Numeric value — The X coordinate of the point where the text was found on the screen. If the text has been search in the foreground window, this value is relative to the top left corner of the window.
- Y: Numeric value — The Y coordinate of the point where the text was found on the screen. If the text has been search in the foreground window, this value is relative to the top left corner of the window.
例外: Wait for image failed; Can't check image in noninteractive mode; Invalid subregion coordinates

## Hover mouse over UI element in window  `#hoveronelement`
Hover the mouse over any UI element on window.
入力:
- UI element: UI element — Select the UI element in window to hover
例外: Failed to hover over element

## Click UI element in window  `#click`
Clicks on any UI element of a window.
入力:
- UI element: UI element — The UI element to click on
- Click type: Left-click, Right-click, Double-click, Middle-click, Left button down, Left button up, Right button down, Right button up = Left-click — The kind of click to perform
- Simulate action: Boolean value = False — Specify whether to simulate the move of the mouse cursor over the element prior to clicking. This option does not require the UI element's screen to be focused, it will not automatically bring it to the foreground. Note this option can be applied only to left-click action and it might not be applicable to every UI element.
- Mouse position relative to UI element: Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right = Middle center — Specify which section of the UI element the mouse will be moved to prior to clicking
- Offset X(任意): Text value = 0 — Offset the mouse from the position by this many pixels to the right
- Offset Y(任意): Text value = 0 — Offset the mouse from the position by this many pixels down
例外: Click failed

## Select menu option in window  `#selectmenuoption`
Selects an option in a menu of a window.
入力:
- UI element: UI element — The menu option to select
例外: Failed to select option

## Drag and drop UI element in window  `#draganddropelement`
Drags and drops a UI element of a window.
入力:
- UI element to drag: UI element — The UI element to drag
- UI element to drop over: UI element — The UI element to drop over
- Click type: Left-click, Right-click = Left-click — Specify which mouse button to use for clicking and holding down, while dragging the UI element over to its destination
- Mouse down offset X(任意): Text value = 0 — Offset the mouse-down click, that will be used to grab the UI element drag, by this many pixels to the right
- Mouse down offset Y(任意): Text value = 0 — Offset the mouse-down click, that will be used to grab the UI element to drag, by this many pixels downwards
- Mouse down position relative to drag-target UI element: Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right = Middle center — Specify which section of the UI element to drop the mouse onto prior to clicking
- Mouse up offset X(任意): Text value = 0 — Offset the mouse-up click, that will be used to grab the UI element to drag, by this many pixels to the right
- Mouse up offset Y(任意): Text value = 0 — Offset the mouse-up click, that will be used to grab the UI element to drag, by this many pixels downwards
- Mouse up position relative to drop-target UI element: Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right = Middle center — Specify which section of the UI element to drag the mouse onto after clicking
例外: UI element to drag wasn't found; Drop target UI element wasn't found; Drag and drop failed

## Expand/collapse tree node in window  `#expandcollapsetreenode`
Expands or collapses a node of a tree view residing in a window.
入力:
- UI element: UI element — The tree node to expand/collapse
- Folders path(任意): Text value — A forward slash separated path made out of folder names leading to the tree node to expand or collapse
- Use regular expressions: Boolean value = False — Specify whether each folder name in the path to interpret as a regular expression
- Operation: Expand, Collapse = Expand — Specify whether to expand or collapse the tree node
例外: Failed to set tree node to the specified state

## If window  `#ifwindowaction`
This action marks the beginning of a conditional block of actions depending on whether a window is open or not or whether a window is the focused (foreground) window.
入力:
- Get window: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the Window using a UI element or a combination of window title/class
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window: UI element — The window UI element
- Window instance: Numeric value — The instance or handle of the window to check
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to be used.
- Check if window: Is open, Isn't open, Is focused, Isn't focused = Is open — The state of the window to be checked

## Wait for window  `#waitforwindowaction`
Suspends the execution or the process until a specific window opens, closes, get or loses the focus.
入力:
- Find window: By window UI element, By window instance/handle, By title and/or class = By window UI element — Specify whether to look for the window using a UI element or a combination of window title/class
- Window title(任意): Text value — The window title. Wildcards can be used, like '?' or '*'.
- Window: UI element — The window UI element
- Window instance: Numeric value — The instance or handle of the window to check
- Window class(任意): Text value — If there are two windows with the same title, window class might help differentiate between them. In this case, enter the class of the window to be used
- Wait for window to: Open, Close, Become focused, Lose focus = Open — Whether to wait for a specific window to open, close, become focused (i.e become the foreground window), or lose focus (i.e stop being the foreground window).
- Focus window after it opens: Boolean value = False — Bring the window to the front after it opens, so later actions are directed at this window
例外: Can't focus window; Wait for window failed; Can't perform window-related action in noninteractive mode
