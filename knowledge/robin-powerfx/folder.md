# Robin: Folder

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Folder.Copy [A]
```
Folder.Copy Folder: $fx'C:\temp' Destination: $fx'C:\temp' IfFolderExists: Folder.IfExists.DoNothing CopiedFolder=> CopiedFolder
```
入力: Destination:FolderObject Folder:FolderObject IfFolderExists:IfExists{DoNothing,Overwrite}
出力: CopiedFolder:FolderObject=>
ON ERROR可: CopyFolderError, FolderNotFoundError, InvalidDestinationFolderError

## Folder.Create [A]
```
Folder.Create FolderPath: $fx'C:\temp' FolderName: $fx'example' Folder=> NewFolder
```
入力: FolderName:String FolderPath:FolderObject
出力: Folder:FolderObject=>
ON ERROR可: CreateFolderError, EmptyNewFolderPathAndNameError, FolderNotFoundError

## Folder.Delete [A]
```
Folder.Delete Folder: $fx'C:\temp'
```
入力: Folder:FolderObject
ON ERROR可: DeleteFolderError, FolderNotFoundError

## Folder.Empty [A]
```
Folder.Empty Folder: $fx'C:\temp'
```
入力: Folder:FolderObject
ON ERROR可: EmptyFolderError, FolderNotFoundError

## Folder.GetFiles [A]
```
Folder.GetFiles Folder: $fx'C:\temp' FileFilter: $fx'*' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> Files
```
入力: FailOnAccessDenied:Boolean FileFilter:String Folder:FolderObject IncludeSubfolders:Boolean SortBy1:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortBy2:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortBy3:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortDescending1:Boolean SortDescending2:Boolean SortDescending3:Boolean
出力: Files:List=>
ON ERROR可: FolderNotFoundError, RetrieveFilesError

## Folder.GetSpecialFolder [A]
```
Folder.GetSpecialFolder SpecialFolder: Folder.SpecialFolder.DesktopDirectory SpecialFolderPath=> SpecialFolderPath
```
入力: SpecialFolder:SpecialFolder{Programs,Personal,Favorites,Startup,Recent,SendTo,StartMenu,MyMusic,DesktopDirectory,Templates,ApplicationData,LocalApplicationData,InternetCache,Cookies,History,CommonApplicationData,System,ProgramFiles,MyPictures,CommonProgramFiles}
出力: SpecialFolderPath:FolderObject=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Folder.GetSubfolders [A]
```
Folder.GetSubfolders Folder: $fx'C:\temp' FolderFilter: $fx'*' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Subfolders=> Folders
```
入力: FailOnAccessDenied:Boolean Folder:FolderObject FolderFilter:String IncludeSubfolders:Boolean SortBy1:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortBy2:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortBy3:SortBy{NoSort,FullName,RootPath,Directory,Name,NameWithoutExtension,Extension,Size,CreationTime,LastAccessed,LastModified,IsHidden,IsSystem,IsReadOnly,IsArchive,Exists} SortDescending1:Boolean SortDescending2:Boolean SortDescending3:Boolean
出力: Subfolders:List=>
ON ERROR可: FolderNotFoundError, RetrieveSubfoldersError

### Folder.IfFolderExists のセレクター: DoesNotExist, Exists

## Folder.IfFolderExists.DoesNotExist [C]
```
IF (Folder.IfFolderExists.DoesNotExist Path: $fx'C:\temp') THEN
```
入力: !Path:FolderObject
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: CheckMode=DoesNotExist

## Folder.IfFolderExists.Exists [C]
```
IF (Folder.IfFolderExists.Exists Path: $fx'C:\temp') THEN
```
入力: !Path:FolderObject
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: CheckMode=Exists

## Folder.Move [A]
```
Folder.Move Folder: $fx'C:\temp' Destination: $fx'C:\temp' MovedFolder=> MovedFolder
```
入力: Destination:FolderObject Folder:FolderObject
出力: MovedFolder:FolderObject=>
ON ERROR可: FolderNotFoundError, InvalidDestinationFolderError, MoveFolderError

## Folder.Rename [A]
```
Folder.Rename Folder: $fx'C:\temp' NewName: $fx'example' RenamedFolder=> RenamedFolder
```
入力: Folder:FolderObject NewName:String
出力: RenamedFolder:FolderObject=>
ON ERROR可: FolderNotFoundError, RenameFolderError
