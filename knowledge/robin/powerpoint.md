# Robin: PowerPoint

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### PowerPoint.AddPowerPointSlide のセレクター: AddSlideAsFirst, AddSlideAsLast, AddSlideAtPosition

## PowerPoint.AddPowerPointSlide.AddSlideAsFirst [A]
```
PowerPoint.AddPowerPointSlide.AddSlideAsFirst Instance: PowerPointInstance SlideIndex=> SlideIndex
```
入力: !Instance:PowerPointInstanceHandle
出力: SlideIndex:Int32=>SlideIndex
ON ERROR可: AddPowerPointSlideError, AddPowerPointSlideInvalidPositionError
固定: AddSlidePosition=FirstSlide

## PowerPoint.AddPowerPointSlide.AddSlideAsLast [A]
```
PowerPoint.AddPowerPointSlide.AddSlideAsLast Instance: PowerPointInstance SlideIndex=> SlideIndex
```
入力: !Instance:PowerPointInstanceHandle
出力: SlideIndex:Int32=>SlideIndex
ON ERROR可: AddPowerPointSlideError, AddPowerPointSlideInvalidPositionError
固定: AddSlidePosition=LastSlide

## PowerPoint.AddPowerPointSlide.AddSlideAtPosition [A]
```
PowerPoint.AddPowerPointSlide.AddSlideAtPosition SlidePosition: 1 Instance: PowerPointInstance SlideIndex=> SlideIndex
```
入力: !SlidePosition:Int32 !Instance:PowerPointInstanceHandle
出力: SlideIndex:Int32=>SlideIndex
ON ERROR可: AddPowerPointSlideError, AddPowerPointSlideInvalidPositionError
固定: AddSlidePosition=AtPosition

## PowerPoint.AttachToRunningPowerPoint [A]
```
PowerPoint.AttachToRunningPowerPoint PresentationName: $'''C:\temp\test.xlsx''' Instance=> PowerPointInstance
```
入力: !PresentationName:FileObject
出力: Instance:PowerPointInstanceHandle=>PowerPointInstance
ON ERROR可: AttachToPowerPointError, LaunchPowerPointInstallationError, PresentationNotFoundError

### PowerPoint.ClosePowerPoint のセレクター: Close, CloseAndSave, CloseAndSaveAs

## PowerPoint.ClosePowerPoint.Close [A]
```
PowerPoint.ClosePowerPoint.Close Instance: PowerPointInstance
```
入力: !Instance:PowerPointInstanceHandle
ON ERROR可: ClosePowerPointError, SavePowerPointError, SavePowerPointFormatMismatchError, SavePowerPointUnsupportedExtensionError, SavePowerPointUnsupportedFormatError
固定: CloseMode=DoNotSave

## PowerPoint.ClosePowerPoint.CloseAndSave [A]
```
PowerPoint.ClosePowerPoint.CloseAndSave Instance: PowerPointInstance
```
入力: !Instance:PowerPointInstanceHandle
ON ERROR可: ClosePowerPointError, SavePowerPointError, SavePowerPointFormatMismatchError, SavePowerPointUnsupportedExtensionError, SavePowerPointUnsupportedFormatError
固定: CloseMode=Save

## PowerPoint.ClosePowerPoint.CloseAndSaveAs [A]
```
PowerPoint.ClosePowerPoint.CloseAndSaveAs DocumentFormat: PowerPoint.PowerPointFormat.FromExtension DocumentPath: $'''C:\temp\test.xlsx''' Instance: PowerPointInstance
```
入力: !DocumentFormat:PowerPointFormat{PPTX,PPTM,PPT,PDF,XPS,POTX,POTM,PPSX,PPSM,ODP,FromExtension} !DocumentPath:FileObject !Instance:PowerPointInstanceHandle
ON ERROR可: ClosePowerPointError, SavePowerPointError, SavePowerPointFormatMismatchError, SavePowerPointUnsupportedExtensionError, SavePowerPointUnsupportedFormatError
固定: CloseMode=SaveAs

## PowerPoint.CopyPastePowerPointSlide [A]
```
PowerPoint.CopyPastePowerPointSlide DestinationInstance: PowerPointInstance DestinationSlidePosition: 1 SourceInstance: PowerPointInstance SourceSlidePosition: 1
```
入力: !DestinationInstance:PowerPointInstanceHandle !DestinationSlidePosition:Int32 !SourceInstance:PowerPointInstanceHandle !SourceSlidePosition:Int32
ON ERROR可: CopyPasteSlideError, CopyPasteSlideInvalidDestinationPositionError, CopyPasteSlideInvalidSourcePositionError, CopyPasteSlideSourceNoSlidesError

### PowerPoint.DeletePowerPointSlide のセレクター: DeleteSlideAtPosition, DeleteSlideFirst, DeleteSlideLast

## PowerPoint.DeletePowerPointSlide.DeleteSlideAtPosition [A]
```
PowerPoint.DeletePowerPointSlide.DeleteSlideAtPosition SlidePosition: 1 Instance: PowerPointInstance
```
入力: !SlidePosition:Int32 !Instance:PowerPointInstanceHandle
ON ERROR可: DeletePowerPointSlideError, DeletePowerPointSlideInvalidPositionError, DeletePowerPointSlideNoSlidesError
固定: DeleteSlidePosition=AtPosition

## PowerPoint.DeletePowerPointSlide.DeleteSlideFirst [A]
```
PowerPoint.DeletePowerPointSlide.DeleteSlideFirst Instance: PowerPointInstance
```
入力: !Instance:PowerPointInstanceHandle
ON ERROR可: DeletePowerPointSlideError, DeletePowerPointSlideInvalidPositionError, DeletePowerPointSlideNoSlidesError
固定: DeleteSlidePosition=FirstSlide

## PowerPoint.DeletePowerPointSlide.DeleteSlideLast [A]
```
PowerPoint.DeletePowerPointSlide.DeleteSlideLast Instance: PowerPointInstance
```
入力: !Instance:PowerPointInstanceHandle
ON ERROR可: DeletePowerPointSlideError, DeletePowerPointSlideInvalidPositionError, DeletePowerPointSlideNoSlidesError
固定: DeleteSlidePosition=LastSlide

### PowerPoint.LaunchPowerPoint のセレクター: Launch, LaunchAndOpen

## PowerPoint.LaunchPowerPoint.Launch [A]
```
PowerPoint.LaunchPowerPoint.Launch Instance=> PowerPointInstance
```
出力: Instance:PowerPointInstanceHandle=>PowerPointInstance
ON ERROR可: LaunchPowerPointError, LaunchPowerPointFileNotFoundError, LaunchPowerPointInstallationError, LaunchPowerPointInvalidFileTypeError, LaunchPowerPointOpenExistingDocumentError
固定: LaunchPowerPointMode=NewPresentation

## PowerPoint.LaunchPowerPoint.LaunchAndOpen [A]
```
PowerPoint.LaunchPowerPoint.LaunchAndOpen ReadOnly: False Path: $'''C:\temp\test.xlsx''' Instance=> PowerPointInstance
```
入力: !ReadOnly:Boolean !Path:FileObject
出力: Instance:PowerPointInstanceHandle=>PowerPointInstance
ON ERROR可: LaunchPowerPointError, LaunchPowerPointFileNotFoundError, LaunchPowerPointInstallationError, LaunchPowerPointInvalidFileTypeError, LaunchPowerPointOpenExistingDocumentError
固定: LaunchPowerPointMode=StoredPresentation

## PowerPoint.MovePowerPointSlide [A]
```
PowerPoint.MovePowerPointSlide DestinationInstance: PowerPointInstance DestinationSlidePosition: 1 SourceInstance: PowerPointInstance SourceSlidePosition: 1
```
入力: !DestinationInstance:PowerPointInstanceHandle !DestinationSlidePosition:Int32 !SourceInstance:PowerPointInstanceHandle !SourceSlidePosition:Int32
ON ERROR可: MoveSlideError, MoveSlideInvalidDestinationPositionError, MoveSlideInvalidSourcePositionError, MoveSlideSourceNoSlidesError

### PowerPoint.ReadFromPowerPoint のセレクター: Read, ReadSlides

## PowerPoint.ReadFromPowerPoint.Read [A]
```
PowerPoint.ReadFromPowerPoint.Read Instance: PowerPointInstance PowerPointData=> PowerPointData
```
入力: !Instance:PowerPointInstanceHandle
出力: PowerPointData:String=>PowerPointData
ON ERROR可: ReadPowerPointError
固定: ReadMode=WholePresentation

## PowerPoint.ReadFromPowerPoint.ReadSlides [A]
```
PowerPoint.ReadFromPowerPoint.ReadSlides Slides: $'''example''' Instance: PowerPointInstance PowerPointData=> PowerPointData
```
入力: !Slides:String !Instance:PowerPointInstanceHandle
出力: PowerPointData:String=>PowerPointData
ON ERROR可: ReadPowerPointError
固定: ReadMode=Slides

### PowerPoint.SavePowerPoint のセレクター: Save, SaveAs

## PowerPoint.SavePowerPoint.Save [A]
```
PowerPoint.SavePowerPoint.Save Instance: PowerPointInstance
```
入力: !Instance:PowerPointInstanceHandle
ON ERROR可: SavePowerPointError, SavePowerPointFormatMismatchError, SavePowerPointInstanceNullError, SavePowerPointUnsupportedExtensionError, SavePowerPointUnsupportedFormatError
固定: SaveMode=Save

## PowerPoint.SavePowerPoint.SaveAs [A]
```
PowerPoint.SavePowerPoint.SaveAs DocumentFormat: PowerPoint.PowerPointFormat.FromExtension DocumentPath: $'''C:\temp\test.xlsx''' Instance: PowerPointInstance
```
入力: !DocumentFormat:PowerPointFormat{PPTX,PPTM,PPT,PDF,XPS,POTX,POTM,PPSX,PPSM,ODP,FromExtension} !DocumentPath:FileObject !Instance:PowerPointInstanceHandle
ON ERROR可: SavePowerPointError, SavePowerPointFormatMismatchError, SavePowerPointInstanceNullError, SavePowerPointUnsupportedExtensionError, SavePowerPointUnsupportedFormatError
固定: SaveMode=SaveAs

### PowerPoint.WriteToPowerPoint のセレクター: WriteToFirstSlide, WriteToLastSlide, WriteToSlideAtPosition

## PowerPoint.WriteToPowerPoint.WriteToFirstSlide [A]
```
PowerPoint.WriteToPowerPoint.WriteToFirstSlide AppendNewLine: False Instance: PowerPointInstance Text: $'''example'''
```
入力: !AppendNewLine:Boolean !Instance:PowerPointInstanceHandle !Text:String
ON ERROR可: WritePowerPointError, WritePowerPointInvalidSlidePositionError, WritePowerPointNoSlidesError
固定: WriteMode=FirstSlide

## PowerPoint.WriteToPowerPoint.WriteToLastSlide [A]
```
PowerPoint.WriteToPowerPoint.WriteToLastSlide AppendNewLine: False Instance: PowerPointInstance Text: $'''example'''
```
入力: !AppendNewLine:Boolean !Instance:PowerPointInstanceHandle !Text:String
ON ERROR可: WritePowerPointError, WritePowerPointInvalidSlidePositionError, WritePowerPointNoSlidesError
固定: WriteMode=LastSlide

## PowerPoint.WriteToPowerPoint.WriteToSlideAtPosition [A]
```
PowerPoint.WriteToPowerPoint.WriteToSlideAtPosition SlidePosition: 1 AppendNewLine: False Instance: PowerPointInstance Text: $'''example'''
```
入力: !SlidePosition:Int32 !AppendNewLine:Boolean !Instance:PowerPointInstanceHandle !Text:String
ON ERROR可: WritePowerPointError, WritePowerPointInvalidSlidePositionError, WritePowerPointNoSlidesError
固定: WriteMode=AtPosition
