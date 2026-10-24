# Robin: File

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## File.ConvertFromBase64 [A]
```
File.ConvertFromBase64 Base64Text: $'''example''' File: $'''C:\temp\test.xlsx''' IfFileExists: File.IfExists.DoNothing
```
入力: Base64Text:String File:FileObject IfFileExists:IfExists{DoNothing,Overwrite}
ON ERROR可: ConvertBase64ToFileError, InvalidDirectoryError

## File.ConvertFromBinary [A]
```
File.ConvertFromBinary BinaryData: BinaryData File: $'''C:\temp\test.xlsx''' IfFileExists: File.IfExists.DoNothing
```
入力: BinaryData:BinaryObject File:FileObject IfFileExists:IfExists{DoNothing,Overwrite}
ON ERROR可: ConvertBinaryToFileError, InvalidDirectoryError

## File.ConvertToBase64 [A]
```
File.ConvertToBase64 File: $'''C:\temp\test.xlsx''' Base64Text=> Base64Text
```
入力: File:FileObject
出力: Base64Text:String=>
ON ERROR可: ConvertFileToBase64Error, FileNotFoundError

## File.ConvertToBinary [A]
```
File.ConvertToBinary File: $'''C:\temp\test.xlsx''' BinaryData=> BinaryData
```
入力: File:FileObject
出力: BinaryData:BinaryObject=>
ON ERROR可: ConvertFileToBinaryError, FileNotFoundError

## File.Copy [A]
```
File.Copy Files: FileList Destination: $'''C:\temp''' IfFileExists: File.IfExists.DoNothing CopiedFiles=> CopiedFiles
```
入力: Destination:FolderObject Files:List IfFileExists:IfExists{DoNothing,Overwrite}
出力: CopiedFiles:List=>
ON ERROR可: CopyFileError, FileNotFoundError, InvalidDestinationFolderError, InvalidSourceFolderError

## File.Delete [A]
```
File.Delete Files: FileList
```
入力: Files:List
ON ERROR可: DeleteFileError, FileNotFoundError, InvalidFilePathError

## File.GetPathPart [A]
```
File.GetPathPart File: $'''C:\temp\test.xlsx''' RootPath=> RootPath Directory=> Directory FileName=> FileName FileNameWithoutExtension=> FileNameNoExtension Extension=> FileExtension
```
入力: File:FileObject
出力: Directory:FolderObject=> Extension:String=> FileName:String=> FileNameWithoutExtension:String=> RootPath:FolderObject=>
ON ERROR可: InvalidFilePathError

## File.GetTempPath [A]
```
File.GetTempPath TempFile=> TempFile
```
出力: TempFile:FileObject=>
ON ERROR可: CreateTempFileError

### File.IfFile のセレクター: DoesNotExist, Exists

## File.IfFile.DoesNotExist [C]
```
IF (File.IfFile.DoesNotExist File: $'''C:\temp\test.xlsx''') THEN
```
入力: !File:FileObject
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: CheckMode=DoesNotExist

## File.IfFile.Exists [C]
```
IF (File.IfFile.Exists File: $'''C:\temp\test.xlsx''') THEN
```
入力: !File:FileObject
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: CheckMode=Exists

## File.Move [A]
```
File.Move Files: FileList Destination: $'''C:\temp''' IfFileExists: File.IfExists.DoNothing MovedFiles=> MovedFiles
```
入力: Destination:FolderObject Files:List IfFileExists:IfExists{DoNothing,Overwrite}
出力: MovedFiles:List=>
ON ERROR可: FileNotFoundError, InvalidDestinationFolderError, InvalidSourceFolderError, MoveFileError

### File.ReadFromCSVFile のセレクター: ReadCSV, ReadCSVWithCustomSeparator, ReadCSVWithFixedColumnWidths

## File.ReadFromCSVFile.ReadCSV [A]
```
File.ReadFromCSVFile.ReadCSV CSVFile: $'''C:\temp\test.xlsx''' Encoding: File.CSVEncoding.UTF8 TrimFields: True FirstLineContainsColumnNames: False ColumnsSeparator: File.CSVColumnsSeparator.SystemDefault CSVTable=> CSVTable
```
入力: ColumnsSeparator:CSVColumnsSeparator{SystemDefault,Comma,Semicolon,Tab} CSVFile:FileObject Encoding:CSVEncoding{SystemDefault,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ASCII} FirstLineContainsColumnNames:Boolean TrimFields:Boolean
出力: CSVTable:DataTable=>
ON ERROR可: ReadFromCsvError
固定: ColumnsSeparatorType=Predefined

## File.ReadFromCSVFile.ReadCSVWithCustomSeparator [A]
```
File.ReadFromCSVFile.ReadCSVWithCustomSeparator FirstLineContainsColumnNames: False Encoding: File.CSVEncoding.UTF8 TrimFields: True CustomColumnsSeparator: $'''example''' CSVFile: $'''C:\temp\test.xlsx''' CSVTable=> CSVTable
```
入力: !FirstLineContainsColumnNames:Boolean !Encoding:CSVEncoding{SystemDefault,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ASCII} !TrimFields:Boolean !CustomColumnsSeparator:String !CSVFile:FileObject
出力: CSVTable:DataTable=>CSVTable
ON ERROR可: ReadFromCsvError
固定: ColumnsSeparatorType=Custom

## File.ReadFromCSVFile.ReadCSVWithFixedColumnWidths [A]
```
File.ReadFromCSVFile.ReadCSVWithFixedColumnWidths FirstLineContainsColumnNames: False Encoding: File.CSVEncoding.UTF8 TrimFields: True FixedColumnWidths: $'''example''' CSVFile: $'''C:\temp\test.xlsx''' CSVTable=> CSVTable
```
入力: !FirstLineContainsColumnNames:Boolean !Encoding:CSVEncoding{SystemDefault,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ASCII} !TrimFields:Boolean !FixedColumnWidths:String !CSVFile:FileObject
出力: CSVTable:DataTable=>CSVTable
ON ERROR可: ReadFromCsvError
固定: ColumnsSeparatorType=FixedColumnWidths

### File.ReadTextFromFile のセレクター: ReadText, ReadTextAsList

## File.ReadTextFromFile.ReadText [A]
```
File.ReadTextFromFile.ReadText File: $'''C:\temp\test.xlsx''' Encoding: File.TextFileEncoding.UTF8 Content=> FileContents
```
入力: Encoding:TextFileEncoding{DefaultEncoding,UTF8,Unicode,BigEndianUnicode,ANSI} File:FileObject
出力: Content:String=>
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, ReadFromFileError
固定: StoreContentAs=SingleTextValue

## File.ReadTextFromFile.ReadTextAsList [A]
```
File.ReadTextFromFile.ReadTextAsList File: $'''C:\temp\test.xlsx''' Encoding: File.TextFileEncoding.UTF8 Contents=> FileContents
```
入力: !File:FileObject !Encoding:TextFileEncoding{DefaultEncoding,UTF8,Unicode,BigEndianUnicode,ANSI}
出力: Contents:List<String>=>FileContents
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, ReadFromFileError
固定: StoreContentAs=List

### File.RenameFiles のセレクター: OverwriteWithSequentialSuffix, Rename, RenameAddCustomDateTime, RenameAddDateOrTime, RenameAddSequentialSuffix, RenameAddText, RenameChangeExtension, RenameRemoveText, RenameReplaceText

## File.RenameFiles.OverwriteWithSequentialSuffix [A]
```
File.RenameFiles.OverwriteWithSequentialSuffix SequenceSeparator: File.Separator.Space StartNumberingAt: 1 SequenceNewName: $'''example''' SequencePosition: File.AddTextPosition.AfterName UsePadding: False Files: Files Padding: 3 IfFileExists: File.IfExists.DoNothing IncrementBy: 1 RenamedFiles=> RenamedFiles
```
入力: !SequenceSeparator:Separator{Nothing,Space,Dash,Period,Underscore} !StartNumberingAt:Int32 !SequenceNewName:String !SequencePosition:AddTextPosition{AfterName,BeforeName} !UsePadding:Boolean !Files:List<FileObject> !Padding:Int32 !IfFileExists:IfExists{DoNothing,Overwrite} !IncrementBy:Int32
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=MakeSequential, SequenceUseExistingName=False

## File.RenameFiles.Rename [A]
```
File.RenameFiles.Rename Files: FileList NewName: $'''example''' KeepExtension: True IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: Files:List IfFileExists:IfExists{DoNothing,Overwrite} KeepExtension:Boolean NewName:String
出力: RenamedFiles:List=>
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=SetNewName

## File.RenameFiles.RenameAddCustomDateTime [A]
```
File.RenameFiles.RenameAddCustomDateTime DateTimeSeparator: File.Separator.Space Files: Files CustomDateTime: $'''2025-01-01''' DateTimeFormat: $'''example''' DateTimePosition: File.AddTextPosition.AfterName IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: !DateTimeSeparator:Separator{Nothing,Space,Dash,Period,Underscore} !Files:List<FileObject> !CustomDateTime:DateTime !DateTimeFormat:String !DateTimePosition:AddTextPosition{AfterName,BeforeName} !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=AddDateTime, UseCustomDateTime=True

## File.RenameFiles.RenameAddDateOrTime [A]
```
File.RenameFiles.RenameAddDateOrTime DateTimeSeparator: File.Separator.Space DateTimeToAdd: File.DateTimeToAdd.Current Files: Files DateTimeFormat: $'''example''' DateTimePosition: File.AddTextPosition.AfterName IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: !DateTimeSeparator:Separator{Nothing,Space,Dash,Period,Underscore} !DateTimeToAdd:DateTimeToAdd{Current,CreationTime,LastAccessed,LastModified} !Files:List<FileObject> !DateTimeFormat:String !DateTimePosition:AddTextPosition{AfterName,BeforeName} !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=AddDateTime, UseCustomDateTime=False

## File.RenameFiles.RenameAddSequentialSuffix [A]
```
File.RenameFiles.RenameAddSequentialSuffix SequenceSeparator: File.Separator.Space StartNumberingAt: 1 SequencePosition: File.AddTextPosition.AfterName UsePadding: False Files: Files Padding: 3 IfFileExists: File.IfExists.DoNothing IncrementBy: 1 RenamedFiles=> RenamedFiles
```
入力: !SequenceSeparator:Separator{Nothing,Space,Dash,Period,Underscore} !StartNumberingAt:Int32 !SequencePosition:AddTextPosition{AfterName,BeforeName} !UsePadding:Boolean !Files:List<FileObject> !Padding:Int32 !IfFileExists:IfExists{DoNothing,Overwrite} !IncrementBy:Int32
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=MakeSequential, SequenceUseExistingName=True

## File.RenameFiles.RenameAddText [A]
```
File.RenameFiles.RenameAddText TextPosition: File.AddTextPosition.AfterName TextToAdd: $'''example''' Files: Files IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: !TextPosition:AddTextPosition{AfterName,BeforeName} TextToAdd:String !Files:List<FileObject> !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=AddText

## File.RenameFiles.RenameChangeExtension [A]
```
File.RenameFiles.RenameChangeExtension Files: Files NewExtension: $'''example''' IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: !Files:List<FileObject> NewExtension:String !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=ChangeExtension

## File.RenameFiles.RenameRemoveText [A]
```
File.RenameFiles.RenameRemoveText TextToRemove: $'''example''' Files: Files IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: TextToRemove:String !Files:List<FileObject> !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=RemoveText

## File.RenameFiles.RenameReplaceText [A]
```
File.RenameFiles.RenameReplaceText ReplaceWith: $'''example''' TextToReplace: $'''example''' Files: Files IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```
入力: ReplaceWith:String !TextToReplace:String !Files:List<FileObject> !IfFileExists:IfExists{DoNothing,Overwrite}
出力: RenamedFiles:List<FileObject>=>RenamedFiles
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, RenameFileError
固定: RenameScheme=ReplaceText

### File.WaitForFile のセレクター: Created, Deleted

## File.WaitForFile.Created [W]
```
WAIT (File.WaitForFile.Created File: $'''C:\temp\test.xlsx''')
```
入力: !File:FileObject
ON ERROR可: (名前なし)
固定: WaitFor=ToBeCreated

## File.WaitForFile.Deleted [W]
```
WAIT (File.WaitForFile.Deleted File: $'''C:\temp\test.xlsx''')
```
入力: !File:FileObject
ON ERROR可: (名前なし)
固定: WaitFor=ToBeDeleted

## File.WriteText [A]
```
File.WriteText File: $'''C:\temp\test.xlsx''' AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.Unicode TextToWrite: $'''sample'''
```
入力: AppendNewLine:Boolean Encoding:FileEncoding{DefaultEncoding,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ANSI} File:FileObject IfFileExists:IfFileExists{Overwrite,Append} TextToWrite:Object
ON ERROR可: InvalidDirectoryError, WriteTextToFileError

### File.WriteToCSVFile のセレクター: WriteCSV, WriteCSVWithCustomSeparator

## File.WriteToCSVFile.WriteCSV [A]
```
File.WriteToCSVFile.WriteCSV VariableToWrite: $'''sample''' CSVFile: $'''C:\temp\test.xlsx''' CsvFileEncoding: File.CSVEncoding.UTF8 IncludeColumnNames: False IfFileExists: File.IfFileExists.Overwrite ColumnsSeparator: File.CSVColumnsSeparator.SystemDefault
```
入力: ColumnsSeparator:CSVColumnsSeparator{SystemDefault,Comma,Semicolon,Tab} CSVFile:FileObject CsvFileEncoding:CSVEncoding{SystemDefault,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ASCII} IfFileExists:IfFileExists{Overwrite,Append} IncludeColumnNames:Boolean VariableToWrite:Object
ON ERROR可: WriteToCSVError
固定: UseCustomSeparator=False

## File.WriteToCSVFile.WriteCSVWithCustomSeparator [A]
```
File.WriteToCSVFile.WriteCSVWithCustomSeparator IncludeColumnNames: False IfFileExists: File.IfFileExists.Overwrite VariableToWrite: $'''sample''' CSVFile: $'''C:\temp\test.xlsx''' CustomColumnsSeparator: $'''example''' CsvFileEncoding: File.CSVEncoding.UTF8
```
入力: !IncludeColumnNames:Boolean !IfFileExists:IfFileExists{Overwrite,Append} !VariableToWrite:Object !CSVFile:FileObject !CustomColumnsSeparator:String !CsvFileEncoding:CSVEncoding{SystemDefault,UTF8,Unicode,BigEndianUnicode,UTF8NoBOM,UnicodeNoBOM,ASCII}
ON ERROR可: WriteToCSVError
固定: UseCustomSeparator=True
