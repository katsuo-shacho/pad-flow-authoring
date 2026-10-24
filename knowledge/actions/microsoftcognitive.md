# Microsoft cognitive actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/microsoftcognitive （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Azure Cognitive Services enables you to accelerate decision-making using artificial intelligence without requiring machine learning expertise. Desktop flows provide a wide variety of Microsoft cognitive actions that allow you to integrate this functionality into your desktop flows. Text analysis, computer vision, and spell-checking are all tasks that Microsoft cognitive actions can perform. All Microsoft cognitive actions require a subscription key that validates your subscription for a service or group of services. The keys are available in the Azure portal for each resource you've created.

## Spell check  `#spellcheck`
Invokes the Microsoft Cognitive service named 'Bing Spell Check.'
入力:
- Subscription key: Text value — The subscription key to use for this API call
- Text: List of Text values — The text or the list of texts to send
- Mode(任意): Text value — Specify the spell-check mode
- Mkt(任意): Text value — For proof mode, the only supported language codes are: en-us, es-es, pt-br. For spell mode, all language codes are supported
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Analyze image  `#analyzeimagemicrosoft`
Invokes the Microsoft Cognitive service named 'Analyze Image.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a URL address
- Image file: File — The full path (folder plus filename) of the image file to transmit
- Image URL: Text value — The URL address of an image
- Visual features(任意): Text value — A text value indicating what visual feature types to return. Multiple values should be comma-separated. For example: categories, tags, description
- Details(任意): Text value — A text value indicating which domain-specific details to return. Multiple values should be comma-separated
- Language(任意): Text value — A text value indicating which language to return. The service will return recognition results in the specified language
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Describe image  `#describeimagemicrosoft`
Invokes the Microsoft Cognitive service named 'Describe Image.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a URL address
- Image file: File — The full path (folder plus filename) of the image file to transmit
- Image URL: Text value — The URL address of an image
- Max candidates(任意): Text value — The maximum number of candidate descriptions to be returned. The default is 1
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## OCR  `#ocrmicrosoft`
Invokes the Microsoft Cognitive service named 'OCR.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a URL address
- Image file: File — The full path (folder plus filename) of the image file to transmit
- Image URL: Text value — The URL address of an image
- Language(任意): Text value — The BCP-47 language code of the text to detect in the image
- Detect orientation(任意): Text value — Specify whether to detect the text orientation in the image
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Tag image  `#tagimagemicrosoft`
Invokes the Microsoft Cognitive service named 'Tag Image.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a URL address
- Image file: File — The full path (folder plus filename) of the image file to transmit
- Image URL: Text value — The URL address of an image
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Detect language  `#detectlanguage`
Invokes the Microsoft Cognitive service named 'Text Analytics - Detect Language.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Text: Text value — The text to analyze
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Key phrases  `#keyphrases`
Invokes the Microsoft Cognitive service named 'Text Analytics - Key Phrases.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Text: List of Text values — The text or the list of texts to analyze
- Language(任意): Text value — The language of the text(s)
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services

## Sentiment  `#sentiment`
Invokes the Microsoft Cognitive service named 'Text Analytics - Sentiment.'
入力:
- Server location: West US, West US 2, East US, East US 2, West Central US, South Central US, West Europe, North Europe, Southeast Asia, East Asia, Australia East, Brazil South, Canada Central, Central India, UK South, Japan East = West US — The server location to be used for this API call
- Subscription key: Text value — The subscription key to use for this API call
- Text: List of Text values — Text
- Language(任意): Text value — The two letter ISO 639-1 representation of the language of the text(s)
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Request timeout expired; Failed to Invoke cognitive services
