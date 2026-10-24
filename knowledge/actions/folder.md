# Folder actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/folder （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate folder actions enable you to manipulate and organize folders. The Get special folder action retrieves the paths for commonly used directories that vary among users and machines. The following example retrieves the desktop directory and stores it in a variable. You can now use the %SpecialFolderPath% variable any time it's necessary, regardless of the user who runs the flow or the computer on which it runs. Create new folders with the Create folder action. To get a list of a folder's contents, use the Get subfolders in folder action. This action retrieves a list of folders locate

## If folder exists  `#iffolderexistsaction`
Mark the beginning of a conditional block of actions depending on whether a folder exists or not.
入力:
- If folder: Exists, Doesn't exist = Exists — Choose the state of the folder to check
- Folder path: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to check its state

## Get files in folder  `#getfiles`
Retrieve the list of files in a folder.
入力:
- Folder: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to retrieve the list of files from
- File filter: Text value = * — Choose a filter to limit the files retrieved. This parameter allows wild cards, for example, *.txt or document?.doc. To allow for multiple file filters, separate the choices with a semi-colon, for example, *.txt;*.exe.
- Include subfolders: Boolean value = False — Specify whether to look into subfolders as well
- Fail upon denied access to any subfolder: Boolean value = True — Specify whether to throw an error when trying to get files of a folder with no access rights or ignore those folders
- Sort by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results and by which criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
- Then by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results by a second criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
- Then by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results by a third criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
出力:
- Files: List of Files — The retrieved files as a list of file objects
例外: Folder doesn't exist; Can't retrieve list of files

## Get subfolders in folder  `#getsubfolders`
Retrieve the list of subfolders in a folder.
入力:
- Folder: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to retrieve the list of subfolders from
- Folder filter: Text value = * — Choose a filter to limit the subfolders retrieved. This parameter allows wild cards, for example, Doc* or Document?. To allow for multiple folder filters, separate the choices with a semi-colon, for example, Doc*;*.
- Include subfolders: Boolean value = False — Specify whether to look into the subfolders and retrieve their subfolders (and so on) as well
- Fail upon denied access to any subfolder: Boolean value = True — Specify whether to throw an error when trying to get subfolders of a folder with no access rights or ignore those folders
- Sort by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results and by which criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
- Then by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results by a second criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
- Then by: No sort, Full name, Root path, Directory, Name, Name without extension, Extension, Size, Creation time, Last accessed, Last modified, Is hidden, Is system, Is read-only, Is archive, Exists = No sort — Specify whether to sort the results by a third criterion
- Descending: Boolean value = False — Specify whether to sort the items in descending or ascending order
出力:
- Folders: List of Folders — The retrieved subfolders as a list of folder objects
例外: Folder doesn't exist; Can't retrieve list of subfolders

## Create folder  `#create`
Create a new folder.
入力:
- Create new folder into: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to create a new folder in
- New folder name: Text value — Enter the text, or a text variable, to be the name of the new folder
出力:
- NewFolder: Folder — The created folder object (which is a representation and can access the folder and all its information)
例外: Folder doesn't exist; Can't create folder; New folder path and name are empty

## Delete folder  `#delete`
Delete an existing folder and its contents (files and subfolders).
入力:
- Folder to delete: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to delete. Remember that all contents of that folder and its subfolders are deleted too.
例外: Folder doesn't exist; Can't delete folder

## Empty folder  `#empty`
Delete all the contents of a folder (files and subfolders) without deleting the folder itself.
入力:
- Folder to empty: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to delete its contents
例外: Folder doesn't exist; Can't delete folder's contents

## Copy folder  `#copy`
Copy a folder into a destination folder.
入力:
- Folder to copy: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to copy. If the folder path ends with a \ only the contents of the folder (files + subfolders) are copied. Otherwise, the folder itself (along with its contents) is copied as a subfolder into the destination folder.
- Destination folder: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to be the destination folder
- If folder exists: Do nothing, Overwrite = Do nothing — Specify whether to overwrite files or not copy them at all, if the destination folder already exists. If the folder exists, but the files have different names, the old files still remain in the folder.
出力:
- CopiedFolder: Folder — The copied folder object (which is a representation and can access the folder and all its information)
例外: Folder doesn't exist; Destination folder doesn't exist; Can't copy folder

## Move folder  `#move`
Move an existing folder into a destination folder.
入力:
- Folder to move: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to move
- Destination folder: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to be the destination folder
出力:
- MovedFolder: Folder — The moved folder object (which is a representation and can access the folder and all its information)
例外: Folder doesn't exist; Destination folder doesn't exist; Can't move folder

## Rename folder  `#rename`
Change the name of a folder.
入力:
- Folder to rename: Folder — Enter or choose the full path of the folder, or a variable containing the folder, to change its name
- New folder name: Text value — Enter the text, or a text variable, to be the new folder name
出力:
- RenamedFolder: Folder — The renamed folder object (which is a representation and can access the folder and all its information)
例外: Folder doesn't exist; Can't rename folder

## Get special folder  `#getspecialfolder`
Retrieve the path of a Windows' special folder (such as Desktop, My Pictures, Internet Cache etc.).
入力:
- Special folder name: Programs, Personal, Favorites, Startup, Recent, Send To, Start Menu, Music, Desktop, Templates, Application Data, Local Application Data, Internet Cache, Cookies, History, Common Application Data, System, Program Files, Pictures, Common Program Files = Desktop — Choose the name of the special folder (like My Documents or Desktop). This option is independent of path, to find the special folder on any computer regardless of path specifics.
出力:
- SpecialFolderPath: Folder — The special folder object (which is a representation and can access the folder and all its information)
