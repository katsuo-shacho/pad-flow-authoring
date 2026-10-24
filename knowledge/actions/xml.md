# XML actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/xml （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate provides the capability to use desktop flows to manage XML attributes and elements. To read an XML file, use the Read XML from file action. Specify the path or browse for the file, and select one of the encoding options. After selecting a file, use the Execute XPath expression action to run an Xpath query. The following example uses a produced variable from the Read XML from file action to specify the document. To retrieve an attribute from an XML file, use the Get XML attribute action. In the following example, status is an attribute of client, which is an element of clientlist

## Read XML from file  `#readfromfile`
Read the contents of an XML file into a variable.
入力:
- File path: File — The file that contains the XML document to read
- Encoding: System default, ASCII, Unicode, Unicode big endian, UTF-8 = System default — The encoding used for the specified file
出力:
- XmlDocument: XML node — The variable that holds the read XML document
例外: Directory not found; File not found; Failed to read from file; File doesn't contain a valid XML document

## Write XML to file  `#writexmltofile`
Write the contents of an XML node variable into a file.
入力:
- File path: File — The file to write the XML document into
- XML to write: Text value — The XML node or document to write into the file
- Encoding: System default, ASCII, Unicode, Unicode big endian, UTF-8 = System default — The encoding used for the specified file
- Format XML: Boolean value = True — Specifies whether to format the XML
- Indentation per level(任意): Numeric value = 2 — Specifies by how many spaces to indent each level of the XML
例外: Invalid directory specified; Failed to write XML to file

## Execute XPath expression  `#executexpathquery`
Extract values from an XML document based on the provided XPath query.
入力:
- XML document to parse: Text value — The XML as text or a previously defined variable that contains the XML document to parse
- XPath query: Text value — The XPath expression to execute against the XML document
- Get first value only: Boolean value = False — Specifies whether to retrieve a single value (the first value only) or all the values that match the provided XPath expression
出力:
- XPathResult: XML node — The extracted node(s) as an XML node
- XPathResults: List of XML nodes — The extracted node(s) as a list of XML nodes
例外: Invalid XML document provided; Invalid XPath expression provided

## Get XML element attribute  `#getxmlelementattribute`
Get the value of an attribute of an XML element.
入力:
- XML document: XML node — The XML document or XML element to retrieve its attribute
- XPath query(任意): Text value — The XPath expression to locate the subelement and retrieve its attribute
- Attribute name: Text value — The name of the attribute to retrieve its value
- Get value as: Text value, Numeric value, Datetime value, Boolean value = Text value — Specifies the data type for the attribute value
出力:
- XmlAttributeValue: Boolean value — The retrieved value of the XML attribute
- XmlAttributeValue: Datetime — The retrieved value of the XML attribute
- XmlAttributeValue: Numeric value — The retrieved value of the XML attribute
- XmlAttributeValue: Text value — The retrieved value of the XML attribute
例外: Invalid XPath expression provided; XPath expression returns no element; Attribute not found in element; Failed to convert attribute value to the requested data type

## Set XML element attribute  `#setelementattribute`
Set the value of an attribute of an XML element.
入力:
- XML document: XML node — The XML document or XML element to set its attribute
- XPath query(任意): Text value — The XPath expression to locate the subelement and set its attribute
- Attribute name: Text value — The name of the attribute to set its value
- Attribute value: Text value — The new value for the attribute
例外: Invalid XPath expression provided; XPath expression returns no element; Failed to set XML attribute

## Remove XML element attribute  `#removeelementattribute`
Remove an attribute from an XML element.
入力:
- XML document: XML node — The XML document or XML element to remove its attribute
- XPath query(任意): Text value — The XPath expression to locate the subelement and remove its attribute
- Attribute name: Text value — The name of the attribute to remove
例外: Invalid XPath expression provided; XPath expression returns no element; Attribute not found in element; Failed to remove XML attribute

## Get XML element value  `#getxmlelementvalue`
Get the value of an XML element.
入力:
- XML document: XML node — The XML document or XML element to retrieve its value
- XPath query(任意): Text value — The XPath expression to locate the subelement and retrieve its value
- Get value as: Text value, Numeric value, Datetime value, Boolean value = Text value — Specifies the data type for the XML element value
出力:
- XmlElementValue: Boolean value — The XML element value
- XmlElementValue: Datetime — The XML element value
- XmlElementValue: Numeric value — The XML element value
- XmlElementValue: Text value — The XML element value
例外: Invalid XPath expression provided; XPath expression returns no element; Failed to convert element value to the requested data type

## Set XML element value  `#setelementvalue`
Set the value of an XML element.
入力:
- XML document: XML node — The XML document or XML element to retrieve it value
- XPath query(任意): Text value — The XPath expression to locate the subelement and retrieve its value
- XML element value: Text value — The new value for the XML element
例外: Invalid XPath expression provided; XPath expression returns no element; Failed to set element value

## Insert XML element  `#insertelement`
Insert a new XML element into an XML document.
入力:
- XML document: XML node — The XML document to insert the new XML element
- XPath query: Text value — The XPath expression to locate the parent XML element and insert the new element into it
- XML element to insert: XML node — The new XML element to insert into the XML document
例外: Invalid XPath expression provided; XPath expression returns no element; Failed to insert XML element

## Remove XML element  `#removeelement`
Remove one or more XML elements from an XML document.
入力:
- XML document: XML node — The XML document that contains the XML element(s) to remove
- XPath query: Text value — The XPath expression to locate the element(s) to remove
例外: Invalid XPath expression provided; Failed to remove XML element
