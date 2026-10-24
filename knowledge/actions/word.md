# Word actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/word （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The Word automation feature enables you to seamlessly interact with Word files stored either locally or in the cloud. To begin, you need to create a Word instance using either the 'Launch Word' or 'Attach to running Word' action. This instance serves as the input parameter for the rest of the actions in the group, allowing you to easily perform actions on the desired Word file. Currently, the below actions are available: * Launch Word: When this action is triggered in Power Automate for desktop, it opens a Word document and creates a Word instance that can be used in subsequent Word actions wi

## Launch Word  `#launchword`
Opens a new Word instance or opens a Word document.
入力:
- Launch Word: With a blank document, and open the following document = With a blank document — Specify whether to open a new Word document, or an existing one
- Document path: File — The full path of the existing Word document to open
- Make instance visible: Boolean value = True — Specify whether to make the Word window visible or hide it
- Open as ReadOnly: Boolean value = False — Specify whether to open the stored document in read-only mode or not
- Read protection password(任意): Direct encrypted input or Text value — The read protection password on the Word document, if it's password protected
- Write protection password(任意): Direct encrypted input or Text value — The write protection password on the Word document, if it's password protected
出力:
- `WordInstance`: Word instance — The specific Word instance for use with later Word actions. This allows the user to specify which of possibly several Word documents to access
例外: Failed to launch Word; The Word document was not found; Failed to open existing Word document; Failed to launch Word application; Word application is not installed

## Attach to running Word  `#attachtorunningword`
Attaches to a Word document that's already open.
入力:
- Document name: File — The name or the path of the Word document to attach to
出力:
- `WordInstance`: Word instance — The Word instance this action has attached to for use with later Word actions
例外: Failed to attach to Word document; Specified Word document not found; Failed to launch Word

## Save Word  `#saveword`
Saves a previously launched Word instance.
入力:
- Word instance: Word instance — The Word instance to save. This variable must have been previously specified in a Launch Word or Attach to running Word action.
- Save mode: Save document, Save document as = Save document — How to save the document of this instance.
- Document format: All available formats from Word app = Default (From Extension) — The format of the document.
- Document path: File — The full path of the document. Insert the desired document file extension according to the selection in the Document format parameter.
例外: Failed to save Word; The Word instance or the Word document is not initialized; The operation cannot be performed on a read-only document

## Close Word  `#closeword`
Closes a Word instance.
入力:
- Word instance: Word instance — The Word instance to close. This variable must have been previously specified in a Launch Word or Attach to running Word action.
- Before closing Word: Do not save document, Save document, Save document as = Don't save document — Specify whether and how to save the document of this instance before closing that instance.
- Document format: All available formats from Word app = Default (From Extension) — The format of the document.
- Document path: File — The full path of the document. Insert the desired document file extension according to the selection in the Document format parameter.
例外: Failed to close Word; Failed to save Word; The operation cannot be performed on a read-only document

## Read from Word document  `#readfromword`
Reads the text content from a document of a Word instance.
入力:
- Word instance: Word instance = The Word instance to work with — This variable must have been previously specified in a Launch Word or Attach to running Word action
- Retrieve: Whole document/Pages/Bookmark = Whole document — Whether to retrieve the content of the whole document, of specific pages, or a bookmark
- Page: Numeric value = 1 — The pages of the Word document to be read. A range of pages or a list can be provided as *2-5*, which will retrieve content from page 2 to page 5 or 2,3,7, retrieve content from 2,3,7 pages
- Bookmark: Text value — The bookmark of the Word document to be read
出力:
- WordData: Text value — The value of the retrieved content
例外: Failed to read the content from a Word document; The Word instance or the Word document is not initialized

## Write to Word document  `#writetoword`
Write or append text to a Word file.
入力:
- Word instance: Word instance = The Word instance to work with — This variable must have been previously specified in a Launch Word or Attach to running Word action
- Text to write(任意): General value = The text to write in the specified Word document — 
- Append new line: Boolean value = True — Specifies whether to append a new line at the start of the overall text to write to the document
- Write text to: Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark = Beginning of Word file — Specifies the position of the Word document where the text will be appended
- Bookmark: Text value = The target bookmark in the Word document where the text will be appended — This action appends text before or after of the specified bookmark in the Word document
例外: The Word instance or the Word document is not initialized; The operation cannot be performed on a read-only document; The write operation on the Word document instance failed

## Insert image in Word document  `#insertimagetoword`
Insert an image to a Word file.
入力:
- Word instance: Word instance = The Word instance to work with — This variable must have been previously specified in a Launch Word or Attach to running Word action
- Insert image to: Beginning of Word file/End of Word file/Before of Bookmark/After of Bookmark/Before specific text /After specific text = Beginning of Word file — Specifies the position of the Word document that image will be appended
- Insert image from: File/Clipboard = File — The location of the image to be inserted in the specified Word document
- Image path: File — The full path of the image to be inserted
- Text to find: Text value = The text to find in the Word document for inserting image — Image will be appended before or after any occurrence of the specified text
- Bookmark: Text value = The target bookmark in the Word document where the image will be appended — 
例外: The Word instance or the Word document is not initialized; The operation cannot be performed on a read-only document; Failed to insert image

## Find and replace words in Word document  `#findandreplaceword`
Finds text and replaces it with another in the active worksheet of an Excel instance.
入力:
- Word instance: Word instance = The Word instance to work with — This variable must have been previously specified in a Launch Word or Attach to running Word action
- All matches: Boolean value = False — Whether to find/ and replace text in all the matching occurrences found or in the first matching occurrence only
- Text to find: Text value = The text to find in the worksheet — 
- Text to replace with: Text value — The text used to replace the matching cells
- Use wildcards: Boolean value = False — Whether to use wildcards for the text to find
- Match case: Boolean value = False — Whether to search for case-sensitive data
- Match whole words only: Boolean value = False — Whether to search for words that are the same as the specified text
例外: Failed to replace text in Word document; The Word instance or the Word document is not initialized; The operation cannot be performed on a read-only document
