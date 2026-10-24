# Robin: Cognitive - IBM

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### IBMCognitive.AnalyzeToneIBM のセレクター: AnalyzeFromFile, AnalyzeFromText

## IBMCognitive.AnalyzeToneIBM.AnalyzeFromFile [A]
```
IBMCognitive.AnalyzeToneIBM.AnalyzeFromFile Sentences: $'''example''' Timeout: 30 VersionDate: $'''example''' Tones: $'''example''' ContentType: Cognitive.ContentType.TextPlain ApiKey: $'''example''' FilePath: $'''C:\temp\test.xlsx''' Location: Cognitive.ToneAnalyzerServiceLocation.UsEast InstanceId: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: Sentences:String !Timeout:Int32 !VersionDate:String Tones:String !ContentType:ContentType{TextPlain,TextHtml,ApplicationJson} !ApiKey:String !FilePath:FileObject !Location:ToneAnalyzerServiceLocation{UsSouth,UsEast,Europe,Australia,Japan,Uk,Korea} !InstanceId:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideText=File

## IBMCognitive.AnalyzeToneIBM.AnalyzeFromText [A]
```
IBMCognitive.AnalyzeToneIBM.AnalyzeFromText ApiKey: $'''example''' VersionDate: $'''example''' Location: Cognitive.ToneAnalyzerServiceLocation.UsEast InstanceId: $'''example''' Text: $'''example''' ContentType: Cognitive.ContentType.TextPlain Timeout: 30 Sentences: $'''example''' Tones: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: ApiKey:String ContentType:ContentType{TextPlain,TextHtml,ApplicationJson} InstanceId:String Location:ToneAnalyzerServiceLocation{UsSouth,UsEast,Europe,Australia,Japan,Uk,Korea} Sentences:String Text:String Timeout:Int32 Tones:String VersionDate:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideText=Text

### IBMCognitive.ClassifyImageIBM のセレクター: ClassifyImageFromFile, ClassifyImageFromUrl

## IBMCognitive.ClassifyImageIBM.ClassifyImageFromFile [A]
```
IBMCognitive.ClassifyImageIBM.ClassifyImageFromFile ApiKey: $'''example''' VersionDate: $'''example''' Location: Cognitive.ImageClassificationServiceLocation.UsSouth InstanceId: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Owners: $'''me''' ClassifierIds: $'''default''' Timeout: 30 Language: $'''example''' Threshold: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: ApiKey:String ClassifierIds:String ImageFile:FileObject InstanceId:String Language:String Location:ImageClassificationServiceLocation{UsSouth,Europe,Korea} Owners:String Threshold:String Timeout:Int32 VersionDate:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## IBMCognitive.ClassifyImageIBM.ClassifyImageFromUrl [A]
```
IBMCognitive.ClassifyImageIBM.ClassifyImageFromUrl Owners: $'''example''' Location: Cognitive.ImageClassificationServiceLocation.UsSouth VersionDate: $'''example''' Timeout: 30 Threshold: $'''example''' ClassifierIds: $'''example''' ApiKey: $'''example''' Language: $'''example''' InstanceId: $'''example''' ImageUrl: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: Owners:String !Location:ImageClassificationServiceLocation{UsSouth,Europe,Korea} !VersionDate:String !Timeout:Int32 Threshold:String ClassifierIds:String !ApiKey:String Language:String !InstanceId:String !ImageUrl:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### IBMCognitive.ConvertDocumentIBM のセレクター: ConvertToAnswerUnits, ConvertToHtml, ConvertToText

## IBMCognitive.ConvertDocumentIBM.ConvertToAnswerUnits [A]
```
IBMCognitive.ConvertDocumentIBM.ConvertToAnswerUnits Username: $'''example''' Password: $'''password''' VersionDate: $'''example''' FilePath: $'''C:\temp\test.xlsx''' MimeType: Cognitive.MimeType.TextHtml Timeout: 30 AnswerUnits: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: AnswerUnits:String FilePath:FileObject MimeType:MimeType{TextHtml,TextXhtmlXml,ApplicationPdf,ApplicationMsWord,ApplicationVndOpenXmlFormatsOfficeDocumentWordProcessingmlDocument} Password:EncryptableObject Timeout:Int32 Username:String VersionDate:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ConversionTarget=AnswerUnits

## IBMCognitive.ConvertDocumentIBM.ConvertToHtml [A]
```
IBMCognitive.ConvertDocumentIBM.ConvertToHtml Timeout: 30 Password: $'''password''' VersionDate: $'''example''' Username: $'''example''' MimeType: Cognitive.MimeType.TextHtml FilePath: $'''C:\temp\test.xlsx''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !Password:EncryptableObject !VersionDate:String !Username:String !MimeType:MimeType{TextHtml,TextXhtmlXml,ApplicationPdf,ApplicationMsWord,ApplicationVndOpenXmlFormatsOfficeDocumentWordProcessingmlDocument} !FilePath:FileObject
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ConversionTarget=NormalizedHtml

## IBMCognitive.ConvertDocumentIBM.ConvertToText [A]
```
IBMCognitive.ConvertDocumentIBM.ConvertToText Timeout: 30 Password: $'''password''' VersionDate: $'''example''' Username: $'''example''' MimeType: Cognitive.MimeType.TextHtml FilePath: $'''C:\temp\test.xlsx''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !Password:EncryptableObject !VersionDate:String !Username:String !MimeType:MimeType{TextHtml,TextXhtmlXml,ApplicationPdf,ApplicationMsWord,ApplicationVndOpenXmlFormatsOfficeDocumentWordProcessingmlDocument} !FilePath:FileObject
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ConversionTarget=NormalizedText

## IBMCognitive.IdentifyLanguageIBM [A]
```
IBMCognitive.IdentifyLanguageIBM ApiKey: $'''example''' VersionDate: $'''example''' Location: Cognitive.LanguageTranslatorServiceLocation.UsEast InstanceId: $'''example''' Text: $'''example''' ContentType: $'''text/plain''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: ApiKey:String ContentType:String InstanceId:String Location:LanguageTranslatorServiceLocation{UsSouth,UsEast,Europe,Australia,Japan,Uk,Korea} Text:String Timeout:Int32 VersionDate:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError

### IBMCognitive.TranslateIBM のセレクター: TranslateWithModelId, TranslateWithSourceAndTarget

## IBMCognitive.TranslateIBM.TranslateWithModelId [A]
```
IBMCognitive.TranslateIBM.TranslateWithModelId ApiKey: $'''example''' VersionDate: $'''example''' Location: Cognitive.LanguageTranslatorServiceLocation.UsEast InstanceId: $'''example''' ModelId: $'''example''' Text: FileList Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: ApiKey:String InstanceId:String Location:LanguageTranslatorServiceLocation{UsSouth,UsEast,Europe,Australia,Japan,Uk,Korea} ModelId:String Text:List Timeout:Int32 VersionDate:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: TranslateMode=ModelId

## IBMCognitive.TranslateIBM.TranslateWithSourceAndTarget [A]
```
IBMCognitive.TranslateIBM.TranslateWithSourceAndTarget Text: List Target: $'''example''' Timeout: 30 VersionDate: $'''example''' InstanceId: $'''example''' ApiKey: $'''example''' Location: Cognitive.LanguageTranslatorServiceLocation.UsEast Source: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Text:List<String> !Target:String !Timeout:Int32 !VersionDate:String !InstanceId:String !ApiKey:String !Location:LanguageTranslatorServiceLocation{UsSouth,UsEast,Europe,Australia,Japan,Uk,Korea} !Source:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: TranslateMode=SourceTarget
