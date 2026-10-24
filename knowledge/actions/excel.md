# Excel actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/excel （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: After setting an Excel instance, either with the Launch Excel or the Attach to running Excel action, you can further handle your Excel worksheets. To read and extract data from an Excel document, use the Read from Excel worksheet action. You can retrieve the value of a single cell or a data table. The following example reads the cells A1 through E5: When the flow runs, the action stores the data in a data table variable: To write data to an Excel spreadsheet, use the Write to Excel worksheet action. This action can write any static data or variable to a specified cell or multiple cells in an E

## Resize columns/rows in Excel worksheet  `#resizecolumnsorrowsaction`
Resizes a selection of columns or rows in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- Resize target: Column, Row = Column — Specify whether to resize columns or rows
- Selection range: Single, Range, All available = Single — Specify whether to select a single column/row, a range of columns/rows or all the available columns/rows in the active worksheet
- Column: Text value — The column's index number or letter. Column numbering starts from index 1.
- Start column: Text value — The index or letter of the first column. Column numbering starts from index 1.
- End column: Text value — The index or letter of the last column. Column numbering starts from index 1.
- Row: Numeric value — The row's index number. The numbering starts from 1.
- Start row: Numeric value — The index or the first row. The numbering starts from 1.
- End row: Numeric value — The index or the last row. The numbering starts from 1.
- Resize type: Autofit, Custom size = Autofit — Specify whether to autofit selected columns/rows or set a custom size
- Width: Numeric value — The width of the selected columns
- Height: Numeric value — The height of the selected rows
例外: Failed to resize columns/rows

## Run Excel macro  `#runmacro`
Runs a specified macro on the document of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Macro: Text value — The macro to run. The text should consist of the name of the macro, followed by any arguments (optional), all separated by semicolons.
例外: Failed to run macro

## Get active Excel worksheet  `#getactiveworksheet`
Retrieves an Excel document's active worksheet.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
出力:
- SheetName: Text value — The name of the active worksheet
- SheetIndex: Numeric value — The index of the active worksheet
例外: Failed to retrieve active worksheet

## Get all Excel worksheets  `#getallworksheets`
Retrieves all worksheet names of an Excel document.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
出力:
- SheetNames: List of Text values — The names of all worksheets
例外: Failed to retrieve all worksheet names

## Delete Excel worksheet  `#deleteworksheet`
Deletes a specific worksheet from an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Delete worksheet with: Index, Name = Name — Whether to find the worksheet by name or index
- Worksheet index: Numeric value — The Index number of the worksheet to delete. The numbering starts from 1, meaning that the index of the first worksheet is 1, the second is 2, and so on.
- Worksheet name: Text value — The name of the worksheet to delete
例外: Can't find worksheet; Failed to delete worksheet

## Rename Excel worksheet  `#renameworksheet`
Renames a specific worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- Rename worksheet with: Index, Name = Name — Specify whether to find the worksheet by name or index
- Worksheet index: Numeric value — The index of the worksheet to rename. The numbering starts from 1, meaning that the index of the first worksheet is 1, the second is 2, and so on.
- Worksheet name: Text value — The name of the worksheet to rename
- Worksheet new name: Text value — The new name of the worksheet
例外: Can't find worksheet; Failed to rename worksheet

## Copy Excel worksheet  `#copyexcelworksheet`
Copies a worksheet from an Excel document and paste it to the Excel document of the same or different Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Copy worksheet with: Index, Name = Name — Specify whether to find the worksheet by name or index
- Worksheet index: Numeric value — The index of the worksheet to copy. The numbering starts from 1, meaning that the index of the first worksheet is 1, the second is 2, and so on.
- Worksheet name: Text value — The name of the worksheet to copy.
- Target Excel instance: Excel instance — The Excel instance of the target file. This variable must be specified in a Launch Excel action.
- Worksheet new name: Text value — The new name of the worksheet
- Paste worksheet as: First worksheet, Last worksheet = First worksheet — Specify whether the copied Excel worksheet will be added before or after the existing worksheets
例外: Failed to copy worksheet; Can't copy worksheet with this name

## Activate cell in Excel worksheet  `#activatecellinexcel`
Activate a cell in the active worksheet of an Excel instance, by providing column, row, and offset.
入力:
- Excel instance: Excel instance — Specify the Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Activate: Absolutely specified cell, Relatively specified cell = Absolutely specified cell — Select whether to specify the cell to activate absolutely, or relatively, by using an offset distance being the number of cells between the currently activated reference cell and the actual cell activate.
- Column: Text value — The numeric value or letter of the cell column.
- Direction: Left, Right, Above, Below = Left — Select offset direction. Select where to look for the cell to activate based on the position of the currently active cell.
- Offset from active cell: Numeric value — The distance in cells between the currently active cell and the desired cell. The numbering starts from 0.
- Row: Numeric value — The numeric value of the cell row. The numbering starts from 1.
例外: Failed to activate cell

## Select cells in Excel worksheet  `#selectcellsfromexcel`
Selects a range of cells in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Select: Absolutely specified cell, Relatively specified cell = Absolutely specified cell — Specify whether to select an explicitly specified range of cells or a range of cells relative to the currently active cell.
- X Axis Direction: Left, Right = Left — The X-axis offset direction. Where to look along the horizontal axis, based on currently activated cell's position.
- Start column: Text value — The index or letter of the first column.
- X Offset: Numeric value — The X-axis offset.
- Start row: Numeric value — The first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the last column.
- Y Axis Direction: Above, Below = Above — The Y-axis offset direction. Where to look along the vertical axis, based on the position of the currently active cell.
- End row: Numeric value — The last row number. The numbering starts from 1.
- Y Offset: Numeric value — The Y-axis offset.
例外: Failed to select cells

## Get selected cell range from Excel worksheet  `#getselectedcellrange`
Retrieve the selected range of cells in a structure consisting of first column, first row, last column, and last row.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
出力:
- FirstColumnIndex: Numeric value — The numeric value of the range's first column
- FirstRowIndex: Numeric value — The numeric value of the range's first row
- LastColumnIndex: Numeric value — The numeric value of the range's last column
- LastRowIndex: Numeric value — The numeric value of the range's last row
例外: Failed to retrieve the selected range of cells

## Copy cells from Excel worksheet  `#copycellsfromexcel`
Copies a range of cells from the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Copy mode: Single Cell's Values, Values from a Range of Cells, Values from Selection = Single Cell's Values — Specify whether to copy a single cell, a range of cells or the current selection of cells
- Start column: Text value — The index or letter of the first column
- Start row: Numeric value — The index of the first row
- End column: Text value — The index or letter of the last column
- End row: Numeric value — The index of the last row
例外: Failed to copy cells

## Paste cells to Excel worksheet  `#pastecellstoexcel`
Pastes a range of cells to the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- Paste mode: On specified cell, On currently active cell = On specified cell — Specify whether to paste on a specified cell or the currently active cell
- Column: Text value — The index or letter of the cell column
- Row: Numeric value — The row number
例外: Failed to paste cells

## Delete from Excel worksheet  `#deletecellsaction`
Deletes a cell or a range of cells from the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Retrieve: The value of a single cell, Values from a range of cells = The value of a single cell — Whether to delete a single cell or a table from a range of cells
- Start column: Text value — The cell column (single cell's value) or first column as a numeric value or a letter
- Start row: Numeric value — The cell row (single cell's value) or first row number
- End column: Text value — The last column as a numeric value or a letter
- End row: Numeric value — The last row number
- Shift direction: Left, Up = Left — The shift direction
例外: Failed to delete cells

## Insert row to Excel worksheet  `#insertrow`
Inserts a row above a selected row of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Row index: Numeric value — The index of the row to add a new row above. The numbering starts from 1.
例外: Can't find row; Failed to insert row

## Delete row from Excel worksheet  `#deleterow`
Deletes a selected row from an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance. This variable must have been previously specified in a Launch Excel action.
- Delete row: Numeric value — The Index number of the row to delete. The numbering starts from 1.
例外: Can't find row; Failed to delete row

## Insert column to Excel worksheet  `#insertcolumn`
Inserts a column to the left of a selected column of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Column: Text value — The column's index number or letter. A new column will appear on the left side of the column indicated.
例外: Can't find column; Failed to insert column

## Delete column from Excel worksheet  `#deletecolumn`
Deletes a selected column from an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Delete column: Text value — The index number or letter of the column to delete.
例外: Can't find column; Failed to delete column

## Find and replace cells in Excel worksheet  `#findandreplaceaction`
Finds text and replaces it with another in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Search mode: Find, Find and replace = Find — The mode to search with
- All matches: Boolean value = False — Whether to find/replace text in all the matching cells found or in the first matching cell only
- Text to find: Text value — The text to find in the worksheet
- Text to replace with: Text value — The text used to replace the matching cells
- Match case: Boolean value = False — Whether to search for case-sensitive data
- Match entire cell contents: Boolean value = False — Whether to search for cells that contain just the specified text
- Search by: Rows, Columns = Rows — The order in which to search for the text
出力:
- FoundColumnIndex: Numeric value — The index of the column found
- FoundRowIndex: Numeric value — The index of the row found
- Cells: Datatable — The list of cells matching the criteria
例外: Failed to find and/or replace text

## Get first free row on column from Excel worksheet  `#getfirstfreerowoncolumn`
Retrieve the first free row, given the column of the active worksheet.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- Column: Text value — The index or letter that identifies the column. Column numbering starts from index 1.
出力:
- FirstFreeRowOnColumn: Numeric value — The numeric value of the given column's first fully empty row
例外: Failed to retrieve first free row

## Read formula from Excel  `#readcellformula`
Reads the formula inside a cell in Excel.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Retrieve: The formula of a single cell, The formula of a named cell = The formula of a single cell — Specify whether to retrieve the formula from a specified cell or a named cell
- Start column: Text value — The cell column (single cell's value) or first column as a numeric value or a letter
- Start row: Numeric value — The cell row (single cell's value) or first row number
- Name: Text value — The name of cells
出力:
- CellFormula: Text value — The formula of a single cell
例外: Failed to read the formula from cell

## Get table range from Excel worksheet  `#gettablerange`
Retrieves the range of a table in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Table name: Text value — Specify the name of the table in Excel.
- Is pivot: Boolean value = False — Determine whether the specified table is a pivot table.
出力:
- FirstColumnIndex: Numeric value — The numeric value of the table's first column
- FirstRowIndex: Numeric value — The numeric value of the table's first row
- LastColumnIndex: Numeric value — The numeric value of the table's last column
- LastRowIndex: Numeric value — The numeric value of the table's last row
例外: Failed to get the range from table

## Auto fill cells in Excel worksheet  `#autofillcells`
Auto fills a range with data, based on the data of another range, in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Ranges format: Named cells, Specific ranges = Named cells — Specify how the ranges are referenced, either using named cells or absolute column/row indexes
- Source cells name: Text value — Name representing the source range for auto filling
- Destination cells name: Text value — Name representing the destination range to auto fill. The source range should begin from the same cell and should be included in the destination range
- Start column: Text value — The index or letter of the first column of both ranges
- Start row: Numeric value — The first row number of both ranges. The numbering starts from 1
- Source end column: Text value — The index or letter of the last column of the source range
- Source end row: Numeric value — The last row number of the source range. The numbering starts from 1
- Destination end column: Text value — The index or letter of the last column of the destination range
- Destination end row: Numeric value — The last row number of the destination range. The numbering starts from 1
例外: Failed to auto fill cells

## Append cells in Excel worksheet  `#appendcells`
Appends a range of cells to the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Append mode: To active sheet, To named cells = To active sheet — Specify whether to append to a sheet or range of named cells
- Name: Text value — The name of the range of cells
- First row has headers: Boolean value = False — Indicates that the first row of the destination contains column headers
- Starting column(任意): Text value — The starting column number or letter, where the data is appended beginning from the destination's first empty row. If the field is left empty, the first column of the specified destination is used instead.
- Starting column header(任意): Text value — The header of the starting column, where the data is appended beginning from the destination's first empty row. If the field is left empty, the first column of the specified destination is used instead.
例外: Failed to append cells

## Lookup range in Excel worksheet  `#lookuprange`
Finds and returns the result of Excel's LOOKUP function.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Lookup value: Text value — The value to lookup in the specified range of cells.
- Ranges format: Named cells, Specific ranges = Named cells — Specify how the ranges are referenced, either using named cells or absolute column/row indexes.
- Cells name: Text value — The name of the cells range to search for the lookup value.
- Start column: Text value — The index or letter of the first column of the range to search for the lookup value.
- Start row: Numeric value — The first row number of the range to search for the lookup value. The numbering starts from 1.
- End column: Text value — The index or letter of the last column of the range to search for the lookup value.
- End row: Numeric value — The last row number of the range to search for the lookup value. The numbering starts from 1.
- Array form: Boolean value = False — The array form of LOOKUP looks in the first row or column of an array for the specified value and returns a value from the same position in the last row or column of the array. Use this form of LOOKUP when the values that you want to match are in the first row or column of the array. If this option remains disabled, the vector form of LOOKUP is used instead, which looks in a one-row or one-column range (known as a vector) for a value and returns a value from the same position in a second one-row or one-column range.
- Cells name of results source(任意): Text value — The name of the cells range from which the matching value is returned.
- Start column of results source: Text value — The index or letter of the first column of the range from which the matching value is returned.
- Start row of results source: Numeric value — The first row number of the range from which the matching value is returned. The numbering starts from 1.
- End column of results source: Text value — The index or letter of the last column of the range from which the matching value is returned.
- End row of results source: Numeric value — The last row number of the range from which the matching value is returned. The numbering starts from 1.
出力:
- LookupResult: Text value — The value returned by the LOOKUP function
例外: Failed to lookup

## Set color of cells in Excel worksheet  `#setcolor`
Fills the background of the selected cells with the specified color, in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must be specified in a Launch Excel action.
- Set color of: Single cell, Range of cells, Named cells = Single cell — Specify whether to set the background color of a single cell, a range of cells, or named cells.
- Start column: Text value — The index or letter of the cell column or range's first column.
- Start row: Numeric value — The cell row or the range's first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the range's last column.
- End row: Numeric value — The range's last row number. The numbering starts from 1.
- Cells name: Text value — Name representing the range that is filled with the specified color.
- Color format: Name, Hexadecimal value = Name — Select whether to specify a color by its name or its hexadecimal value.
- Color name: Text value — Select one of the system defined colors.
- Color hexadecimal value: Text value — Specify the hexadecimal (RGB) value of the color.
例外: Failed to set color

## Launch Excel  `#launchexcel`
Launches a new Excel instance or opens an Excel document.
入力:
- Launch Excel: With a blank document, and open the following document = With a blank document — Specify whether to open a New Excel document, or an existing document
- Document path: File — The full path of the existing Excel document to open
- Make instance visible: Boolean value = True — Specify whether to make the Excel window visible or hidden
- Nest under a new Excel process: Boolean value = False — Specify whether the Excel spreadsheet should be under a unique Excel process. Macros and add-ins from other spreadsheets won't be accessible.
- Password(任意): Direct encrypted input or Text value — The password on the Excel document, if it's password protected
- Open as ReadOnly: Boolean value = False — Specify whether to open the stored document in read-only mode or not
- Load add-ins and macros: Boolean value = False — Specify whether to load add-ins and macros into the new Excel instance
出力:
- ExcelInstance: Excel instance — The specific Excel instance for use with later Excel actions. This allows the user to specify which of possibly several Excel spreadsheets to access
例外: Failed to launch Excel; Failed to open Excel document

## Attach to running Excel  `#attach`
Attaches to an Excel document that's already open.
入力:
- Document name: File — The name or the path of the Excel document to attach to
出力:
- ExcelInstance: Excel instance — The Excel instance this action has attached to for use with later Excel actions
例外: Specified Excel document not found; Failed to attach to Excel document

## Read from Excel worksheet  `#readfromexcel`
Reads the value of a cell or a range of cells from the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Retrieve: The value of a single cell, Values from a range of cells, Values from selection, All available values from worksheet = The value of a single cell — Whether to retrieve the value of a single cell, a table from a range of cells or the entire worksheet
- Start column: Text value — The cell column (single cell's value) or first column as a numeric value or a letter
- Start row: Numeric value — The cell row (single cell's Value) or first row number
- End column: Text value — The last column as a numeric value or a letter
- End row: Numeric value — The last row number
- Get cell(s) contents as: Typed values,Plain text,Formatted text values = Typed values — Specify whether to retrieve the content of the cells as the closest matching type, such as Date Time for dates or Numeric for numbers, purely as text, or as formatted cell text.
- First line of range contains column names: Boolean value = False — Specify whether to consider the first row as column names. In this case, the names won't be read as data into the table and later actions can search the data by column names.
出力:
- ExcelData: General value — The value of the single cell
- ExcelData: Datatable — The value of the range of cells as a DataTable
例外: Failed to read cell values

## Get active cell on Excel worksheet  `#getactivecell`
Get the active cell in the active worksheet of the Excel document.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
出力:
- ActiveCellColumnIndex: Numeric value — The numeric value of the active cell's column
- ActiveCellRowIndex: Numeric value — The numeric value of the active cell's row
例外: Failed to get active cell

## Save Excel  `#saveexcel`
Saves a previously launched Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to save. This variable must have been previously specified in a Launch Excel action.
- Save mode: Save document, Save document as = Save document — How to save the document of this instance
- Document format: Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-In (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb) = Default (From Extension) — The format to save the document as
- Document path: File — The full path to save the document as
例外: Failed to save Excel document

## Write to Excel worksheet  `#writetoexcel`
Writes a value into a cell or a range of cells of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Value to write: General value — Enter the text, number, or variable to insert. If the variable contains a table, it will fill in cells to the right and below, writing over other cell data if need be and a list will fill in cells below.
- Write mode: On specified cell, On currently active cell = On specified cell — Whether to write into a specified cell or the currently active cell
- Column: Text value — The column number or letter for the cell to write to
- Row: Numeric value — The row of the cell to write to. The numbering starts from 1, meaning that the index of the first worksheet is 1, the second is 2, and so on.
例外: Failed to write value to Excel

## Close Excel  `#closeexcel`
Closes an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to close. This variable must have been previously specified in a Launch Excel action.
- Before closing Excel: Do not save document, Save document, Save document as = Don't save document — Whether and how to save the document of this instance before closing that instance
- Document format: Default (From Extension), Excel Workbook (.xlsx), Excel Workbook Macro Enabled (.xlsm), Excel 97-2003 Workbook (.xls), Web Page (.htm, .html), Excel Template (.xltx), Excel Template Macro Enabled (.xltm), Excel 97-2003 Template (.xlt), Text (.txt), Unicode Text (.txt), Text Macintosh (.txt), Text DOS (.txt), XML Spreadsheet (.xml), Excel 95 (.xls), CSV (.csv), DIF (.dif), SYLK (.slk), Excel add-in (.xlam), Excel 97-2003 add-in (.xla), Strict Open XML Workbook (.xlsx), OpenDocument Spreadsheet (.ods), XML Data (.xml), Excel Binary Workbook (.xlsb) = Default (From Extension) — The format of the document
- Document path: File — The full path of the document
例外: Failed to save Excel document; Failed to close Excel instance

## Set active Excel worksheet  `#setactiveworksheet`
Activates a specific worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- Activate worksheet with: Index, Name = Name — Specify whether to find the worksheet by name or index
- Worksheet index: Numeric value — The index number of the worksheet to activate. The numbering starts from 1, meaning that the index of the first worksheet is 1, the second is 2, and so on.
- Worksheet name: Text value — The name of the worksheet to activate
例外: Can't find worksheet; Failed to activate worksheet

## Add new worksheet  `#addworksheet`
Adds a new worksheet to the document of an Excel instance.
入力:
- Excel instance: Excel instance — Specify the Excel instance. This variable must have been previously specified in a Launch Excel action.
- New worksheet name: Text value — Specify the name of the new worksheet
- Add worksheet as: First worksheet, Last worksheet = First worksheet — Specify whether the new Excel worksheet will be added before or after the existing worksheets
例外: A worksheet with the same name already exists; Failed to add worksheet

## Get first free column/row from Excel worksheet  `#getfirstfreecolumnrow`
Retrieves the first free column and/or row of the active worksheet. This is useful for adding new data into a worksheet that already has data in it.
入力:
- Excel instance: Excel instance — Specify The Excel instance. This variable must have been previously specified in a Launch Excel action.
出力:
- FirstFreeColumn: Numeric value — The numeric value of the first fully empty column. For example, if column F is the first empty column, it will be stored as '6'.
- FirstFreeRow: Numeric value — The numeric value of the first fully empty row. For example, if row 7 is the first empty row, it will be stored as '7'.
例外: Failed to retrieve first free column/row

## Get column name on Excel worksheet  `#getcolumnname`
Gets the name of the column.
入力:
- Column number: Numeric value — The column number
出力:
- ColumnName: Text value — The name of the column

## Clear cells in Excel worksheet  `#clearcellsfromexcel`
Clears a range of cells or a named cell in the active worksheet of an Excel instance.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Clear: Range of cells, Range of cells relative to active cell, Named cells, Single cell = Range of cells — Specify whether to select an explicitly specified range of cells, a range of cells relative to the currently active cell, named cells, or a single cell.
- X Axis Direction: Left, Right = Left — The X-axis offset direction. Where to look along the horizontal axis, based on currently activated cell's position.
- Start column: Text value — The index or letter of the first column.
- X Offset: Numeric value — The X-axis offset.
- Start row: Numeric value — The first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the last column.
- Y Axis Direction: Above, Below = Above — The Y-axis offset direction. Where to look along the vertical axis, based on the position of the currently active cell.
- End row: Numeric value — The last row number. The numbering starts from 1.
- Y Offset: Numeric value — The Y-axis offset.
- Name: Text value — The name of cells.
- Column: Text value — The index or letter of the column.
- Row: Numeric value — The row number. Enumeration starts from 1.
出力:
- Failed to clear cells: Indicates a problem occurred while trying to clear the specified cells in the Excel instance. — 

## Sort cells in Excel worksheet  `#sortcellsfromexcel`
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Sort column in: Active sheet, Table, Range = Active sheet — Specify whether the column to be sorted is part of a table, a specified range, either by name or absolute coordinates or if it's part of the general active worksheet.
- Table name: Text value — The name of the table.
- Range: Named cells, Specific range = Named cells — Specify the range to be sorted, either using named cell or absolute column and row index.
- Cells name: Text value — Name representing the range.
- Start column: Text value — The index or letter of the first column.
- Start row: Numeric value — The first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the last column.
- End row: Numeric value — The last row number. The numbering starts from 1.
- Sort by(任意): Sorting rules as defined by the user = N/A — Sorting rules to apply.
- First row is header(任意): Boolean value — Indicates that the first row of the worksheet is a header.
例外: Failed to sort cells in worksheet

## Filter cells in Excel worksheet  `#filtercellsfromexcel`
The Filter cells in Excel worksheet allows makers to create and apply a filter in the active sheet, table, or range on the values of a specified column. To filter multiple columns in an active sheet/table/range, multiple Filter cells in Excel worksheet actions must be used, each one applying the respective filter.
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Filter column in: Active sheet, Table, Range = Active sheet — Specify whether the column to be filtered is part of a table, a specified range, either by name or absolute coordinates or if it's part of the general active worksheet
- Table name: Text value — The name of the table.
- Range: Named cells, Specific range = Named cells — Specify the range to be filtered, either using named cell or absolute column/row index
- Cells name: Text value — Name representing the range
- Start column: Text value — The index or letter of the first column.
- Start row: Numeric value — The first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the last column.
- End row: Numeric value — The last row number. The numbering starts from 1.
- Column to filter: Text value — Name or index of the column to be filtered. If the column is part of a table use the header name.
- Filters to apply(任意): Filtering rules as defined by the user = N/A — Filtering rules applied to the defined column
例外: Failed to apply filter on cells in worksheet

## Clear filters in Excel worksheet  `#clearfilterfromexcel`
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Clear filters in: Active sheet, Table = Active sheet — Specify whether to clear filters from the entire active worksheet or from a specific table.
- Table name: Text value — The name of the table.
- Clear filters from specific column(任意): Boolean value — Clear filters from specific column.
- Clear filter in column: Text value — The column name to clear applied filter.
例外: Failed to clear filter on cells in worksheet

## Get empty cell  `#getemptycellfromexcel`
入力:
- Excel instance: Excel instance — The Excel instance to work with. This variable must have been previously specified in a Launch Excel action.
- Operation: First empty cell, First empty cell in column, First empty cell in row, All empty cells = First empty cell — Specify whether to search for the first empty cell, the first empty cell on column, the first empty cell on row, or all empty cells inside a specific range.
- Search direction: By row, By column = By row — Specify whether to search by rows or columns to find the first empty cell inside a specific range.
- Search in: Named cells, Specific range = Named cells — Search for empty cell in a named cell or a range defined by start column/row and end column/row.
- Cells name: Text value — Name representing the range.
- Column: Text value — Column.
- Row: Numeric value — Row.
- Start column: Text value — The index or letter of the first column.
- Start row: Numeric value — The first row number. The numbering starts from 1.
- End column: Text value — The index or letter of the last column.
- End row: Numeric value — The last row number. The numbering starts from 1.
出力:
- EmptyCellColumnIndex: Numeric value — The index of the column the first empty cell is found.
- EmptyCellRowIndex: Numeric value — The index of the row the first empty cell is found.
- EmptyCells: Datatable — The list of empty cells found.
例外: Get empty cells failed
