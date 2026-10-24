# PAD アクション カタログ（第1層・コア）

出典: Microsoft Power Automate documentation (MicrosoftDocs/power-automate-docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/) の actions-reference を本プロジェクトが要約・圧縮したもの。Microsoft の見解ではない（LEGAL.md）。
1行＝1アクション。
詳細（引数・既定値・例外）は `actions/<group>.md` を読む。
Robin（貼付テキスト）上の正式名はDesignerからのコピーで確認する（ここには無い）。

業務でまず使う群。クラウド/AD/SAP/認知サービス等は catalog-extended.md。
各群の `Robin:` 行が貼付用 ID の置き場（knowledge/robin/）。KB だけにある群: powerpoint, triggers, computeruse, llm。
自分のノウハウ（使い方のコツ・はまりどころ）は各群の末尾に `  - memo:` 行で足してよい。再生成時は scripts/ の MEMO を参照。

## Clipboard actions reference → actions/clipboard.md (3)
Robin: robin/clipboard.md
- Get clipboard text: Gets clipboard text.
- Set clipboard Text: Sets clipboard text.
- Clear clipboard contents: Clears clipboard contents.

## Cloud Connectors in Power Automate for desktop → actions/cloudconnectors.md (5)
Robin: KB未収録（Designerコピーで確認）
- Prerequisites and limitations: - To use premium connectors, you need an Attended RPA license. If you have a free work ...
- Use files in cloud connector actions: To pass a file as an input to a cloud connector action, first convert the file to binar...
- Embed connection references on a desktop flow: By using connection reference embedding, you can give other co-owners access to your co...
- Bring your own connection in console runs: If you're a co-owner, bring your own connection (BYOC) in console runs for connection r...
- List of cloud connectors: Power Automate for desktop adds these cloud connectors to desktop flows by default. You...

## CMD session actions reference → actions/cmd.md (5)
Robin: robin/cmd.md
- Open CMD session: Open a new CMD session.
- Read from CMD session: Read the output of a CMD session.
- Write to CMD session: Execute a command on an open CMD session.
- Wait for text on CMD session: Wait for a specific text on a previously opened CMD session.
- Close CMD session: Close a previously opened CMD session.

## Compression actions reference → actions/compression.md (2)
Robin: robin/compression.md
- ZIP files: Compress one or more files or folders into a ZIP archive.
- Unzip files: Uncompress one or more files or folders contained in a ZIP archive.

## Conditional actions reference → actions/conditionals.md (6)
Robin: （組込み文: robin-rules.md）
- Case: An expression that, if met, a block of actions associated with that particular case runs.
- Default case: A block of actions that is run, if no case expression has been met in the switch body.
- Else: Marks the beginning of a block of actions that ran if the condition specified in the pr...
- Else if: Marks the beginning of a block of actions that run if the conditions specified in the p...
- If: Marks the beginning of a block of actions that is run if the condition specified in thi...
- Switch: Dispatches execution to different parts of the switch body based on the value of the ex...

## Database actions reference → actions/database.md (4)
Robin: robin/database.md
- Open SQL connection: Open a new connection to a database.
- Execute SQL statement: Connect to a database and execute a SQL statement.
- Natural language to script powered by copilot (preview): !INCLUDE [cc-beta-prerelease-disclaimer]
- Close SQL connection: Close an open connection to a database.

## Date time actions reference → actions/datetime.md (3)
Robin: robin/datetime.md
- Add to datetime: Adds (or subtracts) a specific number of seconds, minutes, hours or days to a datetime ...
- Subtract dates: Finds the time difference between two given dates in days, hours, minutes, or seconds.
- Get current date and time: Retrieves the current date or the current date and time.

## Message boxes actions reference → actions/display.md (7)
Robin: robin/display.md
- Display message: Displays a message box.
- Display input dialog: Displays a dialog box that prompts the user to enter text.
- Display select date dialog: Displays a dialog box that prompts the user to enter a date or date range.
- Display select from list dialog: Displays a dialog box with options that lets the user select from a list.
- Display select file dialog: Displays the select file dialog and prompts the user to select one or more files.
- Display select folder dialog: Displays the select folder dialog and prompts the user to select a folder.
- Display custom form: Display a customized form that can include multiple types of elements, like text, numbe...

## Email actions reference → actions/email.md (3)
Robin: robin/email.md
- Retrieve email messages: Retrieves email messages from an IMAP server.
- Process email messages: Moves, deletes or marks as unread an email (or a list of emails) retrieved by a Retriev...
- Send email: Creates and sends a new email message.

## Excel actions reference → actions/excel.md (41)
Robin: robin/excel.md
- Resize columns/rows in Excel worksheet: Resizes a selection of columns or rows in the active worksheet of an Excel instance.
- Run Excel macro: Runs a specified macro on the document of an Excel instance.
- Get active Excel worksheet: Retrieves an Excel document's active worksheet.
- Get all Excel worksheets: Retrieves all worksheet names of an Excel document.
- Delete Excel worksheet: Deletes a specific worksheet from an Excel instance.
- Rename Excel worksheet: Renames a specific worksheet of an Excel instance.
- Copy Excel worksheet: Copies a worksheet from an Excel document and paste it to the Excel document of the sam...
- Activate cell in Excel worksheet: Activate a cell in the active worksheet of an Excel instance, by providing column, row,...
- Select cells in Excel worksheet: Selects a range of cells in the active worksheet of an Excel instance.
- Get selected cell range from Excel worksheet: Retrieve the selected range of cells in a structure consisting of first column, first r...
- Copy cells from Excel worksheet: Copies a range of cells from the active worksheet of an Excel instance.
- Paste cells to Excel worksheet: Pastes a range of cells to the active worksheet of an Excel instance.
- Delete from Excel worksheet: Deletes a cell or a range of cells from the active worksheet of an Excel instance.
- Insert row to Excel worksheet: Inserts a row above a selected row of an Excel instance.
- Delete row from Excel worksheet: Deletes a selected row from an Excel instance.
- Insert column to Excel worksheet: Inserts a column to the left of a selected column of an Excel instance.
- Delete column from Excel worksheet: Deletes a selected column from an Excel instance.
- Find and replace cells in Excel worksheet: Finds text and replaces it with another in the active worksheet of an Excel instance.
- Get first free row on column from Excel worksheet: Retrieve the first free row, given the column of the active worksheet.
- Read formula from Excel: Reads the formula inside a cell in Excel.
- Get table range from Excel worksheet: Retrieves the range of a table in the active worksheet of an Excel instance.
- Auto fill cells in Excel worksheet: Auto fills a range with data, based on the data of another range, in the active workshe...
- Append cells in Excel worksheet: Appends a range of cells to the active worksheet of an Excel instance.
- Lookup range in Excel worksheet: Finds and returns the result of Excel's LOOKUP function.
- Set color of cells in Excel worksheet: Fills the background of the selected cells with the specified color, in the active work...
- Launch Excel: Launches a new Excel instance or opens an Excel document.
- Attach to running Excel: Attaches to an Excel document that's already open.
- Read from Excel worksheet: Reads the value of a cell or a range of cells from the active worksheet of an Excel ins...
- Get active cell on Excel worksheet: Get the active cell in the active worksheet of the Excel document.
- Save Excel: Saves a previously launched Excel instance.
- Write to Excel worksheet: Writes a value into a cell or a range of cells of an Excel instance.
- Close Excel: Closes an Excel instance.
- Set active Excel worksheet: Activates a specific worksheet of an Excel instance.
- Add new worksheet: Adds a new worksheet to the document of an Excel instance.
- Get first free column/row from Excel worksheet: Retrieves the first free column and/or row of the active worksheet. This is useful for ...
- Get column name on Excel worksheet: Gets the name of the column.
- Clear cells in Excel worksheet: Clears a range of cells or a named cell in the active worksheet of an Excel instance.
- Sort cells in Excel worksheet: 
- Filter cells in Excel worksheet: The Filter cells in Excel worksheet allows makers to create and apply a filter in the a...
- Clear filters in Excel worksheet: 
- Get empty cell: 

## File actions reference → actions/file.md (16)
Robin: robin/file.md
- If file exists: Marks the beginning of a conditional block of actions depending on whether a file exist...
- Wait for file: Suspend the execution of the automation until a file is created or deleted.
- Copy file(s): Copy one or more files into a destination folder.
- Move file(s): Move one or more files into a destination folder.
- Delete file(s): Delete one or more files.
- Rename file(s): Change the name of one or more files.
- Read text from file: Read the contents of a text file.
- Write text to file: Write or appends text to a file.
- Read from CSV file: Read a CSV file into a data table.
- Write to CSV file: Write a data table, data row or list to a CSV file.
- Get file path part: Retrieve one or more parts (directory, filename, extension, etc.) from a text that repr...
- Get temporary file: Create a uniquely named, empty temporary file on disk, and get the file object (which i...
- Convert file to Base64: Convert a file to Base64 encoded text.
- Convert Base64 to file: Convert a Base64 encoded text to file.
- Convert file to binary data: Convert a file to binary data.
- Convert binary data to file: Convert binary data to file.

## Flow control actions reference → actions/flowcontrol.md (14)
Robin: flowcontrol（IF/LOOP/BLOCK等の組込み文は robin-rules.md）
- If safe stop requested: Checks whether safe stop is requested for the specific flow.
- Comment: User comment.
- End: Signifies the end of a block.
- End region: Marks the end of a group of actions.
- Exit subflow: Exits current subflow and returns to the point it was called from.
- Get last error: Retrieves the last error that occurred in the flow.
- Go to: Transfers the flow of execution to another point, indicated by a label.
- Label: Acts as the destination of a 'go to' statement.
- Throw custom error: Raises a user-defined error by using a specified error name and message. By using this ...
- On block error: Marks the beginning of a block to handle actions errors.
- Region: Marks the beginning of a group of actions.
- Run subflow: Runs a subflow and specifies any required arguments.
- Stop flow: Terminates the flow.
- Wait: Suspends the execution of the flow for a specified number of seconds.

## Folder actions reference → actions/folder.md (10)
Robin: robin/folder.md
- If folder exists: Mark the beginning of a conditional block of actions depending on whether a folder exis...
- Get files in folder: Retrieve the list of files in a folder.
- Get subfolders in folder: Retrieve the list of subfolders in a folder.
- Create folder: Create a new folder.
- Delete folder: Delete an existing folder and its contents (files and subfolders).
- Empty folder: Delete all the contents of a folder (files and subfolders) without deleting the folder ...
- Copy folder: Copy a folder into a destination folder.
- Move folder: Move an existing folder into a destination folder.
- Rename folder: Change the name of a folder.
- Get special folder: Retrieve the path of a Windows' special folder (such as Desktop, My Pictures, Internet ...

## Logging actions reference → actions/logging.md (1)
Robin: robin/logging.md
- Log message: Adds a custom text message to the flow run action details.

## Loops actions reference → actions/loops.md (5)
Robin: （組込み文: robin-rules.md）
- Exit loop: Terminates the loop and the flow resumes at the next action or statement following the ...
- For each: Iterates over items in a list, data table or data row, allowing a block of actions to b...
- Loop: Iterates a block of actions for a specified number of times
- Loop condition: Iterates a block of actions as long as a specified condition proves to be true.
- Next loop: Forces the next iteration of the block to take place, skipping any actions in between.

## Mouse and keyboard actions reference → actions/mouseandkeyboard.md (12)
Robin: robin/mouseandkeyboard.md
- Block Input: Blocks user mouse and keyboard input, so that the flow can perform mouse and keyboard a...
- Get mouse position: Retrieves the current position of the mouse cursor on the screen in pixel coordinates.
- Move mouse: Moves the mouse to a specific position.
- Move mouse to image: Moves the mouse over an image found on screen or on the foreground window.
- Move mouse to text on screen (OCR): Moves the mouse over a text found on the screen or on the foreground window using OCR.
- Send mouse click: Sends a mouse click event.
- Send keys: Sends keys to the application that is currently active.
- Press/release key: Presses (and holds) or releases one or more modifier keys (Alt, Control, or Shift).
- Set key state: Sets the state (on or off) for the keys Caps Lock, Num Lock or Scroll Lock
- Wait for mouse: Suspends the execution of the flow until the mouse pointer changes, usually to or from ...
- Get keyboard identifier: Retrieves the active keyboard identifier from the machine's registry.
- Wait for shortcut key: Pause the flow run until a specific shortcut key is pressed. Shortcut keys must contain...

## OCR actions reference → actions/ocr.md (3)
Robin: robin/ocr.md
- Use the Tesseract OCR engine: Apart from the Windows OCR engine, Power Automate supports the Tesseract engine. This e...
- Wait for text on screen (OCR): Wait until a specific text appears/disappears on the screen, on the foreground window, ...
- Extract text with OCR: Extract text from a given source using the given OCR engine.

## Office 365 Outlook → actions/office365outlook.md (2)
Robin: KB未収録（Designerコピーで確認）
- Prerequisites and limitations: - You need an Attended RPA license.
- Send an email with attachments: This section presents an example of how to send an email with attachments in your deskt...

## Outlook actions reference → actions/outlook.md (7)
Robin: robin/outlook.md
- Launch Outlook: Launch Outlook and create a new Outlook instance.
- Retrieve email messages from Outlook: Retrieve email messages from an Outlook account.
- Send email through Outlook: Create and send a new email message through Outlook.
- Process email messages in Outlook: Move or deletes an email (or a list of email messages) retrieved by a 'Retrieve emails ...
- Save Outlook email messages: Save Outlook email messages given an account.
- Respond to Outlook mail message: Respond to an Outlook message, by replying, replying to all or forwarding it.
- Close Outlook: Close a previously launched Outlook instance.

## PDF actions reference → actions/pdf.md (5)
Robin: robin/pdf.md
- Extract text from PDF: You can extract text from a PDF file by using the "Extract text from PDF" action. In th...
- Extract tables from PDF: You can extract tables that are contained in a PDF file by using the Extract tables fro...
- Extract images from PDF: To extract images from a PDF file you can use the Extract images from PDF action. In th...
- Extract PDF file pages to new PDF file: You can create a new PDF file by extracting pages from an existing PDF file by using th...
- Merge PDF files: Merges multiple PDF files into a new one.

## Power Automate environment actions reference → actions/powerautomateenvironment.md (1)
Robin: robin/powerautomateenvironment.md
- Retrieve environment variable: Retrieves a Power Automate environment variable.

## Run desktop flow actions reference → actions/runflow.md (1)
Robin: KB未収録（Designerコピーで確認）
- Run desktop flow: Runs a desktop flow that can receive input variables and might produce output variables...

## Scripting actions reference → actions/scripting.md (6)
Robin: system（Scripting.* はここ）
- Run DOS command: Executes a DOS command or console application in invisible mode and retrieves its outpu...
- Run VBScript: Executes some custom VBScript code and retrieves its output into a variable.
- Run JavaScript: Executes some custom JavaScript code and retrieves its output into a variable.
- Run PowerShell script: Executes some custom PowerShell script and retrieves its output into a variable.
- Run Python script: Executes Python script code and retrieves its output.
- Run .NET script: Executes .NET (C#/VB.NET) script code and retrieves its output.

## Windows services actions reference → actions/services.md (6)
Robin: robin/services.md
- If service: Marks the beginning of a conditional block of actions depending on whether a service is...
- Wait for service: Suspend the execution of the automation until a service is running, paused or stopped o...
- Start service: Start a stopped Windows service.
- Stop service: Stop a running Windows service.
- Pause service: Pause a running Windows service.
- Resume service: Resume a paused Windows service.

## System actions reference → actions/system.md (8)
Robin: robin/system.md
- If process: Marks the beginning of a conditional block of actions depending on whether a process is...
- Wait for process: Suspends the execution until a process starts or stops.
- Run application: Executes an application or opens a document by executing the associated application.
- Terminate process: Immediately stops a running process.
- Ping: Sends a message to determine whether a remote computer is accessible over the network.
- Set Windows environment variable: Sets an environment variable to a given value.
- Get Windows environment variable: Retrieves the value of an environment variable.
- Delete Windows environment variable: Deletes an environment variable from a given scope.

## Testing actions → actions/testing.md (2)
Robin: robin/testing.md
- Test a desktop flow: Test a desktop flow that receives input variables and might produce output variables. T...
- Assert: Validates output against expected results using operators like equals, contains, or gre...

## Text actions reference → actions/text.md (19)
Robin: robin/text.md
- Append line to text: Appends a new line of text to a text value.
- Get subtext: Retrieve a subtext from a text value.
- Crop text: Retrieves a text value that occurs before, after or between the specified text flag(s) ...
- Pad text: Creates a fixed length text by adding characters to the left or to the right of an exis...
- Trim text: Removes all occurrences of white space characters (such as space, tab, or new line) fro...
- Reverse text: Reverses the order of letters in a text string.
- Change text case: Changes the casing of a text to uppercase, lowercase, title case or sentence case.
- Convert text to number: Converts a text representation of a number to a variable that contains a numeric value.
- Convert number to text: Converts a number to text using a specified format.
- Convert text to datetime: Converts a text representation of a date and/or time value to a datetime value.
- Convert datetime to text: Converts a datetime value to text using a specified custom format.
- Create random text: Generates a text of specified length consisting of random characters. This action can b...
- Join text: Converts a list into a text value by separating its items with a specified delimiter.
- Split text: Creates a list containing the substrings of a text that are separated by a specified de...
- Parse text: Parses a text to find the first or all occurrences of a specified subtext or a regular ...
- Replace text: Replaces all occurrences of a specified subtext with another text. It can also be used ...
- Escape text for regular expression: Escapes a minimal set of characters (\, *, +, ?, |, {, [, (,), ^, $,., #, and white spa...
- Recognize entities in text: Recognizes entities in text, such as numbers, units, data/time and others expressed in ...
- Create HTML content: Generates rich HTML content and stores it in a variable.

## UI automation actions reference → actions/uiautomation.md (33)
Robin: robin/uiautomation.md
- Get details of window: Gets a property of a window such as its title or its source text.
- Get details of a UI element in window: Gets the value of a UI element's attribute in a window.
- Get selected checkboxes in window: Retrieves the names of the selected checkboxes in a checkbox group or the state of a sp...
- Get selected radio button in window: Retrieves the names of the selected radio button in a radio button group or the state o...
- Extract data from window: Extracts data from specific parts of a window in the form of single values, lists, or t...
- Extract data from table: Extracts data from a table in the form of a datatable.
- Take screenshot of UI element: Takes a screenshot of a UI element in window.
- Focus text field in window: Sets the focus on a text box of a window and scrolls it into view.
- Populate text field in window: Fills a text box in a window with the specified text.
- Press button in window: Presses a window button.
- Select radio button in window: Selects a radio button on a window.
- Set checkbox state in window: Checks or unchecks a checkbox in a window form.
- Set drop-down list value in window: Sets or clears the selected options for a drop-down list in a window form.
- Get window: Gets a running window, for automating desktop applications.
- Focus window: Activates and brings to the foreground a specific window.
- Set window state: Restores, maximizes or minimizes a specific window.
- Set window visibility: Shows a hidden window or hides a visible window.
- Move window: Sets the position of a specific window.
- Resize window: Sets the size of a specific window.
- Close window: Closes a specific window.
- If window contains: Marks the beginning of a conditional block of actions depending on whether a specific p...
- Wait for window content: Suspends the execution of the automation until a specific piece of text or UI element a...
- If image: This action marks the beginning of a conditional block of actions depending on whether ...
- Use desktop: Performs desktop and taskbar related operations.
- Select tab in window: Selects a tab from a group of tabs.
- Wait for image: This action waits until a specific image appears on the screen or on the foreground win...
- Hover mouse over UI element in window: Hover the mouse over any UI element on window.
- Click UI element in window: Clicks on any UI element of a window.
- Select menu option in window: Selects an option in a menu of a window.
- Drag and drop UI element in window: Drags and drops a UI element of a window.
- Expand/collapse tree node in window: Expands or collapses a node of a tree view residing in a window.
- If window: This action marks the beginning of a conditional block of actions depending on whether ...
- Wait for window: Suspends the execution or the process until a specific window opens, closes, get or los...

## Variables actions reference → actions/variables.md (36)
Robin: robin/variables.md
- Create new data table: Creates a new data table variable.
- Insert row into data table: Inserts a row at the end or before a specific index value.
- Delete row from data table: Delete a data table row at the corresponding row index.
- Update data table item: Update a data table row item on a defined column.
- Find or replace in data table: Finds and/or replaces data table values.
- Insert column into data table: Inserts a column at the end or before a specific index value.
- Delete column from data table: Delete a data table column at the specified column index or column name.
- Delete empty rows from data table: Deletes the rows of the data table that have all of their cells empty.
- Delete duplicate rows from data table: Deletes all the rows that are duplicate from the data table, if the values have the sam...
- Clear data table: Deletes all the rows of the data table, keeping table headers unaffected.
- Sort data table: Sorts the data table rows in ascending or descending order by the specified column, if ...
- Filter data table: Filters the data table rows based on the applied rules.
- Merge data tables: Merges two data tables together, specifying the merging behavior in case their number o...
- Join data tables: Joins two data tables based on the specified join rule.
- Read from CSV text variable: Generates a data table from a CSV text.
- Convert data table to text: Converts a data table to a CSV text.
- Truncate number: Get the integral or fractional digits of a numeric value, or round up the value to a sp...
- Generate random number: Generate a random number or a list of random numbers that fall between a minimum and ma...
- Clear list: Remove all items from a list.
- Remove item from list: Remove one or multiple items from a list.
- Sort list: Sort the items of a list. Use items of the same type.
- Shuffle list: Create a random permutation of a list.
- Merge lists: Merge two lists into one.
- Reverse list: Reverse the order of the items of a list.
- Remove duplicate items from list: Remove the multiple occurrences of items in a list, so that in the resulting list each ...
- Find common list items: Compare two lists and create a new list with the items that are common to both.
- Subtract lists: Compare two lists and create a new list with the items that are in the first list but n...
- Retrieve data table column into list: Convert the contents of a data table column into a list.
- Convert JSON to custom object: Convert a JSON string to a custom object.
- Convert custom object to JSON: Convert a custom object to a JSON string.
- Add item to list: Append a new item to a list.
- Create new list: Create a new empty list.
- Increase variable: Increase the value of a variable by a specific amount.
- Decrease variable: Decrease the value of a variable by a specific amount.
- Run Power Fx expression: Runs the provided Power Fx expression.
- Set variable: Set the value of a new or existing variable, create a new variable or overwrite a previ...

## HTTP actions reference → actions/web.md (3)
Robin: robin/web.md
- Download from web: Downloads text or a file from the web and stores it.
- Invoke SOAP web service: Invokes a method from a SOAP web service.
- Invoke web service: Invokes a web service by sending data and stores the response text.

## Browser automation actions reference → actions/webautomation.md (23)
Robin: robin/webautomation.md
- Extract data from web page: Extract data from specific parts of a web page as single values, lists, rows, or tables.
- Get details of web page: Get a property of a web page, such as its title or its source text.
- Get details of element on web page: Get the value of an element's attribute on a web page.
- Take screenshot of web page: Takes a screenshot of the web page (or an element of the web page) currently displayed ...
- Focus text field on web page: Set the focus on an input element of a web page and scroll it into view.
- Populate text field on web page: Fill a text field in a web page with the specified text.
- Set check box state on web page: Check or uncheck a check box in a web form.
- Select radio button on web page: Select a radio button on the web page.
- Set drop-down list value on web page: Set or clear the selected options for a drop-down list in a web form.
- Press button on web page: Press a web page button.
- If web page contains: Mark the beginning of a conditional block of actions, depending on whether a specific p...
- Wait for web page content: Suspend the flow until a specific piece of text or web page element appears or disappea...
- Launch new Internet Explorer: Launch a new instance or attach to a running instance of Internet Explorer for automati...
- Launch new Firefox: Launch a new instance or attach to a running instance of Firefox for automating website...
- Launch new Chrome: Launch a new instance or attach to a running instance of Chrome for automating websites...
- Launch new Microsoft Edge: Launch a new instance or attach to a running instance of Microsoft Edge for automating ...
- Create new tab: Create a new tab and go to the given URL (supported in Microsoft Edge, Chrome, and Fire...
- Go to web page: Navigate the web browser to a new page.
- Click link on web page: Click on a link or any other element of a web page.
- Click download link on web page: Select a link in a web page that results in downloading a file.
- Run JavaScript function on web page: Run a JavaScript function on the web page and get the returned result.
- Hover mouse over element on web page: Hover the mouse over an element of a web page.
- Close web browser: Closes a web browser window.

## Word actions reference → actions/word.md (8)
Robin: robin/word.md
- Launch Word: Opens a new Word instance or opens a Word document.
- Attach to running Word: Attaches to a Word document that's already open.
- Save Word: Saves a previously launched Word instance.
- Close Word: Closes a Word instance.
- Read from Word document: Reads the text content from a document of a Word instance.
- Write to Word document: Write or append text to a Word file.
- Insert image in Word document: Insert an image to a Word file.
- Find and replace words in Word document: Finds text and replaces it with another in the active worksheet of an Excel instance.

## Work queues actions → actions/workqueues.md (8)
Robin: robin/workqueues.md
- Process work queue items: The Process work queue items action indicates to the queue orchestrator that the machin...
- Update work queue item: The Update work queue item action allows users to change the status and processing resu...
- Add work queue item: The Add work queue item action allows users to populate work queue items into a work qu...
- Add multiple work queue items: The Add multiple work queue items action allows users to add one or more work queue ite...
- Requeue item with delay: The Requeue item with delay action allows users to readd a queue item being processed i...
- Update work queue item processing notes: The Update work queue item processing notes action allows users to update or clear proc...
- Get work queue items by filter: The Get work queue items by filter action allows users to retrieve one or more work que...
- Related information: - Work queue overview

## Workstation actions reference → actions/workstation.md (13)
Robin: system（Workstation.* はここ）
- Print document: Prints a document on the default printer.
- Get default printer: Gets the name of the default printer.
- Set default printer: Sets a printer as the default printer.
- Show desktop: Shows the desktop.
- Lock workstation: Locks the workstation's display to protect it from unauthorized use.
- Play sound: Plays a system sound or a wav file.
- Empty recycle bin: Deletes all files from the windows recycle bin.
- Take screenshot: Takes a screenshot of the foreground window or the specified screen and saves the image...
- Control screen saver: Enables, disables, starts or stops the screensaver.
- Get screen resolution: Gets the width, height, bit count and frequency of a selected monitor.
- Set screen resolution: Sets the width, height, bit count and frequency of a selected monitor during an attende...
- Log off user: Logs off the current user.
- Shutdown computer: Instructs the computer to shut down.

## XML actions reference → actions/xml.md (10)
Robin: robin/xml.md
- Read XML from file: Read the contents of an XML file into a variable.
- Write XML to file: Write the contents of an XML node variable into a file.
- Execute XPath expression: Extract values from an XML document based on the provided XPath query.
- Get XML element attribute: Get the value of an attribute of an XML element.
- Set XML element attribute: Set the value of an attribute of an XML element.
- Remove XML element attribute: Remove an attribute from an XML element.
- Get XML element value: Get the value of an XML element.
- Set XML element value: Set the value of an XML element.
- Insert XML element: Insert a new XML element into an XML document.
- Remove XML element: Remove one or more XML elements from an XML document.
