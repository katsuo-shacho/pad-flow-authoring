# Variables actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/variables （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: To manually create a variable in a desktop flow, deploy the Set variable action. This action requires you to provide a name and a value for the new variable. To increase or decrease the value of a numeric variable, use the Increase variable and Decrease variable actions, respectively. Most actions output their result into a variable. For example, the Create new list action produces an empty list. Similarly, the Generate random number action produces a random numeric value. If you enable Generate multiple numbers in this action, you create a list variable containing multiple random numeric valu

## Create new data table  `#createnewdatatable`
Creates a new data table variable.
入力:
- New table: Datatable — The input data table
出力:
- DataTable: Datatable — The new data table

## Insert row into data table  `#addrowtodatatable`
Inserts a row at the end or before a specific index value.
入力:
- Data table: Datatable — The data table variable to work with. This variable must have been previously specified by an action that produces a data table variable
- Into location: End of data table, Before row index = End of data table — Specify whether to insert the new row at the end of the data table or before a specified row index
- Row index: Numeric value — Insert the row index value to be used when before row index is specified as the into location parameter
- New value(s): List, Datarow — This parameter accepts a list or datarow variable where the column count should match the column count in the data table
例外: Item index is out of range; Invalid input arguments; Incompatible type error

## Delete row from data table  `#deleterowfromdatatable`
Delete a data table row at the corresponding row index.
入力:
- Data table: Datatable — The data table variable to work with. This variable must be specified by an action that produces a data table variable
- Row index: Numeric value — The row index within a data table that should be deleted
例外: Item index is out of range

## Update data table item  `#modifydatatableitem`
Update a data table row item on a defined column.
入力:
- Data table: Datatable — The data table variable to work with. This variable must have been previously specified by an action that produces a data table variable.
- Column: Text value — The column name or index of the item to update.
- Row: Numeric value — The row index of the item to update.
- New value: Text value — The new value to update at the specified row index and column.
例外: Item index is out of range; Column name doesn't exist; Column index is out of range; Incompatible type error

## Find or replace in data table  `#findorreplaceindatatable`
Finds and/or replaces data table values.
入力:
- Data table: Datatable — The data table variable to work with. This variable must have been previously specified by an action that produces a data table variable
- Search mode: Find, Find and replace = Find — The mode to search with (find or find and replace)
- All matches: Boolean value = True — Specify whether to find or replace text in all the matching cells found or the first matching cell only
- Text to find: Text value — The text to find in the data table
- Find using a regular expression: Boolean value = False — Specify whether to use a regular expression to match the cell contents with the text to find
- Match case: Boolean value = False — Specify whether to search for case-sensitive data
- Match entire cell contents: Boolean value = False — Specify whether to search for cells that contain just the specified text
- Text to replace with: Text value — The text used to replace the matching cells
- Search by: Everywhere, On column = Everywhere — The order in which to search for the text (everywhere, or on column)
- Column index or name: Text value — The column header or index value
出力:
- DataTableMatches: Datatable — The data table containing the row and column indexes for matches
例外: Provided regular expression is invalid; Column name doesn't exist; Column index is out of range; Incompatible type error

## Insert column into data table  `#addcolumntodatatableaction`
Inserts a column at the end or before a specific index value.
入力:
- Data table: Datatable — The data table variable to work with. This variable must be specified by an action that produces a data table variable.
- Into location: End of data table, Before column index = End of data table — Specify whether to insert the new column at the end of the data table or before a specified column index.
- Column name: Text value — Specify the header of the new column.
- Column index: Numeric value — Specify the column index value that is utilized when the Before column index option is selected for the Into location parameter.
例外: Column index is out of range; Duplicate column name

## Delete column from data table  `#deletecolumnfromdatatableaction`
Delete a data table column at the specified column index or column name.
入力:
- Data table: Datatable — The data table variable to work with. This variable must be specified by an action that produces a data table variable.
- Specify column with: Name, Index = Name — Specify whether to find the column by name or index.
- Column name: Text value — The name of the column that should be deleted.
- Column index: Numeric value — The index of the column that should be deleted. Column indexes start from 0.
例外: Column name doesn't exist; Column index is out of range

## Delete empty rows from data table  `#deleteemptyrowsfromdatatableaction`
Deletes the rows of the data table that have all of their cells empty.
入力:
- Data table: Datatable — The data table variable to work with. This variable must have been previously specified by an action that produces a data table variable

## Delete duplicate rows from data table  `#deleteduplicaterowsfromdatatableaction`
Deletes all the rows that are duplicate from the data table, if the values have the same data type in each column.
入力:
- Data table: Datatable — The data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
例外: Type mismatch in the cells of a column

## Clear data table  `#cleardatatableaction`
Deletes all the rows of the data table, keeping table headers unaffected.
入力:
- Data table: Datatable — The data table variable to work with. The specified variable must be defined through an action that generates a data table variable.

## Sort data table  `#sortdatatableaction`
Sorts the data table rows in ascending or descending order by the specified column, if all its values have the same data type.
入力:
- Data table: Datatable — The data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
- Specify column with: Name, Index = Name — Specify whether to find the column by name or index.
- Column name: Text value — The name of the column that should be sorted.
- Column index: Numeric value — The index of the column that should be sorted. Column indexes start from 0.
- Order: Ascending, Descending = Ascending — The order to sort the data table.
例外: Column name doesn't exist; Column index is out of range; Type mismatch in the cells of a column

## Filter data table  `#filterdatatableaction`
Filters the data table rows based on the applied rules.
入力:
- Data table: Datatable — The data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
- Filters to apply: Filtering rules as defined by the user = N/A — Filtering rules applied to the defined columns
- Match case: Boolean value = True — Specify whether to search for case-sensitive data. Applies only in filters: Equal to, Not equal to, Contains, Does not contain, Starts with, Does not start with, Ends with, Does not end with.
出力:
- FilteredDataTable: Datatable — The generated data table after applying the filters
例外: Column name doesn't exist; Column index is out of range; Type mismatch in the cells of a column

## Merge data tables  `#mergedatatablesaction`
Merges two data tables together, specifying the merging behavior in case their number of columns is different.
入力:
- First data table: Datatable — The first data table variable to work with. This is also the action's produced variable that holds the merged data table
- Second data table: Datatable — The second data table that is merged into the first data table
- Merge mode: Add extra columns, Ignore extra columns, Error on extra columns = Add extra columns — The merging behavior that is applied when the tables don't have the same number of columns
例外: Missing Schema

## Join data tables  `#joindatatableaction`
Joins two data tables based on the specified join rule.
入力:
- First data table: Datatable — The first data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
- Second data table: Datatable — The second data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
- Join operation: Inner, Left, Full = Inner — The join operation that is used to join the two tables
- Join rules: Join rules as defined by the user = N/A — Define the columns and the operation to be used for joining the two data tables
出力:
- JoinedDataTable: Datatable — The generated data table after the join operation
例外: Column name doesn't exist; Column index is out of range

## Read from CSV text variable  `#generatedatatablefromcsv`
Generates a data table from a CSV text.
入力:
- CSV text: Text value — The CSV text variable to read.
- Trim fields: Boolean value = True — Specifies whether to automatically trim off the leading and trailing whitespaces of the extracted cells.
- First line contains column names: Boolean value = False — Specifies whether to use the first row of the CSV text to set the column names of the resulting data table. Enable this option to avoid reading the names as data into the table. Subsequent actions might access the data held by the data table using column names (instead of column numbers).
- Get CSV fields as text: Boolean value = False — Specify whether to retrieve the content of the CSV text fields purely as text or as the closest matching type. For example, Date Time for dates and Numeric for numbers.
- Columns separator: Predefined, Custom, Fixed Column Widths = Predefined — Specifies whether to use a predefined columns separator, a custom separator, or fixed column widths.
- Separator: System default, Comma, Semicolon, Tab = System default — The column-separator to parse the CSV text.
- Custom separator: Text value — The custom column-separator to use for parsing the CSV text.
- Fixed column widths: Text value — The fixed column-widths to use for parsing the CSV text. Separate the widths using commas, spaces, tabs, or newlines.
出力:
- CSVTable: Datatable — The contents of the CSV text as a data table
例外: CSV parsing failed

## Convert data table to text  `#convertdatatabletocsvaction`
Converts a data table to a CSV text.
入力:
- Data table: Datatable — The data table variable to work with. The specified variable must be defined through an action that generates a data table variable.
- Include column names: Boolean value = False — Specifies whether the column names of the variant specified should become the first row of the CSV text.
- Use custom columns separator: Boolean value = False — Specifies whether to use a custom column separator or a predefined column separator.
- Separator: System default, Comma, Semicolon, Tab = System default — The column separator to use in the specified CSV text.
- Custom columns separator: Text value — The custom column separator to use in the specified CSV text.
出力:
- CSVText: Text value — The variable in which the CSV result is stored
例外: Conversion failed

## Truncate number  `#truncatenumber`
Get the integral or fractional digits of a numeric value, or round up the value to a specified number of decimal places.
入力:
- Number to truncate: Numeric value — The number or variable that holds the numeric value to truncate/round up
- Operation: Get integer part, Get decimal part, Round number = Get integer part — Specifies the operation to perform on the given number
- Decimal places(任意): Numeric value = 3 — The number of decimal places to round the given number up to. Enter 0 to return an integer as a result
出力:
- TruncatedValue: Numeric value — The truncated or rounded number

## Generate random number  `#generaterandomnumber`
Generate a random number or a list of random numbers that fall between a minimum and maximum value.
入力:
- Minimum value(任意): Numeric value = 0 — The lower boundary for the random number(s) to generate
- Maximum value(任意): Numeric value = 100 — The upper boundary for the random number(s) to generate
- Generate multiple numbers: Boolean value = False — Specifies whether to generate a single random number or a list of random numbers
- How many numbers(任意): Numeric value = 10 — Specifies how many random numbers to generate
- Allow duplicates: Boolean value = False — Specifies whether to permit or prevent the same number from appearing more than once in the random numbers list
出力:
- RandomNumber: Numeric value — The newly generated random number
- RandomNumbers: List of Numeric values — The newly generated list of random numbers
例外: Failed to generate random number

## Clear list  `#clearlist`
Remove all items from a list.
入力:
- List to clear: List of General values — A list variable to remove its elements

## Remove item from list  `#removeitemfromlist`
Remove one or multiple items from a list.
入力:
- Remove item by: Index, Value = Index — Specifies whether to remove the item at a specified index or the item(s) with a specific value
- At index: Numeric value — The index number of the item to remove
- With value: General value — The item to remove
- Remove all item occurrences: Boolean value = False — Removes all the occurrences that match the item specified
- From list: List of General values — The list with items to remove
例外: Item index is out of range; Item not found

## Sort list  `#sortlistbase`
Sort the items of a list. Use items of the same type.
入力:
- List to sort: List of General values — The variable that holds the list to sort
- Sort by list item's properties: Boolean value = False — If the list items are objects (such are files, folders, etc.), enable this option to sort the item by a specific property. Leave this option disabled to sort the elements by their default property (for example, file objects are sorted by their full path)
- First property to sort by(任意): Text value — The name of an item's property to sort the list by. Refer to the help file for the property names of each object
- Sort: Ascending, Descending = Ascending — Specifies whether to sort by the first property ascending or descending
- Second property to sort by(任意): Text value — The name of a second property to sort the list by
- Sort: Ascending, Descending = Ascending — Specifies whether to sort by the second property ascending or descending
- Third property to sort by(任意): Text value — The name of a third property to sort the list by
- Sort: Ascending, Descending = Ascending — Specifies whether to sort by the third property ascending or descending

## Shuffle list  `#shufflelist`
Create a random permutation of a list.
入力:
- List to shuffle: List of General values — The variable that contains the list to shuffle

## Merge lists  `#mergelists`
Merge two lists into one.
入力:
- First list: List of General values — The first list of items to merge
- Second list: List of General values — The second list of items to merge
出力:
- OutputList: List of General values — The merged list. The initial lists aren't affected
例外: The lists supplied are of incompatible types

## Reverse list  `#reverselist`
Reverse the order of the items of a list.
入力:
- List to reverse: List of General values — The list whose items order to reverse

## Remove duplicate items from list  `#removeduplicateitemsfromlist`
Remove the multiple occurrences of items in a list, so that in the resulting list each item is unique.
入力:
- List to remove duplicate items from: List of General values — The list variable to remove duplicate items from
- Ignore text case while searching for duplicate items: Boolean value = False — Specifies whether to perform case insensitive comparison of text while searching for duplicate items (only applies to lists made of text items)

## Find common list items  `#findcommonlistitems`
Compare two lists and create a new list with the items that are common to both.
入力:
- First list: List of General values — The variable that contains the first list to compare
- Second list: List of General values — The variable that contains the second list to compare
出力:
- IntersectionList: List of General values — The new list of common items

## Subtract lists  `#subtractlists`
Compare two lists and create a new list with the items that are in the first list but not in the second.
入力:
- First list: List of General values — The variable that holds the first list to compare
- Second list: List of General values — The variable that holds the second list to compare
出力:
- ListDifference: List of General values — The new resulting list

## Retrieve data table column into list  `#retrievedatatablecolumnintolist`
Convert the contents of a data table column into a list.
入力:
- Data table: Datatable — The data table with the column to convert into a list
- Column name or index: Text value — The column name, if column names are defined, or the index number of the column to retrieve
出力:
- ColumnAsList: List of General values — The new list that holds the contents of the specified data table
例外: Column name doesn't exist; Column index is out of range

## Convert JSON to custom object  `#convertjsontocustomobject`
Convert a JSON string to a custom object.
入力:
- JSON: Text value — A JSON text, or a previously created variable containing one, to convert it to a custom object
出力:
- JsonAsCustomObject: General value — The converted custom object from the provided JSON
例外: Error parsing the JSON

## Convert custom object to JSON  `#convertcustomobjecttojson`
Convert a custom object to a JSON string.
入力:
- Custom object: Custom object — The custom object to convert to JSON
出力:
- CustomObjectAsJson: Text value — The converted JSON from the provided custom object
例外: Error parsing the custom object

## Add item to list  `#additemtolist`
Append a new item to a list.
入力:
- Add item: General value — A value or a variable to add to the list. Provide a list of values to append multiple elements. If the list has a specific type of elements, the new element is converted over to that type
- Into list: List of General values — A list variable to append the new elements to
出力:
- NewList: List of General values — The new list

## Create new list  `#createnewlist`
Create a new empty list.
出力:
- List: List of General values — The new list

## Increase variable  `#increasevariable`
Increase the value of a variable by a specific amount.
入力:
- Variable name: Numeric value — The numeric value to increase
- Increase by: Numeric value — A numeric value, or a previously created variable containing one, to increase the variable by

## Decrease variable  `#decreasevariable`
Decrease the value of a variable by a specific amount.
入力:
- Variable name: Numeric value — A numeric value, or a previously created variable containing one, to decrease the variable by
- Decrease by: Numeric value — A numeric value, or a previously created variable containing one, to decrease the variable by

## Run Power Fx expression
Runs the provided Power Fx expression.
入力:
- Expression: * — The Power Fx expression to run

## Set variable  `#assign`
Set the value of a new or existing variable, create a new variable or overwrite a previously created variable.
入力:
- To: * — The value to assign to the variable
出力:
- NewVar: * — The name of the variable to set
