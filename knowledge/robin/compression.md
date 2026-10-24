# Robin: Compression

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Compression.UnzipFiles [A]
```
Compression.UnzipFiles ArchivePath: $'''C:\temp\test.xlsx''' DestinationFolder: $'''C:\temp''' IncludeMask: $'''*''' ExcludeMask: $'''example''' Password: $'''password'''
```
入力: ArchivePath:FileObject DestinationFolder:FolderObject ExcludeMask:String IncludeMask:String Password:EncryptableObject
ON ERROR可: ArchiveNotFoundError, CreateFolderError, InvalidArchiveError, UnzipError

## Compression.ZipFiles [A]
```
Compression.ZipFiles ArchivePath: $'''C:\temp\test.xlsx''' FilesOrFoldersToZip: FileList CompressionLevel: Compression.CompressionLevel.BestBalanceOfSpeedAndCompression ArchiveComment: $'''''' Password: $'''password''' ZipFile=> ZipFile
```
入力: ArchiveComment:String ArchivePath:FileObject CompressionLevel:CompressionLevel{None,BestSpeed,BestBalanceOfSpeedAndCompression,BestCompression} FilesOrFoldersToZip:List Password:EncryptableObject
出力: ZipFile:FileObject=>
ON ERROR可: ArchiveExistsInvalidError, FileNotFoundError, InvalidFileError, ZipError
