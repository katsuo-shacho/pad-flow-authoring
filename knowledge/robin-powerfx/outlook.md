# Robin: Outlook

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Outlook.Close [A]
```
Outlook.Close Instance: OutlookInstance
```
入力: Instance:OutlookInstanceHandle
ON ERROR可: CloseOutlookError

## Outlook.Launch [A]
```
Outlook.Launch Instance=> OutlookInstance
```
出力: Instance:OutlookInstanceHandle=>
ON ERROR可: LaunchOutlookError

### Outlook.ProcessEmailMessages のセレクター: DeleteEmails, MarkEmailsAsUnread, MoveEmails

## Outlook.ProcessEmailMessages.DeleteEmails [A]
```
Outlook.ProcessEmailMessages.DeleteEmails Instance: OutlookInstance Account: $fx'example' EmailsToProcess: List
```
入力: !Instance:OutlookInstanceHandle !Account:String !EmailsToProcess:List<OutlookMailMessage>
ON ERROR可: MailFolderNotFoundError, OutlookAccountNotFoundError, ProcessEmailMessagesError
固定: Operation=Delete

## Outlook.ProcessEmailMessages.MarkEmailsAsUnread [A]
```
Outlook.ProcessEmailMessages.MarkEmailsAsUnread Instance: OutlookInstance Account: $fx'example' EmailsToProcess: List
```
入力: !Instance:OutlookInstanceHandle !Account:String !EmailsToProcess:List<OutlookMailMessage>
ON ERROR可: MailFolderNotFoundError, OutlookAccountNotFoundError, ProcessEmailMessagesError
固定: Operation=MarkAsUnread

## Outlook.ProcessEmailMessages.MoveEmails [A]
```
Outlook.ProcessEmailMessages.MoveEmails MailFolder: $fx'example' Instance: OutlookInstance Account: $fx'example' EmailsToProcess: List
```
入力: !MailFolder:String !Instance:OutlookInstanceHandle !Account:String !EmailsToProcess:List<OutlookMailMessage>
ON ERROR可: MailFolderNotFoundError, OutlookAccountNotFoundError, ProcessEmailMessagesError
固定: Operation=Move

### Outlook.RespondToMailMessage のセレクター: ForwardEmail, ReplyAllToEmail, ReplyToEmail

## Outlook.RespondToMailMessage.ReplyToEmail [A]
```
Outlook.RespondToMailMessage.ReplyToEmail Instance: OutlookInstance Account: $fx'test@test.com' MailMessage: MailMessage Body: $fx'test'
```
入力: Account:String Attachments:List Body:String Instance:OutlookInstanceHandle MailMessage:OutlookMailMessage
ON ERROR可: AttachmentNotFoundError, OutlookAccountNotFoundError, SendEmailMessageError
固定: ResponseAction=Reply

### Outlook.RetrieveEmailMessages のセレクター: RetrieveEmails, RetrieveEmailsAndSaveAttachments

## Outlook.RetrieveEmailMessages.RetrieveEmails [A]
```
Outlook.RetrieveEmailMessages.RetrieveEmails Instance: OutlookInstance Account: $fx'test@test.com' MailFolder: $fx'example' EmailsToRetrieve: Outlook.RetrieveMessagesMode.All MarkAsRead: True ReadBodyAsHtml: False
```
入力: BodyContains:String FromContains:String MailFolder:String MarkAsRead:Boolean SubjectContains:String ToContains:String !ReadBodyAsHtml:Boolean !Account:String !Instance:OutlookInstanceHandle !EmailsToRetrieve:RetrieveMessagesMode{All,Unread,Read}
出力: Messages:List<OutlookMailMessage>=>
ON ERROR可: InvalidMailFolderError, OutlookAccountNotFoundError, RetrieveEmailMessagesError, SaveAttachmentsDirectoryNotFoundError
固定: AttachmentsOptions=DoNotSave

## Outlook.RetrieveEmailMessages.RetrieveEmailsAndSaveAttachments [A]
```
Outlook.RetrieveEmailMessages.RetrieveEmailsAndSaveAttachments ReadBodyAsHtml: False MarkAsRead: True MailFolder: $fx'example' ToContains: $fx'example' SubjectContains: $fx'example' SaveAttachmentsInto: $fx'C:\temp' BodyContains: $fx'example' Account: $fx'example' Instance: OutlookInstance FromContains: $fx'example' EmailsToRetrieve: Outlook.RetrieveMessagesMode.All Messages=> RetrievedEmails
```
入力: !ReadBodyAsHtml:Boolean !MarkAsRead:Boolean !MailFolder:String ToContains:String SubjectContains:String !SaveAttachmentsInto:FolderObject BodyContains:String !Account:String !Instance:OutlookInstanceHandle FromContains:String !EmailsToRetrieve:RetrieveMessagesMode{All,Unread,Read}
出力: Messages:List<OutlookMailMessage>=>RetrievedEmails
ON ERROR可: InvalidMailFolderError, OutlookAccountNotFoundError, RetrieveEmailMessagesError, SaveAttachmentsDirectoryNotFoundError
固定: AttachmentsOptions=Save

### Outlook.SaveOutlookEmailMessages のセレクター: SaveEmails, SaveEmailsAs

## Outlook.SaveOutlookEmailMessages.SaveEmails [A]
```
Outlook.SaveOutlookEmailMessages.SaveEmails Instance: OutlookInstance Account: $fx'example' EmailsToSave: FileList SaveFormat: Outlook.MessageType.OutlookMessageFormatUnicode SaveEmailsTo: $fx'C:\temp' MessagesFiles=> StoredMessagesFiles
```
入力: Account:String EmailsToSave:List Instance:OutlookInstanceHandle SaveEmailsTo:FolderObject SaveFormat:MessageType{TextOnly,OutlookTemplate,OutlookMessageFormat,OutlookMessageFormatUnicode,Html,MhtFiles}
出力: MessagesFiles:List=>
ON ERROR可: DirectoryNotFoundError, MessageDeletedOrMovedError, OutlookAccountNotFoundError, SaveEmailMessagesError
固定: SaveAsMode=DefaultName

## Outlook.SaveOutlookEmailMessages.SaveEmailsAs [A]
```
Outlook.SaveOutlookEmailMessages.SaveEmailsAs SaveEmailsAs: $fx'example' SaveEmailsTo: $fx'C:\temp' SaveFormat: Outlook.MessageType.OutlookMessageFormatUnicode Account: $fx'example' EmailsToSave: List Instance: OutlookInstance MessagesFiles=> StoredMessagesFiles
```
入力: !SaveEmailsAs:String !SaveEmailsTo:FolderObject !SaveFormat:MessageType{TextOnly,OutlookTemplate,OutlookMessageFormat,OutlookMessageFormatUnicode,Html,MhtFiles} !Account:String !EmailsToSave:List<OutlookMailMessage> !Instance:OutlookInstanceHandle
出力: MessagesFiles:List<String>=>StoredMessagesFiles
ON ERROR可: DirectoryNotFoundError, MessageDeletedOrMovedError, OutlookAccountNotFoundError, SaveEmailMessagesError
固定: SaveAsMode=CustomName

### Outlook.SendEmailThroughOutlook のセレクター: SendEmail, SendEmailFromMailbox

## Outlook.SendEmailThroughOutlook.SendEmail [A]
```
Outlook.SendEmailThroughOutlook.SendEmail Instance: OutlookInstance Account: $fx'test@test.com' SendTo: $fx'example' IsBodyHtml: False IsDraft: False
```
入力: Attachments:List BCC:String Body:String CC:String IsBodyHtml:Boolean SendTo:String Subject:String !IsDraft:Boolean !Account:String !Instance:OutlookInstanceHandle
ON ERROR可: AttachmentNotFoundError, OutlookAccountNotFoundError, SendEmailMessageError
固定: SendEmailFrom=Account

## Outlook.SendEmailThroughOutlook.SendEmailFromMailbox [A]
```
Outlook.SendEmailThroughOutlook.SendEmailFromMailbox IsDraft: False IsBodyHtml: False Subject: $fx'example' SendTo: $fx'example' SendFrom: $fx'example' BCC: $fx'example' Attachments: Files Account: $fx'example' Instance: OutlookInstance CC: $fx'example' Body: $fx'example'
```
入力: !IsDraft:Boolean !IsBodyHtml:Boolean Subject:String !SendTo:String !SendFrom:String BCC:String Attachments:List<FileObject> !Account:String !Instance:OutlookInstanceHandle CC:String Body:String
ON ERROR可: AttachmentNotFoundError, OutlookAccountNotFoundError, SendEmailMessageError
固定: SendEmailFrom=OtherMailbox
