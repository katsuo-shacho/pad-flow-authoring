# Robin: Word

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Word.Attach [A]
```
Word.Attach DocumentName: $fx'C:\temp\test.xlsx' Instance=> WordInstance
```
入力: DocumentName:FileObject
出力: Instance:WordInstanceHandle=>
ON ERROR可: AttachToWordError, DocumentNotFoundError, LauchWordError

### Word.CloseWord のセレクター: Close, CloseAndSave, CloseAndSaveAs

## Word.CloseWord.Close [A]
```
Word.CloseWord.Close Instance: WordInstance
```
入力: Instance:WordInstanceHandle
ON ERROR可: CloseWordError, SaveWordError, WordOperationOnReadOnlyDocumentError
固定: CloseMode=DoNotSave

## Word.CloseWord.CloseAndSave [A]
```
Word.CloseWord.CloseAndSave Instance: WordInstance
```
入力: !Instance:WordInstanceHandle
ON ERROR可: CloseWordError, SaveWordError, WordOperationOnReadOnlyDocumentError
固定: CloseMode=Save

## Word.CloseWord.CloseAndSaveAs [A]
```
Word.CloseWord.CloseAndSaveAs DocumentFormat: Word.WordFormat.FromExtension DocumentPath: $fx'C:\temp\test.xlsx' Instance: WordInstance
```
入力: !DocumentFormat:WordFormat{DOCX,DOCM,DOC,DOTX,DOTM,DOT,PDF,XPS,WebPageArchive,WebPage,WebPageFiltered,RTF,Text,TextLineBreaks,DOSText,DOSTextLineBreaks,UnicodeText,XML,StrictOpenXMLDocument,ODT,FromExtension} !DocumentPath:FileObject !Instance:WordInstanceHandle
ON ERROR可: CloseWordError, SaveWordError, WordOperationOnReadOnlyDocumentError
固定: CloseMode=SaveAs

### Word.FindAndReplaceWord のセレクター: FindAndReplaceAllWildcards, FindAndReplaceAllWithoutWildcards, FindAndReplaceSingle, FindAndReplaceSingleWildcards

## Word.FindAndReplaceWord.FindAndReplaceAllWildcards [A]
```
Word.FindAndReplaceWord.FindAndReplaceAllWildcards TextToReplaceWith: $fx'example' Instance: WordInstance TextToFind: $fx'example'
```
入力: !TextToReplaceWith:String !Instance:WordInstanceHandle !TextToFind:String
ON ERROR可: FindAndReplaceError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: AllMatches=True, MatchWildCards=True

## Word.FindAndReplaceWord.FindAndReplaceAllWithoutWildcards [A]
```
Word.FindAndReplaceWord.FindAndReplaceAllWithoutWildcards MatchCase: False MatchEntireWord: False TextToReplaceWith: $fx'example' Instance: WordInstance TextToFind: $fx'example'
```
入力: !MatchCase:Boolean !MatchEntireWord:Boolean !TextToReplaceWith:String !Instance:WordInstanceHandle !TextToFind:String
ON ERROR可: FindAndReplaceError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: AllMatches=True, MatchWildCards=False

## Word.FindAndReplaceWord.FindAndReplaceSingle [A]
```
Word.FindAndReplaceWord.FindAndReplaceSingle Instance: WordInstance TextToFind: $fx'example' TextToReplaceWith: $fx'example' MatchCase: False MatchEntireWord: False
```
入力: Instance:WordInstanceHandle TextToFind:String TextToReplaceWith:String MatchCase:Boolean MatchEntireWord:Boolean
ON ERROR可: FindAndReplaceError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: AllMatches=False, MatchWildCards=False

## Word.FindAndReplaceWord.FindAndReplaceSingleWildcards [A]
```
Word.FindAndReplaceWord.FindAndReplaceSingleWildcards TextToReplaceWith: $fx'example' Instance: WordInstance TextToFind: $fx'example'
```
入力: !TextToReplaceWith:String !Instance:WordInstanceHandle !TextToFind:String
ON ERROR可: FindAndReplaceError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: AllMatches=False, MatchWildCards=True

### Word.InsertImageToWord のセレクター: InsertImageBookmarkEndFromClipboard, InsertImageBookmarkEndFromFile, InsertImageBookmarkStartFromClipboard, InsertImageBookmarkStartFromFile, InsertImageDocumentEndFromClipboard, InsertImageDocumentEndFromFile, InsertImageDocumentStartFromClipboard, InsertImageDocumentStartFromFile, InsertImageEndOfTextFromClipBoard, InsertImageEndOfTextFromFile, InsertImageStartOfTextFromClipBoard, InsertImageStartOfTextFromFile

## Word.InsertImageToWord.InsertImageBookmarkEndFromClipboard [A]
```
Word.InsertImageToWord.InsertImageBookmarkEndFromClipboard Instance: WordInstance Bookmark: $fx'example'
```
入力: !Instance:WordInstanceHandle !Bookmark:String
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfBookmark, Source=Clipboard

## Word.InsertImageToWord.InsertImageBookmarkEndFromFile [A]
```
Word.InsertImageToWord.InsertImageBookmarkEndFromFile Path: $fx'C:\temp\test.xlsx' Instance: WordInstance Bookmark: $fx'example'
```
入力: !Path:FileObject !Instance:WordInstanceHandle !Bookmark:String
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfBookmark, Source=File

## Word.InsertImageToWord.InsertImageBookmarkStartFromClipboard [A]
```
Word.InsertImageToWord.InsertImageBookmarkStartFromClipboard Instance: WordInstance Bookmark: $fx'example'
```
入力: !Instance:WordInstanceHandle !Bookmark:String
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfBookmark, Source=Clipboard

## Word.InsertImageToWord.InsertImageBookmarkStartFromFile [A]
```
Word.InsertImageToWord.InsertImageBookmarkStartFromFile Path: $fx'C:\temp\test.xlsx' Instance: WordInstance Bookmark: $fx'example'
```
入力: !Path:FileObject !Instance:WordInstanceHandle !Bookmark:String
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfBookmark, Source=File

## Word.InsertImageToWord.InsertImageDocumentEndFromClipboard [A]
```
Word.InsertImageToWord.InsertImageDocumentEndFromClipboard Instance: WordInstance
```
入力: !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfDocument, Source=Clipboard

## Word.InsertImageToWord.InsertImageDocumentEndFromFile [A]
```
Word.InsertImageToWord.InsertImageDocumentEndFromFile Path: $fx'C:\temp\test.xlsx' Instance: WordInstance
```
入力: !Path:FileObject !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfDocument, Source=File

## Word.InsertImageToWord.InsertImageDocumentStartFromClipboard [A]
```
Word.InsertImageToWord.InsertImageDocumentStartFromClipboard Instance: WordInstance
```
入力: !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfDocument, Source=Clipboard

## Word.InsertImageToWord.InsertImageDocumentStartFromFile [A]
```
Word.InsertImageToWord.InsertImageDocumentStartFromFile Instance: WordInstance Path: $fx'C:\temp\test.xlsx'
```
入力: Instance:WordInstanceHandle Path:FileObject
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfDocument, Source=File

## Word.InsertImageToWord.InsertImageEndOfTextFromClipBoard [A]
```
Word.InsertImageToWord.InsertImageEndOfTextFromClipBoard TextToFind: $fx'example' Instance: WordInstance
```
入力: !TextToFind:String !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfText, Source=Clipboard

## Word.InsertImageToWord.InsertImageEndOfTextFromFile [A]
```
Word.InsertImageToWord.InsertImageEndOfTextFromFile TextToFind: $fx'example' Path: $fx'C:\temp\test.xlsx' Instance: WordInstance
```
入力: !TextToFind:String !Path:FileObject !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=EndOfText, Source=File

## Word.InsertImageToWord.InsertImageStartOfTextFromClipBoard [A]
```
Word.InsertImageToWord.InsertImageStartOfTextFromClipBoard TextToFind: $fx'example' Instance: WordInstance
```
入力: !TextToFind:String !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfText, Source=Clipboard

## Word.InsertImageToWord.InsertImageStartOfTextFromFile [A]
```
Word.InsertImageToWord.InsertImageStartOfTextFromFile TextToFind: $fx'example' Path: $fx'C:\temp\test.xlsx' Instance: WordInstance
```
入力: !TextToFind:String !Path:FileObject !Instance:WordInstanceHandle
ON ERROR可: InsertImageWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: InsertImageMode=StartOfText, Source=File

### Word.LaunchWord のセレクター: Launch, LaunchAndOpen

## Word.LaunchWord.Launch [A]
```
Word.LaunchWord.Launch Visible: True Instance=> WordInstance
```
入力: Visible:Boolean
出力: Instance:WordInstanceHandle=>
ON ERROR可: LauchWordError, LaunchWordApplicationError, LaunchWordFileNotFoundError, LaunchWordInstallationError, LaunchWordOpenExistingDocumentError
固定: LaunchWordMode=NewDocument

## Word.LaunchWord.LaunchAndOpen [A]
```
Word.LaunchWord.LaunchAndOpen Visible: True ReadProtectionPassword: $fx'password' WriteProtectionPassword: $fx'password' Path: $fx'C:\temp\test.xlsx' ReadOnly: False Instance=> WordInstance
```
入力: !Visible:Boolean ReadProtectionPassword:EncryptableObject WriteProtectionPassword:EncryptableObject !Path:FileObject !ReadOnly:Boolean
出力: Instance:WordInstanceHandle=>WordInstance
ON ERROR可: LauchWordError, LaunchWordApplicationError, LaunchWordFileNotFoundError, LaunchWordInstallationError, LaunchWordOpenExistingDocumentError
固定: LaunchWordMode=StoredDocument

### Word.ReadFromWord のセレクター: Read, ReadBookmark, ReadPage

## Word.ReadFromWord.Read [A]
```
Word.ReadFromWord.Read Instance: WordInstance WordData=> WordData
```
入力: Instance:WordInstanceHandle
出力: WordData:String=>
ON ERROR可: ReadWordError, WordInstanceNotInitializedError
固定: ReadMode=WholeDocument

## Word.ReadFromWord.ReadBookmark [A]
```
Word.ReadFromWord.ReadBookmark Bookmark: $fx'example' Instance: WordInstance WordData=> WordData
```
入力: !Bookmark:String !Instance:WordInstanceHandle
出力: WordData:String=>WordData
ON ERROR可: ReadWordError, WordInstanceNotInitializedError
固定: ReadMode=Bookmark

## Word.ReadFromWord.ReadPage [A]
```
Word.ReadFromWord.ReadPage Pages: $fx'example' Instance: WordInstance WordData=> WordData
```
入力: !Pages:String !Instance:WordInstanceHandle
出力: WordData:String=>WordData
ON ERROR可: ReadWordError, WordInstanceNotInitializedError
固定: ReadMode=Page

### Word.SaveWord のセレクター: Save, SaveAs

## Word.SaveWord.Save [A]
```
Word.SaveWord.Save Instance: WordInstance
```
入力: Instance:WordInstanceHandle
ON ERROR可: SaveWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: SaveMode=Save

## Word.SaveWord.SaveAs [A]
```
Word.SaveWord.SaveAs DocumentFormat: Word.WordFormat.FromExtension DocumentPath: $fx'C:\temp\test.xlsx' Instance: WordInstance
```
入力: !DocumentFormat:WordFormat{DOCX,DOCM,DOC,DOTX,DOTM,DOT,PDF,XPS,WebPageArchive,WebPage,WebPageFiltered,RTF,Text,TextLineBreaks,DOSText,DOSTextLineBreaks,UnicodeText,XML,StrictOpenXMLDocument,ODT,FromExtension} !DocumentPath:FileObject !Instance:WordInstanceHandle
ON ERROR可: SaveWordError, WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError
固定: SaveMode=SaveAs

### Word.WriteToWord のセレクター: WriteEndOfBookmark, WriteEndOfDocument, WriteStartOfBookmark, WriteStartOfDocument

## Word.WriteToWord.WriteEndOfBookmark [A]
```
Word.WriteToWord.WriteEndOfBookmark Bookmark: $fx'example' AppendNewLine: False Instance: WordInstance Text: $fx'example'
```
入力: !Bookmark:String !AppendNewLine:Boolean !Instance:WordInstanceHandle !Text:String
ON ERROR可: WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError, WriteWordError
固定: WriteMode=EndOfBookmark

## Word.WriteToWord.WriteEndOfDocument [A]
```
Word.WriteToWord.WriteEndOfDocument AppendNewLine: False Instance: WordInstance Text: $fx'example'
```
入力: !AppendNewLine:Boolean !Instance:WordInstanceHandle !Text:String
ON ERROR可: WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError, WriteWordError
固定: WriteMode=EndOfDocument

## Word.WriteToWord.WriteStartOfBookmark [A]
```
Word.WriteToWord.WriteStartOfBookmark Bookmark: $fx'example' AppendNewLine: False Instance: WordInstance Text: $fx'example'
```
入力: !Bookmark:String !AppendNewLine:Boolean !Instance:WordInstanceHandle !Text:String
ON ERROR可: WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError, WriteWordError
固定: WriteMode=StartOfBookmark

## Word.WriteToWord.WriteStartOfDocument [A]
```
Word.WriteToWord.WriteStartOfDocument Instance: WordInstance Text: $fx'example' AppendNewLine: False
```
入力: Instance:WordInstanceHandle Text:String AppendNewLine:Boolean
ON ERROR可: WordInstanceNotInitializedError, WordOperationOnReadOnlyDocumentError, WriteWordError
固定: WriteMode=StartOfDocument
