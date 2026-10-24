# Robin: PDF

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Pdf.ExtractImagesFromPDF のセレクター: ExtractImages, ExtractImagesFromPage, ExtractImagesFromPageRange

## Pdf.ExtractImagesFromPDF.ExtractImages [A]
```
Pdf.ExtractImagesFromPDF.ExtractImages PDFFile: $'''C:\temp\test.xlsx''' ImagesName: $'''example''' ImagesFolder: $'''C:\temp''' Password: $'''password'''
```
入力: ImagesFolder:FolderObject ImagesName:String Password:EncryptableObject PDFFile:FileObject
ON ERROR可: FailedToExtractImagesError, FolderDoesNotExistError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=All

## Pdf.ExtractImagesFromPDF.ExtractImagesFromPage [A]
```
Pdf.ExtractImagesFromPDF.ExtractImagesFromPage Password: $'''password''' PDFFile: $'''C:\temp\test.xlsx''' ImagesFolder: $'''C:\temp''' PageNumber: 1 ImagesName: $'''example'''
```
入力: Password:EncryptableObject !PDFFile:FileObject !ImagesFolder:FolderObject !PageNumber:Int32 !ImagesName:String
ON ERROR可: FailedToExtractImagesError, FolderDoesNotExistError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Single

## Pdf.ExtractImagesFromPDF.ExtractImagesFromPageRange [A]
```
Pdf.ExtractImagesFromPDF.ExtractImagesFromPageRange Password: $'''password''' ToPageNumber: 1 PDFFile: $'''C:\temp\test.xlsx''' ImagesFolder: $'''C:\temp''' FromPageNumber: 1 ImagesName: $'''example'''
```
入力: Password:EncryptableObject !ToPageNumber:Int32 !PDFFile:FileObject !ImagesFolder:FolderObject !FromPageNumber:Int32 !ImagesName:String
ON ERROR可: FailedToExtractImagesError, FolderDoesNotExistError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Range

## Pdf.ExtractPages [A]
```
Pdf.ExtractPages PDFFile: $'''C:\temp\test.xlsx''' PageSelection: $'''example''' ExtractedPDFPath: $'''C:\temp\test.xlsx''' IfFileExists: Pdf.IfFileExists.AddSequentialSuffix Password: $'''password''' ExtractedPDFFile=> ExtractedPDF
```
入力: ExtractedPDFPath:FileObject IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix} PageSelection:String Password:EncryptableObject PDFFile:FileObject
出力: ExtractedPDFFile:FileObject=>
ON ERROR可: FailedToExtractNewPDFFileError, InvalidPageSelectionError, InvalidPasswordError, PageOutOfBoundsError, PDFFileDoesNotExistError

### Pdf.ExtractTablesFromPDF のセレクター: ExtractTables, ExtractTablesFromPage, ExtractTablesFromPageRange

## Pdf.ExtractTablesFromPDF.ExtractTables [A]
```
Pdf.ExtractTablesFromPDF.ExtractTables PDFFile: $'''C:\temp\test.xlsx''' MultiPageTables: True SetFirstRowAsHeader: True Password: $'''password''' ExtractedPDFTables=> ExtractedPDFTables
```
入力: MultiPageTables:Boolean Password:EncryptableObject PDFFile:FileObject SetFirstRowAsHeader:Boolean
出力: ExtractedPDFTables:List=>
ON ERROR可: FailedToExtractTablesError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=All

## Pdf.ExtractTablesFromPDF.ExtractTablesFromPage [A]
```
Pdf.ExtractTablesFromPDF.ExtractTablesFromPage PDFFile: $'''C:\temp\test.xlsx''' Password: $'''password''' SetFirstRowAsHeader: True MultiPageTables: True PageNumber: 1 ExtractedPDFTables=> ExtractedPDFTables
```
入力: !PDFFile:FileObject Password:EncryptableObject !SetFirstRowAsHeader:Boolean !MultiPageTables:Boolean !PageNumber:Int32
出力: ExtractedPDFTables:List<PDFTableInfo>=>ExtractedPDFTables
ON ERROR可: FailedToExtractTablesError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Single

## Pdf.ExtractTablesFromPDF.ExtractTablesFromPageRange [A]
```
Pdf.ExtractTablesFromPDF.ExtractTablesFromPageRange PDFFile: $'''C:\temp\test.xlsx''' Password: $'''password''' ToPageNumber: 1 SetFirstRowAsHeader: True MultiPageTables: True FromPageNumber: 1 ExtractedPDFTables=> ExtractedPDFTables
```
入力: !PDFFile:FileObject Password:EncryptableObject !ToPageNumber:Int32 !SetFirstRowAsHeader:Boolean !MultiPageTables:Boolean !FromPageNumber:Int32
出力: ExtractedPDFTables:List<PDFTableInfo>=>ExtractedPDFTables
ON ERROR可: FailedToExtractTablesError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Range

### Pdf.ExtractTextFromPDF のセレクター: ExtractText, ExtractTextFromPage, ExtractTextFromPageRange

## Pdf.ExtractTextFromPDF.ExtractText [A]
```
Pdf.ExtractTextFromPDF.ExtractText PDFFile: $'''C:\temp\test.xlsx''' DetectLayout: False Password: $'''password''' ExtractedText=> ExtractedPDFText
```
入力: Password:EncryptableObject PDFFile:FileObject DetectLayout:Boolean
出力: ExtractedText:String=>
ON ERROR可: FailedToExtractTextError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=All

## Pdf.ExtractTextFromPDF.ExtractTextFromPage [A]
```
Pdf.ExtractTextFromPDF.ExtractTextFromPage PDFFile: $'''C:\temp\test.xlsx''' DetectLayout: False Password: $'''password''' PageNumber: 1 ExtractedText=> ExtractedPDFText
```
入力: !PDFFile:FileObject !DetectLayout:Boolean Password:EncryptableObject !PageNumber:Int32
出力: ExtractedText:String=>ExtractedPDFText
ON ERROR可: FailedToExtractTextError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Single

## Pdf.ExtractTextFromPDF.ExtractTextFromPageRange [A]
```
Pdf.ExtractTextFromPDF.ExtractTextFromPageRange PDFFile: $'''C:\temp\test.xlsx''' ToPageNumber: 1 DetectLayout: False Password: $'''password''' FromPageNumber: 1 ExtractedText=> ExtractedPDFText
```
入力: !PDFFile:FileObject !ToPageNumber:Int32 !DetectLayout:Boolean Password:EncryptableObject !FromPageNumber:Int32
出力: ExtractedText:String=>ExtractedPDFText
ON ERROR可: FailedToExtractTextError, InvalidPasswordError, PDFFileDoesNotExistError
固定: PagesToExtract=Range

## Pdf.MergeFiles [A]
```
Pdf.MergeFiles PDFFiles: FileList MergedPDFPath: $'''C:\temp\test.xlsx''' IfFileExists: Pdf.IfFileExists.AddSequentialSuffix PasswordDelimiter: $''',''' Passwords: $'''password''' MergedPDF=> MergedPDF
```
入力: IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix} MergedPDFPath:FileObject PasswordDelimiter:String Passwords:EncryptableObject PDFFiles:List
出力: MergedPDF:FileObject=>
ON ERROR可: FailedToMergePDFFilesError, InvalidPasswordError, PDFFileDoesNotExistError
