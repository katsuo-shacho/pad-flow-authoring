# Clipboard actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/clipboard （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Use the Clipboard actions to manipulate or extract the contents of your machine's clipboard. To retrieve the contents of the clipboard and store them in a variable, use the Get clipboard text action. To change the text of the clipboard, use the Set clipboard text action. The following example uses a variable to set the current date and time on the clipboard. To clear the clipboard, use the Clear clipboard contents action.

## Get clipboard text  `#gettext`
Gets clipboard text.
出力:
- ClipboardText: Text value — The text stored in the clipboard
例外: Can't retrieve clipboard contents

## Set clipboard Text  `#settext`
Sets clipboard text.
入力:
- Clipboard text: Text value — The text to set to the clipboard
例外: Can't set clipboard contents

## Clear clipboard contents  `#clear`
Clears clipboard contents.
