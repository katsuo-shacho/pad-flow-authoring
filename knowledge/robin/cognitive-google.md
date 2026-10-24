# Robin: Cognitive - Google

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### GoogleCognitive.AnalyzeEntitiesGoogle のセレクター: AnalyzeEntitiesFromFile, AnalyzeEntitiesFromGCS

## GoogleCognitive.AnalyzeEntitiesGoogle.AnalyzeEntitiesFromFile [A]
```
GoogleCognitive.AnalyzeEntitiesGoogle.AnalyzeEntitiesFromFile APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText FilePath: $'''C:\temp\test.xlsx''' Timeout: 30 Language: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String DocumentType:DocumentType{PlainText,Html} FilePath:FileObject Language:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=FilePath

## GoogleCognitive.AnalyzeEntitiesGoogle.AnalyzeEntitiesFromGCS [A]
```
GoogleCognitive.AnalyzeEntitiesGoogle.AnalyzeEntitiesFromGCS Language: $'''example''' Timeout: 30 GcsUrl: $'''example''' APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText StatusCode=> StatusCode Response=> JSONResponse
```
入力: Language:String !Timeout:Int32 !GcsUrl:String !APIKey:String !DocumentType:DocumentType{PlainText,Html}
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=Url

### GoogleCognitive.AnalyzeSentimentGoogle のセレクター: AnalyzeSentimentFromFile, AnalyzeSentimentFromGCS

## GoogleCognitive.AnalyzeSentimentGoogle.AnalyzeSentimentFromFile [A]
```
GoogleCognitive.AnalyzeSentimentGoogle.AnalyzeSentimentFromFile APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText FilePath: $'''C:\temp\test.xlsx''' Timeout: 30 Language: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String DocumentType:DocumentType{PlainText,Html} FilePath:FileObject Language:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=FilePath

## GoogleCognitive.AnalyzeSentimentGoogle.AnalyzeSentimentFromGCS [A]
```
GoogleCognitive.AnalyzeSentimentGoogle.AnalyzeSentimentFromGCS Language: $'''example''' Timeout: 30 GcsUrl: $'''example''' APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText StatusCode=> StatusCode Response=> JSONResponse
```
入力: Language:String !Timeout:Int32 !GcsUrl:String !APIKey:String !DocumentType:DocumentType{PlainText,Html}
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=Url

### GoogleCognitive.AnalyzeSyntaxGoogle のセレクター: AnalyzeSyntaxFromFile, AnalyzeSyntaxFromGCS

## GoogleCognitive.AnalyzeSyntaxGoogle.AnalyzeSyntaxFromFile [A]
```
GoogleCognitive.AnalyzeSyntaxGoogle.AnalyzeSyntaxFromFile APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText FilePath: $'''C:\temp\test.xlsx''' Timeout: 30 Language: $'''example''' Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String DocumentType:DocumentType{PlainText,Html} FilePath:FileObject Language:String Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=FilePath

## GoogleCognitive.AnalyzeSyntaxGoogle.AnalyzeSyntaxFromGCS [A]
```
GoogleCognitive.AnalyzeSyntaxGoogle.AnalyzeSyntaxFromGCS Language: $'''example''' Timeout: 30 GcsUrl: $'''example''' APIKey: $'''example''' DocumentType: Cognitive.DocumentType.PlainText StatusCode=> StatusCode Response=> JSONResponse
```
入力: Language:String !Timeout:Int32 !GcsUrl:String !APIKey:String !DocumentType:DocumentType{PlainText,Html}
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideFile=Url

### GoogleCognitive.ImagePropertiesDetectionGoogle のセレクター: ImagePropertiesDetectionFromFile, ImagePropertiesDetectionFromGCS

## GoogleCognitive.ImagePropertiesDetectionGoogle.ImagePropertiesDetectionFromFile [A]
```
GoogleCognitive.ImagePropertiesDetectionGoogle.ImagePropertiesDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.ImagePropertiesDetectionGoogle.ImagePropertiesDetectionFromGCS [A]
```
GoogleCognitive.ImagePropertiesDetectionGoogle.ImagePropertiesDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### GoogleCognitive.LabelDetectionGoogle のセレクター: LabelDetectionFromFile, LabelDetectionFromGCS

## GoogleCognitive.LabelDetectionGoogle.LabelDetectionFromFile [A]
```
GoogleCognitive.LabelDetectionGoogle.LabelDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.LabelDetectionGoogle.LabelDetectionFromGCS [A]
```
GoogleCognitive.LabelDetectionGoogle.LabelDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### GoogleCognitive.LandmarkDetectionGoogle のセレクター: LandmarkDetectionFromFile, LandmarkDetectionFromGCS

## GoogleCognitive.LandmarkDetectionGoogle.LandmarkDetectionFromFile [A]
```
GoogleCognitive.LandmarkDetectionGoogle.LandmarkDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.LandmarkDetectionGoogle.LandmarkDetectionFromGCS [A]
```
GoogleCognitive.LandmarkDetectionGoogle.LandmarkDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### GoogleCognitive.LogoDetectionGoogle のセレクター: LogoDetectionFromFile, LogoDetectionFromGCS

## GoogleCognitive.LogoDetectionGoogle.LogoDetectionFromFile [A]
```
GoogleCognitive.LogoDetectionGoogle.LogoDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.LogoDetectionGoogle.LogoDetectionFromGCS [A]
```
GoogleCognitive.LogoDetectionGoogle.LogoDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### GoogleCognitive.SafeSearchDetectionGoogle のセレクター: SafeSearchDetectionFromFile, SafeSearchDetectionFromGCS

## GoogleCognitive.SafeSearchDetectionGoogle.SafeSearchDetectionFromFile [A]
```
GoogleCognitive.SafeSearchDetectionGoogle.SafeSearchDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.SafeSearchDetectionGoogle.SafeSearchDetectionFromGCS [A]
```
GoogleCognitive.SafeSearchDetectionGoogle.SafeSearchDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url

### GoogleCognitive.TextDetectionGoogle のセレクター: TextDetectionFromFile, TextDetectionFromGCS

## GoogleCognitive.TextDetectionGoogle.TextDetectionFromFile [A]
```
GoogleCognitive.TextDetectionGoogle.TextDetectionFromFile APIKey: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' Timeout: 30 Response=> JSONResponse StatusCode=> StatusCode
```
入力: APIKey:String ImageFile:FileObject Timeout:Int32
出力: Response:CustomObject=> StatusCode:Int32=>
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=FilePath

## GoogleCognitive.TextDetectionGoogle.TextDetectionFromGCS [A]
```
GoogleCognitive.TextDetectionGoogle.TextDetectionFromGCS Timeout: 30 ImageUrl: $'''example''' APIKey: $'''example''' StatusCode=> StatusCode Response=> JSONResponse
```
入力: !Timeout:Int32 !ImageUrl:String !APIKey:String
出力: StatusCode:Int32=>StatusCode Response:CustomObject=>JSONResponse
ON ERROR可: InvokeCognitiveServiceError, RequestTimeoutExpiredError
固定: ProvideImage=Url
