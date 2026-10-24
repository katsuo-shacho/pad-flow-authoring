# FTP actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/ftp （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Use the FTP action group to upload and download files and manipulate directories on FTP servers. To establish an FTP connection, use the Open FTP connection action. The following example has a specified host, port, and credentials. Additionally, the set timeout makes the action fail if the connection isn't established on time. Download files using the Download file(s) from FTP action. The following example shows the connection variable in use and the selected destination folder. The remote file has also been specified and set to overwrite existing files in the same location. Upload files using

## Open FTP connection  `#openconnection`
This action establishes a specific connection to a remote FTP server, and stores that connection as a variable for later use.
入力:
- Host: Text value — Enter the FTP server address here.
- Port(任意): Numeric value = 21 — Enter the FTP server port here.
- Active mode: Boolean value = False — Specify the mode of the connection
- Username: Text value — Specify the username of the FTP account to use
- Password(任意): Direct encrypted input or Text value — Specify the password of the FTP account to use
- Timeout(任意): Numeric value = 10 — Set the time in seconds that you want to wait for the connection to be established before the action fails
出力:
- FTPConnection: FTP connection — The FTP connection
例外: Login failure error; Connection error

## List FTP directory  `#listdirectory`
This action returns the subdirectories and files contained in the current directory of an FTP connection.
入力:
- Connection: FTP connection — The FTP connection
- Path(任意): Text value — The path that you want to list.
出力:
- Directories: List of FTP directories — The listed directories
- Files: List of FTP files — The listed files
例外: Listing error; Not connected error; Directory doesn't exist error

## Open secure FTP connection  `#opensecureconnection`
This action establishes a specific secure connection to a remote FTP server, and stores that connection as a variable for later use.
入力:
- Host: Text value — Enter the FTP server address here.
- Port(任意): Numeric value = 22 — Enter the FTP server port here.
- Active mode: Boolean value = True — Specify the mode of the connection
- Secure FTP Protocol: SFTP, FTPS explicit, FTPS implicit = SFTP — Choose the FTP protocol you wish to use to encrypt your connection
- Authentication method: Username and password, Private key, Private key and passphrase = Username and password — Choose the method you wish to use to authenticate yourself on the FTP server
- User name: Text value — Specify the username of the FTP account to use
- Password(任意): Direct encrypted input or Text value — Specify the password of the FTP account you wish to use
- Path to private key: Text value — Enter the file path to the private-key to be used for authentication
- Private key pass phrase(任意): Direct encrypted input or Text value — Enter a variable containing the private-key pass phrase here
- Timeout(任意): Numeric value = 10 — Set the time in seconds that you want to wait for the connection to be established before the action fails
出力:
- SftpConnection: FTP connection — SFTP connection
例外: Login failure error; Connection error

## Close connection  `#closeconnection`
This action closes an open FTP connection.
入力:
- Connection: FTP connection — The FTP connection
例外: Not connected error

## Change working directory  `#changeworkingdirectory`
This action sets the current working directory for an FTP connection.
入力:
- Connection: FTP connection — The FTP connection
- Set working directory to: Text value — Set the path to be set as the working directory
例外: Not connected error; Directory doesn't exist error; Can't change working directory error

## Download file(s) from FTP  `#downloadfiles`
Downloads one or more files from an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Download into folder: Folder — The folder to be the destination of the file(s) that will be downloaded
- File(s) to download: List of FTP files — The file(s) to download
- Transfer type: Auto, Binary, ASCII = Auto — Enter ASCII or binary to specify the method for downloading a single file. If the file type is uncertain, or more than one is downloaded, choose Auto to follow the transfer rules specified in options
- If file exists: Overwrite, Do not download, Download with unique name = Overwrite — Specify what to do if the file already exists. Overwrite writes over the original file so you can't access it anymore, and download with unique name adds an underscore and a sequential number to the end
例外: Not connected error; Remote file doesn't exist error; Directory doesn't exist error; FTP connection aborted error; Can't download file error

## Download folder(s) from FTP  `#downloadfolders`
Downloads one or more folders from an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Folder(s) to download: List of FTP directories — The name of the folder path(s), or FTP folder(s) to download
- Download into local folder: Folder — The full path of the destination of the FTP folder(s) you're downloading
例外: Not connected error; Remote directory doesn't exist error; Directory doesn't exist error; FTP connection aborted error; Can't download directory error

## Upload File(s) to FTP  `#uploadfiles`
Uploads one or more files to an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- File(s) to upload: List of Files — The file(s) to upload
- Remote location(任意): Text value — The location where the files should be uploaded
- Transfer type: Auto, Binary, ASCII = Auto — Enter ASCII or binary to specify the method for downloading a single file. If you're not sure what type the file will be, or if you're downloading more than one, choose Auto to follow the transfer rules specified in Options
- If file exists: Overwrite, Do not download, Download with unique name = Overwrite — Specify what to do if the file already exists. Overwrite writes over the original file so you can't access it anymore, and Download with Unique Name adds an underscore and a sequential number to the end
例外: Not connected error; File not found error; FTP connection aborted error; Upload file error

## Upload folder(s) to FTP  `#uploadfolders`
Uploads one or more folders to an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Folder(s) to upload: List of Folders — The folder(s) to upload. The folders being uploaded shouldn't already exist within the active directory of the FTP server
- Remote location: Text value — The location where the folders should be uploaded
例外: Not connected error; Remote directory doesn't exist error; FTP connection aborted error; Upload directory error

## Delete FTP file  `#deletefiles`
Deletes one or more files from an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Files to delete: List of FTP files — The files to delete
例外: Not connected error; File not found error; Can't delete file error

## Rename FTP File  `#renamefile`
Renames a file that resides on an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- File to rename: FTP file — The file to rename
- New file name: Text value — The new name for the file. If you enter a name with a path, the file will also be moved to that location. If the location doesn't exist, it will throw an exception
例外: Not connected error; Can't rename file error; File not found error

## Create FTP directory  `#createdirectory`
Creates a directory on an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- New directory: FTP directory — The new directory. If a path is specified, all of the new folders leading to the new directory will be created
例外: Access denied error; File exists error; Create directory error; Directory doesn't exist error; Not connected error

## Delete FTP directory  `#deletedirectory`
Deletes a directory from an FTP server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Directory to delete: FTP directory — The folder to be deleted. Everything in the folder will be deleted as well
例外: Delete directory error; Remote directory doesn't exist error; Working directory change error; Not connected error

## Invoke FTP command  `#invokecommand`
Invokes the given literal FTP command on the server.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an open FTP connection action
- FTP command: Text value — The command to run along with any arguments. For example, you could run FEAT, or CHMOD here
- Valid reply code(s)(任意): Text value — The code(s) that could be returned by the command, separated by semi-colon. If the FTP command returns a code that wasn't entered here, this action will throw an exception. Only applies over simple FTP or FTPS connections
出力:
- ReplyCode: Text value — The actual code that was returned. Only applies over simple FTP or FTPS connections
- ReplyText: Text value — The text returned by the FTP server
例外: Invoke command error; Not connected error

## Synchronize directories  `#synchronizedirectoryaction`
Synchronize the files and subdirectories of a given Folder with a given remote FTP directory.
入力:
- FTP connection: FTP connection — The FTP connection to work with. This variable must have been previously specified in an Open FTP connection action
- Synchronization direction: Remote -> local (Download), Local -> remote (Upload) = Remote -> local (Download) — Direction of the Synchronization method. Whether the local folder will be synchronized to the remote directory (DOWNLOAD) or the remote directory will be synchronized to the local folder (UPLOAD)
- Files to sync: All files, Only files matching the file filter, Only files not matching the file filter = All files — Choose whether you want to synchronize all files, or you want to use a file filter to include or exclude a specific set of files
- File filter: Text value = * — File-name pattern that controls which files will be included or excluded. This option allows wildcards such as "*.txt", "document?.doc". The option also allows for multiple filters by using coma as a separator, "*.txt,*.pdf,document?"
- Local folder: Folder — Name of the local folder to be synchronized
- FTP directory(任意): FTP directory = / — Name of the FTP directory to be synchronized
- Delete if source is absent: Boolean value = False — This option will delete a file or folder that exists in the target directory and not the source.
- Include subdirectories: Boolean value = True — This option will include subdirectories in the synchronization process.
- Time difference in hours(任意): Numeric value = 0 — Time difference in hours of the remote server in case it operates on a different Time Zone.
- Time difference in minutes(任意): Numeric value = 0 — Time difference in Minutes of the remote server in case it operates on a different Time Zone.
- Time difference ahead: Boolean value = True — Specify whether the server's time zone is ahead or not.
出力:
- FtpFilesAdded: List of FTP files — List of FTP files that initially existed in the source and after the synchronization process were added to the target.
- FtpFilesModified: List of FTP files — List of FTP files that initially existed in both the source and the target and after the synchronization process were added to the target.
- FtpFilesDeleted: List of FTP files — List of FTP files that initially existed in the target directory and after the synchronization process were deleted.
- FilesAdded: List of Files — List of files that initially existed in the source and after the synchronization process were added to the target.
- FilesModified: List of Files — List of files that initially existed in both the source and the target and after the synchronization process were added to the target.
- FilesDeleted: List of Files — List of files that initially existed in the target directory and after the synchronization process were deleted.
例外: Listing error; Not connected error; File not found error; FTP connection aborted error; Upload file error; Remote file doesn't exist error; Can't download file error; Delete directory error; Synchronization failed error
