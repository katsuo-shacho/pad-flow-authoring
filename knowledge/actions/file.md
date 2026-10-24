# File actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/file （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Handling files and their content is essential for most automation scenarios. You can use the file actions to manage files, retrieve their properties, read and write data, and convert them to other types. Most file actions require paths that specify the files you want to manipulate. These paths can be hard-coded values or file datatype variables. Similarly, you can populate a hard-coded value or a folder datatype variable to specify a destination folder in the actions that need one. Some file actions provide an extensive configuration, allowing you to automate virtually any scenario. For exampl

## If file exists  `#iffileaction`
Marks the beginning of a conditional block of actions depending on whether a file exists or not.
入力:
- If file: Exists, Doesn't exist = Exists — The state of the file to check
- File path: File — The full path to look for the file

## Wait for file  `#waitforfileaction`
Suspend the execution of the automation until a file is created or deleted.
入力:
- Wait for file to be: Created, Deleted = Created — Specifies whether to pause the flow on the creation or deletion of a certain file
- File path: File — The full path to look for the file

## Copy file(s)  `#copy`
Copy one or more files into a destination folder.
入力:
- File(s) to copy: List of Files — The file(s) to copy. This value can be a file path, or a variable containing a file, a list of files, a text path, or a list of text paths. Use the 'Get files in folder' action to populate a variable with a list of files.
- Destination folder: Folder — The destination folder for the copied files
- If file exists: Do nothing, Overwrite = Do nothing — Specifies what to do if a file with the same name already exists in the destination folder
出力:
- CopiedFiles: List of Files — The copied file(s) as a list of files
例外: Source folder doesn't exist; Destination folder doesn't exist; File not found; Can't copy file

## Move file(s)  `#move`
Move one or more files into a destination folder.
入力:
- File(s) to move: List of Files — The file(s) to move. This value can be a file path, or a variable containing a file, a list of files, a textual path, or a list of text paths. Use the 'Get files in folder' action to populate a variable with a list of files.
- Destination folder: Folder — The destination folder for the moved files
- If file exists: Do nothing, Overwrite = Do nothing — Specifies what to do if a file with the same name already exists in the destination folder
出力:
- MovedFiles: List of Files — The moved file(s) as a list of files
例外: Source folder doesn't exist; Destination folder doesn't exist; File not found; Can't move file

## Delete file(s)  `#delete`
Delete one or more files.
入力:
- File(s) to delete: List of Files — The file(s) to delete. This value can be a file path, or a variable containing a file, a list of files, a text path, or a list of text paths. Use the 'Get files in folder' to populate a variable with a list of files
例外: File path doesn't exist; File not found; Can't delete file

## Rename file(s)  `#renamefiles`
Change the name of one or more files.
入力:
- File to rename: List of Files — The file(s) to rename. This value can be a file path, or a variable containing a file, a list of files, a text path, or a list of text paths. Use the 'Get files in folder' action to populate a variable with a list of files.
- Add number to: Boolean value = True — Specifies whether to add the number to the existing file name(s) or a new name
- Rename scheme: Set new name, Add text, Remove text, Replace text, Change extension, Add datetime, Make sequential = Set new name — Specifies how to rename the file(s)
- New file name: Text value — The new name of the file(s)
- New extension(任意): Text value — The text to add as the new extension for the file(s)
- New file name: Text value — The new name of the file(s)
- Add number to: After name, Before name = After name — Specifies whether to add the number before or after the original name(s) or a new base name
- Text to add(任意): Text value — The text to add to the original file name(s)
- Text to remove(任意): Text value — The text to remove from the original file name(s). This rename scheme searches each file name, and removes the entered text anywhere in the name, each time it occurs.
- Text to replace: Text value — The text to replace in the original file name(s). This rename scheme searches each file name, and replaces the entered text anywhere in the name, each time it occurs
- Use custom datetime: Boolean value = False — Specifies whether to use a custom datetime
- Datetime to add: Current datetime, Creation time, Last accessed, Last modified = Current datetime — Specifies what datetime value to add to the file name(s)
- Keep extension: Boolean value = True — Specifies whether to include the previous extension with the file name(s). Disable this option to add the extension to the file(s) manually.
- Replace with(任意): Text value — The text to replace the original text with
- Start numbering at: Numeric value — The starting number value
- Add text: After name, Before name = After name — Specifies whether to add the text before or after the original name(s)
- Custom datetime: Datetime — The datetime to add to the file name(s)
- Increment by: Numeric value — The number to increment the starting value by
- Add datetime: After name, Before name = After name — Specifies whether to add the datetime before or after the original name(s)
- Separator: Nothing, Space, Dash, Period, Underscore = Space — Specifies what to use to separate the original file name and the number added, including the option to not use a separator
- Separator: Nothing, Space, Dash, Period, Underscore = Space — Specifies what to use to separate the original file name and the datetime value added, including the option to not use a separator
- Use padding: Boolean value = False — Specifies whether to use padding
- Datetime format: Text value = yyyyMMdd — The format of the datetime value to add to the file name, such as MM/dd/yyyy for date, and hh:mm:sstt for time
- Make each number at least(任意): Numeric value = 3 — The minimum length for each number added
- If file exists: Do nothing, Overwrite = Do nothing — Specifies what to do if a file with the same name already exists in the folder
出力:
- RenamedFiles: List of Files — The renamed file(s) as a list of files
例外: Directory not found; File not found; Can't rename file

## Read text from file  `#readtextfromfile`
Read the contents of a text file.
入力:
- File path: File — The file to read
- Store content as: Single text value, List (each is a list item) = Single text value — Specifies how to store the text. Choose 'Single text value' to store the entire text as a single text value. Choose 'List' to store each line of the original text as a text item in a list.
- Encoding: System default, ASCII, Unicode, Unicode (big-endian), UTF-8 = UTF-8 — The encoding to read the specified text from the text file with.
出力:
- FileContents: Text value — The contents as a text
- FileContents: List of Text values — The contents as a list of texts
例外: Directory not found; File not found; Failed to read from file

## Write text to file  `#writetext`
Write or appends text to a file.
入力:
- File path: File — The file to write the text. This value can be a file path, or a variable containing a file or a textual path.
- Text to write(任意): General value — The text to write in the specified file
- Append new line: Boolean value = True — Specifies whether to append a new line at the end of the overall text to write to the file
- If file exists: Overwrite existing content, Append content = Overwrite existing content — Specifies whether to overwrite the existing content, or to append to the end of the existing content. If the file doesn't exist, this action automatically creates it.
- Encoding: System default, ASCII, Unicode, Unicode (big-endian), UTF-8, Unicode (without byte order mask), UTF-8 (without byte order mask) = Unicode — The encoding to use for the specified text to write into the text file
例外: Failed to write text to file; Invalid directory for file

## Read from CSV file  `#readfromcsvfile`
Read a CSV file into a data table.
入力:
- File path: File — The CSV file to read. This value can be a file path, or a variable containing a file or a textual path
- Encoding: UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII = UTF-8 — The encoding to be used for reading the specified CSV file
- Trim fields: Boolean value = True — Specifies whether to automatically trim off the leading and trailing whitespaces of the extracted cells
- First line contains column names: Boolean value = False — Specifies whether to use the first row of the CSV resource to set the column names of the resulting data table variant. Enable this option to avoid reading the names as data into the table. Subsequent actions may access the data held by the data table using column names (instead of column numbers).
- Columns separator: Predefined, Custom, Fixed column widths = Predefined — Specifies whether to use a predefined columns separator, a custom one or fixed column widths
- Separator: System default, Comma, Semicolon, Tab = System default — The column-separator to parse the CSV file
- Custom separator: Text value — The custom column-separator to use for parsing the CSV resource specified
- Fixed column widths: Text value — The fixed column-widths to use for parsing the CSV resource specified. Separate the widths using commas, spaces, tabs or newlines.
出力:
- CSVTable: Datatable — The contents of the CSV file as a data table
例外: Read from CSV failed

## Write to CSV file  `#writetocsvfile`
Write a data table, data row or list to a CSV file.
入力:
- Variable to write: General value — The data table, data row variable or list variable to write into the target CSV file
- File path: File — The CSV file to export the variable to. This value can be a file path, or a variable containing a file or a textual path.
- Encoding: UTF-8, Unicode, Unicode (big-endian), UTF-8 (No byte order mark), Unicode (no byte order mark), System default, ASCII = UTF-8 — The encoding to use for writing to the specified CSV file
- Include column names: Boolean value = False — Specifies whether the column names of the variant specified should become the first row of the CSV file. This option takes effect if and only if the target CSV file either doesn't initially exist or exists but is otherwise empty of text.
- If file exists: Overwrite existing content, Append content = Overwrite existing content — Specifies the desired behavior when the targeted CSV file already exists in the filesystem
- Separator: System default, Comma, Semicolon, Tab = System default — The column separator to use in the specified CSV file
- Custom columns separator: Text value — The custom column separator to use in the CSV file
- Use custom columns separator: Boolean value = False — Specifies whether to use a custom columns separator or a predefined one
例外: Write failed

## Get file path part  `#getpathpart`
Retrieve one or more parts (directory, filename, extension, etc.) from a text that represents a file path.
入力:
- File path: File — The file path to use as the source
出力:
- RootPath: File — The root path of the source file
- Directory: Folder — The directory of the source file
- FileName: Text value — The name of the source file
- FileNameNoExtension: Text value — The file name (without the extension) of the source file
- FileExtension: Text value — The extension (for example, .doc) of the source file
例外: File path contains invalid characters

## Get temporary file  `#gettemppath`
Create a uniquely named, empty temporary file on disk, and get the file object (which is a representation, and can access the file and all its information).
出力:
- TempFile: File — The temporary file object
例外: Failed to create temporary file

## Convert file to Base64  `#convertfiletobase64action`
Convert a file to Base64 encoded text.
入力:
- File path: File — The file path to read from
出力:
- Base64Text: Text value — The Base64 encoded text
例外: File not found; Can't convert file to Base64

## Convert Base64 to file  `#convertbase64tofileaction`
Convert a Base64 encoded text to file.
入力:
- Base64 encoded text: Text value — The Base64 encoded text
- File path: File — The file to write to
- If file exists: Do nothing, Overwrite = Do nothing — Specifies what to do if a file with the same name already exists in the destination folder
例外: Invalid directory for file; Can't convert Base64 to file

## Convert file to binary data  `#convertfiletobinaryaction`
Convert a file to binary data.
入力:
- File path: File — The file to read from
出力:
- BinaryData: Text value — The binary data to write
例外: File not found; Can't convert file to binary data

## Convert binary data to file  `#convertbinarytofileaction`
Convert binary data to file.
入力:
- Binary data: Text value — The binary data
- File path: File — The file to write to
- If file exists: Do nothing, Overwrite = Do nothing — Specifies what to do if a file with the same name already exists in the destination folder
例外: Invalid directory for file; Can't convert binary file to file
