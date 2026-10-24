# Database actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/database （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: To connect to a database, use the Open SQL connection action. A connection string specifies all information necessary to connect to a database, such as the driver, the database, server names, and the username and password. The following connection string connects to an Excel database: ```Connection string Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\myFolder\myExcelFile.xlsx;Extended Properties="Excel 12.0 Xml;HDR=YES"; ``` The following connection string connects to an Access database: ```Connection string Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\myFolder\myAccessFile.accdb; Persi

## Open SQL connection  `#connect`
Open a new connection to a database.
入力:
- Connection string: Text value — The connection string to use to connect to the database
出力:
- SQLConnection: SQL connection — A handle for the new SQL connection
例外: Can't connect to data source; Invalid connection string

## Execute SQL statement  `#executesqlstatement`
Connect to a database and execute a SQL statement.

## Natural language to script powered by copilot (preview)
!INCLUDE [cc-beta-prerelease-disclaimer]
入力:
- Get connection by: Connection string, [SQL connection variable] = SQL connection variable — Specifies whether to create a new connection from a given connection string or select an already open connection
- SQL connection: SQL connection — The handle for the new SQL connection
- Connection string: Text value — The connection string to use to connect to the database
- SQL statement: Text value — The SQL statement to execute to the database
- Timeout(任意): Numeric value = 30 — The maximum amount of time to wait for a result from the database
出力:
- QueryResult: Datatable — The result from the database in the form of a data table, with rows and columns
例外: Can't connect to data source; Invalid connection string; Error in SQL statement

## Close SQL connection  `#close`
Close an open connection to a database.
入力:
- SQL connection: SQL connection — The handle for the new SQL connection
