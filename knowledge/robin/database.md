# Robin: Database

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Database.Close [A]
```
Database.Close Connection: SQLConnection
```
入力: Connection:SqlConnectionHandle
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Database.Connect のセレクター: Connect, ConnectOracle

## Database.Connect.Connect [A]
```
Database.Connect.Connect ConnectionString: $'''example''' Connection=> SQLConnection
```
入力: !ConnectionString:String
出力: Connection:SqlConnectionHandle=>SQLConnection
ON ERROR可: ConnectToDataSourceError, InvalidConnectionStringError, NativeProviderNotAvailable
固定: DatabaseType=Other

## Database.Connect.ConnectOracle [A]
```
Database.Connect.ConnectOracle ProviderLibraryPath: $'''C:\temp\test.xlsx''' ConnectionString: $'''example''' Connection=> SQLConnection
```
入力: !ProviderLibraryPath:FileObject !ConnectionString:String
出力: Connection:SqlConnectionHandle=>SQLConnection
ON ERROR可: ConnectToDataSourceError, InvalidConnectionStringError, NativeProviderNotAvailable
固定: DatabaseType=Oracle

### Database.ExecuteSqlStatement のセレクター: ConnectAndExecute, ConnectAndExecuteOracle, Execute

## Database.ExecuteSqlStatement.ConnectAndExecute [A]
```
Database.ExecuteSqlStatement.ConnectAndExecute Statement: $'''example''' Timeout: 30 ConnectionString: $'''example''' Result=> QueryResult
```
入力: !Statement:String !Timeout:Int32 !ConnectionString:String
出力: Result:DataTable=>QueryResult
ON ERROR可: ConnectToDataSourceError, InvalidConnectionStringError, NativeProviderNotAvailable, SqlStatementError
固定: GetConnection=ConnectionString, DatabaseType=Other

## Database.ExecuteSqlStatement.ConnectAndExecuteOracle [A]
```
Database.ExecuteSqlStatement.ConnectAndExecuteOracle Statement: $'''example''' Timeout: 30 ProviderLibraryPath: $'''C:\temp\test.xlsx''' ConnectionString: $'''example''' Result=> QueryResult
```
入力: !Statement:String !Timeout:Int32 !ProviderLibraryPath:FileObject !ConnectionString:String
出力: Result:DataTable=>QueryResult
ON ERROR可: ConnectToDataSourceError, InvalidConnectionStringError, NativeProviderNotAvailable, SqlStatementError
固定: GetConnection=ConnectionString, DatabaseType=Oracle

## Database.ExecuteSqlStatement.Execute [A]
```
Database.ExecuteSqlStatement.Execute Connection: SQLConnection Statement: $'''example''' Timeout: 30 Result=> QueryResult
```
入力: Connection:SqlConnectionHandle Statement:String Timeout:Int32
出力: Result:DataTable=>
ON ERROR可: ConnectToDataSourceError, InvalidConnectionStringError, NativeProviderNotAvailable, SqlStatementError
固定: GetConnection=SQLConnectionVariable
