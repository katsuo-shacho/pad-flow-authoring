# Robin: Access

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Access.CloseAccess [A]
```
Access.CloseAccess Instance: AccessInstance
```
入力: Instance:AccessInstanceHandle CloseMode:CloseAccessMode{DoNotSave,Save}
ON ERROR可: CloseAccessError

### Access.LaunchAccess のセレクター: LaunchExistingDbInAutomationMode, LaunchExistingDbInUserControlMode

## Access.LaunchAccess.LaunchExistingDbInAutomationMode [A]
```
Access.LaunchAccess.LaunchExistingDbInAutomationMode Path: $'''C:\temp\test.xlsx''' Visible: True Exclusive: False Password: $'''password''' Instance=> AccessInstance
```
入力: Path:FileObject Visible:Boolean Password:EncryptableObject Exclusive:Boolean
出力: Instance:AccessInstanceHandle=>
ON ERROR可: LaunchAccessError, LaunchAccessFileNotFoundError, LaunchAccessInstallationError, LaunchAccessOpenCurrentDatabaseError
固定: UserControl=False

## Access.LaunchAccess.LaunchExistingDbInUserControlMode [A]
```
Access.LaunchAccess.LaunchExistingDbInUserControlMode Password: $'''password''' Exclusive: False Path: $'''C:\temp\test.xlsx''' Instance=> AccessInstance
```
入力: Password:EncryptableObject !Exclusive:Boolean !Path:FileObject
出力: Instance:AccessInstanceHandle=>AccessInstance
ON ERROR可: LaunchAccessError, LaunchAccessFileNotFoundError, LaunchAccessInstallationError, LaunchAccessOpenCurrentDatabaseError
固定: UserControl=True

## Access.ReadAccessTable [A]
```
Access.ReadAccessTable Instance: AccessInstance TableName: $'''example''' Result=> Result
```
入力: Instance:AccessInstanceHandle TableName:String
出力: Result:DataTable=>
ON ERROR可: ReadAccessTableError

### Access.RunAccessMacro のセレクター: RunAccessMacro, RunAccessVBAMacro, RunAccessVBAMacroWithParameters

## Access.RunAccessMacro.RunAccessMacro [A]
```
Access.RunAccessMacro.RunAccessMacro Instance: AccessInstance MacroName: $'''example'''
```
入力: Instance:AccessInstanceHandle MacroName:String
ON ERROR可: RunAccessMacroError
固定: IsVBMacro=False

## Access.RunAccessMacro.RunAccessVBAMacro [A]
```
Access.RunAccessMacro.RunAccessVBAMacro Instance: AccessInstance MacroName: $'''example'''
```
入力: !Instance:AccessInstanceHandle !MacroName:String
ON ERROR可: RunAccessMacroError
固定: IsVBMacro=True, HasParameters=False

## Access.RunAccessMacro.RunAccessVBAMacroWithParameters [A]
```
Access.RunAccessMacro.RunAccessVBAMacroWithParameters MacroParameters: RecognizedEntities Instance: AccessInstance MacroName: $'''example'''
```
入力: MacroParameters:DataTable !Instance:AccessInstanceHandle !MacroName:String
ON ERROR可: RunAccessMacroError
固定: IsVBMacro=True, HasParameters=True

### Access.RunAccessQuery のセレクター: RunAccessActionQuery, RunAccessActionQueryWithParameters, RunAccessSelectQuery, RunAccessSelectQueryWithParameters

## Access.RunAccessQuery.RunAccessActionQuery [A]
```
Access.RunAccessQuery.RunAccessActionQuery Instance: AccessInstance QueryName: $'''example''' AffectedRows=> AffectedRows
```
入力: !Instance:AccessInstanceHandle !QueryName:String
出力: AffectedRows:Int32=>AffectedRows
ON ERROR可: RunAccessQueryError
固定: QueryType=ActionQuery, HasParameters=False

## Access.RunAccessQuery.RunAccessActionQueryWithParameters [A]
```
Access.RunAccessQuery.RunAccessActionQueryWithParameters QueryParameters: RecognizedEntities Instance: AccessInstance QueryName: $'''example''' AffectedRows=> AffectedRows
```
入力: QueryParameters:DataTable !Instance:AccessInstanceHandle !QueryName:String
出力: AffectedRows:Int32=>AffectedRows
ON ERROR可: RunAccessQueryError
固定: QueryType=ActionQuery, HasParameters=True

## Access.RunAccessQuery.RunAccessSelectQuery [A]
```
Access.RunAccessQuery.RunAccessSelectQuery Instance: AccessInstance QueryName: $'''example''' QueryResult=> QueryResult
```
入力: Instance:AccessInstanceHandle QueryName:String
出力: QueryResult:DataTable=>
ON ERROR可: RunAccessQueryError
固定: QueryType=SelectQuery, HasParameters=False

## Access.RunAccessQuery.RunAccessSelectQueryWithParameters [A]
```
Access.RunAccessQuery.RunAccessSelectQueryWithParameters QueryParameters: RecognizedEntities Instance: AccessInstance QueryName: $'''example''' QueryResult=> QueryResult
```
入力: QueryParameters:DataTable !Instance:AccessInstanceHandle !QueryName:String
出力: QueryResult:DataTable=>QueryResult
ON ERROR可: RunAccessQueryError
固定: QueryType=SelectQuery, HasParameters=True
