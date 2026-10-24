# Robin: Variables

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Variables.AddColumnToDataTable のセレクター: AppendColumnToDataTable, InsertColumnToDataTable

## Variables.AddColumnToDataTable.AppendColumnToDataTable [A]
```
Variables.AddColumnToDataTable.AppendColumnToDataTable DataTable: DataTable ColumnName: $fx'example'
```
入力: DataTable:DataTable ColumnName:String
ON ERROR可: ColumnIndexOutOfRangeError, DuplicateColumnNameError
固定: PositionToAddColumn=LastColumn

## Variables.AddColumnToDataTable.InsertColumnToDataTable [A]
```
Variables.AddColumnToDataTable.InsertColumnToDataTable ColumnName: $fx'example' ColumnIndex: 1 DataTable: RecognizedEntities
```
入力: !ColumnName:String !ColumnIndex:Int32 !DataTable:DataTable
ON ERROR可: ColumnIndexOutOfRangeError, DuplicateColumnNameError
固定: PositionToAddColumn=BeforeColumnIndex

## Variables.AddItemToList [A]
```
Variables.AddItemToList Item: $fx'sample' List: FileList
```
入力: Item:Object List:List
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.AddRowToDataTable のセレクター: AppendRowToDataTable, InsertItemToDataTable

## Variables.AddRowToDataTable.AppendRowToDataTable [A]
```
Variables.AddRowToDataTable.AppendRowToDataTable DataTable: DataTable RowToAdd: FileList
```
入力: DataTable:DataTable RowToAdd:List
ON ERROR可: IncompatibleTypeError, IndexOutOfRangeError, InvalidInputError
固定: PositionToAddRow=EndOfDataTable

## Variables.AddRowToDataTable.InsertItemToDataTable [A]
```
Variables.AddRowToDataTable.InsertItemToDataTable RowIndex: 1 RowToAdd: List DataTable: RecognizedEntities
```
入力: !RowIndex:Int32 !RowToAdd:List<Object> !DataTable:DataTable
ON ERROR可: IncompatibleTypeError, IndexOutOfRangeError, InvalidInputError
固定: PositionToAddRow=BeforeRowIndex

## Variables.ClearDataTable [A]
```
Variables.ClearDataTable DataTable: DataTable
```
入力: DataTable:DataTable
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.ClearList [A]
```
Variables.ClearList List: FileList
```
入力: List:List
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.ConvertCustomObjectToJson [A]
```
Variables.ConvertCustomObjectToJson CustomObject: MyCustomObject Json=> CustomObjectAsJson
```
入力: CustomObject:CustomObject
出力: Json:String=>
ON ERROR可: ParseCustomObjectError

### Variables.ConvertDataTableToCSV のセレクター: DataTableToCSVCommonSeparator, DataTableToCSVCustomSeparator

## Variables.ConvertDataTableToCSV.DataTableToCSVCommonSeparator [A]
```
Variables.ConvertDataTableToCSV.DataTableToCSVCommonSeparator DataTable: DataTable IncludeColumnNames: False ColumnsSeparator: Variables.CSVColumnsSeparator.SystemDefault CSVText=> CSVText
```
入力: DataTable:DataTable IncludeColumnNames:Boolean ColumnsSeparator:CSVColumnsSeparator{SystemDefault,Comma,Semicolon,Tab}
出力: CSVText:String=>
ON ERROR可: ConvertToCSVError
固定: UseCustomSeparator=False

## Variables.ConvertDataTableToCSV.DataTableToCSVCustomSeparator [A]
```
Variables.ConvertDataTableToCSV.DataTableToCSVCustomSeparator CustomColumnsSeparator: $fx'example' DataTable: RecognizedEntities IncludeColumnNames: False CSVText=> CSVText
```
入力: !CustomColumnsSeparator:String !DataTable:DataTable !IncludeColumnNames:Boolean
出力: CSVText:String=>CSVText
ON ERROR可: ConvertToCSVError
固定: UseCustomSeparator=True

## Variables.ConvertJsonToCustomObject [A]
```
Variables.ConvertJsonToCustomObject Json: $fx'example' CustomObject=> JsonAsCustomObject
```
入力: Json:String
出力: CustomObject:Object=>
ON ERROR可: ParseJsonError

## Variables.CreateNewDatatable [A]
```
Variables.CreateNewDatatable InputTable: { } DataTable=> DataTable
```
入力: InputTable:DataTable
出力: DataTable:DataTable=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.CreateNewList [A]
```
Variables.CreateNewList List=> List
```
出力: List:List=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.DecreaseVariable [A]
```
Variables.DecreaseVariable Value: MyVar DecrementValue: 1
```
入力: DecrementValue:Decimal Value:Decimal
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.DeleteColumnFromDataTable のセレクター: DeleteColumnWithIndex, DeleteColumnWithName

## Variables.DeleteColumnFromDataTable.DeleteColumnWithIndex [A]
```
Variables.DeleteColumnFromDataTable.DeleteColumnWithIndex ColumnIndex: 1 DataTable: RecognizedEntities
```
入力: !ColumnIndex:Int32 !DataTable:DataTable
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError
固定: ColumnSpecifier=Index

## Variables.DeleteColumnFromDataTable.DeleteColumnWithName [A]
```
Variables.DeleteColumnFromDataTable.DeleteColumnWithName DataTable: DataTable ColumnName: $fx'example'
```
入力: DataTable:DataTable ColumnName:String
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError
固定: ColumnSpecifier=Name

## Variables.DeleteDuplicateRowsFromDataTable [A]
```
Variables.DeleteDuplicateRowsFromDataTable DataTable: DataTable
```
入力: DataTable:DataTable
ON ERROR可: ColumnTypeMismatchError

## Variables.DeleteEmptyRowsFromDataTable [A]
```
Variables.DeleteEmptyRowsFromDataTable DataTable: DataTable
```
入力: DataTable:DataTable
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.DeleteRowFromDataTable [A]
```
Variables.DeleteRowFromDataTable DataTable: DataTable RowIndex: 1
```
入力: DataTable:DataTable RowIndex:Int32
ON ERROR可: IndexOutOfRangeError

## Variables.FilterDataTable [A]
```
Variables.FilterDataTable DataTable: DataTable FilterParameters: DataTable MatchCase: True FilteredDataTable=> FilteredDataTable
```
入力: DataTable:DataTable FilterParameters:DataTable MatchCase:Boolean
出力: FilteredDataTable:DataTable=>
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, ColumnTypeMismatchError

## Variables.FilterList [A]
```
Variables.FilterList IgnoreCase: False FilterParameters: RecognizedEntities ListToFilter: List FilteredList=> FilteredList
```
入力: !IgnoreCase:Boolean !FilterParameters:DataTable !ListToFilter:List<Object>
出力: FilteredList:List<Object>=>FilteredList
ON ERROR可: IncompatibleTypesListsError

## Variables.FindCommonListItems [A]
```
Variables.FindCommonListItems FirstList: FileList SecondList: FileList OutputList=> IntersectionList
```
入力: FirstList:List SecondList:List
出力: OutputList:List=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.FindOrReplaceInDataTable のセレクター: FindItemInDataTableByColumnIndex, FindItemInDataTableEverywhere, FindItemInDataTableWithRegexByColumnIndex, FindItemInDataTableWithRegexEverywhere, ReplaceItemInDataTableByColumnIndex, ReplaceItemInDataTableEverywhere, ReplaceItemInDataTableWithRegexByColumnIndex, ReplaceItemInDataTableWithRegexEverywhere

## Variables.FindOrReplaceInDataTable.FindItemInDataTableByColumnIndex [A]
```
Variables.FindOrReplaceInDataTable.FindItemInDataTableByColumnIndex MatchEntireCellContents: False MatchCase: False ColumnNameOrIndex: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !MatchEntireCellContents:Boolean !MatchCase:Boolean !ColumnNameOrIndex:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=OnColumn, SearchMode=Find, UseRegex=False

## Variables.FindOrReplaceInDataTable.FindItemInDataTableEverywhere [A]
```
Variables.FindOrReplaceInDataTable.FindItemInDataTableEverywhere DataTable: DataTable AllMatches: True ValueToFind: $fx'example' MatchCase: False MatchEntireCellContents: False DataTableMatches=> DataTableMatches
```
入力: DataTable:DataTable AllMatches:Boolean ValueToFind:String MatchCase:Boolean MatchEntireCellContents:Boolean
出力: DataTableMatches:DataTable=>
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=Everywhere, SearchMode=Find, UseRegex=False

## Variables.FindOrReplaceInDataTable.FindItemInDataTableWithRegexByColumnIndex [A]
```
Variables.FindOrReplaceInDataTable.FindItemInDataTableWithRegexByColumnIndex ColumnNameOrIndex: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !ColumnNameOrIndex:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=OnColumn, SearchMode=Find, UseRegex=True

## Variables.FindOrReplaceInDataTable.FindItemInDataTableWithRegexEverywhere [A]
```
Variables.FindOrReplaceInDataTable.FindItemInDataTableWithRegexEverywhere DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=Everywhere, SearchMode=Find, UseRegex=True

## Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableByColumnIndex [A]
```
Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableByColumnIndex MatchEntireCellContents: False MatchCase: False TextToReplaceWith: $fx'example' ColumnNameOrIndex: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !MatchEntireCellContents:Boolean !MatchCase:Boolean !TextToReplaceWith:String !ColumnNameOrIndex:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=OnColumn, SearchMode=FindAndReplace, UseRegex=False

## Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableEverywhere [A]
```
Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableEverywhere MatchEntireCellContents: False MatchCase: False TextToReplaceWith: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !MatchEntireCellContents:Boolean !MatchCase:Boolean !TextToReplaceWith:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=Everywhere, SearchMode=FindAndReplace, UseRegex=False

## Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableWithRegexByColumnIndex [A]
```
Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableWithRegexByColumnIndex TextToReplaceWith: $fx'example' ColumnNameOrIndex: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !TextToReplaceWith:String !ColumnNameOrIndex:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=OnColumn, SearchMode=FindAndReplace, UseRegex=True

## Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableWithRegexEverywhere [A]
```
Variables.FindOrReplaceInDataTable.ReplaceItemInDataTableWithRegexEverywhere TextToReplaceWith: $fx'example' DataTable: RecognizedEntities AllMatches: True ValueToFind: $fx'example' DataTableMatches=> DataTableMatches
```
入力: !TextToReplaceWith:String !DataTable:DataTable !AllMatches:Boolean !ValueToFind:String
出力: DataTableMatches:DataTable=>DataTableMatches
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, InvalidRegexError
固定: SearchBy=Everywhere, SearchMode=FindAndReplace, UseRegex=True

### Variables.GenerateDataTableFromCSV のセレクター: ReadCustomSeparator, ReadFixedColumnWidths, ReadPredefinedSeparator

## Variables.GenerateDataTableFromCSV.ReadCustomSeparator [A]
```
Variables.GenerateDataTableFromCSV.ReadCustomSeparator CustomColumnsSeparator: $fx'example' TrimFields: True CSVText: $fx'example' ReadFieldsAsText: False FirstLineContainsColumnNames: False CSVTable=> CSVTable
```
入力: !CustomColumnsSeparator:String !TrimFields:Boolean !CSVText:String !ReadFieldsAsText:Boolean !FirstLineContainsColumnNames:Boolean
出力: CSVTable:DataTable=>CSVTable
ON ERROR可: ReadFromCSVError
固定: ColumnsSeparatorType=Custom

## Variables.GenerateDataTableFromCSV.ReadFixedColumnWidths [A]
```
Variables.GenerateDataTableFromCSV.ReadFixedColumnWidths FixedColumnWidths: $fx'example' TrimFields: True CSVText: $fx'example' ReadFieldsAsText: False FirstLineContainsColumnNames: False CSVTable=> CSVTable
```
入力: !FixedColumnWidths:String !TrimFields:Boolean !CSVText:String !ReadFieldsAsText:Boolean !FirstLineContainsColumnNames:Boolean
出力: CSVTable:DataTable=>CSVTable
ON ERROR可: ReadFromCSVError
固定: ColumnsSeparatorType=FixedColumnWidths

## Variables.GenerateDataTableFromCSV.ReadPredefinedSeparator [A]
```
Variables.GenerateDataTableFromCSV.ReadPredefinedSeparator CSVText: $fx'example' TrimFields: True FirstLineContainsColumnNames: False ReadFieldsAsText: False ColumnsSeparator: Variables.CSVColumnsSeparator.SystemDefault CSVTable=> CSVTable
```
入力: CSVText:String TrimFields:Boolean FirstLineContainsColumnNames:Boolean ReadFieldsAsText:Boolean ColumnsSeparator:CSVColumnsSeparator{SystemDefault,Comma,Semicolon,Tab}
出力: CSVTable:DataTable=>
ON ERROR可: ReadFromCSVError
固定: ColumnsSeparatorType=Predefined

### Variables.GenerateRandomNumber のセレクター: ListOfRandomNumbers, RandomNumber

## Variables.GenerateRandomNumber.ListOfRandomNumbers [A]
```
Variables.GenerateRandomNumber.ListOfRandomNumbers MinimumValue: 0 NumbersCount: 10 MaximumValue: 100 AllowDuplicates: False RandomNumbers=> RandomNumbers
```
入力: !MinimumValue:Int32 !NumbersCount:Int32 !MaximumValue:Int32 !AllowDuplicates:Boolean
出力: RandomNumbers:List<Decimal>=>RandomNumbers
ON ERROR可: GenerateRandomNumberError
固定: GenerateMultipleNumbers=True

## Variables.GenerateRandomNumber.RandomNumber [A]
```
Variables.GenerateRandomNumber.RandomNumber MinimumValue: 0 MaximumValue: 100 RandomNumber=> RandomNumber
```
入力: MaximumValue:Int32 MinimumValue:Int32
出力: RandomNumber:Decimal=>
ON ERROR可: GenerateRandomNumberError
固定: GenerateMultipleNumbers=False

## Variables.IncreaseVariable [A]
```
Variables.IncreaseVariable Value: MyVar IncrementValue: 1
```
入力: IncrementValue:Decimal Value:Decimal
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.JoinDataTable [A]
```
Variables.JoinDataTable FirstDataTable: DataTable SecondDataTable: DataTable JoinOperation: Variables.JoinOperationType.Inner JoinParameters: DataTable JoinedDataTable=> JoinedDataTable
```
入力: FirstDataTable:DataTable SecondDataTable:DataTable JoinOperation:JoinOperationType{Inner,Left,Full} JoinParameters:DataTable
出力: JoinedDataTable:DataTable=>
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError

## Variables.MergeDataTables [A]
```
Variables.MergeDataTables FirstDataTable: DataTable SecondDataTable: DataTable MergeMode: Variables.MergeMode.AddExtraColumns
```
入力: FirstDataTable:DataTable SecondDataTable:DataTable MergeMode:MergeMode{AddExtraColumns,IgnoreExtraColumns,ErrorOnExtraColumns}
ON ERROR可: MissingSchemaError

## Variables.MergeLists [A]
```
Variables.MergeLists FirstList: FileList SecondList: FileList OutputList=> OutputList
```
入力: FirstList:List SecondList:List
出力: OutputList:List=>
ON ERROR可: IncompatibleTypesListsError

## Variables.ModifyDataTableItem [A]
```
Variables.ModifyDataTableItem DataTable: DataTable ColumnNameOrIndex: $fx'example' RowIndex: 1 Value: $fx'sample'
```
入力: DataTable:DataTable ColumnNameOrIndex:String RowIndex:Int32 Value:Object
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, IncompatibleTypeError, IndexOutOfRangeError

## Variables.RemoveDuplicateItemsFromList [A]
```
Variables.RemoveDuplicateItemsFromList List: FileList IgnoreCase: False
```
入力: IgnoreCase:Boolean List:List
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.RemoveItemFromList のセレクター: RemoveItemFromListByIndex, RemoveItemFromListByValue

## Variables.RemoveItemFromList.RemoveItemFromListByIndex [A]
```
Variables.RemoveItemFromList.RemoveItemFromListByIndex ItemIndex: 1 List: FileList
```
入力: ItemIndex:Int32 List:List
ON ERROR可: IndexOutOfRangeError, ItemNotFoundError
固定: Mode=ByIndex

## Variables.RemoveItemFromList.RemoveItemFromListByValue [A]
```
Variables.RemoveItemFromList.RemoveItemFromListByValue List: List ItemMatchAllOccurrences: False Item: $fx'sample'
```
入力: !List:List<Object> !ItemMatchAllOccurrences:Boolean !Item:Object
ON ERROR可: IndexOutOfRangeError, ItemNotFoundError
固定: Mode=ByValue

## Variables.RetrieveDataTableColumnIntoList [A]
```
Variables.RetrieveDataTableColumnIntoList DataTable: DataTable ColumnNameOrIndex: $fx'example' ColumnAsList=> ColumnAsList
```
入力: ColumnNameOrIndex:String DataTable:DataTable
出力: ColumnAsList:List=>
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError

## Variables.ReverseList [A]
```
Variables.ReverseList List: FileList
```
入力: List:List
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Variables.ShuffleList [A]
```
Variables.ShuffleList List: FileList
```
入力: List:List
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.SortDataTable のセレクター: SortWithColumnIndex, SortWithColumnName

## Variables.SortDataTable.SortWithColumnIndex [A]
```
Variables.SortDataTable.SortWithColumnIndex ColumnIndex: 1 Order: Variables.SortDirection.Ascending DataTable: RecognizedEntities
```
入力: !ColumnIndex:Int32 !Order:SortDirection{Ascending,Descending} !DataTable:DataTable
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, ColumnTypeMismatchError
固定: ColumnSpecifier=Index

## Variables.SortDataTable.SortWithColumnName [A]
```
Variables.SortDataTable.SortWithColumnName DataTable: DataTable ColumnName: $fx'example' Order: Variables.SortDirection.Ascending
```
入力: DataTable:DataTable ColumnName:String Order:SortDirection{Ascending,Descending}
ON ERROR可: ColumnIndexOutOfRangeError, ColumnNameNotFoundError, ColumnTypeMismatchError
固定: ColumnSpecifier=Name

### Variables.SortList のセレクター: SortList, SortListByProperty

## Variables.SortList.SortList [A]
```
Variables.SortList.SortList List: List
```
入力: !List:List<Object>
ON ERROR可: NoPropertySpecifiedError
固定: SortByProperty=False

## Variables.SortList.SortListByProperty [A]
```
Variables.SortList.SortListByProperty SortDirection1: Variables.SortDirection.Ascending SortDirection3: Variables.SortDirection.Ascending SortDirection2: Variables.SortDirection.Ascending Property1: $fx'example' List: List Property3: $fx'example' Property2: $fx'example'
```
入力: !SortDirection1:SortDirection{Ascending,Descending} !SortDirection3:SortDirection{Ascending,Descending} !SortDirection2:SortDirection{Ascending,Descending} Property1:String !List:List<Object> Property3:String Property2:String
ON ERROR可: NoPropertySpecifiedError
固定: SortByProperty=True

## Variables.SubtractLists [A]
```
Variables.SubtractLists FirstList: FileList SecondList: FileList OutputList=> ListDifference
```
入力: FirstList:List SecondList:List
出力: OutputList:List=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Variables.TruncateNumber のセレクター: GetDecimalPart, GetIntegerPart, RoundNumber

## Variables.TruncateNumber.GetDecimalPart [A]
```
Variables.TruncateNumber.GetDecimalPart Number: 1.0 Result=> TruncatedValue
```
入力: !Number:Decimal
出力: Result:Decimal=>TruncatedValue
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Operation=GetDecimalPart

## Variables.TruncateNumber.GetIntegerPart [A]
```
Variables.TruncateNumber.GetIntegerPart Number: 1.0 Result=> TruncatedValue
```
入力: Number:Decimal
出力: Result:Decimal=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Operation=GetIntegerPart

## Variables.TruncateNumber.RoundNumber [A]
```
Variables.TruncateNumber.RoundNumber Number: 1.0 DecimalPlaces: 3 Result=> TruncatedValue
```
入力: !Number:Decimal !DecimalPlaces:Int32
出力: Result:Decimal=>TruncatedValue
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Operation=RoundAtNthDecimalDigits
