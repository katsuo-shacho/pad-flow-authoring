# Exchange Server actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/exchange （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The Exchange Server actions enable you to connect to an Exchange server and manage your correspondence. Exchange Server actions require a connection to an Exchange server that you can establish using the Connect to Exchange server action. The following example contains a manually populated server address rather than using auto-discovery. The credentials are set to user defined, so the domain, username, and password are manually entered. A set timeout in the Advanced section allows the action to return an error if a connection hasn't been established within the specified time frame. To retrieve

## Connect to Exchange server  `#connecttoexchangeserver`
Open a new connection to an Exchange server.
入力:
- Exchange server version: Exchange 2010, Exchange 2010 SP1, Exchange 2010 SP2, Exchange 2013, Exchange 2013 SP1 = Exchange 2013 SP1 — The version of the Exchange server
- Connection type: Auto discovery, Exchange server address = Auto discovery — Specifies how to connect to the Exchange server
- Server address: Text value — The Exchange server address
- Email address: Text value — The Exchange account email address
- Credentials: Exchange default, User defined = Exchange default — Specifies the way to provide the user's Exchange credentials
- Domain(任意): Text value — The Exchange account domain. To extract the account domain from the username, left this field empty
- Username: Text value — The Exchange account username
- Password: Direct encrypted input or Text value — The Exchange account password
- Timeout(任意): Numeric value = 30 — The time in seconds to wait for the connection to be established before the action fails
出力:
- ExchangeConnection: Exchange connection — The specific Exchange connection for use with later Exchange actions
例外: Failed to connect to the Exchange server

## Retrieve Exchange email messages  `#retrieveexchangemessages`
Retrieve email messages from the specified Exchange server.
入力:
- Exchange connection: Exchange connection — The Exchange connection. Create an Exchange connection with the 'Connect to Exchange server' action
- Mailbox type: Personal, Shared = Personal — The type of the mailbox to retrieve email messages from
- Shared mailbox address: Text value — The address of the shared mailbox to retrieve email messages from
- Retrieve email messages from custom folder: Boolean value = False — Specifies whether to retrieve email messages from a custom folder or a predefined Exchange folder
- Exchange folder: Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email = Inbox — A predefined Exchange folder to retrieve email messages from
- Mail folder: Text value = Inbox — The name or path (e.g. folder1\folder2) of the mail-folder to retrieve email messages from
- Retrieve: All email messages, Unread email messages only, Read email messages only = Unread email messages only — Specifies whether to retrieve all email messages in the folder or only the unread ones
- Mark as read: Boolean value = True — Specifies whether to mark as read the retrieved email messages or leave them as is
- From contains(任意): Text value — The full email address of the sender to retrieve messages from. Leave this attribute blank to retrieve all messages regardless of the sender
- To contains(任意): Text value — The full email address(es) of the recipient(s) (separated by space if more than one) for the email messages to retrieve. Leave this attribute blank to retrieve all email messages regardless of the recipient(s)
- Subject contains(任意): Text value — The key phrase to find within the email subject. Leave this attribute blank to retrieve all email messages regardless of their subject
- Body contains(任意): Text value — The key phrase to find within the email body. Leave this attribute blank to retrieve all email messages regardless of their content
- Attachments: Save attachments, Do not save attachments = Do not save attachments — Specifies whether to save the attachments of the email messages retrieved or not
- Save attachments into: Folder — The folder to save the attachments into
出力:
- RetrievedEmails: List of Exchange mail messages — The retrieved email messages for later processing as a list of Exchange mail messages objects
例外: Failed to save attachments; Specified mail-folder doesn't exist; Failed to retrieve email messages

## Send Exchange email message  `#sendmessage`
Create and send a new email message.
入力:
- Exchange connection: Exchange connection — The Exchange connection. Create an Exchange connection with the 'Connect to Exchange server' action
- From: Text value — The sender's email address
- Sender display name(任意): Text value — The sender's display name
- To: Text value — The email(s) of the recipient(s). To enter more than one email, separate the list of addresses by semi-colons
- CC(任意): Text value — The email(s) of the CC recipient(s). To enter more than one email, separate the list of addresses by semi-colons
- BCC(任意): Text value — The email(s) of the BCC (hidden) recipient(s). To enter more than one email, separate the list of addresses by semi-colons
- Subject(任意): Text value — The subject of the email
- Body(任意): Text value — The text of the body
- Body is HTML: Boolean value = False — Specifies whether to interpret the body of the email as HTML coding
- Attachment(s)(任意): List of Files — The full path of any attachment(s). Enclose multiple files in double quotes (") and separate them by a space character
例外: Attachment not found; Failed to send email

## Process Exchange email messages  `#processexchangemessages`
Move, delete or mark as unread an email message (or a list of email messages).
入力:
- Exchange connection: Exchange connection — The Exchange connection. Create an Exchange connection with the 'Connect to Exchange server' action
- Email message(s) to process: List of Exchange mail messages — The email message(s) to process. Use a variable populated by a 'Retrieve Exchange email messages' action
- Operation: Delete email messages from server, Mark email messages as unread, Move email messages to mail folder = Move email messages to mail folder — Specifies which operation to perform on the specified email messages
- Mailbox type: Personal, Shared = Personal — The type of the mailbox to retrieve email messages from
- Shared mailbox address: Text value — The address of the shared mailbox to retrieve email messages from
- Move to custom folder: Boolean value = False — Specifies whether to move email messages to a custom folder or a predefined Exchange folder
- Exchange folder: Inbox, Deleted items, Drafts, Outbox, Sent items, Junk email = Inbox — A predefined Exchange folder to move email messages from
- Mail folder: Text value = Inbox — The name or path (e.g. folder1\folder2) of the mail-folder to move email messages to
例外: Specified mail-folder doesn't exist; Failed to process email messages
