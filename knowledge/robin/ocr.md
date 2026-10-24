# Robin: OCR

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### OCR.ExtractTextWithOCR のセレクター: ExtractTextFromFile, ExtractTextFromFileRelativeToImage, ExtractTextFromFileRelativeToImageWithCustomTesseract, ExtractTextFromFileRelativeToImageWithTesseract, ExtractTextFromFileRelativeToImageWithWindowsOcr, ExtractTextFromFileWithCustomTesseract, ExtractTextFromFileWithTesseract, ExtractTextFromFileWithWindowsOcr, ExtractTextFromForegroundWindow, ExtractTextFromForegroundWindowRelativeToImage, ExtractTextFromForegroundWindowRelativeToImageWithCustomTesseract, ExtractTextFromForegroundWindowRelativeToImageWithTesseract, ExtractTextFromForegroundWindowRelativeToImageWithWindowsOcr, ExtractTextFromForegroundWindowWithCustomTesseract, ExtractTextFromForegroundWindowWithTesseract, ExtractTextFromForegroundWindowWithWindowsOcr, ExtractTextFromRegionOfFile, ExtractTextFromRegionOfFileWithCustomTesseract, ExtractTextFromRegionOfFileWithTesseract, ExtractTextFromRegionOfFileWithWindowsOcr, ExtractTextFromRegionOfForegroundWindow, ExtractTextFromRegionOfForegroundWindowWithCustomTesseract, ExtractTextFromRegionOfForegroundWindowWithTesseract, ExtractTextFromRegionOfForegroundWindowWithWindowsOcr, ExtractTextFromRegionOfScreen, ExtractTextFromRegionOfScreenWithCustomTesseract, ExtractTextFromRegionOfScreenWithTesseract, ExtractTextFromRegionOfScreenWithWindowsOcr, ExtractTextFromScreen, ExtractTextFromScreenRelativeToImage, ExtractTextFromScreenRelativeToImageWithCustomTesseract, ExtractTextFromScreenRelativeToImageWithTesseract, ExtractTextFromScreenRelativeToImageWithWindowsOcr, ExtractTextFromScreenWithCustomTesseract, ExtractTextFromScreenWithTesseract, ExtractTextFromScreenWithWindowsOcr, WaitAndExtractTextFromForegroundWindowRelativeToImage, WaitAndExtractTextFromForegroundWindowRelativeToImageWithCustomTesseract, WaitAndExtractTextFromForegroundWindowRelativeToImageWithTesseract, WaitAndExtractTextFromForegroundWindowRelativeToImageWithWindowsOcr, WaitAndExtractTextFromScreenRelativeToImage, WaitAndExtractTextFromScreenRelativeToImageWithCustomTesseract, WaitAndExtractTextFromScreenRelativeToImageWithTesseract, WaitAndExtractTextFromScreenRelativeToImageWithWindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromFile [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromFile OCREngine: OCREngine ImageFile: $'''C:\temp\test.xlsx''' OcrText=> OcrText
```
入力: !OCREngine:OCREngineObject !ImageFile:FileObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=Whole, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromFileWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromFileWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' ImageFile: $'''C:\temp\test.xlsx''' OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !LanguageDataPath:FolderObject !LanguageAbbreviation:String !ImageFile:FileObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromFileWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromFileWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English ImageFile: $'''C:\temp\test.xlsx''' OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} !ImageFile:FileObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromFileWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromFileWithWindowsOcr ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageFile: $'''C:\temp\test.xlsx''' OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageFile:FileObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=Whole, OCREngineType=WindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindow [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindow OCREngine: OCREngine OcrText=> OcrText
```
入力: !OCREngine:OCREngineObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=Whole, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !LanguageDataPath:FolderObject !LanguageAbbreviation:String
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian}
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromForegroundWindowWithWindowsOcr ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish}
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=Whole, OCREngineType=WindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFile [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFile Y2: 1 OCREngine: OCREngine Y1: 1 ImageFile: $'''C:\temp\test.xlsx''' X1: 1 X2: 1 OcrText=> OcrText
```
入力: Y2:Nullable<Int32> !OCREngine:OCREngineObject Y1:Nullable<Int32> !ImageFile:FileObject X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=SpecificSubregion, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' Y1: 1 ImageFile: $'''C:\temp\test.xlsx''' X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !LanguageDataPath:FolderObject !LanguageAbbreviation:String Y1:Nullable<Int32> !ImageFile:FileObject X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 Language: OCR.TesseractLanguage.English Y1: 1 ImageFile: $'''C:\temp\test.xlsx''' X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !Language:TesseractLanguage{English,German,Spanish,French,Italian} Y1:Nullable<Int32> !ImageFile:FileObject X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfFileWithWindowsOcr ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English Y1: 1 ImageFile: $'''C:\temp\test.xlsx''' X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} Y1:Nullable<Int32> !ImageFile:FileObject X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=File, SearchMode=SpecificSubregion, OCREngineType=WindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindow [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindow Y2: 1 OCREngine: OCREngine Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: Y2:Nullable<Int32> !OCREngine:OCREngineObject Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=SpecificSubregion, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !LanguageDataPath:FolderObject !LanguageAbbreviation:String Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 Language: OCR.TesseractLanguage.English Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !Language:TesseractLanguage{English,German,Spanish,French,Italian} Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfForegroundWindowWithWindowsOcr ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=ForegroundWindow, SearchMode=SpecificSubregion, OCREngineType=WindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreen [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreen Y2: 1 OCREngine: OCREngine Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: Y2:Nullable<Int32> !OCREngine:OCREngineObject Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=SpecificSubregion, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !LanguageDataPath:FolderObject !LanguageAbbreviation:String Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 Language: OCR.TesseractLanguage.English Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !Language:TesseractLanguage{English,German,Spanish,French,Italian} Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=SpecificSubregion, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromRegionOfScreenWithWindowsOcr ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English Y1: 1 X1: 1 X2: 1 OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} Y1:Nullable<Int32> X1:Nullable<Int32> X2:Nullable<Int32>
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=SpecificSubregion, OCREngineType=WindowsOcr

## OCR.ExtractTextWithOCR.ExtractTextFromScreen [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromScreen OCREngine: OCREngine OcrText=> OcrText
```
入力: !OCREngine:OCREngineObject
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=Whole, OCREngineType=Predefined

## OCR.ExtractTextWithOCR.ExtractTextFromScreenWithCustomTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromScreenWithCustomTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 LanguageDataPath: $'''C:\temp''' LanguageAbbreviation: $'''example''' OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !LanguageDataPath:FolderObject !LanguageAbbreviation:String
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.ExtractTextWithOCR.ExtractTextFromScreenWithTesseract [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromScreenWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English OcrText=> OcrText
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian}
出力: OcrText:String=>OcrText
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=Whole, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.ExtractTextWithOCR.ExtractTextFromScreenWithWindowsOcr [A]
```
OCR.ExtractTextWithOCR.ExtractTextFromScreenWithWindowsOcr WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 ImageHeightMultiplier: 1 OcrText=> OcrText
```
入力: ImageHeightMultiplier:Int32 ImageWidthMultiplier:Int32 WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish}
出力: OcrText:String=>
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, ExtractTextWithOCRError, GetTextFromScreenInNonInteractiveModeError, ImageFileNotFoundError, LandmarkImageNotFoundError, LanguageNotInstalledError, OCREngineNotAliveError
固定: OcrSource=Screen, SearchMode=Whole, OCREngineType=WindowsOcr

### OCR.IfTextOnScreen のセレクター: TextOnScreenDoesNotExist, TextOnScreenDoesNotExistWithCustomTesseract, TextOnScreenDoesNotExistWithTesseract, TextOnScreenDoesNotExistWithWindowsOcr, TextOnScreenExists, TextOnScreenExistsWithCustomTesseract, TextOnScreenExistsWithTesseract, TextOnScreenExistsWithWindowsOcr, TextOnSubregionOfScreenDoesNotExist, TextOnSubregionOfScreenDoesNotExistWithCustomTesseract, TextOnSubregionOfScreenDoesNotExistWithTesseract, TextOnSubregionOfScreenDoesNotExistWithWindowsOcr, TextOnSubregionOfScreenExists, TextOnSubregionOfScreenExistsWithCustomTesseract, TextOnSubregionOfScreenExistsWithTesseract, TextOnSubregionOfScreenExistsWithWindowsOcr, TextOnSubregionRelativeToImageOnScreenDoesNotExist, TextOnSubregionRelativeToImageOnScreenDoesNotExistWithCustomTesseract, TextOnSubregionRelativeToImageOnScreenDoesNotExistWithTesseract, TextOnSubregionRelativeToImageOnScreenDoesNotExistWithWindowsOcr, TextOnSubregionRelativeToImageOnScreenExists, TextOnSubregionRelativeToImageOnScreenExistsWithCustomTesseract, TextOnSubregionRelativeToImageOnScreenExistsWithTesseract, TextOnSubregionRelativeToImageOnScreenExistsWithWindowsOcr

## OCR.IfTextOnScreen.TextOnScreenDoesNotExist [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenDoesNotExist OCREngine: OCREngine TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !OCREngine:OCREngineObject !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=DoesNotExist, OCREngineType=Predefined

## OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithCustomTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithCustomTesseract ImageHeightMultiplier: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=DoesNotExist, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=DoesNotExist, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithWindowsOcr [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenDoesNotExistWithWindowsOcr ImageHeightMultiplier: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=DoesNotExist, OCREngineType=WindowsOcr

## OCR.IfTextOnScreen.TextOnScreenExists [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenExists OCREngine: OCREngine TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !OCREngine:OCREngineObject !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=Exists, OCREngineType=Predefined

## OCR.IfTextOnScreen.TextOnScreenExistsWithCustomTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenExistsWithCustomTesseract ImageHeightMultiplier: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=Exists, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.IfTextOnScreen.TextOnScreenExistsWithTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnScreenExistsWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=Exists, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.IfTextOnScreen.TextOnScreenExistsWithWindowsOcr [C UI]
```
IF (OCR.IfTextOnScreen.TextOnScreenExistsWithWindowsOcr TextToFind: $'''example''' IsRegex: False WindowsOcrLanguage: OCR.WindowsOcrLanguage.English SearchForTextOn: OCR.SearchTarget.EntireScreen ImageWidthMultiplier: 1 ImageHeightMultiplier: 1 TextLocationX=> LocationOfTextFoundX TextLocationY=> LocationOfTextFoundY) THEN
```
入力: !ImageHeightMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, CheckMode=Exists, OCREngineType=WindowsOcr

## OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExist [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExist OCREngine: OCREngine X2: 1 Y1: 1 Y2: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !OCREngine:OCREngineObject X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=DoesNotExist, OCREngineType=Predefined

## OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithCustomTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithCustomTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=DoesNotExist, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=DoesNotExist, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithWindowsOcr [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenDoesNotExistWithWindowsOcr ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=DoesNotExist, OCREngineType=WindowsOcr

## OCR.IfTextOnScreen.TextOnSubregionOfScreenExists [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenExists OCREngine: OCREngine X2: 1 Y1: 1 Y2: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !OCREngine:OCREngineObject X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=Exists, OCREngineType=Predefined

## OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithCustomTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithCustomTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=Exists, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithTesseract [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=Exists, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithWindowsOcr [C]
```
IF (OCR.IfTextOnScreen.TextOnSubregionOfScreenExistsWithWindowsOcr ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX) THEN
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, CheckMode=Exists, OCREngineType=WindowsOcr

### OCR.WaitForTextOnScreen のセレクター: TextOnScreenToAppear, TextOnScreenToAppearWithCustomTesseract, TextOnScreenToAppearWithTesseract, TextOnScreenToAppearWithWindowsOcr, TextOnScreenToDisappear, TextOnScreenToDisappearWithCustomTesseract, TextOnScreenToDisappearWithTesseract, TextOnScreenToDisappearWithWindowsOcr, TextOnSubregionOfScreenToAppear, TextOnSubregionOfScreenToAppearWithCustomTesseract, TextOnSubregionOfScreenToAppearWithTesseract, TextOnSubregionOfScreenToAppearWithWindowsOcr, TextOnSubregionOfScreenToDisappear, TextOnSubregionOfScreenToDisappearWithCustomTesseract, TextOnSubregionOfScreenToDisappearWithTesseract, TextOnSubregionOfScreenToDisappearWithWindowsOcr, TextOnSubregionRelativeToImageOnScreenToAppear, TextOnSubregionRelativeToImageOnScreenToAppearWithCustomTesseract, TextOnSubregionRelativeToImageOnScreenToAppearWithTesseract, TextOnSubregionRelativeToImageOnScreenToAppearWithWindowsOcr, TextOnSubregionRelativeToImageOnScreenToDisappear, TextOnSubregionRelativeToImageOnScreenToDisappearWithCustomTesseract, TextOnSubregionRelativeToImageOnScreenToDisappearWithTesseract, TextOnSubregionRelativeToImageOnScreenToDisappearWithWindowsOcr

## OCR.WaitForTextOnScreen.TextOnScreenToAppear [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToAppear OCREngine: OCREngine TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !OCREngine:OCREngineObject !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Appear, OCREngineType=Predefined

## OCR.WaitForTextOnScreen.TextOnScreenToAppearWithCustomTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToAppearWithCustomTesseract ImageHeightMultiplier: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Appear, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.WaitForTextOnScreen.TextOnScreenToAppearWithTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToAppearWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Appear, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.WaitForTextOnScreen.TextOnScreenToAppearWithWindowsOcr [W UI]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToAppearWithWindowsOcr TextToFind: $'''example''' IsRegex: False WindowsOcrLanguage: OCR.WindowsOcrLanguage.English SearchForTextOn: OCR.SearchTarget.EntireScreen ImageWidthMultiplier: 1 ImageHeightMultiplier: 1 TextLocationX=> LocationOfTextFoundX TextLocationY=> LocationOfTextFoundY)
```
入力: !ImageHeightMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Appear, OCREngineType=WindowsOcr

## OCR.WaitForTextOnScreen.TextOnScreenToDisappear [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToDisappear OCREngine: OCREngine TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !OCREngine:OCREngineObject !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Disappear, OCREngineType=Predefined

## OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithCustomTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithCustomTesseract ImageHeightMultiplier: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Disappear, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithTesseract ImageHeightMultiplier: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Disappear, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithWindowsOcr [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnScreenToDisappearWithWindowsOcr ImageHeightMultiplier: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=Whole, WaitFor=Disappear, OCREngineType=WindowsOcr

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppear [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppear OCREngine: OCREngine X2: 1 Y1: 1 Y2: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !OCREngine:OCREngineObject X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Appear, OCREngineType=Predefined

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithCustomTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithCustomTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Appear, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Appear, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithWindowsOcr [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToAppearWithWindowsOcr ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Appear, OCREngineType=WindowsOcr

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappear [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappear OCREngine: OCREngine X2: 1 Y1: 1 Y2: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !OCREngine:OCREngineObject X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Disappear, OCREngineType=Predefined

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithCustomTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithCustomTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 LanguageDataPath: $'''C:\temp''' ImageWidthMultiplier: 1 LanguageAbbreviation: $'''example''' X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !LanguageDataPath:FolderObject !ImageWidthMultiplier:Int32 !LanguageAbbreviation:String X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Disappear, OCREngineType=Tesseract, UseOtherLanguage=True

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithTesseract [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithTesseract ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 ImageWidthMultiplier: 1 Language: OCR.TesseractLanguage.English X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !ImageWidthMultiplier:Int32 !Language:TesseractLanguage{English,German,Spanish,French,Italian} X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Disappear, OCREngineType=Tesseract, UseOtherLanguage=False

## OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithWindowsOcr [W]
```
WAIT (OCR.WaitForTextOnScreen.TextOnSubregionOfScreenToDisappearWithWindowsOcr ImageHeightMultiplier: 1 X2: 1 Y1: 1 Y2: 1 WindowsOcrLanguage: OCR.WindowsOcrLanguage.English ImageWidthMultiplier: 1 X1: 1 TextToFind: $'''example''' IsRegex: False SearchForTextOn: OCR.SearchTarget.EntireScreen TextLocationY=> LocationOfTextFoundY TextLocationX=> LocationOfTextFoundX)
```
入力: !ImageHeightMultiplier:Int32 X2:Nullable<Int32> Y1:Nullable<Int32> Y2:Nullable<Int32> !WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish} !ImageWidthMultiplier:Int32 X1:Nullable<Int32> !TextToFind:String !IsRegex:Boolean !SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow}
出力: TextLocationY:Int32=>LocationOfTextFoundY TextLocationX:Int32=>LocationOfTextFoundX
ON ERROR可: CannotCheckIfTextExistsInNonInteractiveModeError, CreateOCREngineError, DataPathFolderNotFoundError, FailedToAnalyzeTextWithOCRError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, OCREngineNotAliveError
固定: SearchMode=SpecificSubregion, WaitFor=Disappear, OCREngineType=WindowsOcr
