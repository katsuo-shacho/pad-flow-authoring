# Mouse and keyboard actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/mouseandkeyboard （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Simulate keyboard activity with the Send Keys action. To insert special keys, such as the arrow keys and Caps Lock, and modifies, such as Shift and Control, select Insert special key. The following examples add a signature to an email message, starting with two line breaks. Then, the action sends Ctrl + A and Ctrl + C to select and copy the text to the clipboard. To simulate mouse movements, use the Move mouse action. The following example moves the mouse manually to specific coordinates at normal speed. Move the mouse to a specific image on the screen with the Move mouse to image action. The 

## Block Input  `#blockinput`
Blocks user mouse and keyboard input, so that the flow can perform mouse and keyboard actions without interference from the user.
入力:
- Block it: Boolean value = True — Specify whether to block or unblock mouse and keyboard input
- Exception:  — 
- Can't block/unblock user input in non interactive mode:  — 
- Failed to block/unblock input:  — 

## Get mouse position  `#getmouseposition`
Retrieves the current position of the mouse cursor on the screen in pixel coordinates.
入力:
- Relative to: Screen, Foreground window = Screen — Specify whether to retrieve the mouse position in screen coordinates or relative to the top left corner of the active window
出力:
- MousePosX: Numeric value — The horizontal (X) value of the mouse position
- MousePosY: Numeric value — The vertical (Y) value of the mouse position
例外: Can't retrieve the mouse position in non interactive mode

## Move mouse  `#movemouse`
Moves the mouse to a specific position.
入力:
- Position X: Numeric value — The horizontal (X) value of the position to send the mouse to
- Position Y: Numeric value — The vertical (Y) value of the position to send the mouse to
- Relative to: Screen, Active window, Current mouse position = Screen — Specify whether the new mouse position will be relative to the top left corner of the screen, the foremost window, or the current mouse position
- Move mouse from previous position: Instant, With animation (low speed), With animation (normal speed), With animation (high speed) = Instant — Specify how to move the mouse
例外: Can't move mouse in non interactive mode; Failed to move mouse

## Move mouse to image  `#movemousetoimagebase`
Moves the mouse over an image found on screen or on the foreground window.
入力:
- Image to move mouse to: List of Images — The list of Images to move the mouse to
- Mouse movement style: Instant, With animation (low speed), With animation (normal speed), With animation (high speed) = Instant — Specify the style of movement in which the mouse will move from its previous position to the beginning of the recorded route (or to its final position)
- Occurrence(任意): Numeric value = 1 — The occurrence of the image found to move the mouse to
- Send a click after moving mouse: Boolean value = False — Specify whether to send a click after the mouse is positioned over the image
- Click type: Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up = Left click — The mouse click to send to the image
- Wait for image to appear: Boolean value = True — Choose whether you want the action to wait if the image isn't found on the screen or foreground window
- Fail timeout(任意): Numeric value = 0 — The fail timeout in seconds
- Seconds before click(任意): Numeric value = 0 — The number of seconds to wait before sending the click
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
- Mouse position relative to image: top left corner, top center, top right corner, middle left part, center, middle right part, bottom left corner, bottom center, bottom right corner = center — The section of the image the mouse will be moved to
- Offset X: Text value = 0 — The pixels to offset the mouse from the position to the right
- Offset Y: Text value = 0 — The pixels to offset the mouse from the position down
- Tolerance(任意): Numeric value = 10 — Specify how much the specified image can differ from the originally chosen image
- Search for image on: Entire screen, Foreground window only = Entire screen — Specify whether to search for the specified Image in the foremost window only, or the entire visible screen. Neither choice will find the image if it isn't clearly visible on the screen
- Search mode: Search whole screen or foreground window, Search on specified subregion of screen or foreground window = Search whole screen or foreground window — Specify whether to scan the entire screen (or window) to find the supplied image or only a subregion of it
- X1(任意): Numeric value — The starting X of the subregion to search in
- Y1(任意): Numeric value — The starting Y of the subregion to search in
- X2(任意): Numeric value — The ending X of the subregion to search in
- Y2(任意): Numeric value — The ending Y of the subregion to search in
出力:
- X: Numeric value — The X coordinate of the point where the image is found on the screen. If the image is being searched for on the foreground window, the coordinate returned is relative to the top left corner of the window
- Y: Numeric value — The Y coordinate of the point where the image is found on the screen. If the image is being searched for on the foreground window, the coordinate returned is relative to the top left corner of the window
例外: Image not found on screen; Can't move mouse in non interactive mode; Failed to move mouse; Invalid subregion coordinates; Not enough Image occurrences found on screen

## Move mouse to text on screen (OCR)  `#movemousetotextonscreenwithocraction`
Moves the mouse over a text found on the screen or on the foreground window using OCR.
入力:
- OCR engine type: OCR engine variable, Tesseract engine = OCR engine variable — The OCR engine type to use. Select a peconfigured OCR engine or set up a new one.
- OCR engine variable: OCREngineObject — The OCR engine to search for the text with
- Text to find: Text value — The text to move the mouse over
- Is regular expression: Boolean value = False — Whether to use a regular expression to look for the text on screen
- Occurrence(任意): Numeric value = 1 — A positive number that will be used as the occurrence of the input text on screen
- Search for text on: Entire screen, Foreground window only = Entire screen — Whether to look for the specified text in the foremost window only or the entire visible screen. Neither choice will find the text if it isn't clearly visible on the screen
- Search mode: Whole of specified source, Specific subregion only, Subregion relative to image = Whole of specified source — Whether to scan the entire screen (or window) to find the supplied text or only a narrows down subregion of it
- Image(s): List of Images — The image(s) specifying the subregion (relative to the top left corner of the image) to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion to scan for the supplied text
- Tolerance(任意): Numeric value = 10 — Specify how much the image(s) searched for can differ from the originally chosen image
- Y1(任意): Numeric value — The start Y coordinate of the subregion to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion relative to the specified image to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion to scan for the supplied text
- Y1(任意): Numeric value — The start Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Move mouse from previous position: Instant, With animation (low speed), With animation (normal speed), With animation (high speed) = Instant — The style of movement in which the mouse will move from its previous position to its final position
- Windows OCR language: Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish = English — The language of the text that the Windows OCR engine detects
- Use other language: Boolean value = False — Specifies whether to use a language not given in the 'Tesseract language' field
- Tesseract language: English, German, Spanish, French, Italian = English — The language of the text that the Tesseract engine detects
- Language abbreviation: Text value — The Tesseract abbreviation of the language to use. For example, if the data is 'eng.traineddata', set this parameter to 'eng'
- Language data path: Text value — The path of the folder that holds the specified language's Tesseract data
- Image width multiplier: Numeric value = 1 — The width multiplier of the image
- Image height multiplier: Numeric value = 1 — The height multiplier of the image
- Wait for text to appear: Boolean value = False — Specify whether to wait if the text isn't found on the screen or foreground window
- Fail if text doesn't appear within(任意): Numeric value = 10 — The number of seconds to wait for the supplied text to appear
- Send a click after moving mouse: Boolean value = False — Specify whether to send a click after the mouse is positioned over the text
- Click type: Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up = Left click — The mouse click type to send to the text
- Wait before clicking for(任意): Numeric value = 1 — The number of seconds to wait before clicking
- Mouse position relative to text: Top left, Top center, Top right, Middle left, Middle center, Middle right, Bottom left, Bottom center, Bottom right = Middle center — Specify which section of the text the mouse will be moved to
- Offset X: Text value = 0 — Offset the mouse from the position by this many pixels to the right
- Offset Y: Text value = 0 — Offset the mouse from the position by this many pixels down
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
出力:
- LocationOfTextFoundX: Numeric value — The X coordinate of the point where the text is found on the screen. If the text is searched for in the foreground window, this coordinate is relative to the top left corner of the window
- LocationOfTextFoundY: Numeric value — The Y coordinate of the point where the text is found on the screen. If the text is searched for in the foreground window, this coordinate is relative to the top left corner of the window
- WidthOfTextFound: Numeric value — The width of the area the text was found on
- HeightOfTextFound: Numeric value — The width of the area the text was found on
例外: Text not found on screen; Can't move mouse in non interactive mode; Failed to move mouse; Invalid subregion coordinates; Failed to create the OCR engine; Data path folder doesn't exist; The selected Windows language pack isn't installed on the machine; OCR engine isn't alive

## Send mouse click  `#sendmouseclick`
Sends a mouse click event.
入力:
- Mouse event to send: Left click, Right click, Double click, Middle click, Left button down, Left button up, Right button down, Right button up = Left click — Specify what form of mouse event to send
- Wait(任意): Numeric value = 0 — The time to delay before sending the mouse event in 1/1000 of a second
- Move mouse: Boolean value = False — Move mouse
- X: Numeric value — The horizontal (X) position of the mouse in pixel coordinates
- Y: Numeric value — The vertical (Y) position of the mouse in pixel coordinates
- Relative to: Screen, Active window, Current mouse position = Screen — Specify whether the new mouse position will be relative to the top left corner of the screen, the foremost window, or the current mouse position
- Mouse movement style: Instant, With animation (low speed), With animation (normal speed), With animation (high speed) = Instant — The style of movement in which the mouse will move from its previous position to the beginning of the recorded route (or to its final position)
例外: Can't send mouse click in non interactive mode; Mouse click out of screen bounds; Failed to send mouse click

## Send keys  `#sendkeys`
Sends keys to the application that is currently active.
入力:
- Send keys to: Foreground window, By UI element, By window instance/handle, By title and/or class = Foreground window — Specify whether to send the keys to the foreground window or to a UI element or to a window instance or a combination of window title/class
- Text to send: Direct encrypted input or Text value — The text to send to the application
- Delay between keystrokes(任意): Numeric value = 10 — Specify the delay in milliseconds between sending keystrokes to avoid input errors
- Send Text as hardware keys: Boolean value = False — Emulate the actual keystrokes on keyboard when sending whole Text
例外: Can't send keystrokes in non interactive mode; Text to send doesn't represent valid keystrokes; There isn't an active application to send keystrokes to; Failed to send keystrokes

## Press/release key  `#pressreleasekey`
Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).
入力:
- Action to perform: Press, Release = Press — Specify whether to press or release keys with this action
- Control: Boolean value = False — Specify whether the Ctrl key will be pressed/released or not
- Alt: Boolean value = False — Specify whether the Alt key will be pressed/released or not
- Shift: Boolean value = False — Specify whether the Shift key will be pressed/released or not
- Win: Boolean value = False — Specify whether the Windows key will be pressed/released or not
例外: Can't press or release key in non interactive mode

## Set key state  `#setkeystate`
Sets the state (on or off) for the keys Caps Lock, Num Lock or Scroll Lock
入力:
- Key: Caps Lock, Num Lock, Scroll Lock = Caps Lock — Specify the key to set
- State: Off, On = On — Whether to set the key state to on or off
例外: Can't set key state in non interactive mode

## Wait for mouse  `#waitformouseaction`
Suspends the execution of the flow until the mouse pointer changes, usually to or from the 'wait cursor' or hourglass.
入力:
- Wait for mouse pointer to: Become, Become not = Become — Choose what action of the mouse cursor to wait for.
- Mouse pointer: Arrow, App starting, Cross, Hand, Help, IBeam, Wait cursor = Arrow — Specify the mouse pointer state.

## Get keyboard identifier  `#getkeyboardlayout`
Retrieves the active keyboard identifier from the machine's registry.
出力:
- KeyboardLayoutId: Numeric value — The registry key of the active keyboard identifier
例外: Keyboard identifier wasn’t found

## Wait for shortcut key  `#waitforshortcutkeyaction`
Pause the flow run until a specific shortcut key is pressed. Shortcut keys must contain at least one key or a key and one of (ctrl, alt, shift). Multiple shortcut keys can be defined.
入力:
- Shortcut keys: Keys combination = Ctrl + A — Specify the shortcut keys to wait for. Shortcut keys must contain exactly one key or a key and a combination of (ctrl, alt, shift). To add more than one shortcut key, select 'New shortcut key'
- Continue flow run on timeout: Boolean value = False — Specify whether the flow run will continue anyway when the set period of time waiting for the shortcut key expires
- Continue after(任意): Numeric value = 10 — The time in seconds before continuing the flow run
出力:
- IndexOfShortcutKeyPressed: Numeric value — The index of the shortcut key if the shortcut keys are in a list format.
例外: Shortcut key failed to register
