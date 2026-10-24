# PDF actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/pdf （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: PDF actions enable you to extract images, text, and tables from PDF files, and arrange pages to create new documents. To extract text from a PDF file, use the Extract text from PDF action. The following example extracts text from a specific range of pages of a password-protected file. The password is specified in the Advanced settings. To extract texts arranged in a tabular form, enable Optimize for structured data to improve the results' format and accuracy. To extract tables from a PDF file, deploy the Extract tables from PDF action, select the file, and specify the pages to extract from. Th

## Extract text from PDF  `#extracttextfrompdfaction`
You can extract text from a PDF file by using the "Extract text from PDF" action. In the action properties you can define the source PDF file and the pages that text should be extracted from. Under the advanced action properties you can define a password in case the PDF file is protected and if the engine should optimize for structured data or not.
入力:
- PDF file: File — The PDF file to extract text from. Enter a file path, a variable containing a file or a text path
- Page(s) to extract: All, Single, Range = All — Specifies how many pages to extract: All pages, a single page or a range of pages
- Single page number: Numeric value — The number of the single page to extract text from
- From page number: Numeric value — The first page number from the range of pages to extract text from
- To page number: Numeric value — The last page number from the range of pages to extract text from
- Password(任意): Direct encrypted input or Text value — The password of the PDF file. Leave this blank if the PDF isn't password protected
- Optimize for structured data: Boolean value = False — Specify whether to detect formatted layout in the document and extract text accordingly
出力:
- ExtractedPDFText: Text value — The extracted text
例外: PDF file doesn't exist; Invalid password; Failed to extract text

## Extract tables from PDF  `#extracttablesfrompdfaction`
You can extract tables that are contained in a PDF file by using the Extract tables from PDF action. In the action properties you can define the PDF file and the range of pages that the tables will be extracted from. Under the advanced action properties you can define a password in case a the PDF file is protected, define if the table has headers or not, and finally if tables that cross page margins should be merged or not.
入力:
- PDF file: File — The PDF file to extract tables from. Enter a file path, a variable containing a file or a text path
- Page(s) to extract: All, Single, Range = All — Specifies how many pages to extract tables from: all pages, a single page or a range of pages
- Single page number: Numeric value — The number of the single page to extract tables from
- From page number: Numeric value — The first page number from the range of pages to extract tables from
- To page number: Numeric value — The last page number from the range of pages to extract tables from
- Password(任意): Direct encrypted input or Text value — The password of the PDF file. Leave this blank if the PDF isn't password protected
- Merge tables that cross page margins: Boolean value = True — Specifies whether to merge tables that cross page margins in the specified page range
- First line contains column names: Boolean value = True — Specifies whether the first line of table contains column names
出力:
- ExtractedPDFTables: List of PDF table info — The extracted tables with their info as a list
例外: PDF file doesn't exist; Invalid password; Failed to extract tables

## Extract images from PDF  `#extractimagesfrompdfaction`
To extract images from a PDF file you can use the Extract images from PDF action. In the action parameters you can define the PDF file and the pages to extract images from, the naming convention of the extacted images and the target location of the saved images. You can also define a password if the PDF file is protected under the advanced settings.
入力:
- PDF file: File — The PDF file to extract images from. Enter a file path, a variable containing a file or a text path
- Password(任意): Direct encrypted input or Text value — The password of the PDF file. Leave this blank if the PDF isn't password protected
- Page(s) to extract: All, Single, Range = All — Specifies how many pages to extract: All pages, a single page or a range of pages
- Single page number: Numeric value — The number of the single page to extract images from
- From page number: Numeric value — The first page number from the range of pages to extract images from
- To page number: Numeric value — The last page number from the range of pages to extract images from
- Image(s) name: Text value — How the name of the image(s) starts. Extracted image(s) name example: GivenName_1, GivenName_2
- Save image(s) to: Folder — The folder to save the extracted images as png files
例外: Invalid password; Failed to extract images; Folder doesn't exist; PDF file doesn't exist

## Extract PDF file pages to new PDF file  `#extractpages`
You can create a new PDF file by extracting pages from an existing PDF file by using the PDF file pages to a new PDF file action. In the action parameters you can define the PDF file to extract the pages from, the page(s) to be extracted, the location of the new PDF file and what should happen if a file with the same name and extension already exists. Finally, under the advanced properties you can define a password in case the source PDF is protected.
入力:
- PDF file: File — The PDF file to extract pages from. Enter a file path, a variable containing a file or a text path
- Password(任意): Direct encrypted input or Text value — The password of the PDF file. Leave this blank if the PDF isn't password protected
- Page selection: Text value — The index numbers of the pages to keep (for example, 1,3,17-24)
- Extracted PDF path: File — The path to store the extracted PDF file
- If file exists: Overwrite, Don't overwrite, Add sequential suffix = Add sequential suffix — Specifies what to do in case the output PDF file already exists
出力:
- ExtractedPDF: File — The new PDF file
例外: Invalid password; PDF file doesn't exist; Page out of bounds; Invalid page selection; Failed to extract new PDF

## Merge PDF files  `#mergefiles`
Merges multiple PDF files into a new one.
入力:
- PDF files: List of Files — The files to merge. Enclose multiple files in double quotes (") and separate them by a delimiter, or use a list of files
- Merged PDF path: File — The path to store the merged PDF
- If file exists: Overwrite, Don't overwrite, Add sequential suffix = Add sequential suffix — Specifies what to do in case the destination file already exists
- Passwords(任意): Direct encrypted input or Text value — The delimited passwords. The order should be the same as the order of the input PDFs. Leave this blank if the PDFs aren't password protected
- Delimiter: Text value = , — A custom password delimiter. This delimiter shouldn't be part of any of the passwords
出力:
- MergedPDF: File — The merged PDF file
例外: PDF file doesn't exist; Invalid password; Failed to merge PDF files
