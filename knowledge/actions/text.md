# Text actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/text （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Text actions enable you to handle, manipulate, and convert text values in your desktop flows. To merge a list of text values and create a single value, use the Join text action. The action requires you to specify the list and a delimiter. To split a single text value into a list, deploy the Split text action, and specify the text value and the delimiters to separate the list items. To replace a subtext in a text, use the Replace text action. The following example replaces the text Product Characteristics with Characteristics. !Screenshot of the Replace text action. Search a text value inside a

## Append line to text  `#appendline`
Appends a new line of text to a text value.
入力:
- Original text: Text value — The original text
- Line to append(任意): Text value — The text to add on as a new line
出力:
- Result: Text value — The new text

## Get subtext  `#getsubtextbase`
Retrieve a subtext from a text value.
入力:
- Original text: Text value — The text to retrieve a section of text from
- Start index: Start of text, Character position = Character position — Specify how to find the starting point for text retrieval
- Character position: Numeric value — The position of the first character to retrieve. This value is a zero-based index, counting from zero for the first character
- Length: End of text, Number of chars = Number of chars — Specify whether the subtext continues to the end of the text, or includes only a certain number of characters
- Number of chars: Numeric value — The number of characters to retrieve
出力:
- Subtext: Text value — The retrieved subtext
例外: Start index or length are out of range

## Crop text  `#croptextaction`
Retrieves a text value that occurs before, after or between the specified text flag(s) in a given text.
入力:
- Original text: Text value — The text to retrieve a section of text from
- Mode: Get text before the specified flag, Get text after the specified flag, Get text between the two specified flags = Get text before the specified flag — Specify whether to retrieve the text before, after, or between flags.
- Start flag: Text value — The retrieved text will be after this flag. The flag can be any character or text
- End flag: Text value — The retrieved text will be before this flag. The flag can be any character or text
- Ignore case: Boolean value = False — Specify whether to find the flags using case-sensitive or case-insensitive matching
出力:
- CroppedText: Text value — The new cropped text
- IsFlagFound: Boolean value — Indicates if flag(s) found or not

## Pad text  `#pad`
Creates a fixed length text by adding characters to the left or to the right of an existing text.
入力:
- Text to pad(任意): Text value — The text to lengthen
- Pad: Left, Right = Left — Specify whether to add characters to the left or right of the existing text
- Text for padding(任意): Text value — The character or text that will be added to lengthen the original text
- Total length(任意): Numeric value = 10 — The total character length of the final padded text. The text for padding will be repeatedly added until the final text is of the specified length
出力:
- PaddedText: Text value — The new, padded text

## Trim text  `#trim`
Removes all occurrences of white space characters (such as space, tab, or new line) from the beginning and/or end of an existing text.
入力:
- Text to trim(任意): Text value — Text to trim
- What to trim: whitespace characters from the beginning, whitespace characters from the end, whitespace characters from the beginning and end = whitespace characters from the beginning and end — Specify where white space characters will be removed from
出力:
- TrimmedText: Text value — The new trimmed text

## Reverse text  `#reverse`
Reverses the order of letters in a text string.
入力:
- Text to reverse: Text value — The text to reverse
出力:
- ReversedText: Text value — The new reversed text

## Change text case  `#changecase`
Changes the casing of a text to uppercase, lowercase, title case or sentence case.
入力:
- Text to convert(任意): Text value — The text to convert
- Convert to: Upper case, Lower case, Title case, Sentence case = Upper case — Specify the text case style to use
出力:
- TextWithNewCase: Text value — The new converted text

## Convert text to number  `#tonumber`
Converts a text representation of a number to a variable that contains a numeric value.
入力:
- Text to convert: Text value — A text variable containing only a number, to convert to a numeric value variable. Spaces are ignored, but non-number text throws an exception
出力:
- TextAsNumber: Numeric value — The new numeric value
例外: Provided text value can't be converted into a valid number

## Convert number to text  `#fromnumber`
Converts a number to text using a specified format.
入力:
- Number to convert: Numeric value — A numeric value to convert to text
- Decimal places(任意): Numeric value = 2 — The number of decimal places that will be included before truncation. Zeros can also be added to the end to pad the text in this way
- Use thousands separator: Boolean value = True — Specify whether or not to use punctuation as a 1000 separator
出力:
- FormattedNumber: Text value — The formatted number as text

## Convert text to datetime  `#converttexttodatetime`
Converts a text representation of a date and/or time value to a datetime value.
入力:
- Text to convert: Text value — The text to convert to a datetime value. This text must be in a recognizably datetime value format
- Date is represented in custom format: Boolean value = False — Specify whether the text to convert contains a representation of the date and time in a nonstandard, nonrecognizable format
- Custom format: Text value — The format in which the date is stored in the text. A custom format can be expressed as, for example, yyyyMMdd for date and hhmmss for time
出力:
- TextAsDateTime: Datetime — The datetime value
例外: Provided text value can't be converted into a valid datetime

## Convert datetime to text  `#convertdatetimetotext`
Converts a datetime value to text using a specified custom format.
入力:
- Datetime to convert: Datetime — The datetime value to convert to text
- Format to use: Standard, Custom = Standard — Specify whether to use a standard datetime format, or create a custom one
- Custom Format: Text value — The custom format to display the datetime value in. A datetime can be expressed as, for example, MM/dd/yyyy for date and hh:mm:sstt for time
- Standard format: Short date, Long date, Short time, Long time, Full datetime (short time), Full datetime (long time), General datetime (short time), General datetime (long time), Sortable datetime = Short date — The standard datetime format the action uses to display the datetime value
出力:
- FormattedDateTime: Text value — The formatted datetime as a text value

## Create random text  `#random`
Generates a text of specified length consisting of random characters. This action can be useful for generating passwords.
入力:
- Use uppercase letters (A-Z): Boolean value = True — Specify whether uppercase characters will be included in the generated text
- Use lowercase letters (a-z): Boolean value = True — Specify whether lowercase characters will be included in the generated text
- Use digits (0-9): Boolean value = True — Specify whether digits will be included in the generated text
- Use symbols ( , . < > ? ! + - _ # $ ^ ): Boolean value = True — Specify whether symbols will be included in the generated text
- Minimum length(任意): Numeric value = 6 — The minimum length of the random text. For a certain length of text, set the minimum and maximum values to that number
- Maximum length(任意): Numeric value = 10 — The maximum length of the random text. For a certain length of text, set the minimum and maximum values to that number
出力:
- RandomText: Text value — The generated random text

## Join text  `#jointext`
Converts a list into a text value by separating its items with a specified delimiter.
入力:
- Specify the list to join: List of Text values — The list to convert to text
- Delimiter to separate list items: None, Standard, Custom = None — Specify whether to use no delimiter, a standard delimiter or a custom one
- Custom delimiter: Text value — The character(s) to use as delimiter
- Standard delimiter: Space, Tab, New line = Space — Specify the delimiter to use
- Times(任意): Numeric value = 1 — Specify how many times to use the specified delimiter
出力:
- JoinedText: Text value — The new delimited text

## Split text  `#splittext`
Creates a list containing the substrings of a text that are separated by a specified delimiter or a regular expression.
入力:
- The text to split: Text value — The text to split
- Delimiter type: Standard, Custom = Standard — Whether the used delimiter is of a standard or custom format
- Custom delimiter: Text value — The character(s) that were used as a delimiter
- Standard delimiter: Space, Tab, New line = Space — The delimiter used
- Times(任意): Numeric value = 1 — Specify how many times the delimiter is used
- Is regular expression: Boolean value = False — Specify whether the delimiter will be a regular expression. A regular expression creates a range of possibilities for the delimiter. For example, '\d' means that the delimiter could be any digit
出力:
- TextList: List of Text values — The new list
例外: Provided regular expression is invalid

## Parse text  `#parsetext`
Parses a text to find the first or all occurrences of a specified subtext or a regular expression pattern.
入力:
- Text to Parse: Text value — The text to parse
- Text to Find: Text value — The subtext or a regular expression to search for
- Is regular expression: Boolean value = False — Specify whether the subtext is a regular expression. For example \d means that the subtext could be any digit
- Start Parsing at Position: Numeric value — The position to start looking for the 'Text to Find'. The first position is zero, so use 0 to start from the beginning
- First occurrence only: Boolean value = True — Specify whether to find the first occurrence only, or each occurrence of the 'Text to find'
- Ignore case: Boolean value = False — Specify whether to find the specified text using case-sensitive or case-insensitive matching
出力:
- Position: Numeric value — The position of the 'Text to find' into the 'Text to parse'. If the text isn't found within the original text, this variable will hold the value -1
- Positions: List of Numeric values — The positions of the 'Text to find' into the 'Text to parse'. If the text isn't found within the original text, this variable will hold the value -1
- Match: Text value — The result that matches the given regular expression
- Matches: List of Text values — The results that match the given regular expression
例外: Provided regular expression is invalid

## Replace text  `#replace`
Replaces all occurrences of a specified subtext with another text. It can also be used with regular expressions.
入力:
- Text to parse: Text value — The text to parse
- Text to find: Text value — The subtext or a regular expression to search for
- Use regular expressions for find and replace: Boolean value = False — Specify whether the subtexts are regular expressions. A regular expression creates a range of possibilities for the subtext. For example, '\d' means that the subtext could be any digit
- Ignore case: Boolean value = False — Specify whether to find the subtext to replace using case-sensitive or case-insensitive matching
- Replace with: Text value — The text or a regular expression to replace found text
- Activate escape sequences: Boolean value = False — Specify whether to use special sequences. For example, '\t' in the replacement text will be interpreted as a tab
出力:
- Replaced: Text value — The new updated text

## Escape text for regular expression  `#escapeforregularexpression`
Escapes a minimal set of characters (\, *, +, ?, |, {, [, (,), ^, $,., #, and white space) by replacing them with their escape codes.
入力:
- Text to escape: Text value — The text to escape
出力:
- EscapedText: Text value — The escaped text

## Recognize entities in text  `#recognizeentitiesintext`
Recognizes entities in text, such as numbers, units, data/time and others expressed in natural language across multiple languages.
入力:
- Text to recognize from: Text value — The text to recognize entities from
- Entity type: Date time, Dimension, Temperature, Currency, Number range, Number, Ordinal, Percentage, Phone number, Email, IP address, Mention, Hashtag, URL, GUID, Quoted text = Date time — The type of entity to recognize (, Date time, Email, URL etc.)
- Language: English, Chinese (Simplified), Spanish, Spanish (Mexico), Portuguese, French, German, Italian, Japanese, Dutch, Korean, Swedish, Turkish, Hindi = English — Specify the language of the text
出力:
- RecognizedEntities: Datatable — The recognized entities

## Create HTML content  `#createhtmlcontentaction`
Generates rich HTML content and stores it in a variable.
出力:
- `HtmlContent`: Text value — The HTML code
