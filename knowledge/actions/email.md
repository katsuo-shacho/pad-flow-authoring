# Email actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/email （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Before deploying any email action, you have to configure the server that will handle the requests. The Retrieve email messages and Process email messages actions require an IMAP server, while the Send email action requires an SMTP server. Common IMAP ports: * 143 (non-encrypted and TLS) * 993 (secure IMAP) Common IMAP servers: * imap-mail.outlook.com (Outlook.com) * outlook.office365.com (Office365.com) * imap.mail.yahoo.com (Yahoo mail) * imap.gmail.com (Google mail) Common SMTP ports: * 25 (non-encrypted) * 587 (non-encrypted and TLS) * 465 (SSL) Common SMTP servers: * smtp-mail.outlook.com 

## Retrieve email messages  `#retrieveemails`
Retrieves email messages from an IMAP server.
入力:
- IMAP server: Text value — The IMAP server address (e.g. imap.gmail.com)
- Port(任意): Numeric value = 993 — The port to use for the IMAP server. Usually this port is 993
- Enable SSL: Boolean value = True — Specify whether to use a secure connection to communicate with the IMAP Server
- User name: Text value — The username of the email account to access
- Password: Direct encrypted input or Text value — The password of the email account to access
- Accept untrusted certificates: Boolean value = False — Specify whether untrusted certificates will be accepted
- Mail folder: Text value — The name of the IMAP mail-folder (also known as 'mailBox') to retrieve messages from
- Retrieve: All email messages, Unread email messages only, Read email messages only = All email messages — Specify whether to retrieve all messages in the folder or only the unread ones
- Mark As read: Boolean value = True — Specify whether to mark as read the retrieved messages or leave them as is
- "From" field contains(任意): Text value — The full email address of the sender whose messages will be retrieved. Leave this attribute blank to retrieve all messages regardless of the sender
- "To" field contains(任意): Text value — The full email address(es) of the recipient(s) (separated by space if more than one) for the messages that will be retrieved. Leave this attribute blank to retrieve all messages regardless of the recipient(s)
- "Subject" contains(任意): Text value — The key phrase to find within the email subject. Leave this attribute blank to retrieve all emails regardless of their subject
- 'Body' contains(任意): Text value — The key phrase to find within the email body. Leave this attribute blank to retrieve all emails regardless of their content
- Save attachments: Save attachments, Do not save attachments = Do not save attachments — Specify whether to save the attachments of the emails retrieved or not
- Save attachments into: Folder — The folder to save the attachments
出力:
- RetrievedEmails: List of Mail Messages — The retrieved emails for later processing as a list of mail message objects
例外: Failed to connect to IMAP server; Failed to authenticate to the IMAP server; Specified mail-folder doesn't exist; Failed to save attachments; Failed to retrieve emails

## Process email messages  `#processemails`
Moves, deletes or marks as unread an email (or a list of emails) retrieved by a Retrieve emails action.
入力:
- IMAP server: Text value — The IMAP server address (e.g. imap.gmail.com)
- Port(任意): Numeric value = 993 — The port to use for the IMAP server. Usually this port is 993
- Enable SSL: Boolean value = True — Specify whether to use a secure connection to communicate with the IMAP server
- Username: Text value — The username of the email account to access
- Password: Direct encrypted input or Text value — The password of the email account to access
- Accept Untrusted Certificates: Boolean value = False — Specify whether untrusted certificates will be accepted
- Email(s) to process: List of Mail Messages — The email or list of emails to process. This parameter should contain a variable populated by a Retrieve emails action
- Operation: Delete emails from server, Mark emails as unread, Move emails to mail folder, Mark emails as unread and move to mail folder = Move emails to mail folder — The operation you want to perform on the specified email messages
- Mail folder: Text value — The name of the mail folder to which the emails will be moved
例外: Failed to connect to IMAP server; Specified mail-folder doesn't exist; Failed to process emails

## Send email  `#sendemail`
Creates and sends a new email message.
入力:
- SMTP server: Text value — The SMTP server address
- Server port(任意): Numeric value = 25 — The port to use for the server. Usually this port is 25
- Enable SSL: Boolean value = False — Specify whether or not to communicate with the server through a secure connection
- SMTP Server needs authentication: Boolean value = False — Specify whether the server requires authentication
- User name: Text value — The username of the email account to access
- Password: Direct encrypted input or Text value — The password of the email account to access
- Accept untrusted certificates: Boolean value = False — Specify whether untrusted certificates will be accepted
- From: Text value — The sender's email address
- Sender display name(任意): Text value — The sender's display name
- To: Text value — The email(s) of the recipient(s). If more than one email is entered, the list of addresses should be separated by semi-colons
- CC(任意): Text value — The email(s) of the Cc recipient(s). If more than one email is entered, the list of addresses should be separated by semi-colons
- BCC(任意): Text value — The email(s) of the BCC (hidden) recipient(s). If more than one email is entered, the list of addresses should be separated by semi-colons
- Subject(任意): Text value — The subject of the email
- Body(任意): Text value — The body of the email
- Body Is HTML: Boolean value = False — Specify whether the body of the email will be interpreted as HTML coding
- Attachment(s)(任意): List of Files — The full path of any attachment(s), or a file or a list of files. Multiple files should be enclosed in double quotes (") and separated by a space character
例外: Invalid email address; Failed to send email; Attachment not found
