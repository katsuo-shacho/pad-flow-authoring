# Robin: XML

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### XML.ExecuteXPathQuery のセレクター: ExecuteXPath, ExecuteXPathAndGetFirstValueOnly

## XML.ExecuteXPathQuery.ExecuteXPath [A]
```
XML.ExecuteXPathQuery.ExecuteXPath XmlDocument: $'''example''' XPathQuery: $'''example''' XPathResults=> XPathResults
```
入力: XmlDocument:String XPathQuery:String
出力: XPathResults:List=>
ON ERROR可: InvalidXMLError, InvalidXPathError
固定: FirstValueOnly=False

## XML.ExecuteXPathQuery.ExecuteXPathAndGetFirstValueOnly [A]
```
XML.ExecuteXPathQuery.ExecuteXPathAndGetFirstValueOnly XPathQuery: $'''example''' XmlDocument: $'''example''' XPathResult=> XPathResult
```
入力: !XPathQuery:String !XmlDocument:String
出力: XPathResult:XmlNodeObject=>XPathResult
ON ERROR可: InvalidXMLError, InvalidXPathError
固定: FirstValueOnly=True

### XML.GetXmlElementAttribute のセレクター: GetElementAttribute, GetElementAttributeAsBoolean, GetElementAttributeAsDateTime, GetElementAttributeAsNumeric

## XML.GetXmlElementAttribute.GetElementAttribute [A]
```
XML.GetXmlElementAttribute.GetElementAttribute Document: XmlDocument AttributeName: $'''example''' XPathQuery: $'''example''' TextValue=> XmlAttributeValue
```
入力: AttributeName:String Document:XmlNodeObject XPathQuery:String
出力: TextValue:String=>
ON ERROR可: AttributeNotFoundError, ConvertAttributeError, InvalidXPathError, XPathNoElementError
固定: ValueType=Text

## XML.GetXmlElementAttribute.GetElementAttributeAsBoolean [A]
```
XML.GetXmlElementAttribute.GetElementAttributeAsBoolean XPathQuery: $'''example''' AttributeName: $'''example''' Document: XmlDocument BooleanValue=> XmlAttributeValue
```
入力: XPathQuery:String !AttributeName:String !Document:XmlNodeObject
出力: BooleanValue:Boolean=>XmlAttributeValue
ON ERROR可: AttributeNotFoundError, ConvertAttributeError, InvalidXPathError, XPathNoElementError
固定: ValueType=Boolean

## XML.GetXmlElementAttribute.GetElementAttributeAsDateTime [A]
```
XML.GetXmlElementAttribute.GetElementAttributeAsDateTime XPathQuery: $'''example''' AttributeName: $'''example''' Document: XmlDocument DateTimeValue=> XmlAttributeValue
```
入力: XPathQuery:String !AttributeName:String !Document:XmlNodeObject
出力: DateTimeValue:DateTime=>XmlAttributeValue
ON ERROR可: AttributeNotFoundError, ConvertAttributeError, InvalidXPathError, XPathNoElementError
固定: ValueType=DateTime

## XML.GetXmlElementAttribute.GetElementAttributeAsNumeric [A]
```
XML.GetXmlElementAttribute.GetElementAttributeAsNumeric XPathQuery: $'''example''' AttributeName: $'''example''' Document: XmlDocument NumericValue=> XmlAttributeValue
```
入力: XPathQuery:String !AttributeName:String !Document:XmlNodeObject
出力: NumericValue:Decimal=>XmlAttributeValue
ON ERROR可: AttributeNotFoundError, ConvertAttributeError, InvalidXPathError, XPathNoElementError
固定: ValueType=Numeric

### XML.GetXmlElementValue のセレクター: GetElementValue, GetElementValueAsBoolean, GetElementValueAsDateTime, GetElementValueAsNumeric

## XML.GetXmlElementValue.GetElementValue [A]
```
XML.GetXmlElementValue.GetElementValue Document: XmlDocument XPathQuery: $'''example''' TextValue=> XmlElementValue
```
入力: Document:XmlNodeObject XPathQuery:String
出力: TextValue:String=>
ON ERROR可: ConvertElementError, InvalidXPathError, XPathNoElementError
固定: ValueType=Text

## XML.GetXmlElementValue.GetElementValueAsBoolean [A]
```
XML.GetXmlElementValue.GetElementValueAsBoolean XPathQuery: $'''example''' Document: XmlDocument BooleanValue=> XmlElementValue
```
入力: XPathQuery:String !Document:XmlNodeObject
出力: BooleanValue:Boolean=>XmlElementValue
ON ERROR可: ConvertElementError, InvalidXPathError, XPathNoElementError
固定: ValueType=Boolean

## XML.GetXmlElementValue.GetElementValueAsDateTime [A]
```
XML.GetXmlElementValue.GetElementValueAsDateTime XPathQuery: $'''example''' Document: XmlDocument DateTimeValue=> XmlElementValue
```
入力: XPathQuery:String !Document:XmlNodeObject
出力: DateTimeValue:DateTime=>XmlElementValue
ON ERROR可: ConvertElementError, InvalidXPathError, XPathNoElementError
固定: ValueType=DateTime

## XML.GetXmlElementValue.GetElementValueAsNumeric [A]
```
XML.GetXmlElementValue.GetElementValueAsNumeric XPathQuery: $'''example''' Document: XmlDocument NumericValue=> XmlElementValue
```
入力: XPathQuery:String !Document:XmlNodeObject
出力: NumericValue:Decimal=>XmlElementValue
ON ERROR可: ConvertElementError, InvalidXPathError, XPathNoElementError
固定: ValueType=Numeric

## XML.InsertElement [A]
```
XML.InsertElement Document: XmlDocument XPathQuery: $'''example''' Element: XmlDocument
```
入力: Document:XmlNodeObject Element:XmlNodeObject XPathQuery:String
ON ERROR可: InsertElementError, InvalidXPathError, XPathNoElementError

## XML.ReadFromFile [A]
```
XML.ReadFromFile File: $'''C:\temp\test.xlsx''' Encoding: XML.FileEncoding.DefaultEncoding XmlDocument=> XmlDocument
```
入力: Encoding:FileEncoding{DefaultEncoding,ASCII,Unicode,BigEndianUnicode,UTF8} File:FileObject
出力: XmlDocument:XmlNodeObject=>
ON ERROR可: DirectoryNotFoundError, FileNotFoundError, InvalidFileError, ReadFileError

## XML.RemoveElement [A]
```
XML.RemoveElement Document: XmlDocument XPathQuery: $'''example'''
```
入力: Document:XmlNodeObject XPathQuery:String
ON ERROR可: InvalidXPathError, RemoveElementError

## XML.RemoveElementAttribute [A]
```
XML.RemoveElementAttribute Document: XmlDocument AttributeName: $'''example''' XPathQuery: $'''example'''
```
入力: AttributeName:String Document:XmlNodeObject XPathQuery:String
ON ERROR可: AttributeNotFoundError, InvalidXPathError, RemoveAttributeError, XPathNoElementError

## XML.SetElementAttribute [A]
```
XML.SetElementAttribute Document: XmlDocument AttributeName: $'''example''' AttributeValue: $'''example''' XPathQuery: $'''example'''
```
入力: AttributeName:String AttributeValue:String Document:XmlNodeObject XPathQuery:String
ON ERROR可: InvalidXPathError, SetAttributeError, XPathNoElementError

## XML.SetElementValue [A]
```
XML.SetElementValue Document: XmlDocument ElementValue: $'''example''' XPathQuery: $'''example'''
```
入力: Document:XmlNodeObject ElementValue:String XPathQuery:String
ON ERROR可: InvalidXPathError, SetElementError, XPathNoElementError

### XML.WriteXmlToFile のセレクター: WriteToFile, WriteToFileFormatted

## XML.WriteXmlToFile.WriteToFile [A]
```
XML.WriteXmlToFile.WriteToFile Xml: $'''example''' Encoding: XML.FileEncoding.DefaultEncoding File: $'''C:\temp\test.xlsx'''
```
入力: !Xml:String !Encoding:FileEncoding{DefaultEncoding,ASCII,Unicode,BigEndianUnicode,UTF8} !File:FileObject
ON ERROR可: InvalidDirectoryError, WriteFileError
固定: FormatXml=False

## XML.WriteXmlToFile.WriteToFileFormatted [A]
```
XML.WriteXmlToFile.WriteToFileFormatted File: $'''C:\temp\test.xlsx''' Xml: $'''example''' Encoding: XML.FileEncoding.DefaultEncoding Indentation: 2
```
入力: Encoding:FileEncoding{DefaultEncoding,ASCII,Unicode,BigEndianUnicode,UTF8} File:FileObject Indentation:Int32 Xml:String
ON ERROR可: InvalidDirectoryError, WriteFileError
固定: FormatXml=True
