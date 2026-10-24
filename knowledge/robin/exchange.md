# Robin: Exchange

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Exchange.ConnectToExchangeServer のセレクター: Connect, ConnectToServer, ConnectToServerWithCredentials, ConnectWithCredentials

## Exchange.ConnectToExchangeServer.Connect [A]
```
Exchange.ConnectToExchangeServer.Connect ServerVersion: Exchange.ServerVersion.Exchange2013_SP1 Timeout: 30 EmailAddress: $'''example''' Connection=> ExchangeConnection
```
入力: !ServerVersion:ServerVersion{Exchange2010,Exchange2010_SP1,Exchange2010_SP2,Exchange2013,Exchange2013_SP1} !Timeout:Int32 !EmailAddress:String
出力: Connection:ExchangeConnectionHandle=>ExchangeConnection
ON ERROR可: ConnectToExchangeServerError
固定: ConnectionType=AutoDiscover, CredentialsMode=ExchangeDefault

## Exchange.ConnectToExchangeServer.ConnectToServer [A]
```
Exchange.ConnectToExchangeServer.ConnectToServer ServerVersion: Exchange.ServerVersion.Exchange2013_SP1 ServerAddress: $'''example''' Timeout: 30 Connection=> ExchangeConnection
```
入力: !ServerVersion:ServerVersion{Exchange2010,Exchange2010_SP1,Exchange2010_SP2,Exchange2013,Exchange2013_SP1} !ServerAddress:String !Timeout:Int32
出力: Connection:ExchangeConnectionHandle=>ExchangeConnection
ON ERROR可: ConnectToExchangeServerError
固定: CredentialsMode=ExchangeDefault, ConnectionType=ExchangeServerAddress

## Exchange.ConnectToExchangeServer.ConnectToServerWithCredentials [A]
```
Exchange.ConnectToExchangeServer.ConnectToServerWithCredentials ServerVersion: Exchange.ServerVersion.Exchange2013_SP1 ServerAddress: $'''example''' Username: $'''example''' Timeout: 30 Password: $'''password''' Domain: $'''example''' Connection=> ExchangeConnection
```
入力: !ServerVersion:ServerVersion{Exchange2010,Exchange2010_SP1,Exchange2010_SP2,Exchange2013,Exchange2013_SP1} !ServerAddress:String !Username:String !Timeout:Int32 !Password:EncryptableObject Domain:String
出力: Connection:ExchangeConnectionHandle=>ExchangeConnection
ON ERROR可: ConnectToExchangeServerError
固定: CredentialsMode=UserDefined, ConnectionType=ExchangeServerAddress

## Exchange.ConnectToExchangeServer.ConnectWithCredentials [A]
```
Exchange.ConnectToExchangeServer.ConnectWithCredentials ServerVersion: Exchange.ServerVersion.Exchange2013_SP1 Username: $'''example''' Timeout: 30 Password: $'''password''' EmailAddress: $'''example''' Domain: $'''example''' Connection=> ExchangeConnection
```
入力: !ServerVersion:ServerVersion{Exchange2010,Exchange2010_SP1,Exchange2010_SP2,Exchange2013,Exchange2013_SP1} !Username:String !Timeout:Int32 !Password:EncryptableObject !EmailAddress:String Domain:String
出力: Connection:ExchangeConnectionHandle=>ExchangeConnection
ON ERROR可: ConnectToExchangeServerError
固定: ConnectionType=AutoDiscover, CredentialsMode=UserDefined

### Exchange.ProcessExchangeMessages のセレクター: DeleteEmails, MarkEmailsAsUnread, MoveEmails, MoveEmailsToAccount, MoveEmailsToAccountFolder, MoveEmailsToFolder

## Exchange.ProcessExchangeMessages.MoveEmails [A]
```
Exchange.ProcessExchangeMessages.MoveEmails Connection: ExchangeConnection EmailsToProcess: FileList ExchangeFolder: Exchange.Folder.Inbox
```
入力: Connection:ExchangeConnectionHandle EmailsToProcess:List ExchangeFolder:Folder{Inbox,DeletedItems,Drafts,Outbox,SentItems,JunkEmail}
ON ERROR可: MailFolderNotFoundError, ProcessEmailMessagesError
固定: MoveToCustomFolder=False, MailboxType=Personal, Operation=Move

### Exchange.RetrieveExchangeMessages のセレクター: RetrieveEmails, RetrieveEmailsAndSaveAttachments, RetrieveEmailsFromAccount, RetrieveEmailsFromAccountAndFolder, RetrieveEmailsFromAccountAndFolderAndSaveAttachments, RetrieveEmailsFromAccountAndSaveAttachments, RetrieveEmailsFromFolder, RetrieveEmailsFromFolderAndSaveAttachments

## Exchange.RetrieveExchangeMessages.RetrieveEmails [A]
```
Exchange.RetrieveExchangeMessages.RetrieveEmails Connection: ExchangeConnection ExchangeFolder: Exchange.Folder.Inbox RetrieveMode: Exchange.RetrieveMessagesMode.Unread MarkAsRead: True EmailMessages=> RetrievedEmails
```
入力: !RetrieveMode:RetrieveMessagesMode{All,Unread,Read} !MarkAsRead:Boolean ToContains:String SubjectContains:String !Connection:ExchangeConnectionHandle BodyContains:String !ExchangeFolder:Folder{Inbox,DeletedItems,Drafts,Outbox,SentItems,JunkEmail} FromContains:String
出力: EmailMessages:List<ExchangeMailMessage>=>RetrievedEmails
ON ERROR可: InvalidMailFolderError, RetrieveEmailMessagesError, SaveAttachmentsError
固定: FromCustomFolder=False, MailboxType=Personal, AttachmentsOptions=DoNotSave

## Exchange.SendMessage [A]
```
Exchange.SendMessage Connection: ExchangeConnection SendFrom: $'''example''' SendTo: $'''example''' IsBodyHtml: False
```
入力: Attachments:List BCC:String Body:String CC:String Connection:ExchangeConnectionHandle IsBodyHtml:Boolean SenderDisplayName:String SendFrom:String SendTo:String Subject:String
ON ERROR可: AttachmentNotFoundError, SendEmailMessageError
