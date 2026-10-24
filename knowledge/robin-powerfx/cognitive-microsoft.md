# Robin: Cognitive - Microsoft

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### MicrosoftCognitive.AnalyzeImageMicrosoft のセレクター: AnalyzeImageFromFile, AnalyzeImageFromUrl

## MicrosoftCognitive.AnalyzeImageMicrosoft.AnalyzeImageFromFile [A]
```
MicrosoftCognitive.AnalyzeImageMicrosoft.AnalyzeImageFromFile ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' ImageFile: $fx'C:\temp\test.xlsx' Timeout: 30 Details: $fx'example' Language: $fx'example' VisualFeatures: $fx'example' Response=> JSONResponse StatusCode=> StatusCode
```
入力: Details:String ImageFile:FileObject Language:String ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} SubscriptionKey:String Timeout:Int32 VisualFeatures:String
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## MicrosoftCognitive.AnalyzeImageMicrosoft.AnalyzeImageFromUrl [A]
```
MicrosoftCognitive.AnalyzeImageMicrosoft.AnalyzeImageFromUrl SubscriptionKey: $fx'example' ServerLocation: Cognitive.MicrosoftServerLocation.WestUS VisualFeatures: $fx'example' Timeout: 30 Details: $fx'example' Language: $fx'example' ImageUrl: $fx'example' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !SubscriptionKey:String !ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} VisualFeatures:String !Timeout:Int32 Details:String Language:String !ImageUrl:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### MicrosoftCognitive.DescribeImageMicrosoft のセレクター: DescribeImageFromFile, DescribeImageFromUrl

## MicrosoftCognitive.DescribeImageMicrosoft.DescribeImageFromFile [A]
```
MicrosoftCognitive.DescribeImageMicrosoft.DescribeImageFromFile ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' ImageFile: $fx'C:\temp\test.xlsx' Timeout: 30 MaxCandidates: $fx'example' Response=> JSONResponse StatusCode=> StatusCode
```
入力: ImageFile:FileObject MaxCandidates:String ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} SubscriptionKey:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## MicrosoftCognitive.DescribeImageMicrosoft.DescribeImageFromUrl [A]
```
MicrosoftCognitive.DescribeImageMicrosoft.DescribeImageFromUrl ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' Timeout: 30 ImageUrl: $fx'example' MaxCandidates: $fx'example' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} !SubscriptionKey:String !Timeout:Int32 !ImageUrl:String MaxCandidates:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### MicrosoftCognitive.OCRMicrosoft のセレクター: OCRFromFile, OCRFromURL

## MicrosoftCognitive.OCRMicrosoft.OCRFromFile [A]
```
MicrosoftCognitive.OCRMicrosoft.OCRFromFile ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' ImageFile: $fx'C:\temp\test.xlsx' Timeout: 30 DetectOrientation: $fx'example' Language: $fx'example' Response=> JSONResponse StatusCode=> StatusCode
```
入力: DetectOrientation:String ImageFile:FileObject Language:String ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} SubscriptionKey:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## MicrosoftCognitive.OCRMicrosoft.OCRFromURL [A]
```
MicrosoftCognitive.OCRMicrosoft.OCRFromURL ServerLocation: Cognitive.MicrosoftServerLocation.WestUS Timeout: 30 SubscriptionKey: $fx'example' DetectOrientation: $fx'example' Language: $fx'example' ImageUrl: $fx'example' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} !Timeout:Int32 !SubscriptionKey:String DetectOrientation:String Language:String !ImageUrl:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

## MicrosoftCognitive.SpellCheckMicrosoft [A]
```
MicrosoftCognitive.SpellCheckMicrosoft SubscriptionKey: $fx'example' Text: FileList Timeout: 30 Mkt: $fx'example' Mode: $fx'example' Response=> JSONResponse StatusCode=> StatusCode
```
入力: Mkt:String Mode:String SubscriptionKey:String Text:List Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError

### MicrosoftCognitive.TagImageMicrosoft のセレクター: TagImageFromFile, TagImageFromURL

## MicrosoftCognitive.TagImageMicrosoft.TagImageFromFile [A]
```
MicrosoftCognitive.TagImageMicrosoft.TagImageFromFile ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' ImageFile: $fx'C:\temp\test.xlsx' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: ImageFile:FileObject ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} SubscriptionKey:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## MicrosoftCognitive.TagImageMicrosoft.TagImageFromURL [A]
```
MicrosoftCognitive.TagImageMicrosoft.TagImageFromURL ServerLocation: Cognitive.MicrosoftServerLocation.WestUS SubscriptionKey: $fx'example' Timeout: 30 ImageUrl: $fx'example' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !ServerLocation:MicrosoftServerLocation{WestUS,WestUS2,EastUS,EastUS2,WestCentralUS,SouthCentralUS,WestEurope,NorthEurope,SoutheastAsia,EastAsia,AustraliaEast,BrazilSouth,CanadaCentral,CentralIndia,UKSouth,JapanEast} !SubscriptionKey:String !Timeout:Int32 !ImageUrl:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url
