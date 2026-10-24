# Terminal emulation actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/terminalemulation （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate provides integration with terminal emulators through the Terminal emulation actions. These actions enable you to handle terminals and mainframes, and perform operations such as moving the cursor, setting and getting text, and sending keys. Before deploying any terminal actions, use the Open terminal session action to open a new connection with the installed provider. If you've installed Micro Focus Reflection on your machine, choose the respective option in the Provider parameter of the action and populate the required configuration. If you've installed another provider, select 

## Open terminal session  `#openterminalsession`
Open a new terminal session.
入力:
- Provider: Micro focus reflection, HLLAPI = Micro focus reflection — The terminal emulation to use
- HLLAPI DLL path: File — The HLLAPI DLL of the provider. RocketSoftware BlueZone default name: 'ehlapi64.dll'. IBM Personal Communications default name: 'EHLAPI32.dll'. MicroFocus Rumba default path: 'System/ehlapi32.Dll'. Cybelesoft zScope default name: 'zHllap32.dll'. Any other provider that offers an HLLAPI DLL in its installation folder.
- Installation path: Folder — The installation path of the provider's application on the user's file system
- Configuration: Existing profile, Specify connection = Existing profile — Choose 'Existing profile' to select a file containing a preconfigured terminal emulation connection. Choose 'Specify connection' to specify the type of the connection, the host address and the port.
- Session name: Text value — The session name to connect to. The HLLAPI short name, and it's a unique identifier for the host session. It can be found in the Terminal emulator's configuration settings.
- Host type: IBM 3270, IBM 5250 = IBM 3270 — The host type of the connection
- Profile: File — The file that contains the preconfigured connection
- Host address: Text value — The host's address to connect to
- Port: Numeric value — The port to be used for this connection
- Attach to running session: Boolean value = False — Specifies whether to attach to a currently open/running terminal session
出力:
- TerminalSession: Terminal session — The specific terminal session for use with later terminal emulation commands
例外: Error communicating with the emulator; Profile error

## Close terminal session  `#closesession`
Close an open terminal session.
入力:
- Terminal session to close: Terminal session — The previously opened terminal session
例外: Error communicating with the emulator

## Move cursor on terminal session  `#movecursor`
Move the terminal's cursor on the specified position.
入力:
- Terminal session: Terminal session — The terminal session to work with
- Row: Numeric value — The vertical position of the cursor on the screen
- Column: Numeric value — The horizontal position of the cursor on the screen
例外: Screen position out of bounds; Position commands aren't supported by the emulator; Operation is unavailable for this session type; Error communicating with the emulator

## Get text from terminal session  `#gettextfromterminalsession`
Get text from a terminal session.
入力:
- Terminal session: Terminal session — The terminal session to work with
- Get text from: Field, Entire screen, Cursor position, Specific position = Field — The location to get the text from
- Get field by: Label, Index, Position = Label — Specifies how to look for the field
- Label: Text value — The label of the field to look for
- Index: Numeric value — The index of the field to look for
- Text length: Numeric value — The length of the text to receive
- Row: Numeric value — The vertical position of the field on the screen
- Column: Numeric value — The horizontal position of the field on the screen
出力:
- TerminalText: Text value — The text retrieved from the terminal session
例外: Error communicating with the emulator; Field index out of bounds; Field label not found; Screen position out of bounds; No field found at the given position; Terminal screen is unformatted; Position commands aren't supported by the emulator; Operation is unavailable for this session type

## Set text on terminal session  `#settextonterminalsession`
Set text on a terminal session.
入力:
- Terminal session: Terminal session — The terminal session to work with
- Text: Direct encrypted input or Text value — The text to set on the specified location
- Set text: Cursor position, Field = Field — The location to set the text to
- Get field by: Label, Index, Position = Label — Specifies the way by which to look for the field
- Label: Text value — The label of the field to look for
- Index: Numeric value — The index of the field on the screen
- Row: Numeric value — The vertical position of the field on the screen
- Column: Numeric value — The horizontal position of the field on the screen
- Treat @ character as literal: Boolean value = False — Check this box to send the '@' character literally. Leave this option disabled to sent it as a special character
例外: Error communicating with the emulator; Field index out of bounds; Field label not found; Screen position out of bounds; No field found at the given position; Terminal screen is unformatted; Position commands aren't supported by the emulator; Operation is unavailable for this session type; Input text was rejected

## Send key to terminal session  `#sendkey`
Send a control key to a terminal session.
入力:
- Terminal session: Terminal session — The terminal session to work with
- Control key: Transmit, Alt cursor, Attention, Backspace, Back tab, Block toggle, Break, Cancel, Center, Clear, Clear comm, Clear display, Clear line, Clear page, Clear partition, Comma, Command line, Command window, Compose, Ctrl+F1, Ctrl+F2, Ctrl+F3, Ctrl+F4, Ctrl+F5, Ctrl+F6, Ctrl+F7, Ctrl+F8, Ctrl+F9, Ctrl+F10, Ctrl+F11, Ctrl+F12, Ctrl+Shift+F1, Ctrl+Shift+F2, Ctrl+Shift+F3, Ctrl+Shift+F4, Ctrl+Shift+F5, Ctrl+Shift+F6, Ctrl+Shift+F7, Ctrl+Shift+F8, Ctrl+Shift+F9, Ctrl+Shift+F10, Ctrl+Shift+F11, Ctrl+Shift+F12, Cursor blink, Cursor select, Decimal, Delete, Delete char, Delete line, Delete word, Destructive back space, Disconnect, Do, Down, Down double, Dup, Duplicate, Edit script, Key end, End of field, Erase EOF, Erase EOL, Erase EOP, Erase input, Escape, ExtGr, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45, F46, F47, F48, Field delimiter, Field exit, Field mark, Field minus, Field plus, Find, Hard reset, Help, Hex, Hex 00, Hex 01, Hex 02, Hex 03, Hex 04, Hex 05, Hex 06, Hex 07, Hex 08, Hex 09, Hex 0A, Hex 0B, Hex 0C, Hex 0D, Hex 0E, Hex 0F, Hex 10, Hex 11, Hex 12, Hex 13, Hex 14, Hex 15, Hex 16, Hex 17, Hex 18, Hex 19, Hex 1A, Hex 1B, Hex 1C, Hex 1D, Hex 1E, Hex 1F, Hex 7F, Hold, Hold clear, Hold set, Home, Home down, Home up, Insert, Insert char, Insert here, Insert line, Insert mode, Invalid key, KeyPad0, KeyPad1, KeyPad2, KeyPad3, KeyPad4, KeyPad5, KeyPad6, KeyPad7, KeyPad8, KeyPad9, Left, Left double, Line feed, Minus, Monitor toggle, New line, Next page, Next screen, Next word, Nul, NumLock, PA1, PA2, PA3, Page, Page down, Page up, Pan left, Pan right, Partition jump, PF1, PF2, PF3, PF4, Plus Cr, Previous word, PrevPage, PrevScreen, Print, Print line, Print Msg, Prent screen, Remove, Replace, Reset, Return, Reserve field, Right, Right double, Roll down, Roll up, Rile line, Run script, Scroll down, Scroll left, Scroll right, Scroll up, Select, Send, Send answer back, Send delete, Send line, Send Msg, Shift+Backspace, Shift+Delete, Shift+Down, Shift+F1, Shift+F2, Shift+F3, Shift+F4, Shift+F5, Shift+F6, Shift+F7, Shift+F8, Shift+F9, Shift+F10, Shift+F11, Shift+F12, Shift+F13, Shift+F14, Shift+F15, Shift F16, Shift+F17, Shift+F18, Shift+F19, Shift+F20, Shift+Home, Shift+Insert, Shift+Left, Shift+Print screen, Shift+Right, Shift+Up, Soft reset, System request, Tab, Tek zoom, Term next page, Term prev page, Test, Text assist begin bold, Text assist begin of line, Text assist begin underline, Text assist bottom of page, Text assist carrier return, Text assist center, Text assist end bold, Text assist end of line, Text assist half index down, Text assist half index up, Text assist insert symbols, Text assist next stop, Text assist next text column, Text assist page end, Text assist required space, Text assist required tab, Text assist stop, Text assist text tab advance, Text assist top of page, Text assist word underline, Trace Toggle, Udk 10, Udk 6, Udk 7, Udk 8, Udk 9, Udk 11, Udk 12, Udk 13, Udk 14, Udk 15, Udk 16, Udk 17, Udk 18, Udk 19, Udk 20, Up, Up double = Transmit — The key to submit to the session
例外: Error communicating with the emulator; Key not supported

## Wait for text on terminal session  `#waitfortextonterminalsession`
Wait for a specific text to appear on a terminal session.
入力:
- Terminal session: Terminal session — The previously opened terminal session
- Text to wait for: Text value — The text or regular expression to wait to appear on the terminal screen or on a specified field
- Regular expression: Boolean value = False — Specifies whether to wait for a regular expression instead of plain text
- Wait for text location: Screen, Field = Screen — The location to wait for the text to appear on
- Get field by: Label, Index, Position = Label — Specifies the way by which to look for the field
- Label: Text value — The label of the field to look for
- Index: Numeric value — The index of the field to look for
- Row: Numeric value — The vertical position of the field on the screen
- Column: Numeric value — The horizontal position of the field on the screen
- Timeout(任意): Numeric value = 0 — The maximum amount of time to wait
例外: Error communicating with the emulator; Field index out of bounds; Field label not found; Screen position out of bounds; No field found at the given position; Terminal screen is unformatted; Position commands aren't supported by the emulator; Operation is unavailable for this session type; Timeout expired

## Search for text on terminal session  `#searchfortextonterminalsession`
Search for all occurrences of a specific text on a terminal session
入力:
- Terminal session: Terminal session — The previously opened terminal session
- Text to search for: Text value — The text or regular expression to search for on the terminal screen
- Regular expression: Boolean value = False — Specifies whether to search for a regular expression instead of plain text
- Column size: Numeric value = 80 — The number of the columns on the terminal screen
出力:
- FindResults: Datatable — The search results retrieved from the terminal session screen
例外: Error communicating with the emulator; Text not found; Invalid regex expression
