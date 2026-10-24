# Outlook actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/outlook （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: For machines with an installation of Outlook, you can manage your mailboxes with the Outlook actions. After creating an Outlook instance with the Launch Outlook action, use the Retrieve email messages from Outlook action to get the messages from a specified account and mail folder. The following example retrieves all the email messages from the folder Tickets, a subfolder of the Inbox. The specified filters limit the results to messages from a specific sender that contain particular words in their subject and body. The Process email messages in Outlook action processes email messages retrieved

## Launch Outlook  `#launch`
Launch Outlook and create a new Outlook instance.
出力:
- OutlookInstance: Outlook instance — The specific Outlook instance for use with later Outlook actions
例外: Failed to launch Outlook

## Retrieve email messages from Outlook  `#retrieveemailmessages`
Retrieve email messages from an Outlook account.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. Specify this variable in a 'Launch Outlook' action
- Account: Text value — The name of the Outlook account (data file name) to work with
- Mail folder: Text value — The name of the folder to retrieve messages from. Enter the full folder path for subfolders (ex: Inbox\Work)
- Retrieve: All email messages, Unread email messages only, Read email messages only = All email messages — Specifies whether to retrieve all messages in the folder or only the unread ones
- Mark as read: Boolean value = True — Specifies whether to mark as read all the unread messages retrieved
- From contains(任意): Text value — The full email address of the sender whose messages to retrieve. Leave this attribute blank to retrieve all messages regardless of the sender
- To contains(任意): Text value — The full email address(es) of the recipient(s) (separated by space or semicolon if more than one) for the messages to retrieve. Leave this attribute blank to retrieve all messages regardless of the recipient(s)
- Subject contains(任意): Text value — The key phrase to find within the email subject. Leave this attribute blank to retrieve all email messages regardless of their subject
- Body contains(任意): Text value — The key phrase to find within the email body. Leave this attribute blank to retrieve all email messages regardless of their content
- Attachments: Save attachments, Don't save attachments = Don't save attachments — Specifies whether to save the attachments of the email messages retrieved or not
- Save attachments into: Folder — The path to save the attachments of the retrieved emails into
出力:
- RetrievedEmails: List of Outlook mail messages — The retrieved email messages for later processing. The variable contain a list of Outlook message objects
例外: Failed to find Outlook account; Mail-folder specified not valid in Outlook; Directory for saving attachments not found; Failed to retrieve email messages from Outlook

## Send email through Outlook  `#sendemailthroughoutlook`
Create and send a new email message through Outlook.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. Specify this variable in a 'Launch Outlook' action
- Account: Text value — The name of the Outlook account (data file name) to work with
- Send email from: Account, Other mailbox = Account — Specifies whether to send the email using the specified account or a different one, for example from a shared mailbox
- Send from: Text value — The name of the Outlook account to send the email from; for example, a shared mailbox.
- To: Text value — The email address(es) of the recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- CC(任意): Text value — The email address(es) of the CC recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- BCC(任意): Text value — The email address(es) of the BCC (hidden) recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- Subject(任意): Text value — The subject of the email
- Body(任意): Text value — The text of the body
- Body is HTML: Boolean value = False — Specifies whether to interpret the body of the email as HTML coding
- Attachment(s)(任意): List of Files — The full path of any attachment(s). Enclose multiple files in double quotes (") and separate them by a space character
例外: Failed to find Outlook account; Failed to send email; Attachment not found

## Process email messages in Outlook  `#processemailmessages`
Move or deletes an email (or a list of email messages) retrieved by a 'Retrieve emails from Outlook' action.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. Specify this variable in a 'Launch Outlook' action
- Account: Text value — The name of the Outlook account (data file name) to work with
- Email messages to process: List of Outlook mail messages — The email message(s) to process. Use a variable populated by a 'Retrieve email messages from Outlook' action
- Operation: Delete email messages, Move email messages to mail folder, Mark as unread = Move email messages to mail folder — Specifies which operation to perform on the specified email messages
- Mail folder: Text value — The name of the folder to retrieve messages from. Enter the full folder path for subfolders (for example, Inbox\Work)
例外: Failed to find Outlook account; Specified mail-folder doesn't exist; Failed to process email messages in Outlook

## Save Outlook email messages  `#saveoutlookemailmessages`
Save Outlook email messages given an account.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. Specify this variable in a 'Launch Outlook' action
- Account: Text value — The name of the Outlook account (data file name) to work with
- Email message(s) to save: List of Outlook mail messages — The email message(s) to save. Use a variable populated by a 'Retrieve email messages from Outlook' action
- Save format: Text only (*.txt), Outlook template (*.oft), Outlook message format (*.msg), Outlook message format - Unicode (*.msg), HTML (*.html), MHT files (*.mht) = Outlook message format (*.msg) — Specifies the format to save the messages
- File name: Default, Custom = Default — Specifies whether to save the messages using the default name (subject) or provide another
- Save as: Text value — Specifies the custom name for messages' name, which differs from message to message by an automatically added suffix
- Save email message(s) to: Folder — The folder to save the messages to
出力:
- StoredMessagesFiles: List of Text values — The file paths of the saved email messages for later processing
例外: Failed to find Outlook account; Directory not found; Email message is deleted or moved to another folder; Failed to save email message(s)

## Respond to Outlook mail message  `#respondtomailmessage`
Respond to an Outlook message, by replying, replying to all or forwarding it.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. Specify this variable in a 'Launch Outlook' action
- Account: Text value — The name of the Outlook account (data file name) to work with
- Mail message: Outlook mail message — The mail message to act upon. Use a variable populated by a 'Retrieve email messages from Outlook' action
- Response action: Reply, Reply all, Forward = Reply — Specifies whether to reply (to sender or all) with a message or forward the received message
- To: Text value — The email address(es) of the recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- CC(任意): Text value — The email address(es) of the CC recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- BCC(任意): Text value — The email address(es) of the BCC (hidden) recipient(s). To enter more than one email address, separate the list of addresses by spaces or semicolons
- Body(任意): Text value — The text of the body
- Attachment(s)(任意): List of Files — The full path of any attachment(s). Enclose multiple files in double quotes (") and separate them by a space character
例外: Failed to find Outlook account; Failed to send email; Attachment not found

## Close Outlook  `#close`
Close a previously launched Outlook instance.
入力:
- Outlook instance: Outlook instance — The Outlook instance to work with. This variable is specified in a 'Launch Outlook' action
例外: Failed to close Outlook instance
