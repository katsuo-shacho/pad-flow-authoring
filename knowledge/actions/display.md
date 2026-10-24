# Message boxes actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/display （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: You can use message boxes in your desktop flows to interact with users, request input, and provide an output. To display a message to the user while a flow runs, use the Display message action. You must specify the title of the message box, its content, the icon and the buttons in the box to be displayed. Moreover, you might set a default button to be preselected as well as to indicate if the message box should always be on top of all other windows on your machine and whether the message box is to be closed automatically after a certain amount of time. The example here displays a message box t

## Display message  `#showmessagedialog`
Displays a message box.
入力:
- Message box title(任意): Text value — The text to use as the message box title
- Message to display(任意): Text value — The text to display as the actual message
- Message box icon: None, Information, Question, Warning, Error = None — The icon to display with the message box
- Message box buttons: OK, OK - Cancel, Yes - No, Yes - No - Cancel, Abort - Retry - Ignore, Retry - Cancel = OK — The buttons to display on the message box
- Default button: First button, Second button, Third button = First button — The button to highlight by default. If the user presses Enter, this button will be pressed
- Keep message box always on top: Boolean value = False — Specify whether the message box should always remain on top of all other windows
- Close message box automatically: Boolean value = False — Specify whether the message box closes automatically after a preset time, as if the default button was pressed. Otherwise, the flow will wait until a button is pressed by the user
- Timeout(任意): Numeric value = 3 — The seconds to pause the automation while waiting for input, until continuing automatically
出力:
- ButtonPressed: Text value — The text of the button pressed
例外: Failed to display message box; Can't display message box in noninteractive mode

## Display input dialog  `#inputdialog`
Displays a dialog box that prompts the user to enter text.
入力:
- Input dialog title(任意): Text value — The dialog title
- Input dialog message(任意): Text value — The dialog message
- Default value(任意): Text value — Specify the text to display by default. If the user wishes to change this text, they can type over it. Otherwise, the default text will be used
- Input type: Single line, Password, Multiline = Single line — The format for the input text. Choose Single line - password to hide the text or multiline so that a larger display box makes visible more than one line of text
- Keep input dialog always on top: Boolean value = False — Specify whether the input dialog should always remain on top of all other windows
- Exception:  — 
- Failed to display input dialog:  — 
- Can't display input dialog in non interactive mode:  — 
出力:
- UserInput: Text value — The text entered by the user, or the default text
- ButtonPressed: Text value — The text of the button pressed. The user will automatically be given the choice of OK or Cancel

## Display select date dialog  `#selectdatedialog`
Displays a dialog box that prompts the user to enter a date or date range.
入力:
- Dialog title(任意): Text value — The dialog title
- Dialog message(任意): Text value — The dialog message
- Dialog type: Single date, Date range (two Dates) = Single date — Whether the user will enter a single date or two dates as the endpoints of a range of dates
- Prompt for: Date only, Date and time = Date only — Specify whether the user will enter the date only or the date and time
- Default value(任意): Datetime — The default value for the date
- Default value for second date(任意): Datetime — The default value for the end date in a range
- Keep date selection dialog always on top: Boolean value = False — Specify whether the date selection dialog should always remain on top of all other windows
出力:
- SelectedDate: Datetime — The date entered by the user or the default date
- SecondSelectedDate: Datetime — The second date entered by the user or that default date
- ButtonPressed: Text value — The text of the button pressed by the user. The user will automatically be given the choice of OK or Cancel
例外: Failed to display select date dialog; Can't display select date dialog in non interactive mode

## Display select from list dialog  `#selectfromlistdialog`
Displays a dialog box with options that lets the user select from a list.
入力:
- Dialog title(任意): Text value — The dialog title
- Dialog message(任意): Text value — The dialog message
- List to choose from: General value — The list to display as a drop-down menu for the user to choose from
- Keep select dialog always on top: Boolean value = False — Specify whether the select dialog should always remain on top of all other windows
- Limit to list: Boolean value = True — Whether to allow the user to enter their own answer outside of the list being displayed
- Allow empty selection: Boolean value = False — Allow the user to not select anything, creating an empty selected item output
- Allow multiple selections: Boolean value = False — Allow the user to select more than one choice. The selected item and selected index variables will hold a list of items
- Preselect items starting with a + sign: Boolean value = False — Specify whether the items with a prepended '+' sign will appear automatically preselected
出力:
- SelectedItem: Text value — The item selected from the list as text
- SelectedItems: List of Text values — The items selected from the list as a list of text
- SelectedIndex: Numeric value — The index number of the item selected from the list. You can use the item number instead of the full text of your choice
- SelectedIndexes: List of Numeric values — The index number of the items selected from the list. This parameter allows you to use the item number instead of the full text of your choice
- ButtonPressed: Text value — The name of the button pressed by the user (OK or Cancel)
例外: Failed to display select dialog; Can't display select dialog in noninteractive mode

## Display select file dialog  `#selectfiledialog`
Displays the select file dialog and prompts the user to select one or more files.
入力:
- Dialog title(任意): Text value — The dialog title
- Initial folder(任意): Folder — The initial folder to open when browsing for a file. This folder is where the select file dialog action will start the user looking for the file(s)
- File filter(任意): Text value — A filter to limit the files retrieved. This parameter allows wild cards, for example "*.txt" or "document?.doc" (without the quotes). To allow the user to choose from multiple file filters, separate the choices with a semi-colon, for example "*.txt;*.exe"
- Keep file selection dialog always on top: Boolean value = False — Whether the file selection dialog should always remain on top of all other windows
- Allow multiple selections: Boolean value = False — Whether the user will be able to select more than one file or not
- Check if file exists: Boolean value = False — Whether only files that already exist will be accepted
出力:
- SelectedFile: File — The file that will be selected through the dialog
- SelectedFiles: List of Files — The file(s) selected
- ButtonPressed: Text value — The text of the button pressed. The user will automatically be given the choice of Open or Cancel
例外: Failed to display select file dialog; Can't display select file dialog in noninteractive mode

## Display select folder dialog  `#selectfolder`
Displays the select folder dialog and prompts the user to select a folder.
入力:
- Dialog description(任意): Text value — The description of the select folder dialog For example, "Please select the folder into which you wish to copy the files"
- Initial folder(任意): Folder — The initial folder to open. This folder will be the default folder unless the user picks a new one
- Keep folder selection dialog always on top: Boolean value = False — Whether the folder selection dialog should always remain on top of all other windows
出力:
- SelectedFolder: Folder — The selected folder
- ButtonPressed: Text value — The text of the button pressed. The user will automatically be given the choice of OK or Cancel
例外: Failed to display select folder dialog; Can't display select folder dialog in noninteractive mode

## Display custom form  `#showcustomdialog`
Display a customized form that can include multiple types of elements, like text, number or file inputs etc.
出力:
- CustomFormData: Custom object — A custom object containing the user's input
- ButtonPressed: Text value — The ID of the button pressed
例外: Failed to display custom form
