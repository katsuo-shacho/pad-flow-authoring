# Robin: FTP

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## FTP.ChangeWorkingDirectory [A]
```
FTP.ChangeWorkingDirectory Connection: SftpConnection SetWorkingDirectoryTo: $fx'example'
```
入力: SetWorkingDirectoryTo:String Connection:FtpConnectionBase
ON ERROR可: CannotChangeWorkingDirectoryError, DirectoryDoesNotExistError, NotConnectedError

## FTP.CloseConnection [A]
```
FTP.CloseConnection Connection: SfTPConnection
```
入力: Connection:FtpConnectionBase
ON ERROR可: NotConnectedError

## FTP.CreateDirectory [A]
```
FTP.CreateDirectory Connection: SftpConnection Directory: $fx'/testdir'
```
入力: Directory:FtpFolderObject Connection:FtpConnectionBase
ON ERROR可: AccessDeniedError, CreateDirectoryError, DirectoryDoesNotExistError, FileExistsError, NotConnectedError

## FTP.DeleteDirectory [A]
```
FTP.DeleteDirectory Connection: SftpConnection Directory: $fx'/testdir'
```
入力: Directory:FtpFolderObject Connection:FtpConnectionBase
ON ERROR可: DeleteDirectoryError, NotConnectedError, RemoteDirectoryDoesNotExistError, WorkingDirectoryChangeError

## FTP.DeleteFiles [A]
```
FTP.DeleteFiles Connection: SftpConnection Files: FileList
```
入力: Files:List Connection:FtpConnectionBase
ON ERROR可: CannotDeleteFileError, FileNotFoundError, NotConnectedError

## FTP.DownloadFiles [A]
```
FTP.DownloadFiles Connection: SftpConnection DownloadInto: $fx'C:\temp' RemoteFilePaths: FileList TransferType: FTP.FtpTransferType.Auto IfFileExists: FTP.IfFtpFileExists.Overwrite
```
入力: DownloadInto:FolderObject IfFileExists:IfFtpFileExists{Overwrite,Skip,TransferWithUniqueName} RemoteFilePaths:List TransferType:FtpTransferType{Auto,Binary,Ascii} Connection:FtpConnectionBase
ON ERROR可: CannotDownloadFileError, DirectoryDoesNotExistError, FTPConnectionAbortedError, NotConnectedError, RemoteFileDoesNotExistError

## FTP.DownloadFolders [A]
```
FTP.DownloadFolders Connection: SftpConnection RemotePath: FileList DownloadInto: $fx'C:\temp'
```
入力: DownloadInto:FolderObject RemotePath:List Connection:FtpConnectionBase
ON ERROR可: CannotDownloadDirectoryError, DirectoryDoesNotExistError, FTPConnectionAbortedError, NotConnectedError, RemoteDirectoryDoesNotExistError

## FTP.InvokeCommand [A]
```
FTP.InvokeCommand Connection: SftpConnection Command: $fx'example' ValidReplyCodes: $fx'' ReplyCode=> ReplyCode ReplyText=> ReplyText
```
入力: Command:String ValidReplyCodes:String Connection:FtpConnectionBase
出力: ReplyCode:String=> ReplyText:String=>
ON ERROR可: InvokeCommandError, NotConnectedError

## FTP.ListDirectory [A]
```
FTP.ListDirectory Connection: SftpConnection Path: $fx'' Directories=> Directories Files=> Files
```
入力: Path:String Connection:FtpConnectionBase
出力: Directories:List=> Files:List=>
ON ERROR可: DirectoryDoesNotExistError, ListingError, NotConnectedError

## FTP.OpenConnection [A]
```
FTP.OpenConnection Host: $fx'localhost' Port: 21 ActiveMode: False Username: $fx'test' Timeout: 10 Connection=> FTPConnection
```
入力: !Port:Int32 !Timeout:Int32 !Username:String !ActiveMode:Boolean !Host:String Password:EncryptableObject
出力: Connection:FtpConnectionBase=>FTPConnection
ON ERROR可: ConnectionError, LoginFailureError

### FTP.OpenSecureConnection のセレクター: ConnectWithFtpsExplicit, ConnectWithFtpsImplicit, ConnectWithSftpPrivateKey, ConnectWithSftpPrivateKeyAndPassPhrase, ConnectWithSftpUsernameAndPassword

## FTP.OpenSecureConnection.ConnectWithFtpsExplicit [A]
```
FTP.OpenSecureConnection.ConnectWithFtpsExplicit Port: 22 Username: $fx'example' Timeout: 10 ActiveMode: True AcceptUntrustedCertificates: False Password: $fx'password' Host: $fx'example' SftpConnection=> SftpConnection
```
入力: !Port:Int32 !Username:String !Timeout:Int32 !ActiveMode:Boolean !AcceptUntrustedCertificates:Boolean Password:EncryptableObject !Host:String
出力: SftpConnection:FtpConnectionBase=>SftpConnection
ON ERROR可: ConnectionError, LoginFailureError
固定: SecureFtpProtocol=FTPSExplicit

## FTP.OpenSecureConnection.ConnectWithFtpsImplicit [A]
```
FTP.OpenSecureConnection.ConnectWithFtpsImplicit Port: 22 Username: $fx'example' Timeout: 10 ActiveMode: True AcceptUntrustedCertificates: False Password: $fx'password' Host: $fx'example' SftpConnection=> SftpConnection
```
入力: !Port:Int32 !Username:String !Timeout:Int32 !ActiveMode:Boolean !AcceptUntrustedCertificates:Boolean Password:EncryptableObject !Host:String
出力: SftpConnection:FtpConnectionBase=>SftpConnection
ON ERROR可: ConnectionError, LoginFailureError
固定: SecureFtpProtocol=FTPSImplicit

## FTP.OpenSecureConnection.ConnectWithSftpPrivateKey [A]
```
FTP.OpenSecureConnection.ConnectWithSftpPrivateKey Port: 22 Username: $fx'example' Timeout: 10 PathToPrivateKey: $fx'example' Host: $fx'example' SftpConnection=> SftpConnection
```
入力: !Port:Int32 !Username:String !Timeout:Int32 !PathToPrivateKey:String !Host:String
出力: SftpConnection:FtpConnectionBase=>SftpConnection
ON ERROR可: ConnectionError, LoginFailureError
固定: SecureFtpProtocol=SFTP, AuthenticationMethod=PrivateKey

## FTP.OpenSecureConnection.ConnectWithSftpPrivateKeyAndPassPhrase [A]
```
FTP.OpenSecureConnection.ConnectWithSftpPrivateKeyAndPassPhrase PrivateKeyPassPhrase: $fx'password' Port: 22 Username: $fx'example' Timeout: 10 PathToPrivateKey: $fx'example' Host: $fx'example' SftpConnection=> SftpConnection
```
入力: PrivateKeyPassPhrase:EncryptableObject !Port:Int32 !Username:String !Timeout:Int32 !PathToPrivateKey:String !Host:String
出力: SftpConnection:FtpConnectionBase=>SftpConnection
ON ERROR可: ConnectionError, LoginFailureError
固定: SecureFtpProtocol=SFTP, AuthenticationMethod=PrivateKeyAndPassphrase

## FTP.OpenSecureConnection.ConnectWithSftpUsernameAndPassword [A]
```
FTP.OpenSecureConnection.ConnectWithSftpUsernameAndPassword Host: $fx'example' Port: 22 Username: $fx'example' Timeout: 10 Password: $fx'password' SftpConnection=> SftpConnection
```
入力: Host:String Password:EncryptableObject Port:Int32 Timeout:Int32 Username:String
出力: SftpConnection:FtpConnectionBase=>
ON ERROR可: ConnectionError, LoginFailureError
固定: SecureFtpProtocol=SFTP, AuthenticationMethod=UsernameAndPassword

## FTP.RenameFile [A]
```
FTP.RenameFile Connection: SftpConnection FileToRename: $fx'/test.txt' NewFileName: $fx'example'
```
入力: FileToRename:FtpFileObject NewFileName:String Connection:FtpConnectionBase
ON ERROR可: CannotRenameFileError, FileNotFoundError, NotConnectedError

### FTP.SynchronizeDirectory のセレクター: SynchronizeDownloadAll, SynchronizeDownloadExcludeFilter, SynchronizeDownloadIncludeFilter, SynchronizeUploadAll, SynchronizeUploadExcludeFilter, SynchronizeUploadIncludeFilter

## FTP.SynchronizeDirectory.SynchronizeDownloadAll [A]
```
FTP.SynchronizeDirectory.SynchronizeDownloadAll Connection: SftpConnection LocalFolder: $fx'C:\temp' FtpDirectory: $fx'/' DeleteIfSourceAbsent: False IncludeSubdirectories: True TimeDifferenceHours: 0 TimeDifferenceMinutes: 0 TimeDifferenceAhead: True FilesAdded=> FilesAdded FilesModified=> FilesModified FilesDeleted=> FilesDeleted
```
入力: DeleteIfSourceAbsent:Boolean FtpDirectory:FtpFolderObject IncludeSubdirectories:Boolean LocalFolder:FolderObject TimeDifferenceAhead:Boolean TimeDifferenceHours:Int32 TimeDifferenceMinutes:Int32 Connection:FtpConnectionBase
出力: FilesAdded:List=> FilesDeleted:List=> FilesModified:List=>
ON ERROR可: CannotDownloadFileError, DeleteDirectoryError, FileNotFoundError, FTPConnectionAbortedError, ListingError, NotConnectedError, RemoteFileDoesNotExistError, SynchronizationFailedError, UploadFileError
固定: SynchronizationDirection=Download, FilesToSync=All

## FTP.UploadFiles [A]
```
FTP.UploadFiles Connection: SftpConnection Files: FileList RemoteLocation: $fx'' TransferType: FTP.FtpTransferType.Auto IfFileExists: FTP.IfFtpFileExists.Overwrite
```
入力: Files:List IfFileExists:IfFtpFileExists{Overwrite,Skip,TransferWithUniqueName} RemoteLocation:String TransferType:FtpTransferType{Auto,Binary,Ascii} Connection:FtpConnectionBase
ON ERROR可: FileNotFoundError, FTPConnectionAbortedError, NotConnectedError, UploadFileError

## FTP.UploadFolders [A]
```
FTP.UploadFolders Connection: SftpConnection Folders: FileList RemoteLocation: $fx'example'
```
入力: Folders:List RemoteLocation:String Connection:FtpConnectionBase
ON ERROR可: FTPConnectionAbortedError, NotConnectedError, RemoteDirectoryDoesNotExistError, UploadDirectoryError
