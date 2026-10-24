# Robin: Email

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Email.ProcessEmails のセレクター: Delete, MarkAsUnread, MarkAsUnreadAndMove, Move

## Email.ProcessEmails.Move [A]
```
Email.ProcessEmails.Move IMAPServer: $fx'imap.test.com' Port: 993 EnableSSL: True Username: $fx'example' Password: $fx'password' AcceptUntrustedCertificates: False EmailsToProcess: FileList MailFolder: $fx'example'
```
入力: EmailsToProcess:List MailFolder:String AcceptUntrustedCertificates:Boolean EnableSSL:Boolean Password:EncryptableObject Port:Int32 Username:String !IMAPServer:String
ON ERROR可: ConnectToImapServerError, InvalidMailFolderError, ProcessEmailsError
固定: Operation=Move

### Email.RetrieveEmails のセレクター: Retrieve, RetrieveAndSaveAttachments

## Email.RetrieveEmails.Retrieve [A]
```
Email.RetrieveEmails.Retrieve IMAPServer: $fx'imap.test.com' Port: 993 EnableSSL: True Username: $fx'example' Password: $fx'password' AcceptUntrustedCertificates: False MailFolder: $fx'example' MailsToRetrieve: Email.RetrieveMessagesMode.All MarkAsRead: True RetrievedEmails=> RetrievedEmails
```
入力: BodyContains:String FromContains:String MailFolder:String MailsToRetrieve:RetrieveMessagesMode{All,Unread,Read} MarkAsRead:Boolean SubjectContains:String ToContains:String AcceptUntrustedCertificates:Boolean EnableSSL:Boolean Password:EncryptableObject Port:Int32 Username:String !IMAPServer:String
出力: RetrievedEmails:List=>
ON ERROR可: ConnectToImapServerError, ImapServerAuthenticationError, InvalidMailFolderError, RetrieveEmailsError, SaveAttachmentsError
固定: SaveAttachments=DoNotSave

## Email.RetrieveEmails.RetrieveAndSaveAttachments [A]
```
Email.RetrieveEmails.RetrieveAndSaveAttachments AcceptUntrustedCertificates: False ToContains: $fx'example' SubjectContains: $fx'example' EnableSSL: True Username: $fx'example' Port: 993 Password: $fx'password' SaveAttachmentsInto: $fx'C:\temp' FromContains: $fx'example' BodyContains: $fx'example' IMAPServer: $fx'example' MailFolder: $fx'example' MarkAsRead: True MailsToRetrieve: Email.RetrieveMessagesMode.All RetrievedEmails=> RetrievedEmails
```
入力: !AcceptUntrustedCertificates:Boolean ToContains:String SubjectContains:String !EnableSSL:Boolean !Username:String !Port:Int32 !Password:EncryptableObject !SaveAttachmentsInto:FolderObject FromContains:String BodyContains:String !IMAPServer:String !MailFolder:String !MarkAsRead:Boolean !MailsToRetrieve:RetrieveMessagesMode{All,Unread,Read}
出力: RetrievedEmails:List<MailMessageObject>=>RetrievedEmails
ON ERROR可: ConnectToImapServerError, ImapServerAuthenticationError, InvalidMailFolderError, RetrieveEmailsError, SaveAttachmentsError
固定: SaveAttachments=Save

### Email.SendEmail のセレクター: AuthenticateAndSend, Send

## Email.SendEmail.AuthenticateAndSend [A]
```
Email.SendEmail.AuthenticateAndSend SendFrom: $fx'example' SendTo: $fx'example' SenderDisplayName: $fx'example' Password: $fx'password' Username: $fx'example' Subject: $fx'example' AcceptUntrustedCertificates: False SMTPServer: $fx'example' Attachments: SelectedFiles EnableSSL: False Port: 25 CC: $fx'example' IsBodyHtml: False BCC: $fx'example' Body: $fx'example'
```
入力: !SendFrom:String !SendTo:String SenderDisplayName:String !Password:EncryptableObject !Username:String Subject:String !AcceptUntrustedCertificates:Boolean !SMTPServer:String Attachments:List<FileObject> !EnableSSL:Boolean !Port:Int32 CC:String !IsBodyHtml:Boolean BCC:String !Body:String
ON ERROR可: AttachmentNotFoundError, InvalidEmailAddressError, SendEmailError
固定: NeedsAuthentication=True

## Email.SendEmail.Send [A]
```
Email.SendEmail.Send SMTPServer: $fx'smtp.test.com' Port: 25 EnableSSL: False AcceptUntrustedCertificates: False SendFrom: $fx'example' SendTo: $fx'example' Body: $fx'' IsBodyHtml: False
```
入力: EnableSSL:Boolean Port:Int32 Attachments:List BCC:String Body:String CC:String IsBodyHtml:Boolean SenderDisplayName:String SendFrom:String SendTo:String Subject:String AcceptUntrustedCertificates:Boolean !SMTPServer:String
ON ERROR可: AttachmentNotFoundError, InvalidEmailAddressError, SendEmailError
固定: NeedsAuthentication=False
