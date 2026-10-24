# Google cognitive actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/googlecognitive （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Google cognitive services allow you to process unstructured data through machine learning and simplify complicated tasks like text analysis and computer vision. You can implement this functionality in your desktop flows using the Google cognitive group of actions. All Google cognitive actions require an API key that authorizes you to use the respective services. You can manage your API keys in the APIs & services section of the Cloud Console.

## Analyze sentiment  `#analyzesentimentgoogle`
Invokes the Google Cloud Natural Language service named 'Analyze Sentiment'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Document type: Plain text, HTML = Plain text — The type of document to transmit
- Provide document: From file, From GCS = From file — Specify whether the document will be provided by a full path or a Google Cloud Storage URI
- File path: File — The full path (folder plus filename) of the document to transmit
- GCS Content URI: Text value — The URI of the image residing on Google Cloud Storage
- Language(任意): Text value — The language of the text
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Analyze entities  `#analyzeentitiesgoogle`
Invokes the Google Cloud Natural Language service named 'Analyze Entities'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Document type: Plain text, HTML = Plain text — The type of the document to transmit
- Provide file: From file, From GCS = From file — Specify whether the document will be provided by a full path or a Google Cloud Storage URI
- File path: File — The full path (folder plus filename) of the document to transmit
- GCS URL: Text value — The URI of the document residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Analyze syntax  `#analyzesyntaxgoogle`
Invokes the Google Cloud Natural Language service named 'Analyze Syntax'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Document type: Plain text, HTML = Plain text — The type of document to transmit
- Provide document: From file, From GCS = From file — Specify whether the document will be provided by a full path or a Google Cloud Storage URI
- File path: File — The full path (folder plus filename) of the document to transmit
- GCS Content URI: Text value — The URI of the image residing on Google Cloud Storage
- Language(任意): Text value — The language of the text
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Label detection  `#labeldetectiongoogle`
Invokes the Google Cloud Vision service named 'Label Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Landmark detection  `#landmarkdetectiongoogle`
Invokes the Google Cloud Vision service named 'Landmark Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file path: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Text Detection  `#textdetectiongoogle`
Invokes the Google Cloud Vision service named 'Text Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Logo detection  `#logodetectiongoogle`
Invokes the Google Cloud Vision service named 'Logo Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Image properties detection  `#imagepropertiesdetectiongoogle`
Invokes the Google Cloud Vision service named 'Image Properties Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired

## Safe search detection  `#safesearchdetectiongoogle`
Invokes the Google Cloud Vision service named 'Safe Search Detection'.
入力:
- API key: Text value — The Google Cloud API key to be used for this API call
- Provide image: From file, From GCS = From file — Specify whether the image will be provided by a full path or a Google Cloud Storage URI
- Image file: File — The full path (folder plus filename) of the image file to transmit
- GCS Image URI: Text value — The URI of the image residing on Google Cloud Storage
- Timeout(任意): Numeric value = 30 — The time (in seconds) that the agent should wait for a connection to be established with the server, before it fails
出力:
- JSONResponse: Custom object — The API response results
- StatusCode: Numeric value — The status code returned
例外: Failed to Invoke cognitive services; Request timeout expired
