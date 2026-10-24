# Access actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/access （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The Access automation feature lets you interact with locally stored Access databases. Start by creating an Access instance using the 'Launch Access' action. This instance serves as the input parameter for the rest of the actions, allowing you to perform actions on the desired Access database. The following actions are available: * Launch Access * Close Access * Read Access table * Run Access query * Run Access macro

## Launch Access  `#launchaccess`
Launches an Access database.
入力:
- Database path: Path of database — The full path of the Access database to open.
- User interaction mode: Boolean value = False — Specify if the Access instance allows user interaction. This mode keeps the application running after the flow closes and permits user interaction alongside automation but can cause popups and errors requiring user attention.
- Make instance visible: Boolean value = True — Specify whether to make the Access window visible or hide it.
- Database password(任意): Direct encrypted input or Text value — The encryption password of the database, if it's password-protected
- Exclusive: Boolean value = False — Specify whether to open the database in exclusive mode. When enabled, the database can't be shared with others while it's open.
出力:
- `AccessInstance`: Access instance — The specific Access instance for use with later Access actions. This allows the user to specify which of potentially several Access documents to access
例外: The Access database was not found; Failed to open existing Access database; Failed to launch Access; Access application is not installed

## Read Access table  `#readaccesstable`
Reads an Access table
入力:
- Access instance: Access instance — The Access instance to work with. This variable must be specified in a Launch Access action.
- Table name: Text — The name of the Access table. You must type the exact name of the table as it is stored in the specific Access database.
出力:
- Result: Text — The result of the read query.
例外: Failed to read an Access table

## Run Access query  `#runaccessquery`
Runs a stored Access query
入力:
- Access instance: Access instance — The Access instance to work with. This variable must be specified in a Launch Access action.
- Query name: Text — The name of the stored Access query. You must type the exact name of the query as it is stored in the specific Access database.
- Query type: Select query, Action query = Select query — Specify whether this query is a Select or Action query.
- Contains parameter(任意): Boolean = False — Specify the parameters required to run the query. Ensure the parameter names and data types match the ones in the query.
出力:
- QueryResult: Text — The result of the Select query execution, returning the output of the query in a datatable.
- AffectedRows: Text — The number of rows that are affected, as a result of executing the Action query.
例外: Failed to run an Access query

## Run Access macro  `#runaccessmacro`
Runs a stored Access macro
入力:
- Access instance: Access instance — The Access instance to work with. This variable must be specified in a Launch Access action.
- Macro name: Text — The name of the stored Access macro. You must type the exact name of the macro as it is stored in the specific Access database.
- Is VBA Macro: Boolean = False — Specify if the macro is a VBA macro.
- Contains parameter(任意): Boolean = False — Specify the parameters required to run the macro. Ensure the parameter names and data types match the ones in the macro.
例外: Failed to run an Access macro

## Close Access  `#closeaccess`
Closes an Access instance
入力:
- Access instance: Access instance — The Access instance to work with. This variable must be specified in a Launch Access action.
- Before closing Access: Do not save changes, Save changes = Do not save changes — Specify whether to save the Access database before closing this instance.
例外: Failed to close Access
