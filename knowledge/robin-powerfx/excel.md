# Robin: Excel

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Excel.ActivateCellInExcel のセレクター: ActivateCell, ActivateCellRelativeTo, ActivateNamedCell

## Excel.ActivateCellInExcel.ActivateCell [A]
```
Excel.ActivateCellInExcel.ActivateCell Instance: ExcelInstance Column: $fx'example' Row: 1
```
入力: Column:String Instance:ExcelInstanceHandle Row:Int32
ON ERROR可: ActivateExcelCellError
固定: SpecifyCellsMode=Absolute

## Excel.ActivateCellInExcel.ActivateCellRelativeTo [A]
```
Excel.ActivateCellInExcel.ActivateCellRelativeTo OffsetFromActiveCell: 1 Direction: Excel.TwoDimensionalDirection.Left Instance: ExcelInstance
```
入力: !OffsetFromActiveCell:Int32 !Direction:TwoDimensionalDirection{Left,Right,Above,Below} !Instance:ExcelInstanceHandle
ON ERROR可: ActivateExcelCellError
固定: SpecifyCellsMode=Relative

## Excel.ActivateCellInExcel.ActivateNamedCell [A]
```
Excel.ActivateCellInExcel.ActivateNamedCell CellName: $fx'example' Instance: ExcelInstance
```
入力: !CellName:String !Instance:ExcelInstanceHandle
ON ERROR可: ActivateExcelCellError
固定: SpecifyCellsMode=NamedCells

## Excel.AddWorksheet [A]
```
Excel.AddWorksheet Instance: ExcelInstance Name: $fx'example' WorksheetPosition: Excel.WorksheetPosition.First
```
入力: Instance:ExcelInstanceHandle Name:String WorksheetPosition:WorksheetPosition{First,Last}
ON ERROR可: AddWorksheetError, WorksheetAlreadyExistsError

### Excel.AppendCells のセレクター: AppendCellsActiveSheetColumn, AppendCellsActiveSheetHeader, AppendCellsNamedCellColumn, AppendCellsNamedCellHeader

## Excel.AppendCells.AppendCellsActiveSheetColumn [A]
```
Excel.AppendCells.AppendCellsActiveSheetColumn Instance: ExcelInstance ColumnName: $fx'example'
```
入力: ColumnName:String Instance:ExcelInstanceHandle
ON ERROR可: AppendCellsError
固定: Mode=ActiveSheet, HasHeaders=False

## Excel.AppendCells.AppendCellsActiveSheetHeader [A]
```
Excel.AppendCells.AppendCellsActiveSheetHeader Instance: ExcelInstance HeaderName: $fx'example'
```
入力: !Instance:ExcelInstanceHandle HeaderName:String
ON ERROR可: AppendCellsError
固定: Mode=ActiveSheet, HasHeaders=True

## Excel.AppendCells.AppendCellsNamedCellColumn [A]
```
Excel.AppendCells.AppendCellsNamedCellColumn Instance: ExcelInstance CellName: $fx'example' ColumnName: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !CellName:String ColumnName:String
ON ERROR可: AppendCellsError
固定: Mode=NamedCell, HasHeaders=False

## Excel.AppendCells.AppendCellsNamedCellHeader [A]
```
Excel.AppendCells.AppendCellsNamedCellHeader Instance: ExcelInstance CellName: $fx'example' HeaderName: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !CellName:String HeaderName:String
ON ERROR可: AppendCellsError
固定: Mode=NamedCell, HasHeaders=True

## Excel.Attach [A]
```
Excel.Attach DocumentName: $fx'C:\temp\test.xlsx' Instance=> ExcelInstance
```
入力: DocumentName:FileObject
出力: Instance:ExcelInstanceHandle=>
ON ERROR可: AttachToExcelError, DocumentNotFoundError

### Excel.AutoFillCells のセレクター: AutoFillCellsFromCoordinates, AutoFillNamedCells

## Excel.AutoFillCells.AutoFillCellsFromCoordinates [A]
```
Excel.AutoFillCells.AutoFillCellsFromCoordinates Instance: ExcelInstance StartRow: 1 StartColumn: $fx'example' DestinationColumn: $fx'example' DestinationRow: 1 EndRow: 1 EndColumn: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !StartRow:Int32 !StartColumn:String !DestinationColumn:String !DestinationRow:Int32 !EndRow:Int32 !EndColumn:String
ON ERROR可: AutoFillCellsError
固定: Mode=CellCoordinates

## Excel.AutoFillCells.AutoFillNamedCells [A]
```
Excel.AutoFillCells.AutoFillNamedCells Instance: ExcelInstance SourceCellName: $fx'example' DestinationCellName: $fx'example'
```
入力: DestinationCellName:String Instance:ExcelInstanceHandle SourceCellName:String
ON ERROR可: AutoFillCellsError
固定: Mode=NamedCells

### Excel.ClearCellsFromExcel のセレクター: ClearCells, ClearCellsRelativeTo, ClearNamedCell, ClearSingleCell

## Excel.ClearCellsFromExcel.ClearCells [A]
```
Excel.ClearCellsFromExcel.ClearCells Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1 EndColumn: $fx'example' EndRow: 1
```
入力: Instance:ExcelInstanceHandle StartColumn:String StartRow:Int32 EndColumn:String EndRow:Int32
ON ERROR可: ClearCellsError
固定: SpecifyCellsMode=Absolute

## Excel.ClearCellsFromExcel.ClearCellsRelativeTo [A]
```
Excel.ClearCellsFromExcel.ClearCellsRelativeTo OffsetY: 1 VerticalDirection: Excel.VerticalDirection.Above Instance: ExcelInstance OffsetX: 1 HorizontalDirection: Excel.HorizontalDirection.Left
```
入力: !OffsetY:Int32 !VerticalDirection:VerticalDirection{Above,Below} !Instance:ExcelInstanceHandle !OffsetX:Int32 !HorizontalDirection:HorizontalDirection{Left,Right}
ON ERROR可: ClearCellsError
固定: SpecifyCellsMode=Relative

## Excel.ClearCellsFromExcel.ClearNamedCell [A]
```
Excel.ClearCellsFromExcel.ClearNamedCell CellName: $fx'example' Instance: ExcelInstance
```
入力: !CellName:String !Instance:ExcelInstanceHandle
ON ERROR可: ClearCellsError
固定: SpecifyCellsMode=NamedCells

## Excel.ClearCellsFromExcel.ClearSingleCell [A]
```
Excel.ClearCellsFromExcel.ClearSingleCell SingleCellRow: 1 SingleCellColumn: $fx'example' Instance: ExcelInstance
```
入力: !SingleCellRow:Int32 !SingleCellColumn:String !Instance:ExcelInstanceHandle
ON ERROR可: ClearCellsError
固定: SpecifyCellsMode=SingleCell

### Excel.ClearFilterFromExcel のセレクター: ClearFilterSpecificColumnWorksheet, ClearFilterTable, ClearFilterTableSpecificColumn, ClearFilterWorksheet

## Excel.ClearFilterFromExcel.ClearFilterSpecificColumnWorksheet [A]
```
Excel.ClearFilterFromExcel.ClearFilterSpecificColumnWorksheet Column: $fx'example' Instance: ExcelInstance
```
入力: !Column:String !Instance:ExcelInstanceHandle
ON ERROR可: ClearFilterFromExcel
固定: ClearFilterMode=ActiveSheet, ClearFiltersSpecificColumn=True

## Excel.ClearFilterFromExcel.ClearFilterTable [A]
```
Excel.ClearFilterFromExcel.ClearFilterTable TableName: $fx'example' Instance: ExcelInstance
```
入力: !TableName:String !Instance:ExcelInstanceHandle
ON ERROR可: ClearFilterFromExcel
固定: ClearFilterMode=Table, ClearFiltersSpecificColumn=False

## Excel.ClearFilterFromExcel.ClearFilterTableSpecificColumn [A]
```
Excel.ClearFilterFromExcel.ClearFilterTableSpecificColumn Column: $fx'example' TableName: $fx'example' Instance: ExcelInstance
```
入力: !Column:String !TableName:String !Instance:ExcelInstanceHandle
ON ERROR可: ClearFilterFromExcel
固定: ClearFilterMode=Table, ClearFiltersSpecificColumn=True

## Excel.ClearFilterFromExcel.ClearFilterWorksheet [A]
```
Excel.ClearFilterFromExcel.ClearFilterWorksheet Instance: ExcelInstance
```
入力: Instance:ExcelInstanceHandle
ON ERROR可: ClearFilterFromExcel
固定: ClearFilterMode=ActiveSheet, ClearFiltersSpecificColumn=False

### Excel.CloseExcel のセレクター: Close, CloseAndSave, CloseAndSaveAs

## Excel.CloseExcel.Close [A]
```
Excel.CloseExcel.Close Instance: ExcelInstance
```
入力: Instance:ExcelInstanceHandle
ON ERROR可: CloseExcelError, SaveExcelError
固定: CloseMode=DoNotSave

## Excel.CloseExcel.CloseAndSave [A]
```
Excel.CloseExcel.CloseAndSave Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: CloseExcelError, SaveExcelError
固定: CloseMode=Save

## Excel.CloseExcel.CloseAndSaveAs [A]
```
Excel.CloseExcel.CloseAndSaveAs Instance: ExcelInstance XmlMapName: $fx'example' DocumentPath: $fx'C:\temp\test.xlsx' DocumentFormat: Excel.ExcelFormat.FromExtension
```
入力: !Instance:ExcelInstanceHandle !XmlMapName:String !DocumentPath:FileObject !DocumentFormat:ExcelFormat{FromExtension,OpenXmlWorkbook,OpenXmlWorkbookMacroEnabled,Excel8,WebPage,Template,TemplateMacroEnabled,Template8,Text,UnicodeText,TextMacintosh,TextDOS,XMLSpreadsheet,Excel595,CSV,DIF,SYLK,ExcelAddIn,Excel972003AddIn,StrictOpenXmlWorkbook,OpenDocumentSpreadsheet,XmlData,ExcelBinaryWorkbook}
ON ERROR可: CloseExcelError, SaveExcelError
固定: CloseMode=SaveAs

### Excel.CopyCellsFromExcel のセレクター: Copy, CopyAllCells, CopyCell, CopyCells, CopyNamedCell

## Excel.CopyCellsFromExcel.Copy [A]
```
Excel.CopyCellsFromExcel.Copy Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: CopyCellsError
固定: CopyMode=Selection

## Excel.CopyCellsFromExcel.CopyAllCells [A]
```
Excel.CopyCellsFromExcel.CopyAllCells Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: CopyCellsError
固定: CopyMode=AllCells

## Excel.CopyCellsFromExcel.CopyCell [A]
```
Excel.CopyCellsFromExcel.CopyCell Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1
```
入力: Instance:ExcelInstanceHandle StartColumn:String StartRow:Int32
ON ERROR可: CopyCellsError
固定: CopyMode=SingleCell

## Excel.CopyCellsFromExcel.CopyCells [A]
```
Excel.CopyCellsFromExcel.CopyCells StartColumn: $fx'example' StartRow: 1 Instance: ExcelInstance EndColumn: $fx'example' EndRow: 1
```
入力: !StartColumn:String !StartRow:Int32 !Instance:ExcelInstanceHandle !EndColumn:String !EndRow:Int32
ON ERROR可: CopyCellsError
固定: CopyMode=RangeOfCells

## Excel.CopyCellsFromExcel.CopyNamedCell [A]
```
Excel.CopyCellsFromExcel.CopyNamedCell CellName: $fx'example' Instance: ExcelInstance
```
入力: !CellName:String !Instance:ExcelInstanceHandle
ON ERROR可: CopyCellsError
固定: CopyMode=NamedCells

### Excel.CopyExcelWorksheet のセレクター: CopyWorksheetWithIndex, CopyWorksheetWithName

## Excel.CopyExcelWorksheet.CopyWorksheetWithIndex [A]
```
Excel.CopyExcelWorksheet.CopyWorksheetWithIndex TargetInstance: ExcelInstance TargetWorksheetName: $fx'example' PasteWorksheetPosition: Excel.WorksheetPosition.First SourceInstance: ExcelInstance SourceWorksheetIndex: 1
```
入力: !TargetInstance:ExcelInstanceHandle !TargetWorksheetName:String !PasteWorksheetPosition:WorksheetPosition{First,Last} !SourceInstance:ExcelInstanceHandle !SourceWorksheetIndex:Int32
ON ERROR可: CopyExcelWorksheetError, CopyExcelWorksheetSetNameError
固定: FindWorksheetMode=Index

## Excel.CopyExcelWorksheet.CopyWorksheetWithName [A]
```
Excel.CopyExcelWorksheet.CopyWorksheetWithName SourceInstance: ExcelInstance SourceWorksheetName: $fx'example' TargetInstance: ExcelInstance TargetWorksheetName: $fx'example' PasteWorksheetPosition: Excel.WorksheetPosition.First
```
入力: SourceInstance:ExcelInstanceHandle SourceWorksheetName:String TargetInstance:ExcelInstanceHandle TargetWorksheetName:String PasteWorksheetPosition:WorksheetPosition{First,Last}
ON ERROR可: CopyExcelWorksheetError, CopyExcelWorksheetSetNameError
固定: FindWorksheetMode=Name

### Excel.DeleteCells のセレクター: DeleteCell, DeleteCells

## Excel.DeleteCells.DeleteCell [A]
```
Excel.DeleteCells.DeleteCell Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1 ShiftCellsDirection: Excel.ShiftCellsDirection.Left
```
入力: Instance:ExcelInstanceHandle StartColumn:String StartRow:Int32 ShiftCellsDirection:ShiftCellsDirection{Left,Up}
ON ERROR可: DeleteCellsError
固定: DeleteCellsMode=SingleCell

## Excel.DeleteCells.DeleteCells [A]
```
Excel.DeleteCells.DeleteCells EndColumn: $fx'example' EndRow: 1 ShiftCellsDirection: Excel.ShiftCellsDirection.Left StartRow: 1 Instance: ExcelInstance StartColumn: $fx'example'
```
入力: !EndColumn:String !EndRow:Int32 !ShiftCellsDirection:ShiftCellsDirection{Left,Up} !StartRow:Int32 !Instance:ExcelInstanceHandle !StartColumn:String
ON ERROR可: DeleteCellsError
固定: DeleteCellsMode=RangeOfCells

## Excel.DeleteColumn [A]
```
Excel.DeleteColumn Instance: ExcelInstance Column: $fx'example'
```
入力: Column:String Instance:ExcelInstanceHandle
ON ERROR可: ColumnNotFoundError, DeleteColumnError

## Excel.DeleteRow [A]
```
Excel.DeleteRow Instance: ExcelInstance Index: 1
```
入力: Index:Int32 Instance:ExcelInstanceHandle
ON ERROR可: DeleteRowError, RowNotFoundError

### Excel.DeleteWorksheet のセレクター: DeleteWorksheetByIndex, DeleteWorksheetByName

## Excel.DeleteWorksheet.DeleteWorksheetByIndex [A]
```
Excel.DeleteWorksheet.DeleteWorksheetByIndex Instance: ExcelInstance Index: 1
```
入力: !Instance:ExcelInstanceHandle !Index:Int32
ON ERROR可: DeleteWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Index

## Excel.DeleteWorksheet.DeleteWorksheetByName [A]
```
Excel.DeleteWorksheet.DeleteWorksheetByName Instance: ExcelInstance Name: $fx'example'
```
入力: Instance:ExcelInstanceHandle Name:String
ON ERROR可: DeleteWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Name

### Excel.FilterCellsFromExcel のセレクター: FilterAdvancedRangeCoordinates, FilterAdvancedRangeNamedCell, FilterAdvancedTable, FilterAdvancedWorksheet, FilterSimpleRangeCoordinates, FilterSimpleRangeNamedCell, FilterSimpleTable, FilterSimpleWorksheet

## Excel.FilterCellsFromExcel.FilterAdvancedRangeCoordinates [A]
```
Excel.FilterCellsFromExcel.FilterAdvancedRangeCoordinates AdvancedFilterFirstConditionValue: $fx'example' AdvancedFilterSecondConditionOperator: Excel.FilterConditionOperator.None EndRow: 1 AdvancedFilterFirstConditionOperator: Excel.FilterConditionOperator.Equal AdvancedFilterSecondConditionValue: $fx'example' AdvancedFilterLogicalOperator: Excel.FilterLogicalOperator.IsOr EndColumn: $fx'example' Instance: ExcelInstance Column: $fx'example' StartColumn: $fx'example' StartRow: 1
```
入力: !AdvancedFilterFirstConditionValue:String !AdvancedFilterSecondConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !EndRow:Int32 !AdvancedFilterFirstConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterSecondConditionValue:String !AdvancedFilterLogicalOperator:FilterLogicalOperator{IsOr,IsAnd} !EndColumn:String !Instance:ExcelInstanceHandle !Column:String !StartColumn:String !StartRow:Int32
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Range, FilterRangeMode=Coordinates, IsAdvancedFilter=True

## Excel.FilterCellsFromExcel.FilterAdvancedRangeNamedCell [A]
```
Excel.FilterCellsFromExcel.FilterAdvancedRangeNamedCell AdvancedFilterFirstConditionValue: $fx'example' AdvancedFilterSecondConditionOperator: Excel.FilterConditionOperator.None AdvancedFilterFirstConditionOperator: Excel.FilterConditionOperator.Equal AdvancedFilterSecondConditionValue: $fx'example' AdvancedFilterLogicalOperator: Excel.FilterLogicalOperator.IsOr Instance: ExcelInstance Column: $fx'example' NamedCell: $fx'example'
```
入力: !AdvancedFilterFirstConditionValue:String !AdvancedFilterSecondConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterFirstConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterSecondConditionValue:String !AdvancedFilterLogicalOperator:FilterLogicalOperator{IsOr,IsAnd} !Instance:ExcelInstanceHandle !Column:String !NamedCell:String
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Range, FilterRangeMode=NamedCell, IsAdvancedFilter=True

## Excel.FilterCellsFromExcel.FilterAdvancedTable [A]
```
Excel.FilterCellsFromExcel.FilterAdvancedTable AdvancedFilterFirstConditionValue: $fx'example' AdvancedFilterSecondConditionOperator: Excel.FilterConditionOperator.None AdvancedFilterFirstConditionOperator: Excel.FilterConditionOperator.Equal AdvancedFilterSecondConditionValue: $fx'example' AdvancedFilterLogicalOperator: Excel.FilterLogicalOperator.IsOr Instance: ExcelInstance Column: $fx'example' TableName: $fx'example'
```
入力: !AdvancedFilterFirstConditionValue:String !AdvancedFilterSecondConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterFirstConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterSecondConditionValue:String !AdvancedFilterLogicalOperator:FilterLogicalOperator{IsOr,IsAnd} !Instance:ExcelInstanceHandle !Column:String !TableName:String
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Table, IsAdvancedFilter=True

## Excel.FilterCellsFromExcel.FilterAdvancedWorksheet [A]
```
Excel.FilterCellsFromExcel.FilterAdvancedWorksheet AdvancedFilterFirstConditionValue: $fx'example' AdvancedFilterSecondConditionOperator: Excel.FilterConditionOperator.None AdvancedFilterFirstConditionOperator: Excel.FilterConditionOperator.Equal AdvancedFilterSecondConditionValue: $fx'example' AdvancedFilterLogicalOperator: Excel.FilterLogicalOperator.IsOr Instance: ExcelInstance Column: $fx'example'
```
入力: !AdvancedFilterFirstConditionValue:String !AdvancedFilterSecondConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterFirstConditionOperator:FilterConditionOperator{None,Equal,GreaterThan,GreaterThanOrEqual,LessThan,LessThanOrEqual,NotEqual,IsEmpty,IsNotEmpty,StartsWith,EndsWith,Contains,NotStartsWith,NotEndsWith,NotContains} !AdvancedFilterSecondConditionValue:String !AdvancedFilterLogicalOperator:FilterLogicalOperator{IsOr,IsAnd} !Instance:ExcelInstanceHandle !Column:String
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=ActiveSheet, IsAdvancedFilter=True

## Excel.FilterCellsFromExcel.FilterSimpleRangeCoordinates [A]
```
Excel.FilterCellsFromExcel.FilterSimpleRangeCoordinates EndRow: 1 SimpleFilterValues: List EndColumn: $fx'example' Instance: ExcelInstance Column: $fx'example' StartColumn: $fx'example' StartRow: 1
```
入力: !EndRow:Int32 !SimpleFilterValues:List<String> !EndColumn:String !Instance:ExcelInstanceHandle !Column:String !StartColumn:String !StartRow:Int32
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Range, FilterRangeMode=Coordinates, IsAdvancedFilter=False

## Excel.FilterCellsFromExcel.FilterSimpleRangeNamedCell [A]
```
Excel.FilterCellsFromExcel.FilterSimpleRangeNamedCell SimpleFilterValues: List Instance: ExcelInstance Column: $fx'example' NamedCell: $fx'example'
```
入力: !SimpleFilterValues:List<String> !Instance:ExcelInstanceHandle !Column:String !NamedCell:String
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Range, FilterRangeMode=NamedCell, IsAdvancedFilter=False

## Excel.FilterCellsFromExcel.FilterSimpleTable [A]
```
Excel.FilterCellsFromExcel.FilterSimpleTable SimpleFilterValues: List Instance: ExcelInstance Column: $fx'example' TableName: $fx'example'
```
入力: !SimpleFilterValues:List<String> !Instance:ExcelInstanceHandle !Column:String !TableName:String
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=Table, IsAdvancedFilter=False

## Excel.FilterCellsFromExcel.FilterSimpleWorksheet [A]
```
Excel.FilterCellsFromExcel.FilterSimpleWorksheet Instance: ExcelInstance Column: $fx'example' SimpleFilterValues: $fx'=[]'
```
入力: Instance:ExcelInstanceHandle Column:String SimpleFilterValues:List
ON ERROR可: FilterCellsFromExcel
固定: FilterMode=ActiveSheet, IsAdvancedFilter=False

### Excel.FindAndReplace のセレクター: FindAll, FindAndReplaceAll, FindAndReplaceSingle, FindSingle

## Excel.FindAndReplace.FindAll [A]
```
Excel.FindAndReplace.FindAll SearchBy: Excel.SearchOrder.Rows TextToFind: $fx'example' Instance: ExcelInstance MatchEntireCellContents: False MatchCase: False Cells=> Cells
```
入力: !SearchBy:SearchOrder{Rows,Columns} !TextToFind:String !Instance:ExcelInstanceHandle !MatchEntireCellContents:Boolean !MatchCase:Boolean
出力: Cells:DataTable=>Cells
ON ERROR可: FindAndReplaceError
固定: Mode=Find, AllMatches=True

## Excel.FindAndReplace.FindAndReplaceAll [A]
```
Excel.FindAndReplace.FindAndReplaceAll SearchBy: Excel.SearchOrder.Rows TextToReplaceWith: $fx'example' TextToFind: $fx'example' Instance: ExcelInstance MatchEntireCellContents: False MatchCase: False Cells=> Cells
```
入力: !SearchBy:SearchOrder{Rows,Columns} !TextToReplaceWith:String !TextToFind:String !Instance:ExcelInstanceHandle !MatchEntireCellContents:Boolean !MatchCase:Boolean
出力: Cells:DataTable=>Cells
ON ERROR可: FindAndReplaceError
固定: Mode=FindAndReplace, AllMatches=True

## Excel.FindAndReplace.FindAndReplaceSingle [A]
```
Excel.FindAndReplace.FindAndReplaceSingle SearchBy: Excel.SearchOrder.Rows TextToReplaceWith: $fx'example' TextToFind: $fx'example' Instance: ExcelInstance MatchEntireCellContents: False MatchCase: False FoundRowIndex=> FoundRowIndex FoundColumnIndex=> FoundColumnIndex
```
入力: !SearchBy:SearchOrder{Rows,Columns} !TextToReplaceWith:String !TextToFind:String !Instance:ExcelInstanceHandle !MatchEntireCellContents:Boolean !MatchCase:Boolean
出力: FoundRowIndex:Int32=>FoundRowIndex FoundColumnIndex:Int32=>FoundColumnIndex
ON ERROR可: FindAndReplaceError
固定: Mode=FindAndReplace, AllMatches=False

## Excel.FindAndReplace.FindSingle [A]
```
Excel.FindAndReplace.FindSingle Instance: ExcelInstance TextToFind: $fx'example' MatchCase: False MatchEntireCellContents: False SearchBy: Excel.SearchOrder.Rows FoundColumnIndex=> FoundColumnIndex FoundRowIndex=> FoundRowIndex
```
入力: Instance:ExcelInstanceHandle MatchCase:Boolean MatchEntireCellContents:Boolean SearchBy:SearchOrder{Rows,Columns} TextToFind:String
出力: FoundColumnIndex:Int32=> FoundRowIndex:Int32=>
ON ERROR可: FindAndReplaceError
固定: Mode=Find, AllMatches=False

## Excel.GetActiveCell [A]
```
Excel.GetActiveCell Instance: ExcelInstance ActiveCellColumnIndex=> ActiveCellColumnIndex ActiveCellRowIndex=> ActiveCellRowIndex
```
入力: Instance:ExcelInstanceHandle
出力: ActiveCellColumnIndex:Int32=> ActiveCellRowIndex:Int32=>
ON ERROR可: GetActiveCellError

## Excel.GetActiveWorksheet [A]
```
Excel.GetActiveWorksheet Instance: ExcelInstance Name=> SheetName Index=> SheetIndex
```
入力: Instance:ExcelInstanceHandle
出力: Index:Int32=> Name:String=>
ON ERROR可: RetrieveActiveWorksheetError

## Excel.GetAllWorksheets [A]
```
Excel.GetAllWorksheets Instance: ExcelInstance Worksheets=> SheetNames
```
入力: Instance:ExcelInstanceHandle
出力: Worksheets:List=>
ON ERROR可: RetrieveAllWorksheetsError

## Excel.GetColumnName [A]
```
Excel.GetColumnName CellColumnIndex: 1 ColumnName=> ColumnName
```
入力: CellColumnIndex:Int32
出力: ColumnName:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Excel.GetEmptyCellFromExcel のセレクター: GetEmptyCellsAbsoluteRangeAllEmptyCells, GetEmptyCellsAbsoluteRangeFirstEmptyCell, GetEmptyCellsAbsoluteRangeFirstEmptyCellInColumn, GetEmptyCellsAbsoluteRangeFirstEmptyCellInRow, GetEmptyCellsNamedCellAllEmptyCells, GetEmptyCellsNamedCellFirstEmptyCell, GetEmptyCellsNamedCellFirstEmptyCellInColumn, GetEmptyCellsNamedCellFirstEmptyCellInRow

## Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeAllEmptyCells [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeAllEmptyCells StartColumn: $fx'example' StartRow: 1 EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance EmptyCells=> EmptyCells
```
入力: !StartColumn:String !StartRow:Int32 !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle
出力: EmptyCells:DataTable=>EmptyCells
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=Coordinates, EmptyCellsOperation=AllEmptyCells

## Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCell [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCell StartColumn: $fx'example' StartRow: 1 EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance EmptyCellsSearchDirection: Excel.EmptyCellsSearchDirection.Rows EmptyCellRowIndex=> EmptyCellRowIndex EmptyCellColumnIndex=> EmptyCellColumnIndex
```
入力: !StartColumn:String !StartRow:Int32 !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle !EmptyCellsSearchDirection:EmptyCellsSearchDirection{Rows,Columns}
出力: EmptyCellRowIndex:Int32=>EmptyCellRowIndex EmptyCellColumnIndex:Int32=>EmptyCellColumnIndex
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=Coordinates, EmptyCellsOperation=FirstEmptyCell

## Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCellInColumn [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCellInColumn StartColumn: $fx'example' StartRow: 1 EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance SearchColumn: $fx'example' EmptyCellRowIndex=> EmptyCellRowIndex EmptyCellColumnIndex=> EmptyCellColumnIndex
```
入力: !StartColumn:String !StartRow:Int32 !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle !SearchColumn:String
出力: EmptyCellRowIndex:Int32=>EmptyCellRowIndex EmptyCellColumnIndex:Int32=>EmptyCellColumnIndex
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=Coordinates, EmptyCellsOperation=FirstEmptyCellInColumn

## Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCellInRow [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsAbsoluteRangeFirstEmptyCellInRow StartColumn: $fx'example' StartRow: 1 EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance SearchRow: 1 EmptyCellRowIndex=> EmptyCellRowIndex EmptyCellColumnIndex=> EmptyCellColumnIndex
```
入力: !StartColumn:String !StartRow:Int32 !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle !SearchRow:Int32
出力: EmptyCellRowIndex:Int32=>EmptyCellRowIndex EmptyCellColumnIndex:Int32=>EmptyCellColumnIndex
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=Coordinates, EmptyCellsOperation=FirstEmptyCellInRow

## Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellAllEmptyCells [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellAllEmptyCells NamedCell: $fx'example' Instance: ExcelInstance EmptyCells=> EmptyCells
```
入力: !NamedCell:String !Instance:ExcelInstanceHandle
出力: EmptyCells:DataTable=>EmptyCells
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=NamedCell, EmptyCellsOperation=AllEmptyCells

## Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCell [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCell Instance: ExcelInstance EmptyCellsSearchDirection: Excel.EmptyCellsSearchDirection.Rows NamedCell: $fx'example' EmptyCellColumnIndex=> EmptyCellColumnIndex EmptyCellRowIndex=> EmptyCellRowIndex
```
入力: Instance:ExcelInstanceHandle EmptyCellsSearchDirection:EmptyCellsSearchDirection{Rows,Columns} NamedCell:String
出力: EmptyCellColumnIndex:Int32=> EmptyCellRowIndex:Int32=>
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=NamedCell, EmptyCellsOperation=FirstEmptyCell

## Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCellInColumn [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCellInColumn NamedCell: $fx'example' Instance: ExcelInstance SearchColumn: $fx'example' EmptyCellRowIndex=> EmptyCellRowIndex EmptyCellColumnIndex=> EmptyCellColumnIndex
```
入力: !NamedCell:String !Instance:ExcelInstanceHandle !SearchColumn:String
出力: EmptyCellRowIndex:Int32=>EmptyCellRowIndex EmptyCellColumnIndex:Int32=>EmptyCellColumnIndex
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=NamedCell, EmptyCellsOperation=FirstEmptyCellInColumn

## Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCellInRow [A]
```
Excel.GetEmptyCellFromExcel.GetEmptyCellsNamedCellFirstEmptyCellInRow NamedCell: $fx'example' Instance: ExcelInstance SearchRow: 1 EmptyCellRowIndex=> EmptyCellRowIndex EmptyCellColumnIndex=> EmptyCellColumnIndex
```
入力: !NamedCell:String !Instance:ExcelInstanceHandle !SearchRow:Int32
出力: EmptyCellRowIndex:Int32=>EmptyCellRowIndex EmptyCellColumnIndex:Int32=>EmptyCellColumnIndex
ON ERROR可: GetEmptyCells
固定: GetEmptyCellsRangeMode=NamedCell, EmptyCellsOperation=FirstEmptyCellInRow

## Excel.GetFirstFreeColumnRow [A]
```
Excel.GetFirstFreeColumnRow Instance: ExcelInstance FirstFreeColumn=> FirstFreeColumn FirstFreeRow=> FirstFreeRow
```
入力: Instance:ExcelInstanceHandle
出力: FirstFreeColumn:Int32=> FirstFreeRow:Int32=>
ON ERROR可: RetrieveFirstFreeColumnRowError

## Excel.GetFirstFreeRowOnColumn [A]
```
Excel.GetFirstFreeRowOnColumn Instance: ExcelInstance Column: $fx'example' FirstFreeRowOnColumn=> FirstFreeRowOnColumn
```
入力: Column:String Instance:ExcelInstanceHandle
出力: FirstFreeRowOnColumn:Int32=>
ON ERROR可: RetrieveFirstFreeRowError

## Excel.GetSelectedCellRange [A]
```
Excel.GetSelectedCellRange Instance: ExcelInstance FirstColumnIndex=> FirstColumnIndex FirstRowIndex=> FirstRowIndex LastColumnIndex=> LastColumnIndex LastRowIndex=> LastRowIndex
```
入力: Instance:ExcelInstanceHandle
出力: FirstColumnIndex:Int32=> FirstRowIndex:Int32=> LastColumnIndex:Int32=> LastRowIndex:Int32=>
ON ERROR可: RetrieveSelectedCellsRangeError

## Excel.GetTableRange [A]
```
Excel.GetTableRange Instance: ExcelInstance TableName: $fx'example' IsPivot: False FirstColumnIndex=> FirstColumnIndex FirstRowIndex=> FirstRowIndex LastColumnIndex=> LastColumnIndex LastRowIndex=> LastRowIndex
```
入力: Instance:ExcelInstanceHandle IsPivot:Boolean TableName:String
出力: FirstColumnIndex:Int32=> FirstRowIndex:Int32=> LastColumnIndex:Int32=> LastRowIndex:Int32=>
ON ERROR可: GetTableRangeError

## Excel.InsertColumn [A]
```
Excel.InsertColumn Instance: ExcelInstance Column: $fx'example'
```
入力: Column:String Instance:ExcelInstanceHandle
ON ERROR可: ColumnNotFoundError, InsertColumnError

## Excel.InsertRow [A]
```
Excel.InsertRow Instance: ExcelInstance Index: 1
```
入力: Index:Int32 Instance:ExcelInstanceHandle
ON ERROR可: InsertRowError, RowNotFoundError

### Excel.LaunchExcel のセレクター: Launch, LaunchAndOpen, LaunchAndOpenUnderExistingProcess, LaunchUnderExistingProcess

## Excel.LaunchExcel.Launch [A]
```
Excel.LaunchExcel.Launch UseMachineLocale: False Visible: True LoadAddInsAndMacros: False Instance=> ExcelInstance
```
入力: !UseMachineLocale:Boolean !Visible:Boolean !LoadAddInsAndMacros:Boolean
出力: Instance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: LaunchExcelError, OpenDocumentError
固定: LaunchExcelMode=NewDocument, LaunchInNewInstance=True

## Excel.LaunchExcel.LaunchAndOpen [A]
```
Excel.LaunchExcel.LaunchAndOpen Path: $fx'C:\temp\test.xlsx' Visible: True ReadOnly: False LoadAddInsAndMacros: False Instance=> ExcelInstance
```
入力: LoadAddInsAndMacros:Boolean Path:FileObject ReadOnly:Boolean Visible:Boolean !UseMachineLocale:Boolean WriteProtectionPassword:EncryptableObject ReadProtectionPassword:EncryptableObject
出力: Instance:ExcelInstanceHandle=>
ON ERROR可: LaunchExcelError, OpenDocumentError
固定: LaunchExcelMode=StoredDocument, LaunchInNewInstance=True

## Excel.LaunchExcel.LaunchAndOpenUnderExistingProcess [A]
```
Excel.LaunchExcel.LaunchAndOpenUnderExistingProcess Path: $fx'C:\temp\test.xlsx' UseMachineLocale: False Visible: True ReadOnly: False WriteProtectionPassword: $fx'password' ReadProtectionPassword: $fx'password' Instance=> ExcelInstance
```
入力: !Path:FileObject !UseMachineLocale:Boolean !Visible:Boolean !ReadOnly:Boolean WriteProtectionPassword:EncryptableObject ReadProtectionPassword:EncryptableObject
出力: Instance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: LaunchExcelError, OpenDocumentError
固定: LaunchExcelMode=StoredDocument, LaunchInNewInstance=False

## Excel.LaunchExcel.LaunchUnderExistingProcess [A]
```
Excel.LaunchExcel.LaunchUnderExistingProcess UseMachineLocale: False Visible: True Instance=> ExcelInstance
```
入力: !UseMachineLocale:Boolean !Visible:Boolean
出力: Instance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: LaunchExcelError, OpenDocumentError
固定: LaunchExcelMode=NewDocument, LaunchInNewInstance=False

### Excel.LookupRange のセレクター: LookupRangeCoordinatesArray, LookupRangeCoordinatesNonArray, LookupRangeNamedCellArray, LookupRangeNamedCellNonArray

## Excel.LookupRange.LookupRangeCoordinatesArray [A]
```
Excel.LookupRange.LookupRangeCoordinatesArray StartRow: 1 StartColumn: $fx'example' EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance LookupValue: $fx'sample' Result=> LookupResult
```
入力: !StartRow:Int32 !StartColumn:String !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle !LookupValue:Object
出力: Result:Object=>LookupResult
ON ERROR可: LookupRangeError
固定: Mode=CellCoordinates, IsArrayForm=True

## Excel.LookupRange.LookupRangeCoordinatesNonArray [A]
```
Excel.LookupRange.LookupRangeCoordinatesNonArray StartRow: 1 StartColumn: $fx'example' ValuesEndColumn: $fx'example' ValuesStartRow: 1 ValuesStartColumn: $fx'example' ValuesEndRow: 1 EndRow: 1 EndColumn: $fx'example' Instance: ExcelInstance LookupValue: $fx'sample' Result=> LookupResult
```
入力: !StartRow:Int32 !StartColumn:String !ValuesEndColumn:String !ValuesStartRow:Int32 !ValuesStartColumn:String !ValuesEndRow:Int32 !EndRow:Int32 !EndColumn:String !Instance:ExcelInstanceHandle !LookupValue:Object
出力: Result:Object=>LookupResult
ON ERROR可: LookupRangeError
固定: Mode=CellCoordinates, IsArrayForm=False

## Excel.LookupRange.LookupRangeNamedCellArray [A]
```
Excel.LookupRange.LookupRangeNamedCellArray CellName: $fx'example' Instance: ExcelInstance LookupValue: $fx'sample' Result=> LookupResult
```
入力: !CellName:String !Instance:ExcelInstanceHandle !LookupValue:Object
出力: Result:Object=>LookupResult
ON ERROR可: LookupRangeError
固定: Mode=NamedCells, IsArrayForm=True

## Excel.LookupRange.LookupRangeNamedCellNonArray [A]
```
Excel.LookupRange.LookupRangeNamedCellNonArray Instance: ExcelInstance LookupValue: $fx'sample' CellName: $fx'example' ValuesCellName: $fx'example' Result=> LookupResult
```
入力: CellName:String Instance:ExcelInstanceHandle LookupValue:Object ValuesCellName:String
出力: Result:Object=>
ON ERROR可: LookupRangeError
固定: Mode=NamedCells, IsArrayForm=False

### Excel.PasteCellsToExcel のセレクター: Paste, PasteAt, PasteAtNamedCell

## Excel.PasteCellsToExcel.Paste [A]
```
Excel.PasteCellsToExcel.Paste Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: PasteCellsError
固定: PasteMode=ActiveCell

## Excel.PasteCellsToExcel.PasteAt [A]
```
Excel.PasteCellsToExcel.PasteAt Instance: ExcelInstance Column: $fx'example' Row: 1
```
入力: Column:String Instance:ExcelInstanceHandle Row:Int32
ON ERROR可: PasteCellsError
固定: PasteMode=SpecifiedCell

## Excel.PasteCellsToExcel.PasteAtNamedCell [A]
```
Excel.PasteCellsToExcel.PasteAtNamedCell CellName: $fx'example' Instance: ExcelInstance
```
入力: !CellName:String !Instance:ExcelInstanceHandle
ON ERROR可: PasteCellsError
固定: PasteMode=NamedCells

### Excel.ReadCellFormula のセレクター: ReadFormulaFromCellCoordinates, ReadFormulaFromNamedCell

## Excel.ReadCellFormula.ReadFormulaFromCellCoordinates [A]
```
Excel.ReadCellFormula.ReadFormulaFromCellCoordinates Instance: ExcelInstance Column: $fx'example' Row: 1 CellFormula=> CellFormula
```
入力: Column:String Instance:ExcelInstanceHandle Row:Int32
出力: CellFormula:String=>
ON ERROR可: ReadCellFormulaError
固定: Mode=CellCoordinates

## Excel.ReadCellFormula.ReadFormulaFromNamedCell [A]
```
Excel.ReadCellFormula.ReadFormulaFromNamedCell Instance: ExcelInstance CellName: $fx'example' CellFormula=> CellFormula
```
入力: !Instance:ExcelInstanceHandle !CellName:String
出力: CellFormula:String=>CellFormula
ON ERROR可: ReadCellFormulaError
固定: Mode=NamedCell

### Excel.ReadFromExcel のセレクター: Read, ReadAllCells, ReadCell, ReadCells, ReadNamedCell

## Excel.ReadFromExcel.Read [A]
```
Excel.ReadFromExcel.Read FirstLineIsHeader: False GetCellContentsMode: Excel.GetCellContentsMode.TypedValues Instance: ExcelInstance RangeValue=> ExcelData
```
入力: !FirstLineIsHeader:Boolean !GetCellContentsMode:GetCellContentsMode{TypedValues,PlainText,FormattedTextValues} !Instance:ExcelInstanceHandle
出力: RangeValue:DataTable=>ExcelData
ON ERROR可: ReadCellsError
固定: ReadMode=Selection

## Excel.ReadFromExcel.ReadAllCells [A]
```
Excel.ReadFromExcel.ReadAllCells FirstLineIsHeader: False GetCellContentsMode: Excel.GetCellContentsMode.TypedValues Instance: ExcelInstance RangeValue=> ExcelData
```
入力: !FirstLineIsHeader:Boolean !GetCellContentsMode:GetCellContentsMode{TypedValues,PlainText,FormattedTextValues} !Instance:ExcelInstanceHandle
出力: RangeValue:DataTable=>ExcelData
ON ERROR可: ReadCellsError
固定: ReadMode=AllCells

## Excel.ReadFromExcel.ReadCell [A]
```
Excel.ReadFromExcel.ReadCell Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1 GetCellContentsMode: Excel.GetCellContentsMode.TypedValues CellValue=> ExcelData
```
入力: Instance:ExcelInstanceHandle GetCellContentsMode:GetCellContentsMode{TypedValues,PlainText,FormattedTextValues} StartColumn:String StartRow:Int32
出力: CellValue:Object=>
ON ERROR可: ReadCellsError
固定: ReadMode=SingleCell

## Excel.ReadFromExcel.ReadCells [A]
```
Excel.ReadFromExcel.ReadCells StartColumn: $fx'example' StartRow: 1 EndRow: 1 EndColumn: $fx'example' FirstLineIsHeader: False GetCellContentsMode: Excel.GetCellContentsMode.TypedValues Instance: ExcelInstance RangeValue=> ExcelData
```
入力: !StartColumn:String !StartRow:Int32 !EndRow:Int32 !EndColumn:String !FirstLineIsHeader:Boolean !GetCellContentsMode:GetCellContentsMode{TypedValues,PlainText,FormattedTextValues} !Instance:ExcelInstanceHandle
出力: RangeValue:DataTable=>ExcelData
ON ERROR可: ReadCellsError
固定: ReadMode=RangeOfCells

## Excel.ReadFromExcel.ReadNamedCell [A]
```
Excel.ReadFromExcel.ReadNamedCell TrimEmptyCells: False CellName: $fx'example' GetCellContentsMode: Excel.GetCellContentsMode.TypedValues Instance: ExcelInstance RangeValue=> ExcelData
```
入力: !TrimEmptyCells:Boolean !CellName:String !GetCellContentsMode:GetCellContentsMode{TypedValues,PlainText,FormattedTextValues} !Instance:ExcelInstanceHandle
出力: RangeValue:DataTable=>ExcelData
ON ERROR可: ReadCellsError
固定: ReadMode=NamedCells

### Excel.RenameWorksheet のセレクター: RenameWorksheetWithIndex, RenameWorksheetWithName

## Excel.RenameWorksheet.RenameWorksheetWithIndex [A]
```
Excel.RenameWorksheet.RenameWorksheetWithIndex NewName: $fx'example' Instance: ExcelInstance Index: 1
```
入力: !NewName:String !Instance:ExcelInstanceHandle !Index:Int32
ON ERROR可: RenameWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Index

## Excel.RenameWorksheet.RenameWorksheetWithName [A]
```
Excel.RenameWorksheet.RenameWorksheetWithName Instance: ExcelInstance Name: $fx'example' NewName: $fx'example'
```
入力: Instance:ExcelInstanceHandle Name:String NewName:String
ON ERROR可: RenameWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Name

### Excel.ResizeColumnsOrRows のセレクター: AutofitAllColumns, AutofitAllRows, AutofitRangeOfColumns, AutofitRangeOfRows, AutofitSingleColumn, AutofitSingleRow, ResizeAllColumns, ResizeAllRows, ResizeRangeOfColumns, ResizeRangeOfRows, ResizeSingleColumn, ResizeSingleRow

## Excel.ResizeColumnsOrRows.AutofitAllColumns [A]
```
Excel.ResizeColumnsOrRows.AutofitAllColumns Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=AllAvailable, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.AutofitAllRows [A]
```
Excel.ResizeColumnsOrRows.AutofitAllRows Instance: ExcelInstance
```
入力: !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=AllAvailable, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.AutofitRangeOfColumns [A]
```
Excel.ResizeColumnsOrRows.AutofitRangeOfColumns EndColumn: $fx'example' Instance: ExcelInstance StartColumn: $fx'example'
```
入力: !EndColumn:String !Instance:ExcelInstanceHandle !StartColumn:String
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=Range, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.AutofitRangeOfRows [A]
```
Excel.ResizeColumnsOrRows.AutofitRangeOfRows EndRow: 1 StartRow: 1 Instance: ExcelInstance
```
入力: !EndRow:Int32 !StartRow:Int32 !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=Range, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.AutofitSingleColumn [A]
```
Excel.ResizeColumnsOrRows.AutofitSingleColumn Instance: ExcelInstance Column: $fx'example'
```
入力: Instance:ExcelInstanceHandle Column:String
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=Single, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.AutofitSingleRow [A]
```
Excel.ResizeColumnsOrRows.AutofitSingleRow Instance: ExcelInstance Row: 1
```
入力: !Instance:ExcelInstanceHandle !Row:Int32
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=Single, ResizeType=Autofit

## Excel.ResizeColumnsOrRows.ResizeAllColumns [A]
```
Excel.ResizeColumnsOrRows.ResizeAllColumns Width: 1 Instance: ExcelInstance
```
入力: !Width:Int32 !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=AllAvailable, ResizeType=CustomSize

## Excel.ResizeColumnsOrRows.ResizeAllRows [A]
```
Excel.ResizeColumnsOrRows.ResizeAllRows Height: 1 Instance: ExcelInstance
```
入力: !Height:Int32 !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=AllAvailable, ResizeType=CustomSize

## Excel.ResizeColumnsOrRows.ResizeRangeOfColumns [A]
```
Excel.ResizeColumnsOrRows.ResizeRangeOfColumns EndColumn: $fx'example' Width: 1 Instance: ExcelInstance StartColumn: $fx'example'
```
入力: !EndColumn:String !Width:Int32 !Instance:ExcelInstanceHandle !StartColumn:String
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=Range, ResizeType=CustomSize

## Excel.ResizeColumnsOrRows.ResizeRangeOfRows [A]
```
Excel.ResizeColumnsOrRows.ResizeRangeOfRows EndRow: 1 StartRow: 1 Height: 1 Instance: ExcelInstance
```
入力: !EndRow:Int32 !StartRow:Int32 !Height:Int32 !Instance:ExcelInstanceHandle
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=Range, ResizeType=CustomSize

## Excel.ResizeColumnsOrRows.ResizeSingleColumn [A]
```
Excel.ResizeColumnsOrRows.ResizeSingleColumn Width: 1 Instance: ExcelInstance Column: $fx'example'
```
入力: !Width:Int32 !Instance:ExcelInstanceHandle !Column:String
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Column, SelectionRange=Single, ResizeType=CustomSize

## Excel.ResizeColumnsOrRows.ResizeSingleRow [A]
```
Excel.ResizeColumnsOrRows.ResizeSingleRow Height: 1 Instance: ExcelInstance Row: 1
```
入力: !Height:Int32 !Instance:ExcelInstanceHandle !Row:Int32
ON ERROR可: ResizeColumnsOrRowsError
固定: ResizeTarget=Row, SelectionRange=Single, ResizeType=CustomSize

## Excel.RunMacro [A]
```
Excel.RunMacro Instance: ExcelInstance Macro: $fx'example'
```
入力: Instance:ExcelInstanceHandle Macro:String
ON ERROR可: RunMacroError

### Excel.SaveExcel のセレクター: Save, SaveAs

## Excel.SaveExcel.Save [A]
```
Excel.SaveExcel.Save Instance: ExcelInstance
```
入力: Instance:ExcelInstanceHandle
ON ERROR可: SaveExcelError
固定: SaveMode=Save

## Excel.SaveExcel.SaveAs [A]
```
Excel.SaveExcel.SaveAs XmlMapName: $fx'example' Instance: ExcelInstance DocumentFormat: Excel.ExcelFormat.FromExtension DocumentPath: $fx'C:\temp\test.xlsx'
```
入力: !XmlMapName:String !Instance:ExcelInstanceHandle !DocumentFormat:ExcelFormat{FromExtension,OpenXmlWorkbook,OpenXmlWorkbookMacroEnabled,Excel8,WebPage,Template,TemplateMacroEnabled,Template8,Text,UnicodeText,TextMacintosh,TextDOS,XMLSpreadsheet,Excel595,CSV,DIF,SYLK,ExcelAddIn,Excel972003AddIn,StrictOpenXmlWorkbook,OpenDocumentSpreadsheet,XmlData,ExcelBinaryWorkbook} !DocumentPath:FileObject
ON ERROR可: SaveExcelError
固定: SaveMode=SaveAs

### Excel.SelectCellsFromExcel のセレクター: SelectCells, SelectCellsRelativeTo, SelectNamedCell

## Excel.SelectCellsFromExcel.SelectCells [A]
```
Excel.SelectCellsFromExcel.SelectCells Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1 EndColumn: $fx'example' EndRow: 1
```
入力: EndColumn:String EndRow:Int32 Instance:ExcelInstanceHandle StartColumn:String StartRow:Int32
ON ERROR可: SelectCellsError
固定: SpecifyCellsMode=Absolute

## Excel.SelectCellsFromExcel.SelectCellsRelativeTo [A]
```
Excel.SelectCellsFromExcel.SelectCellsRelativeTo VerticalDirection: Excel.VerticalDirection.Above OffsetY: 1 HorizontalDirection: Excel.HorizontalDirection.Left OffsetX: 1 Instance: ExcelInstance
```
入力: !VerticalDirection:VerticalDirection{Above,Below} !OffsetY:Int32 !HorizontalDirection:HorizontalDirection{Left,Right} !OffsetX:Int32 !Instance:ExcelInstanceHandle
ON ERROR可: SelectCellsError
固定: SpecifyCellsMode=Relative

## Excel.SelectCellsFromExcel.SelectNamedCell [A]
```
Excel.SelectCellsFromExcel.SelectNamedCell CellName: $fx'example' Instance: ExcelInstance
```
入力: !CellName:String !Instance:ExcelInstanceHandle
ON ERROR可: SelectCellsError
固定: SpecifyCellsMode=NamedCells

### Excel.SetActiveWorksheet のセレクター: ActivateWorksheetByIndex, ActivateWorksheetByName

## Excel.SetActiveWorksheet.ActivateWorksheetByIndex [A]
```
Excel.SetActiveWorksheet.ActivateWorksheetByIndex Instance: ExcelInstance Index: 1
```
入力: !Instance:ExcelInstanceHandle !Index:Int32
ON ERROR可: ActivateWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Index

## Excel.SetActiveWorksheet.ActivateWorksheetByName [A]
```
Excel.SetActiveWorksheet.ActivateWorksheetByName Instance: ExcelInstance Name: $fx'example'
```
入力: Instance:ExcelInstanceHandle Name:String
ON ERROR可: ActivateWorksheetError, WorksheetNotFoundError
固定: FindWorksheetBy=Name

### Excel.SetColor のセレクター: SetColorNamedCellHex, SetColorNamedCellPredefined, SetColorRangeHex, SetColorRangePredefined, SetColorSingleCellHex, SetColorSingleCellPredefined

## Excel.SetColor.SetColorNamedCellHex [A]
```
Excel.SetColor.SetColorNamedCellHex Instance: ExcelInstance ColorHexValue: $fx'example' CellName: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !ColorHexValue:String !CellName:String
ON ERROR可: SetColorError
固定: Mode=NamedCell, ColorMode=HexValue

## Excel.SetColor.SetColorNamedCellPredefined [A]
```
Excel.SetColor.SetColorNamedCellPredefined Instance: ExcelInstance CellName: $fx'example' ColorName: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !CellName:String !ColorName:String
ON ERROR可: SetColorError
固定: Mode=NamedCell, ColorMode=Name

## Excel.SetColor.SetColorRangeHex [A]
```
Excel.SetColor.SetColorRangeHex Instance: ExcelInstance EndRow: 1 StartRow: 1 StartColumn: $fx'example' ColorHexValue: $fx'example' EndColumn: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !EndRow:Int32 !StartRow:Int32 !StartColumn:String !ColorHexValue:String !EndColumn:String
ON ERROR可: SetColorError
固定: Mode=CellCoordinates, ColorMode=HexValue

## Excel.SetColor.SetColorRangePredefined [A]
```
Excel.SetColor.SetColorRangePredefined Instance: ExcelInstance EndRow: 1 StartRow: 1 StartColumn: $fx'example' ColorName: $fx'example' EndColumn: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !EndRow:Int32 !StartRow:Int32 !StartColumn:String !ColorName:String !EndColumn:String
ON ERROR可: SetColorError
固定: Mode=CellCoordinates, ColorMode=Name

## Excel.SetColor.SetColorSingleCellHex [A]
```
Excel.SetColor.SetColorSingleCellHex Instance: ExcelInstance StartRow: 1 StartColumn: $fx'example' ColorHexValue: $fx'example'
```
入力: !Instance:ExcelInstanceHandle !StartRow:Int32 !StartColumn:String !ColorHexValue:String
ON ERROR可: SetColorError
固定: Mode=SingleCell, ColorMode=HexValue

## Excel.SetColor.SetColorSingleCellPredefined [A]
```
Excel.SetColor.SetColorSingleCellPredefined Instance: ExcelInstance StartColumn: $fx'example' StartRow: 1 ColorName: $fx'example'
```
入力: ColorName:String Instance:ExcelInstanceHandle StartColumn:String StartRow:Int32
ON ERROR可: SetColorError
固定: Mode=SingleCell, ColorMode=Name

### Excel.SortCellsFromExcel のセレクター: SortRangeCoordinates, SortRangeNamedCell, SortTable, SortWorksheet

## Excel.SortCellsFromExcel.SortRangeCoordinates [A]
```
Excel.SortCellsFromExcel.SortRangeCoordinates EndColumn: $fx'example' StartRow: 1 EndRow: 1 FirstRowIsHeader: False SortParameters: RecognizedEntities StartColumn: $fx'example' Instance: ExcelInstance
```
入力: !EndColumn:String !StartRow:Int32 !EndRow:Int32 !FirstRowIsHeader:Boolean !SortParameters:DataTable !StartColumn:String !Instance:ExcelInstanceHandle
ON ERROR可: SortCellsFromExcel
固定: SortMode=Range, SortRangeMode=Coordinates

## Excel.SortCellsFromExcel.SortRangeNamedCell [A]
```
Excel.SortCellsFromExcel.SortRangeNamedCell FirstRowIsHeader: False SortParameters: RecognizedEntities Instance: ExcelInstance NamedCell: $fx'example'
```
入力: !FirstRowIsHeader:Boolean !SortParameters:DataTable !Instance:ExcelInstanceHandle !NamedCell:String
ON ERROR可: SortCellsFromExcel
固定: SortMode=Range, SortRangeMode=NamedCell

## Excel.SortCellsFromExcel.SortTable [A]
```
Excel.SortCellsFromExcel.SortTable SortParameters: RecognizedEntities Instance: ExcelInstance TableName: $fx'example'
```
入力: !SortParameters:DataTable !Instance:ExcelInstanceHandle !TableName:String
ON ERROR可: SortCellsFromExcel
固定: SortMode=Table

## Excel.SortCellsFromExcel.SortWorksheet [A]
```
Excel.SortCellsFromExcel.SortWorksheet Instance: ExcelInstance SortParameters: { ^['Column1', 'Column2'] } FirstRowIsHeader: False
```
入力: Instance:ExcelInstanceHandle SortParameters:DataTable FirstRowIsHeader:Boolean
ON ERROR可: SortCellsFromExcel
固定: SortMode=Sheet

### Excel.WriteToExcel のセレクター: Write, WriteCell, WriteNamedCell

## Excel.WriteToExcel.Write [A]
```
Excel.WriteToExcel.Write Value: $fx'sample' Instance: ExcelInstance
```
入力: !Value:Object !Instance:ExcelInstanceHandle
ON ERROR可: WriteToExcelError
固定: WriteMode=ActiveCell

## Excel.WriteToExcel.WriteCell [A]
```
Excel.WriteToExcel.WriteCell Instance: ExcelInstance Value: $fx'sample' Column: $fx'example' Row: 1
```
入力: Column:String Instance:ExcelInstanceHandle Row:Int32 Value:Object
ON ERROR可: WriteToExcelError
固定: WriteMode=SpecifiedCell

## Excel.WriteToExcel.WriteNamedCell [A]
```
Excel.WriteToExcel.WriteNamedCell CellName: $fx'example' WriteToAllCells: False Value: $fx'sample' Instance: ExcelInstance
```
入力: !CellName:String !WriteToAllCells:Boolean !Value:Object !Instance:ExcelInstanceHandle
ON ERROR可: WriteToExcelError
固定: WriteMode=NamedCells
