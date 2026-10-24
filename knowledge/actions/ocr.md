# OCR actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/ocr （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate enables users to read, extract, and manage data within files through optical character recognition (OCR). To create an OCR engine and extract text from images and documents, use the Extract text with OCR action. The following example extracts text from the entire specified image. !Screenshot of the Extract text with OCR action. All OCR actions can create a new OCR engine variable or use an existing one. You can use existing OCR engine variables in any action that offers OCR capabilities. Power Automate supports the Windows OCR and Tesseract engines. To configure the selected OCR

## Use the Tesseract OCR engine
Apart from the Windows OCR engine, Power Automate supports the Tesseract engine. This engine can extract text in five languages without further configuration: English, German, Spanish, French, and Italian.
入力:
- If text: Exists, Doesn't exist = Exists — Specifies whether to check if the text exists or not on the given source to analyze
- OCR engine type: Windows OCR engine, Tesseract engine, OCR engine variable = OCR engine variable — The OCR engine type to use. Select a preconfigured OCR engine or set up a new one.
- OCR engine variable: OCREngineObject — The engine to use for the OCR operation
- Text to find: Text value — The text to search for in the specified source
- Is regular expression: Boolean value = False — Specifies whether to use a regular expression to find the specified text
- Search for text on: Entire screen, Foreground window = Entire screen — Specifies whether to search for the specified text on the entire visible screen or just the foreground window
- Search mode: Whole of specified source, Specific subregion only, Subregion relative to image = Whole of specified source — Specifies whether to scan the entire screen (or window) or a narrowed down subregion of it
- Image(s): List of Images — The image(s) specifying the subregion (relative to the top left corner of the image) to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion to scan for the supplied text
- Tolerance(任意): Numeric value = 10 — Specifies how much the image(s) searched for can differ from the originally chosen image
- Y1(任意): Numeric value — The start Y coordinate of the subregion to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion relative to the specified image to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion to scan for the supplied text
- Y1(任意): Numeric value — The start Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Windows OCR language: Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish = English — The language of the text that the Windows OCR engine detects
- Use other language: Boolean value = False — Specifies whether to use a language not given in the 'Tesseract language' field
- Tesseract language: English, German, Spanish, French, Italian = English — The language of the text that the Tesseract engine detects
- Language abbreviation: Text value — The Tesseract abbreviation of the language to use. For example, if the data is 'eng.traineddata', set this parameter to 'eng'
- Language data path: Text value — The path of the folder that holds the specified language's Tesseract data
- Image width multiplier: Numeric value = 1 — The width multiplier of the image
- Image height multiplier: Numeric value = 1 — The height multiplier of the image
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
出力:
- LocationOfTextFoundX: Numeric value — The X coordinate of the point where the text appears on the screen. If the search is performed in the foreground window, the coordinate returned is relative to the top left corner of the window
- LocationOfTextFoundY: Numeric value — The X coordinate of the point where the text appears on the screen. If the search is performed in the foreground window, the coordinate returned is relative to the top left corner of the window
例外: Can't check if text exists in non-interactive mode; Invalid subregion coordinates; Failed to analyze text with OCR; Failed to create the OCR engine; Data path folder doesn't exist; The selected Windows language pack isn't installed on the machine; OCR engine not alive

## Wait for text on screen (OCR)  `#waittextonscreenaction`
Wait until a specific text appears/disappears on the screen, on the foreground window, or relative to an image on the screen or foreground window using OCR.
入力:
- Wait for text to: Appear, Disappear = Appear — Specifies whether to wait for the text to appear or disappear
- OCR engine type: Windows OCR engine, Tesseract engine, OCR engine variable = OCR engine variable — The OCR engine type to use. Select a preconfigured OCR engine or set up a new one.
- OCR engine variable: OCREngineObject — The engine to use for the OCR operation
- Text to find: Text value — The text to search for in the specified source
- Is regular expression: Boolean value = False — Specifies whether to use a regular expression to find the specified text
- Search for text on: Entire screen, Foreground window = Entire screen — Specifies whether to search for the specified text on the entire visible screen or just the foreground window
- Search mode: Whole of specified source, Specific subregion only, Subregion relative to image = Whole of specified source — Specifies whether to scan the entire screen (or window) or a narrowed down subregion of it
- Image(s): List of Images — The image(s) specifying the subregion (relative to the top left corner of the image) to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion to scan for the supplied text
- Tolerance(任意): Numeric value = 10 — Specifies how much the image(s) searched for can differ from the originally chosen image
- Y1(任意): Numeric value — The start Y coordinate of the subregion to scan for the supplied text
- X1(任意): Numeric value — The start X coordinate of the subregion relative to the specified image to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion to scan for the supplied text
- Y1(任意): Numeric value — The start Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion to scan for the supplied text
- X2(任意): Numeric value — The end X coordinate of the subregion relative to the specified image to scan for the supplied text
- Y2(任意): Numeric value — The end Y coordinate of the subregion relative to the specified image to scan for the supplied text
- Windows OCR language: Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish = English — The language of the text that the Windows OCR engine detects
- Use other language: Boolean value = False — Specifies whether to use a language not given in the 'Tesseract language' field
- Tesseract language: English, German, Spanish, French, Italian = English — The language of the text that the Tesseract engine detects
- Language abbreviation: Text value — The Tesseract abbreviation of the language to use. For example, if the data is 'eng.traineddata', set this parameter to 'eng'
- Language data path: Text value — The path of the folder that holds the specified language's Tesseract data
- Image width multiplier: Numeric value = 1 — The width multiplier of the image
- Image height multiplier: Numeric value = 1 — The height multiplier of the image
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
- Fail with timeout error: Boolean value = False — Specify whether you want the action to wait indefinitely or fail after a set time period
出力:
- LocationOfTextFoundX: Numeric value — The X coordinate of the point where the text appears on the screen. If the search is performed in the foreground window, the coordinate returned is relative to the top left corner of the window
- LocationOfTextFoundY: Numeric value — The X coordinate of the point where the text appears on the screen. If the search is performed in the foreground window, the coordinate returned is relative to the top left corner of the window
例外: Can't check if text exists in non-interactive mode; Invalid subregion coordinates; Failed to analyze text with OCR; Failed to create the OCR engine; Data path folder doesn't exist; The selected Windows language pack isn't installed on the machine; OCR engine not alive; Timeout error

## Extract text with OCR  `#extracttextwithocr`
Extract text from a given source using the given OCR engine.
入力:
- OCR engine: Windows OCR engine, Tesseract engine, OCR engine variable = OCR engine variable — The OCR engine type to use. Select a preconfigured OCR engine or set up a new one
- OCR engine variable: OCREngineObject — The engine to use for the OCR operation
- OCR source: Screen, Foreground window, Image on disk = Screen — The source of the image to perform the OCR operation on
- Image file path: File — The path of the image to perform the OCR operation on
- Search mode: Whole of specified source, Specific subregion only, Subregion relative to image = Whole of specified source — The selected mode for the OCR operation
- Image: List of Images — The image to use for narrowing down the scan to a subregion that is relative to the specified image
- Tolerance(任意): Numeric value = 10 — Specifies how much the image can differ from the originally chosen image
- X1(任意): Numeric value — The start X coordinate of the subregion to narrow down the scan
- X2(任意): Numeric value — The end X coordinate of the subregion to narrow down the scan
- Y1(任意): Numeric value — The start Y coordinate of the subregion to narrow down the scan
- Y2(任意): Numeric value — The end Y coordinate of the subregion to narrow down the scan
- Windows OCR language: Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian (Cyrillic), Serbian (Latin), Slovak, Spanish, Swedish, Turkish = English — The language of the text that the Windows OCR engine detects
- Use other language: Boolean value = False — Specifies whether to use a language not given in the 'Tesseract language' field
- Tesseract language: English, German, Spanish, French, Italian = English — The language of the text that the Tesseract engine detects
- Language abbreviation: Text value — The Tesseract abbreviation of the language to use. For example, if the data is 'eng.traineddata', set this parameter to 'eng'
- Language data path: Text value — The path of the folder that holds the specified language's Tesseract data
- Image width multiplier: Numeric value = 1 — The width multiplier of the image
- Image height multiplier: Numeric value = 1 — The height multiplier of the image
- Wait for image to appear: Boolean value = True — Specifies whether to wait or not for the image to appear on the screen or foreground window
- Timeout: Numeric value = 5 — Specifies the time to wait for the operation to complete before the action fails
- Image matching algorithm: Basic, Advanced = Basic — Which image algorithm to use when searching for image
出力:
- OcrText: Text value — The result after the text extraction
例外: Failed to extract text with OCR; Image file not found; Landmark image not found; Can't get text from screen in non-interactive mode; Failed to create the OCR engine; Data path folder doesn't exist; The selected Windows language pack isn't installed on the machine; OCR engine not alive
