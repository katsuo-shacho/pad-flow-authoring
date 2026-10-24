# Robin: WebAutomation

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### WebAutomation.Click のセレクター: Click, ClickCloseDialog, ClickNoWait, ClickPressDialogButton

## WebAutomation.Click.Click [A UI]
```
WebAutomation.Click.Click OffsetY: 0 WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OffsetX: 0 ClickType: WebAutomation.ClickType.LeftClick MousePositionRelativeToElement: WebAutomation.RectangleEdgePoint.MiddleCenter MouseClick: True
```
入力: !OffsetY:Int32 !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OffsetX:Int32 !ClickType:ClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MousePositionRelativeToElement:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !MouseClick:Boolean
ON ERROR可: ClickElementError, ElementNotFoundError
固定: WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.Click.ClickCloseDialog [A UI]
```
WebAutomation.Click.ClickCloseDialog OffsetY: 0 WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OffsetX: 0 ClickType: WebAutomation.ClickType.LeftClick MousePositionRelativeToElement: WebAutomation.RectangleEdgePoint.MiddleCenter MouseClick: True
```
入力: !OffsetY:Int32 !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OffsetX:Int32 !ClickType:ClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MousePositionRelativeToElement:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !MouseClick:Boolean
ON ERROR可: ClickElementError, ElementNotFoundError
固定: WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.Click.ClickNoWait [A UI]
```
WebAutomation.Click.ClickNoWait OffsetY: 0 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OffsetX: 0 ClickType: WebAutomation.ClickType.LeftClick MousePositionRelativeToElement: WebAutomation.RectangleEdgePoint.MiddleCenter MouseClick: True
```
入力: !OffsetY:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OffsetX:Int32 !ClickType:ClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MousePositionRelativeToElement:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !MouseClick:Boolean
ON ERROR可: ClickElementError, ElementNotFoundError
固定: WaitForPageToLoad=False

## WebAutomation.Click.ClickPressDialogButton [A UI]
```
WebAutomation.Click.ClickPressDialogButton OffsetY: 0 WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OffsetX: 0 DialogButton: $'''example''' ClickType: WebAutomation.ClickType.LeftClick MousePositionRelativeToElement: WebAutomation.RectangleEdgePoint.MiddleCenter MouseClick: True
```
入力: !OffsetY:Int32 !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OffsetX:Int32 !DialogButton:String !ClickType:ClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MousePositionRelativeToElement:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !MouseClick:Boolean
ON ERROR可: ClickElementError, ElementNotFoundError
固定: WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.ClickDownloadLink [A UI]
```
WebAutomation.ClickDownloadLink BrowserInstance: Browser Control: $'''body''' DestinationFolder: $'''C:\temp''' DownloadedFile=> DownloadedFile
```
入力: DestinationFolder:FolderObject BrowserInstance:WebBrowserInstanceHandle Control:WebControl
出力: DownloadedFile:FileObject=>
ON ERROR可: ClickElementError, DownloadFileError, ElementNotFoundError, SaveFileError

## WebAutomation.CloseWebBrowser [A]
```
WebAutomation.CloseWebBrowser BrowserInstance: Browser
```
入力: BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: CloseWebBrowserError

### WebAutomation.CreateNewTab のセレクター: CreateNewTab, CreateNewTabCloseDialog, CreateNewTabNoWait, CreateNewTabPressDialogButton

## WebAutomation.CreateNewTab.CreateNewTab [A]
```
WebAutomation.CreateNewTab.CreateNewTab Url: $'''example''' WaitForPageToLoadTimeout: 60 BrowserInstance: Browser NewBrowserInstance=> NewBrowser
```
入力: !Url:String !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
出力: NewBrowserInstance:WebBrowserInstanceHandle=>NewBrowser
ON ERROR可: CreateNewTabError, InvalidUrlError
固定: WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.CreateNewTab.CreateNewTabCloseDialog [A]
```
WebAutomation.CreateNewTab.CreateNewTabCloseDialog Url: $'''example''' WaitForPageToLoadTimeout: 60 BrowserInstance: Browser NewBrowserInstance=> NewBrowser
```
入力: !Url:String !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
出力: NewBrowserInstance:WebBrowserInstanceHandle=>NewBrowser
ON ERROR可: CreateNewTabError, InvalidUrlError
固定: WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.CreateNewTab.CreateNewTabNoWait [A]
```
WebAutomation.CreateNewTab.CreateNewTabNoWait Url: $'''example''' BrowserInstance: Browser NewBrowserInstance=> NewBrowser
```
入力: !Url:String !BrowserInstance:WebBrowserInstanceHandle
出力: NewBrowserInstance:WebBrowserInstanceHandle=>NewBrowser
ON ERROR可: CreateNewTabError, InvalidUrlError
固定: WaitForPageToLoad=False

## WebAutomation.CreateNewTab.CreateNewTabPressDialogButton [A]
```
WebAutomation.CreateNewTab.CreateNewTabPressDialogButton Url: $'''example''' WaitForPageToLoadTimeout: 60 BrowserInstance: Browser DialogButton: $'''example''' NewBrowserInstance=> NewBrowser
```
入力: !Url:String !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
出力: NewBrowserInstance:WebBrowserInstanceHandle=>NewBrowser
ON ERROR可: CreateNewTabError, InvalidUrlError
固定: WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.ExecuteJavascript [A]
```
WebAutomation.ExecuteJavascript BrowserInstance: Browser Javascript: $'''function ExecuteScript() { /*your code here, return something (optionally); */ }''' Result=> Result
```
入力: BrowserInstance:WebBrowserInstanceHandle Javascript:String
出力: Result:String=>
ON ERROR可: JavaScriptExecutionError

### WebAutomation.ExtractData のセレクター: ExtractData, ExtractDataInExcel, ExtractDataUsingPagingFromAllPages, ExtractDataUsingPagingFromAllPagesInExcel, ExtractDataUsingPagingFromNumberOfPages, ExtractDataUsingPagingFromNumberOfPagesInExcel, ExtractHandPickedValues, ExtractHandPickedValuesInExcel, ExtractHandPickedValuesUsingPagingFromAllPages, ExtractHandPickedValuesUsingPagingFromAllPagesInExcel, ExtractHandPickedValuesUsingPagingFromNumberOfPages, ExtractHandPickedValuesUsingPagingFromNumberOfPagesInExcel, ExtractHtmlTable, ExtractHtmlTableInExcel, ExtractHtmlTableUsingPagingFromAllPages, ExtractHtmlTableUsingPagingFromAllPagesInExcel, ExtractHtmlTableUsingPagingFromNumberOfPages, ExtractHtmlTableUsingPagingFromNumberOfPagesInExcel, ExtractList, ExtractListInExcel, ExtractListUsingPagingFromAllPages, ExtractListUsingPagingFromAllPagesInExcel, ExtractListUsingPagingFromNumberOfPages, ExtractListUsingPagingFromNumberOfPagesInExcel, ExtractSingleValue, ExtractSingleValueInExcel, ExtractSingleValueUsingPagingFromAllPages, ExtractSingleValueUsingPagingFromAllPagesInExcel, ExtractSingleValueUsingPagingFromNumberOfPages, ExtractSingleValueUsingPagingFromNumberOfPagesInExcel, ExtractTable, ExtractTableInExcel, ExtractTableUsingPagingFromAllPages, ExtractTableUsingPagingFromAllPagesInExcel, ExtractTableUsingPagingFromNumberOfPages, ExtractTableUsingPagingFromNumberOfPagesInExcel

## WebAutomation.ExtractData.ExtractData [A]
```
WebAutomation.ExtractData.ExtractData TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=Variable, UsePaging=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractDataInExcel [A]
```
WebAutomation.ExtractData.ExtractDataInExcel TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=ExcelSpreadsheet, UsePaging=False

## WebAutomation.ExtractData.ExtractDataUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractDataUsingPagingFromAllPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractDataUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractDataUsingPagingFromAllPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractDataUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractDataUsingPagingFromNumberOfPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractDataUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractDataUsingPagingFromNumberOfPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Undefined, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValues [A]
```
WebAutomation.ExtractData.ExtractHandPickedValues TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=Variable, UsePaging=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValuesInExcel [A]
```
WebAutomation.ExtractData.ExtractHandPickedValuesInExcel TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=ExcelSpreadsheet, UsePaging=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromAllPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromAllPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromNumberOfPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractHandPickedValuesUsingPagingFromNumberOfPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=HandpickedValues, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractHtmlTable [A]
```
WebAutomation.ExtractData.ExtractHtmlTable PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=Variable, UsePaging=False

## WebAutomation.ExtractData.ExtractHtmlTableInExcel [A]
```
WebAutomation.ExtractData.ExtractHtmlTableInExcel PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=ExcelSpreadsheet, UsePaging=False

## WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromAllPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromAllPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromNumberOfPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False

## WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractHtmlTableUsingPagingFromNumberOfPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=EntireHtmlTable, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False

## WebAutomation.ExtractData.ExtractList [A]
```
WebAutomation.ExtractData.ExtractList PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=Variable, UsePaging=False

## WebAutomation.ExtractData.ExtractListInExcel [A]
```
WebAutomation.ExtractData.ExtractListInExcel PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=ExcelSpreadsheet, UsePaging=False

## WebAutomation.ExtractData.ExtractListUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractListUsingPagingFromAllPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractListUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractListUsingPagingFromAllPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractListUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractListUsingPagingFromNumberOfPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False

## WebAutomation.ExtractData.ExtractListUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractListUsingPagingFromNumberOfPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=List, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False

## WebAutomation.ExtractData.ExtractSingleValue [A]
```
WebAutomation.ExtractData.ExtractSingleValue TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=Variable, UsePaging=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractSingleValueInExcel [A]
```
WebAutomation.ExtractData.ExtractSingleValueInExcel TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=ExcelSpreadsheet, UsePaging=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromAllPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromAllPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True, PostProcessData=False

## WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromNumberOfPages PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractSingleValueUsingPagingFromNumberOfPagesInExcel PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=SingleValue, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False, PostProcessData=False

## WebAutomation.ExtractData.ExtractTable [A]
```
WebAutomation.ExtractData.ExtractTable PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=Variable, UsePaging=False

## WebAutomation.ExtractData.ExtractTableInExcel [A]
```
WebAutomation.ExtractData.ExtractTableInExcel PostProcessData: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=ExcelSpreadsheet, UsePaging=False

## WebAutomation.ExtractData.ExtractTableUsingPagingFromAllPages [A]
```
WebAutomation.ExtractData.ExtractTableUsingPagingFromAllPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractTableUsingPagingFromAllPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractTableUsingPagingFromAllPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=True

## WebAutomation.ExtractData.ExtractTableUsingPagingFromNumberOfPages [A]
```
WebAutomation.ExtractData.ExtractTableUsingPagingFromNumberOfPages PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExtractedData=> DataFromWebPage
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExtractedData:DataTable=>DataFromWebPage
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=Variable, UsePaging=True, GetAllWebPages=False

## WebAutomation.ExtractData.ExtractTableUsingPagingFromNumberOfPagesInExcel [A]
```
WebAutomation.ExtractData.ExtractTableUsingPagingFromNumberOfPagesInExcel PostProcessData: False PagerCssSelector: $'''example''' UsePhysicalClick: False TimeoutInSeconds: 60 Control: $'''example''' BrowserInstance: Browser MaxWebPagesToProcess: 1 ExtractionParameters: RecognizedEntities ExcelInstance=> ExcelInstance
```
入力: !PostProcessData:Boolean !PagerCssSelector:String !UsePhysicalClick:Boolean !TimeoutInSeconds:Int32 !Control:String !BrowserInstance:WebBrowserInstanceHandle !MaxWebPagesToProcess:Int32 !ExtractionParameters:DataTable
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataError, LaunchExcelError, WriteToExcelError
固定: ExtractionMode=Table, StoreDataMode=ExcelSpreadsheet, UsePaging=True, GetAllWebPages=False

### WebAutomation.Focus のセレクター: Focus, FocusCloseDialog, FocusNoWait, FocusPressDialogButton

## WebAutomation.Focus.Focus [A UI]
```
WebAutomation.Focus.Focus WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, FocusTextFieldError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True

## WebAutomation.Focus.FocusCloseDialog [A UI]
```
WebAutomation.Focus.FocusCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, FocusTextFieldError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True

## WebAutomation.Focus.FocusNoWait [A UI]
```
WebAutomation.Focus.FocusNoWait BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, FocusTextFieldError
固定: WaitForPageToLoad=False

## WebAutomation.Focus.FocusPressDialogButton [A UI]
```
WebAutomation.Focus.FocusPressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !DialogButton:String
ON ERROR可: ElementNotFoundError, FocusTextFieldError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True

## WebAutomation.GetDetailsOfElement [A UI]
```
WebAutomation.GetDetailsOfElement BrowserInstance: Browser Control: $'''body''' AttributeName: $'''Own Text''' AttributeValue=> AttributeValue
```
入力: AttributeName:String BrowserInstance:WebBrowserInstanceHandle Control:WebControl
出力: AttributeValue:String=>
ON ERROR可: RetrieveAttributeError

## WebAutomation.GetDetailsOfWebPage [A]
```
WebAutomation.GetDetailsOfWebPage BrowserInstance: Browser DetailsType: WebAutomation.DetailsType.Description Details=> WebPageProperty
```
入力: BrowserInstance:WebBrowserInstanceHandle DetailsType:DetailsType{Description,MetaKeywords,Title,Text,Source,URLAddress}
出力: Details:String=>
ON ERROR可: ElementNotFoundError, GetDetailsOfWebPageError

## WebAutomation.GetWebControl [A UI]
```
WebAutomation.GetWebControl Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] WebControl=> WebControl
```
入力: !Control:WebControl
出力: WebControl:WebControl=>WebControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### WebAutomation.GoToWebPage のセレクター: GoToWebPage, GoToWebPageCloseDialog, GoToWebPageNoWait, GoToWebPagePressDialogButton, NavigateBack, NavigateBackCloseDialog, NavigateBackNoWait, NavigateBackPressDialogButton, NavigateForward, NavigateForwardCloseDialog, NavigateForwardNoWait, NavigateForwardPressDialogButton, ReloadWebPage, ReloadWebPageCloseDialog, ReloadWebPageNoWait, ReloadWebPagePressDialogButton

## WebAutomation.GoToWebPage.GoToWebPage [A]
```
WebAutomation.GoToWebPage.GoToWebPage BrowserInstance: Browser Url: $'''example''' WaitForPageToLoadTimeout: 60
```
入力: BrowserInstance:WebBrowserInstanceHandle Url:String WaitForPageToLoadTimeout:Int32
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateToUrl, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.GoToWebPage.GoToWebPageCloseDialog [A]
```
WebAutomation.GoToWebPage.GoToWebPageCloseDialog Url: $'''example''' WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !Url:String !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateToUrl, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.GoToWebPage.GoToWebPageNoWait [A]
```
WebAutomation.GoToWebPage.GoToWebPageNoWait Url: $'''example''' BrowserInstance: Browser
```
入力: !Url:String !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateToUrl, WaitForPageToLoad=False

## WebAutomation.GoToWebPage.GoToWebPagePressDialogButton [A]
```
WebAutomation.GoToWebPage.GoToWebPagePressDialogButton Url: $'''example''' WaitForPageToLoadTimeout: 60 BrowserInstance: Browser DialogButton: $'''example'''
```
入力: !Url:String !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateToUrl, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.GoToWebPage.NavigateBack [A]
```
WebAutomation.GoToWebPage.NavigateBack WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateBack, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.GoToWebPage.NavigateBackCloseDialog [A]
```
WebAutomation.GoToWebPage.NavigateBackCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateBack, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.GoToWebPage.NavigateBackNoWait [A]
```
WebAutomation.GoToWebPage.NavigateBackNoWait BrowserInstance: Browser
```
入力: !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateBack, WaitForPageToLoad=False

## WebAutomation.GoToWebPage.NavigateBackPressDialogButton [A]
```
WebAutomation.GoToWebPage.NavigateBackPressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateBack, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.GoToWebPage.NavigateForward [A]
```
WebAutomation.GoToWebPage.NavigateForward WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateForward, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.GoToWebPage.NavigateForwardCloseDialog [A]
```
WebAutomation.GoToWebPage.NavigateForwardCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateForward, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.GoToWebPage.NavigateForwardNoWait [A]
```
WebAutomation.GoToWebPage.NavigateForwardNoWait BrowserInstance: Browser
```
入力: !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateForward, WaitForPageToLoad=False

## WebAutomation.GoToWebPage.NavigateForwardPressDialogButton [A]
```
WebAutomation.GoToWebPage.NavigateForwardPressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=NavigateForward, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.GoToWebPage.ReloadWebPage [A]
```
WebAutomation.GoToWebPage.ReloadWebPage WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=ReloadWebPage, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.GoToWebPage.ReloadWebPageCloseDialog [A]
```
WebAutomation.GoToWebPage.ReloadWebPageCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=ReloadWebPage, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.GoToWebPage.ReloadWebPageNoWait [A]
```
WebAutomation.GoToWebPage.ReloadWebPageNoWait BrowserInstance: Browser
```
入力: !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=ReloadWebPage, WaitForPageToLoad=False

## WebAutomation.GoToWebPage.ReloadWebPagePressDialogButton [A]
```
WebAutomation.GoToWebPage.ReloadWebPagePressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
ON ERROR可: InvalidUrlError, NavigateToWebPageError
固定: NavigationType=ReloadWebPage, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.HoverOverElement [A UI]
```
WebAutomation.HoverOverElement BrowserInstance: Browser Control: $'''body''' UseActualMouse: False
```
入力: UseActualMouse:Boolean BrowserInstance:WebBrowserInstanceHandle Control:WebControl
ON ERROR可: HoverOverElementError

### WebAutomation.IfWebPageContains のセレクター: WebPageContainsElement, WebPageContainsElementInState, WebPageContainsText, WebPageDoesNotContainElement, WebPageDoesNotContainText

## WebAutomation.IfWebPageContains.WebPageContainsElement [C UI]
```
IF (WebAutomation.IfWebPageContains.WebPageContainsElement BrowserInstance: Browser Control: $'''body''') THEN
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: BrowserContinuousErrors
固定: CheckElementState=False, ContainsMode=ContainsElement

## WebAutomation.IfWebPageContains.WebPageContainsElementInState [C UI]
```
IF (WebAutomation.IfWebPageContains.WebPageContainsElementInState State: WebAutomation.ElementState.Enabled BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']) THEN
```
入力: !State:ElementState{Enabled,Disabled} !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: BrowserContinuousErrors
固定: CheckElementState=True, ContainsMode=ContainsElement

## WebAutomation.IfWebPageContains.WebPageContainsText [C]
```
IF (WebAutomation.IfWebPageContains.WebPageContainsText BrowserInstance: Browser Text: $'''example''') THEN
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Text:String
ON ERROR可: BrowserContinuousErrors
固定: ContainsMode=ContainsText

## WebAutomation.IfWebPageContains.WebPageDoesNotContainElement [C UI]
```
IF (WebAutomation.IfWebPageContains.WebPageDoesNotContainElement BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']) THEN
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: BrowserContinuousErrors
固定: ContainsMode=DoesNotContainElement

## WebAutomation.IfWebPageContains.WebPageDoesNotContainText [C]
```
IF (WebAutomation.IfWebPageContains.WebPageDoesNotContainText BrowserInstance: Browser Text: $'''example''') THEN
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Text:String
ON ERROR可: BrowserContinuousErrors
固定: ContainsMode=DoesNotContainText

### WebAutomation.LaunchChrome のセレクター: AttachToChromeByTitle, AttachToChromeByUrl, AttachToForegroundChrome, LaunchChrome, LaunchChromeCloseDialog, LaunchChromeCloseDialogCustomProfile, LaunchChromeCustomProfile, LaunchChromeNoWait, LaunchChromeNoWaitCustomProfile, LaunchChromePressDialogButton, LaunchChromePressDialogButtonCustomProfile, LaunchChromeWithDriver, LaunchChromeWithDriverCloseDialog, LaunchChromeWithDriverCloseDialogCustomProfile, LaunchChromeWithDriverCustomProfile, LaunchChromeWithDriverNoWait, LaunchChromeWithDriverNoWaitCustomProfile, LaunchChromeWithDriverPressDialogButton, LaunchChromeWithDriverPressDialogButtonCustomProfile

## WebAutomation.LaunchChrome.AttachToChromeByTitle [A]
```
WebAutomation.LaunchChrome.AttachToChromeByTitle TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed TabTitle: $'''example''' BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex} !TabTitle:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=Attach, AttachMode=ByTitle

## WebAutomation.LaunchChrome.AttachToChromeByUrl [A]
```
WebAutomation.LaunchChrome.AttachToChromeByUrl TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension TabUrl: $'''example''' AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !TabUrl:String !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex}
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=Attach, AttachMode=ByUrl

## WebAutomation.LaunchChrome.AttachToForegroundChrome [A]
```
WebAutomation.LaunchChrome.AttachToForegroundChrome TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=Attach, AttachMode=ForegroundWindow

## WebAutomation.LaunchChrome.LaunchChrome [A]
```
WebAutomation.LaunchChrome.LaunchChrome Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False WaitForPageToLoadTimeout: 60 Timeout: 60 BrowserInstance=> Browser
```
入力: ClearCache:Boolean ClearCookies:Boolean Timeout:Int32 Url:String WaitForPageToLoadTimeout:Int32 WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile}
出力: BrowserInstance:WebBrowserInstanceHandle=>
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeCloseDialog [A]
```
WebAutomation.LaunchChrome.LaunchChromeCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeCloseDialogCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeNoWait [A]
```
WebAutomation.LaunchChrome.LaunchChromeNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeNoWaitCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromePressDialogButton [A]
```
WebAutomation.LaunchChrome.LaunchChromePressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromePressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromePressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchChrome.LaunchChromeWithDriver [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriver WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverCloseDialog [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverCloseDialogCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverNoWait [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverNoWaitCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverPressDialogButton [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverPressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=WebDriver

## WebAutomation.LaunchChrome.LaunchChromeWithDriverPressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchChrome.LaunchChromeWithDriverPressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchChromeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

### WebAutomation.LaunchEdge のセレクター: AttachToEdgeByTitle, AttachToEdgeByUrl, AttachToTheForegroundEdge, LaunchEdge, LaunchEdgeCloseDialog, LaunchEdgeCloseDialogCustomProfile, LaunchEdgeCustomProfile, LaunchEdgeNoWait, LaunchEdgeNoWaitCustomProfile, LaunchEdgePressDialogButton, LaunchEdgePressDialogButtonCustomProfile, LaunchEdgeWithDriver, LaunchEdgeWithDriverCloseDialog, LaunchEdgeWithDriverCloseDialogCustomProfile, LaunchEdgeWithDriverCustomProfile, LaunchEdgeWithDriverNoWait, LaunchEdgeWithDriverNoWaitCustomProfile, LaunchEdgeWithDriverPressDialogButton, LaunchEdgeWithDriverPressDialogButtonCustomProfile

## WebAutomation.LaunchEdge.AttachToEdgeByTitle [A]
```
WebAutomation.LaunchEdge.AttachToEdgeByTitle TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed TabTitle: $'''example''' BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex} !TabTitle:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=Attach, AttachMode=ByTitle

## WebAutomation.LaunchEdge.AttachToEdgeByUrl [A]
```
WebAutomation.LaunchEdge.AttachToEdgeByUrl TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension TabUrl: $'''example''' AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !TabUrl:String !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex}
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=Attach, AttachMode=ByUrl

## WebAutomation.LaunchEdge.AttachToTheForegroundEdge [A]
```
WebAutomation.LaunchEdge.AttachToTheForegroundEdge TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=Attach, AttachMode=ForegroundWindow

## WebAutomation.LaunchEdge.LaunchEdge [A]
```
WebAutomation.LaunchEdge.LaunchEdge Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False WaitForPageToLoadTimeout: 60 Timeout: 60 BrowserInstance=> Browser
```
入力: ClearCache:Boolean ClearCookies:Boolean Timeout:Int32 Url:String WaitForPageToLoadTimeout:Int32 WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile}
出力: BrowserInstance:WebBrowserInstanceHandle=>
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeCloseDialog [A]
```
WebAutomation.LaunchEdge.LaunchEdgeCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeCloseDialogCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeNoWait [A]
```
WebAutomation.LaunchEdge.LaunchEdgeNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeNoWaitCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgePressDialogButton [A]
```
WebAutomation.LaunchEdge.LaunchEdgePressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgePressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgePressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchEdge.LaunchEdgeWithDriver [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriver WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverCloseDialog [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverCloseDialogCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverNoWait [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverNoWaitCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverPressDialogButton [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverPressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=WebDriver

## WebAutomation.LaunchEdge.LaunchEdgeWithDriverPressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchEdge.LaunchEdgeWithDriverPressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchEdgeError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

### WebAutomation.LaunchFirefox のセレクター: AttachToFirefoxByTitle, AttachToFirefoxByUrl, AttachToForegroundFirefox, LaunchFirefox, LaunchFirefoxCloseDialog, LaunchFirefoxCloseDialogCustomProfile, LaunchFirefoxCustomProfile, LaunchFirefoxNoWait, LaunchFirefoxNoWaitCustomProfile, LaunchFirefoxPressDialogButton, LaunchFirefoxPressDialogButtonCustomProfile, LaunchFirefoxWithDriver, LaunchFirefoxWithDriverCloseDialog, LaunchFirefoxWithDriverCloseDialogCustomProfile, LaunchFirefoxWithDriverCustomProfile, LaunchFirefoxWithDriverNoWait, LaunchFirefoxWithDriverNoWaitCustomProfile, LaunchFirefoxWithDriverPressDialogButton, LaunchFirefoxWithDriverPressDialogButtonCustomProfile

## WebAutomation.LaunchFirefox.AttachToFirefoxByTitle [A]
```
WebAutomation.LaunchFirefox.AttachToFirefoxByTitle TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed TabTitle: $'''example''' BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex} !TabTitle:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=Attach, AttachMode=ByTitle

## WebAutomation.LaunchFirefox.AttachToFirefoxByUrl [A]
```
WebAutomation.LaunchFirefox.AttachToFirefoxByUrl TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension TabUrl: $'''example''' AttachTimeout: 5 MatchMode: WebAutomation.MatchMode.Mixed BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !TabUrl:String !AttachTimeout:Int32 !MatchMode:MatchMode{Mixed,Exact,Partial,Regex}
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=Attach, AttachMode=ByUrl

## WebAutomation.LaunchFirefox.AttachToForegroundFirefox [A]
```
WebAutomation.LaunchFirefox.AttachToForegroundFirefox TargetDesktop: $'''example''' CommunicationMode: WebAutomation.BrowserCommunicationMethod.Extension AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TargetDesktop:String !CommunicationMode:BrowserCommunicationMethod{Extension,WebDriver} !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=Attach, AttachMode=ForegroundWindow

## WebAutomation.LaunchFirefox.LaunchFirefox [A]
```
WebAutomation.LaunchFirefox.LaunchFirefox Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False WaitForPageToLoadTimeout: 60 Timeout: 60 BrowserInstance=> Browser
```
入力: ClearCache:Boolean ClearCookies:Boolean Timeout:Int32 Url:String WaitForPageToLoadTimeout:Int32 WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile}
出力: BrowserInstance:WebBrowserInstanceHandle=>
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxCloseDialog [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxCloseDialogCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxNoWait [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxNoWaitCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxPressDialogButton [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxPressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxPressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxPressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=Extension

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriver [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriver WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCloseDialog [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCloseDialog WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCloseDialogCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCloseDialogCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=CloseIt, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=DoNothing, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverNoWait [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverNoWait Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverNoWaitCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverNoWaitCustomProfile Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False BrowserInstance=> Browser
```
入力: !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=False, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverPressDialogButton [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverPressDialogButton WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal TargetDesktop: $'''example''' PiPUserDataFolderMode: WebAutomation.PiPUserDataFolderModeEnum.AutomaticProfile ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !TargetDesktop:String !PiPUserDataFolderMode:PiPUserDataFolderModeEnum{AutomaticProfile,DefaultProfile,CustomProfile} !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, CommunicationMode=WebDriver

## WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverPressDialogButtonCustomProfile [A]
```
WebAutomation.LaunchFirefox.LaunchFirefoxWithDriverPressDialogButtonCustomProfile WaitForPageToLoadTimeout: 60 Timeout: 60 Url: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal PiPUserDataFolderPath: $'''C:\temp''' TargetDesktop: $'''example''' ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Timeout:Int32 !Url:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !PiPUserDataFolderPath:FolderObject !TargetDesktop:String !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchFirefoxError
固定: LaunchMode=LaunchNew, WaitForPageToLoad=True, HandleDialogAction=PressButton, PiPUserDataFolderMode=CustomProfile, CommunicationMode=WebDriver

### WebAutomation.LaunchInternetExplorer のセレクター: AttachToForegroundInternetExplorer, AttachToInternetExplorerByTitle, AttachToInternetExplorerByUrl, LaunchAutomationBrowser, LaunchAutomationBrowserCloseDialog, LaunchAutomationBrowserNoWait, LaunchAutomationBrowserPressDialogButton, LaunchInternetExplorer, LaunchInternetExplorerCloseDialog, LaunchInternetExplorerNoWait, LaunchInternetExplorerPressDialogButton

## WebAutomation.LaunchInternetExplorer.AttachToForegroundInternetExplorer [A]
```
WebAutomation.LaunchInternetExplorer.AttachToForegroundInternetExplorer TargetDesktop: $'''example''' AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TargetDesktop:String !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=AttachToRunningInternetExplorer, AttachMode=ForegroundWindow

## WebAutomation.LaunchInternetExplorer.AttachToInternetExplorerByTitle [A]
```
WebAutomation.LaunchInternetExplorer.AttachToInternetExplorerByTitle TabTitle: $'''example''' TargetDesktop: $'''example''' AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TabTitle:String !TargetDesktop:String !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=AttachToRunningInternetExplorer, AttachMode=ByTitle

## WebAutomation.LaunchInternetExplorer.AttachToInternetExplorerByUrl [A]
```
WebAutomation.LaunchInternetExplorer.AttachToInternetExplorerByUrl TabUrl: $'''example''' TargetDesktop: $'''example''' AttachTimeout: 5 BrowserInstance=> Browser
```
入力: !TabUrl:String !TargetDesktop:String !AttachTimeout:Int32
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=AttachToRunningInternetExplorer, AttachMode=ByUrl

## WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowser [A]
```
WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowser Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False CustomUserAgentString: $'''example''' BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean !CustomUserAgentString:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewAutomationBrowser, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserCloseDialog [A]
```
WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserCloseDialog Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False CustomUserAgentString: $'''example''' BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean !CustomUserAgentString:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewAutomationBrowser, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserNoWait [A]
```
WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserNoWait Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False CustomUserAgentString: $'''example''' BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !ClearCache:Boolean !ClearCookies:Boolean !CustomUserAgentString:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewAutomationBrowser, WaitForPageToLoad=False

## WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserPressDialogButton [A]
```
WebAutomation.LaunchInternetExplorer.LaunchAutomationBrowserPressDialogButton Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False DialogButton: $'''example''' CustomUserAgentString: $'''example''' BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String !CustomUserAgentString:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewAutomationBrowser, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.LaunchInternetExplorer.LaunchInternetExplorer [A]
```
WebAutomation.LaunchInternetExplorer.LaunchInternetExplorer Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewInternetExplorer, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerCloseDialog [A]
```
WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerCloseDialog Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewInternetExplorer, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerNoWait [A]
```
WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerNoWait Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !ClearCache:Boolean !ClearCookies:Boolean
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewInternetExplorer, WaitForPageToLoad=False

## WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerPressDialogButton [A]
```
WebAutomation.LaunchInternetExplorer.LaunchInternetExplorerPressDialogButton Url: $'''example''' TargetDesktop: $'''example''' WindowState: WebAutomation.BrowserWindowState.Normal WaitForPageToLoadTimeout: 60 ClearCache: False ClearCookies: False DialogButton: $'''example''' BrowserInstance=> Browser
```
入力: !Url:String !TargetDesktop:String !WindowState:BrowserWindowState{Normal,Maximized,Minimized} !WaitForPageToLoadTimeout:Int32 !ClearCache:Boolean !ClearCookies:Boolean !DialogButton:String
出力: BrowserInstance:WebBrowserInstanceHandle=>Browser
ON ERROR可: InvalidUrlError, LaunchInternetExplorerError
固定: LaunchMode=LaunchNewInternetExplorer, WaitForPageToLoad=True, HandleDialogAction=PressButton

### WebAutomation.PopulateTextField のセレクター: PopulateTextField, PopulateTextFieldCloseDialog, PopulateTextFieldCloseDialogUsePhysicalKeyboard, PopulateTextFieldNoWait, PopulateTextFieldNoWaitUsePhysicalKeyboard, PopulateTextFieldPressDialogButton, PopulateTextFieldPressDialogButtonUsePhysicalKeyboard, PopulateTextFieldUsePhysicalKeyboard

## WebAutomation.PopulateTextField.PopulateTextField [A UI]
```
WebAutomation.PopulateTextField.PopulateTextField WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True EmulateTyping: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !EmulateTyping:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True, UsePhysicalKeyboard=False

## WebAutomation.PopulateTextField.PopulateTextFieldCloseDialog [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldCloseDialog WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True EmulateTyping: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !EmulateTyping:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True, UsePhysicalKeyboard=False

## WebAutomation.PopulateTextField.PopulateTextFieldCloseDialogUsePhysicalKeyboard [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldCloseDialogUsePhysicalKeyboard WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True, UsePhysicalKeyboard=True

## WebAutomation.PopulateTextField.PopulateTextFieldNoWait [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldNoWait Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True EmulateTyping: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !EmulateTyping:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: WaitForPageToLoad=False, UsePhysicalKeyboard=False

## WebAutomation.PopulateTextField.PopulateTextFieldNoWaitUsePhysicalKeyboard [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldNoWaitUsePhysicalKeyboard Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: WaitForPageToLoad=False, UsePhysicalKeyboard=True

## WebAutomation.PopulateTextField.PopulateTextFieldPressDialogButton [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldPressDialogButton WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True EmulateTyping: True DialogButton: $'''example''' Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !EmulateTyping:Boolean !DialogButton:String !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True, UsePhysicalKeyboard=False

## WebAutomation.PopulateTextField.PopulateTextFieldPressDialogButtonUsePhysicalKeyboard [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldPressDialogButtonUsePhysicalKeyboard WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True DialogButton: $'''example''' Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !DialogButton:String !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True, UsePhysicalKeyboard=True

## WebAutomation.PopulateTextField.PopulateTextFieldUsePhysicalKeyboard [A UI]
```
WebAutomation.PopulateTextField.PopulateTextFieldUsePhysicalKeyboard WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser UnfocusAfterPopulate: True Text: $'''password''' Mode: WebAutomation.PopulateTextMode.Replace
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !UnfocusAfterPopulate:Boolean !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append}
ON ERROR可: ElementNotFoundError, PopulateTextFieldError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True, UsePhysicalKeyboard=True

### WebAutomation.PressButton のセレクター: PressButton, PressButtonCloseDialog, PressButtonNoWait, PressButtonPressDialogButton

## WebAutomation.PressButton.PressButton [A UI]
```
WebAutomation.PressButton.PressButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, PressButtonError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True

## WebAutomation.PressButton.PressButtonCloseDialog [A UI]
```
WebAutomation.PressButton.PressButtonCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, PressButtonError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True

## WebAutomation.PressButton.PressButtonNoWait [A UI]
```
WebAutomation.PressButton.PressButtonNoWait BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, PressButtonError
固定: WaitForPageToLoad=False

## WebAutomation.PressButton.PressButtonPressDialogButton [A UI]
```
WebAutomation.PressButton.PressButtonPressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !DialogButton:String
ON ERROR可: ElementNotFoundError, PressButtonError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True

### WebAutomation.SelectRadioButton のセレクター: SelectRadioButton, SelectRadioButtonCloseDialog, SelectRadioButtonNoWait, SelectRadioButtonPressDialogButton

## WebAutomation.SelectRadioButton.SelectRadioButton [A UI]
```
WebAutomation.SelectRadioButton.SelectRadioButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, SelectRadioButtonError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True

## WebAutomation.SelectRadioButton.SelectRadioButtonCloseDialog [A UI]
```
WebAutomation.SelectRadioButton.SelectRadioButtonCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, SelectRadioButtonError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True

## WebAutomation.SelectRadioButton.SelectRadioButtonNoWait [A UI]
```
WebAutomation.SelectRadioButton.SelectRadioButtonNoWait BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, SelectRadioButtonError
固定: WaitForPageToLoad=False

## WebAutomation.SelectRadioButton.SelectRadioButtonPressDialogButton [A UI]
```
WebAutomation.SelectRadioButton.SelectRadioButtonPressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !DialogButton:String
ON ERROR可: ElementNotFoundError, SelectRadioButtonError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True

### WebAutomation.SetCheckboxState のセレクター: SetCheckboxState, SetCheckboxStateCloseDialog, SetCheckboxStateNoWait, SetCheckboxStatePressDialogButton

## WebAutomation.SetCheckboxState.SetCheckboxState [A UI]
```
WebAutomation.SetCheckboxState.SetCheckboxState WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] State: WebAutomation.CheckboxState.Checked
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !State:CheckboxState{Checked,Unchecked}
ON ERROR可: ElementNotFoundError, SetCheckboxStateError
固定: HandleDialogAction=DoNothing, WaitForPageToLoad=True

## WebAutomation.SetCheckboxState.SetCheckboxStateCloseDialog [A UI]
```
WebAutomation.SetCheckboxState.SetCheckboxStateCloseDialog WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] State: WebAutomation.CheckboxState.Checked
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !State:CheckboxState{Checked,Unchecked}
ON ERROR可: ElementNotFoundError, SetCheckboxStateError
固定: HandleDialogAction=CloseIt, WaitForPageToLoad=True

## WebAutomation.SetCheckboxState.SetCheckboxStateNoWait [A UI]
```
WebAutomation.SetCheckboxState.SetCheckboxStateNoWait BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] State: WebAutomation.CheckboxState.Checked
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !State:CheckboxState{Checked,Unchecked}
ON ERROR可: ElementNotFoundError, SetCheckboxStateError
固定: WaitForPageToLoad=False

## WebAutomation.SetCheckboxState.SetCheckboxStatePressDialogButton [A UI]
```
WebAutomation.SetCheckboxState.SetCheckboxStatePressDialogButton WaitForPageToLoadTimeout: 60 BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] DialogButton: $'''example''' State: WebAutomation.CheckboxState.Checked
```
入力: !WaitForPageToLoadTimeout:Int32 !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !DialogButton:String !State:CheckboxState{Checked,Unchecked}
ON ERROR可: ElementNotFoundError, SetCheckboxStateError
固定: HandleDialogAction=PressButton, WaitForPageToLoad=True

### WebAutomation.SetDropDownListValue のセレクター: ClearDropDownListValue, ClearDropDownListValueCloseDialog, ClearDropDownListValueNoWait, ClearDropDownListValuePressDialogButton, SetDropDownListValueByIndex, SetDropDownListValueByIndexCloseDialog, SetDropDownListValueByIndexNoWait, SetDropDownListValueByIndexPressDialogButton, SetDropDownListValueByName, SetDropDownListValueByNameCloseDialog, SetDropDownListValueByNameNoWait, SetDropDownListValueByNamePressDialogButton

## WebAutomation.SetDropDownListValue.ClearDropDownListValue [A UI]
```
WebAutomation.SetDropDownListValue.ClearDropDownListValue WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=ClearAllOptions, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.SetDropDownListValue.ClearDropDownListValueCloseDialog [A UI]
```
WebAutomation.SetDropDownListValue.ClearDropDownListValueCloseDialog WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=ClearAllOptions, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.SetDropDownListValue.ClearDropDownListValueNoWait [A UI]
```
WebAutomation.SetDropDownListValue.ClearDropDownListValueNoWait Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser
```
入力: !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=ClearAllOptions, WaitForPageToLoad=False

## WebAutomation.SetDropDownListValue.ClearDropDownListValuePressDialogButton [A UI]
```
WebAutomation.SetDropDownListValue.ClearDropDownListValuePressDialogButton WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser DialogButton: $'''example'''
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=ClearAllOptions, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.SetDropDownListValue.SetDropDownListValueByIndex [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByIndex WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionsIndeces: Positions
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionsIndeces:List<Int32>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByIndex, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexCloseDialog [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexCloseDialog WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionsIndeces: Positions
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionsIndeces:List<Int32>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByIndex, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexNoWait [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexNoWait Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionsIndeces: Positions
```
入力: !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionsIndeces:List<Int32>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByIndex, WaitForPageToLoad=False

## WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexPressDialogButton [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByIndexPressDialogButton WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser DialogButton: $'''example''' OptionsIndeces: Positions
```
入力: !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String !OptionsIndeces:List<Int32>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByIndex, WaitForPageToLoad=True, HandleDialogAction=PressButton

## WebAutomation.SetDropDownListValue.SetDropDownListValueByName [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByName UseRegularExpression: False WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionNames: TextList
```
入力: !UseRegularExpression:Boolean !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionNames:List<String>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByName, WaitForPageToLoad=True, HandleDialogAction=DoNothing

## WebAutomation.SetDropDownListValue.SetDropDownListValueByNameCloseDialog [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByNameCloseDialog UseRegularExpression: False WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionNames: TextList
```
入力: !UseRegularExpression:Boolean !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionNames:List<String>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByName, WaitForPageToLoad=True, HandleDialogAction=CloseIt

## WebAutomation.SetDropDownListValue.SetDropDownListValueByNameNoWait [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByNameNoWait UseRegularExpression: False Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser OptionNames: TextList
```
入力: !UseRegularExpression:Boolean !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !OptionNames:List<String>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByName, WaitForPageToLoad=False

## WebAutomation.SetDropDownListValue.SetDropDownListValueByNamePressDialogButton [A UI]
```
WebAutomation.SetDropDownListValue.SetDropDownListValueByNamePressDialogButton UseRegularExpression: False WaitForPageToLoadTimeout: 60 Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] BrowserInstance: Browser DialogButton: $'''example''' OptionNames: TextList
```
入力: !UseRegularExpression:Boolean !WaitForPageToLoadTimeout:Int32 !Control:WebControl !BrowserInstance:WebBrowserInstanceHandle !DialogButton:String !OptionNames:List<String>
ON ERROR可: ElementNotFoundError, SetDropDownListValueError
固定: Operation=SelectOptionsByName, WaitForPageToLoad=True, HandleDialogAction=PressButton

### WebAutomation.TakeScreenshot のセレクター: TakeScreenshot, TakeScreenshotOfElement, TakeScreenshotOfElementSaveToFile, TakeScreenshotSaveToFile

## WebAutomation.TakeScreenshot.TakeScreenshot [A]
```
WebAutomation.TakeScreenshot.TakeScreenshot BrowserInstance: Browser
```
入力: BrowserInstance:WebBrowserInstanceHandle
ON ERROR可: ElementNotFoundError, SaveFileError, SaveToClipboardError, TakeScreenshotError
固定: Operation=WebPage, SaveMode=Clipboard

## WebAutomation.TakeScreenshot.TakeScreenshotOfElement [A UI]
```
WebAutomation.TakeScreenshot.TakeScreenshotOfElement BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\'']
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: ElementNotFoundError, SaveFileError, SaveToClipboardError, TakeScreenshotError
固定: Operation=Element, SaveMode=Clipboard

## WebAutomation.TakeScreenshot.TakeScreenshotOfElementSaveToFile [A UI]
```
WebAutomation.TakeScreenshot.TakeScreenshotOfElementSaveToFile BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''] File: $'''C:\temp\test.xlsx''' FileFormat: WebAutomation.FileFormat.Bmp
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl !File:FileObject !FileFormat:FileFormat{Bmp,Gif,Jpg,Png,Tiff}
ON ERROR可: ElementNotFoundError, SaveFileError, SaveToClipboardError, TakeScreenshotError
固定: Operation=Element, SaveMode=File

## WebAutomation.TakeScreenshot.TakeScreenshotSaveToFile [A]
```
WebAutomation.TakeScreenshot.TakeScreenshotSaveToFile BrowserInstance: Browser File: $'''C:\temp\test.xlsx''' FileFormat: WebAutomation.FileFormat.Bmp
```
入力: !BrowserInstance:WebBrowserInstanceHandle !File:FileObject !FileFormat:FileFormat{Bmp,Gif,Jpg,Png,Tiff}
ON ERROR可: ElementNotFoundError, SaveFileError, SaveToClipboardError, TakeScreenshotError
固定: Operation=WebPage, SaveMode=File

### WebAutomation.WaitForWebPageContent のセレクター: WebPageToContainElement, WebPageToContainElementInState, WebPageToContainText, WebPageToNotContainElement, WebPageToNotContainText

## WebAutomation.WaitForWebPageContent.WebPageToContainElement [W UI]
```
WAIT (WebAutomation.WaitForWebPageContent.WebPageToContainElement BrowserInstance: Browser Control: $'''body''')
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: WaitForWebPageContentError
固定: CheckElementState=False, ContainsMode=ToContainElement

## WebAutomation.WaitForWebPageContent.WebPageToContainElementInState [W UI]
```
WAIT (WebAutomation.WaitForWebPageContent.WebPageToContainElementInState State: WebAutomation.ElementState.Enabled BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''])
```
入力: !State:ElementState{Enabled,Disabled} !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: WaitForWebPageContentError
固定: CheckElementState=True, ContainsMode=ToContainElement

## WebAutomation.WaitForWebPageContent.WebPageToContainText [W]
```
WAIT (WebAutomation.WaitForWebPageContent.WebPageToContainText BrowserInstance: Browser Text: $'''example''')
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Text:String
ON ERROR可: WaitForWebPageContentError
固定: ContainsMode=ToContainText

## WebAutomation.WaitForWebPageContent.WebPageToNotContainElement [W UI]
```
WAIT (WebAutomation.WaitForWebPageContent.WebPageToNotContainElement BrowserInstance: Browser Control: appmask['Web Page \'KB Test Page\'']['Button \'Submit\''])
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Control:WebControl
ON ERROR可: WaitForWebPageContentError
固定: ContainsMode=ToNotContainElement

## WebAutomation.WaitForWebPageContent.WebPageToNotContainText [W]
```
WAIT (WebAutomation.WaitForWebPageContent.WebPageToNotContainText BrowserInstance: Browser Text: $'''example''')
```
入力: !BrowserInstance:WebBrowserInstanceHandle !Text:String
ON ERROR可: WaitForWebPageContentError
固定: ContainsMode=ToNotContainText
