# IBM cognitive actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/ibmcognitive （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: IBM cognitive services are machine learning algorithms that use artificial intelligence to perform complex operations, such as language tone analysis and visual recognition. Desktop flows enable you to use these services through the IBM cognitive actions. All IBM cognitive actions require an API key that you can create and manage through the IBM Cloud console. Additionally, they require the release date of the used API and the service endpoint location.

## Convert document  `#convertdocumentibm`
Invokes the IBM service named 'Convert Document'.
入力:
- Username: Text value — The username to be used for this call
- Password: Direct encrypted input or Text value — The password to use for this call
- Version date: Text value — The release date of the API to use
- File path: File — The path to the file to analyze
- Mime type: text/html, text/xhtml+xml, application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document = text/html — The MIME type of the file
- Conversion target: Answer units, Normalized HTML, Normalized text = Answer units — The output format of the conversion
- Answer units(任意): Text value — The heading levels as a comma-separated string
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The results of the API call
- StatusCode: Numeric value — The status code of the API call
例外: Request timeout expired; Failed to Invoke cognitive services

## Translate  `#translateibm`
Invokes the IBM service named 'Translate'.
入力:
- API key: Text value — The API key to use for this call
- Version date: Text value — The release date of the API to use
- Service endpoint location: US South, US East, Europe, Australia, Japan, UK, Korea = US East — The account's service location. Can be seen through IBM "Manage" in the resources section
- Instance ID: Text value — The Instance ID of the service.
- Translate mode: Model ID, Source and target = Model ID — Specify the mode to be used for this call
- Model ID: Text value — The unique model_id of the translation model that will be used to translate the text
- Source: Text value — The source language of the text
- Target: Text value — The translation target language in 2 or 5 letter language code
- Text: List of Text values — The text to send or list of words to be separately translated
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The results of the API call
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Identify language  `#identifylanguage`
Invokes the IBM service named 'Identify Language'.
入力:
- API key: Text value — The API key to use for this call
- Version date: Text value — The release date of the API to use
- Service endpoint location: US South, US East, Europe, Australia, Japan, UK, Korea = US East — The account's service location. Can be seen through IBM "Manage" in the resources section
- Instance ID: Text value — The Instance ID of the service.
- Text: Text value — The text to analyze
- Content type(任意): Text value = text/plain — The format of the requested values
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The results of the API call
- StatusCode: Numeric value — The status code of the API call
例外: Request timeout expired; Failed to Invoke cognitive services

## Analyze tone  `#analyzetoneibm`
Invokes the IBM service named 'Analyze Tone'.
入力:
- API key: Text value — The API key to use for this call
- Version date: Text value — The release date of the API to use
- Service endpoint location: US South, US East, Europe, Australia, Japan, UK, Korea = US East — The account's service location. Can be seen through IBM "Manage" in the resources section
- Instance ID: Text value — The Instance ID of the service.
- Provide text: From text, From file = From text — Specify how the text to be analyzed will be provided
- Text: Text value — The text to analyze
- File path: File — The path to the file to analyze
- Content type: text/plain, text/html, application/json = text/plain — The content type of the text that will be sent
- Tones(任意): Text value — The tone with which the results will be filtered (optional)
- Sentences(任意): Text value — Specify whether to remove the sentence analysis
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The results of the API call
- StatusCode: Numeric value — The status code of the API call
例外: Request timeout expired; Failed to Invoke cognitive services

## Classify Image  `#classifyimageibm`
Invokes the IBM service named 'Classify Image'.
入力:
- API key: Text value — The API key to use for this call
- Version date: Text value — The release date of the API to use
- Service endpoint location: US South, Europe, Korea = US South — The account's service location. Can be seen through IBM "Manage" in the resources section
- Instance ID: Text value — The Instance ID of the service.
- Provide image: From file, From GCS = From file — Specify how the image will be provided
- Image file path: File — The path to the image to be analyzed
- Image URL: Text value — The URL of the image to be analyzed
- Owners(任意): Text value = me — The classifiers to be used as a comma separated list
- Classifier IDs(任意): Text value = default — The classifier Ids to be used as a comma separated list
- Threshold(任意): Text value — The minimum score a class must have to be displayed in the response as a floating value
- Language(任意): Text value — The language of the output
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The results of the API call
- StatusCode: Numeric value — The status code of the API call
例外: Request timeout expired; Failed to Invoke cognitive services
