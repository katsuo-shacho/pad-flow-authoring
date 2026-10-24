# Robin: MouseAndKeyboard

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## MouseAndKeyboard.BlockInput [A]
```
MouseAndKeyboard.BlockInput BlockIt: True
```
入力: BlockIt:Boolean
ON ERROR可: BlockInNonInteractiveModeError, BlockInputError

## MouseAndKeyboard.GetKeyboardLayout [A]
```
MouseAndKeyboard.GetKeyboardLayout KeyboardLayoutId=> KeyboardLayoutId
```
出力: KeyboardLayoutId:Int64=>
ON ERROR可: GetCurrentKeyboardLayoutError

## MouseAndKeyboard.GetMousePosition [A]
```
MouseAndKeyboard.GetMousePosition RelativeTo: MouseAndKeyboard.MousePositionRelativeTo.Screen X=> MousePosX Y=> MousePosY
```
入力: RelativeTo:MousePositionRelativeTo{Screen,ForegroundWindow}
出力: X:Int32=> Y:Int32=>
ON ERROR可: RetrieveMousePositionInNonInteractiveModeError

## MouseAndKeyboard.MoveMouse [A]
```
MouseAndKeyboard.MoveMouse X: 1 Y: 1 RelativeTo: MouseAndKeyboard.PositionRelativeTo.Screen MovementStyle: MouseAndKeyboard.MovementStyle.Instant
```
入力: MovementStyle:MovementStyle{Instant,AnimateSlow,AnimateNormal,AnimateFast} RelativeTo:PositionRelativeTo{Screen,ActiveWindow,CurrentMousePosition} X:Int32 Y:Int32
ON ERROR可: MoveMouseError, MoveMouseInNonInteractiveModeError

### MouseAndKeyboard.MoveMouseToTextOnScreenWithOCR のセレクター: ClickTextOnScreenWithCustomTesseractOCR, ClickTextOnScreenWithOCR, ClickTextOnScreenWithTesseractOCR, ClickTextOnScreenWithWindowsOcr, ClickTextOnSubregionOfScreenWithCustomTesseractOCR, ClickTextOnSubregionOfScreenWithOCR, ClickTextOnSubregionOfScreenWithTesseractOCR, ClickTextOnSubregionOfScreenWithWindowsOcr, ClickTextOnSubregionRelativeToImageOfScreenWithCustomTesseractOCR, ClickTextOnSubregionRelativeToImageOfScreenWithOCR, ClickTextOnSubregionRelativeToImageOfScreenWithTesseractOCR, ClickTextOnSubregionRelativeToImageOfScreenWithWindowsOcr, MoveMouseToTextOnScreenWithCustomTesseractOCR, MoveMouseToTextOnScreenWithOCR, MoveMouseToTextOnScreenWithTesseractOCR, MoveMouseToTextOnScreenWithWindowsOcr, MoveMouseToTextOnSubregionOfScreenWithCustomTesseractOCR, MoveMouseToTextOnSubregionOfScreenWithOCR, MoveMouseToTextOnSubregionOfScreenWithTesseractOCR, MoveMouseToTextOnSubregionOfScreenWithWindowsOcr, MoveMouseToTextOnSubregionRelativeToImageOfScreenWithCustomTesseractOCR, MoveMouseToTextOnSubregionRelativeToImageOfScreenWithOCR, MoveMouseToTextOnSubregionRelativeToImageOfScreenWithTesseractOCR, MoveMouseToTextOnSubregionRelativeToImageOfScreenWithWindowsOcr, WaitForTextToAppearAndClickTextOnScreenWithCustomTesseractOCR, WaitForTextToAppearAndClickTextOnScreenWithOCR, WaitForTextToAppearAndClickTextOnScreenWithTesseractOCR, WaitForTextToAppearAndClickTextOnScreenWithWindowsOcr, WaitForTextToAppearAndClickTextOnSubregionOfScreenWithCustomTesseractOCR, WaitForTextToAppearAndClickTextOnSubregionOfScreenWithOCR, WaitForTextToAppearAndClickTextOnSubregionOfScreenWithTesseractOCR, WaitForTextToAppearAndClickTextOnSubregionOfScreenWithWindowsOcr, WaitForTextToAppearAndClickTextOnSubregionRelativeToImageOfScreenWithCustomTesseractOCR, WaitForTextToAppearAndClickTextOnSubregionRelativeToImageOfScreenWithOCR, WaitForTextToAppearAndClickTextOnSubregionRelativeToImageOfScreenWithTesseractOCR, WaitForTextToAppearAndClickTextOnSubregionRelativeToImageOfScreenWithWindowsOcr, WaitForTextToAppearAndMoveMouseToTextOnScreenWithCustomTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnScreenWithOCR, WaitForTextToAppearAndMoveMouseToTextOnScreenWithTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnScreenWithWindowsOcr, WaitForTextToAppearAndMoveMouseToTextOnSubregionOfScreenWithCustomTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionOfScreenWithOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionOfScreenWithTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionOfScreenWithWindowsOcr, WaitForTextToAppearAndMoveMouseToTextOnSubregionRelativeToImageOfScreenWithCustomTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionRelativeToImageOfScreenWithOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionRelativeToImageOfScreenWithTesseractOCR, WaitForTextToAppearAndMoveMouseToTextOnSubregionRelativeToImageOfScreenWithWindowsOcr

## MouseAndKeyboard.MoveMouseToTextOnScreenWithOCR.WaitForTextToAppearAndMoveMouseToTextOnScreenWithWindowsOcr [A UI]
```
MouseAndKeyboard.MoveMouseToTextOnScreenWithOCR.WaitForTextToAppearAndMoveMouseToTextOnScreenWithWindowsOcr TextToFind: $'''example''' IsRegEx: False WindowsOcrLanguage: MouseAndKeyboard.WindowsOcrLanguage.English Occurence: 1 SearchForTextOn: MouseAndKeyboard.SearchTarget.EntireScreen ImageWidthMultiplier: 1 ImageHeightMultiplier: 1 MovementStyle: MouseAndKeyboard.MovementStyle.Instant Timeout: 5 PositionRelativeToText: MouseAndKeyboard.PositionOnImage.MiddleCenter OffsetX: 0 OffsetY: 0 X=> LocationOfTextFoundX Y=> LocationOfTextFoundY Width=> WidthOfTextFound Height=> HeightOfTextFound
```
入力: TextToFind:String IsRegEx:Boolean Occurence:Int32 SearchForTextOn:SearchTarget{EntireScreen,ForegroundWindow} MovementStyle:MovementStyle{Instant,AnimateSlow,AnimateNormal,AnimateFast} Timeout:Int32 PositionRelativeToText:PositionOnImage{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} OffsetX:Int32 OffsetY:Int32 ImageHeightMultiplier:Int32 ImageWidthMultiplier:Int32 WindowsOcrLanguage:WindowsOcrLanguage{ChineseSimplified,ChineseTraditional,Czech,Danish,Dutch,English,Finnish,French,German,Greek,Hungarian,Italian,Japanese,Korean,Norwegian,Polish,Portuguese,Romanian,Russian,SerbianCyrillic,SerbianLatin,Slovak,Spanish,Swedish,Turkish}
出力: X:Int32=> Y:Int32=> Width:Int32=> Height:Int32=>
ON ERROR可: CreateOCREngineError, DataPathFolderNotFoundError, InvalidSubregionCoordinatesError, LanguageNotInstalledError, MoveMouseError, MoveMouseInNonInteractiveModeError, OCREngineNotAliveError, TextNotFoundOnScreenError
固定: SearchMode=Whole, WaitForTextToAppear=True, SendMouseClick=False, OCREngineType=WindowsOcr

### MouseAndKeyboard.PressReleaseKey のセレクター: PressKey, ReleaseKey

## MouseAndKeyboard.PressReleaseKey.PressKey [A]
```
MouseAndKeyboard.PressReleaseKey.PressKey Control: False Alt: False Shift: False Win: False
```
入力: Alt:Boolean Control:Boolean Shift:Boolean Win:Boolean
ON ERROR可: PressReleaseKeyInNonInteractiveModeError
固定: Event=Press

## MouseAndKeyboard.PressReleaseKey.ReleaseKey [A]
```
MouseAndKeyboard.PressReleaseKey.ReleaseKey Shift: False Win: False Alt: False Control: False
```
入力: !Shift:Boolean !Win:Boolean !Alt:Boolean !Control:Boolean
ON ERROR可: PressReleaseKeyInNonInteractiveModeError
固定: Event=Release

### MouseAndKeyboard.SendKeys のセレクター: FocusAndSendKeys, FocusAndSendKeysByControl, FocusAndSendKeysByInstanceOrHandle, FocusAndSendKeysByTitleClass

## MouseAndKeyboard.SendKeys.FocusAndSendKeys [A]
```
MouseAndKeyboard.SendKeys.FocusAndSendKeys TextToSend: $'''password''' DelayBetweenKeystrokes: 10 SendTextAsHardwareKeys: False
```
入力: DelayBetweenKeystrokes:Int32 SendTextAsHardwareKeys:Boolean TextToSend:EncryptableObject
ON ERROR可: InvalidKeystrokesError, NoActiveApplicationError, SendKeystrokesError, SendKeystrokesInNonInteractiveModeError, WindowNotFoundError
固定: SendKeysTo=Foreground

## MouseAndKeyboard.SendKeys.FocusAndSendKeysByControl [A UI]
```
MouseAndKeyboard.SendKeys.FocusAndSendKeysByControl TextToSend: $'''password''' SendTextAsHardwareKeys: False Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] DelayBetweenKeystrokes: 10
```
入力: !TextToSend:EncryptableObject !SendTextAsHardwareKeys:Boolean !Control:UIControl !DelayBetweenKeystrokes:Int32
ON ERROR可: InvalidKeystrokesError, NoActiveApplicationError, SendKeystrokesError, SendKeystrokesInNonInteractiveModeError, WindowNotFoundError
固定: SendKeysTo=Control

## MouseAndKeyboard.SendKeys.FocusAndSendKeysByInstanceOrHandle [A]
```
MouseAndKeyboard.SendKeys.FocusAndSendKeysByInstanceOrHandle TextToSend: $'''password''' SendTextAsHardwareKeys: False WindowInstance: 1 DelayBetweenKeystrokes: 10
```
入力: !TextToSend:EncryptableObject !SendTextAsHardwareKeys:Boolean !WindowInstance:Int32 !DelayBetweenKeystrokes:Int32
ON ERROR可: InvalidKeystrokesError, NoActiveApplicationError, SendKeystrokesError, SendKeystrokesInNonInteractiveModeError, WindowNotFoundError
固定: SendKeysTo=InstanceOrHandle

## MouseAndKeyboard.SendKeys.FocusAndSendKeysByTitleClass [A]
```
MouseAndKeyboard.SendKeys.FocusAndSendKeysByTitleClass TextToSend: $'''password''' SendTextAsHardwareKeys: False Title: $'''example''' Class: $'''example''' DelayBetweenKeystrokes: 10
```
入力: !TextToSend:EncryptableObject !SendTextAsHardwareKeys:Boolean !Title:String !Class:String !DelayBetweenKeystrokes:Int32
ON ERROR可: InvalidKeystrokesError, NoActiveApplicationError, SendKeystrokesError, SendKeystrokesInNonInteractiveModeError, WindowNotFoundError
固定: SendKeysTo=TitleAndClass

### MouseAndKeyboard.SendMouseClick のセレクター: Click, ClickAt

## MouseAndKeyboard.SendMouseClick.Click [A]
```
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
```
入力: ClickType:MouseClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} MillisecondsDelay:Int32
ON ERROR可: ClickOutOfScreenBoundsError, SendClickError, SendClickInNonInteractiveModeError
固定: MoveMouse=False

## MouseAndKeyboard.SendMouseClick.ClickAt [A]
```
MouseAndKeyboard.SendMouseClick.ClickAt RelativeTo: MouseAndKeyboard.PositionRelativeTo.Screen X: 1 Y: 1 ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0 MovementStyle: MouseAndKeyboard.MovementStyle.Instant
```
入力: !RelativeTo:PositionRelativeTo{Screen,ActiveWindow,CurrentMousePosition} !X:Int32 !Y:Int32 !ClickType:MouseClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MillisecondsDelay:Int32 !MovementStyle:MovementStyle{Instant,AnimateSlow,AnimateNormal,AnimateFast}
ON ERROR可: ClickOutOfScreenBoundsError, SendClickError, SendClickInNonInteractiveModeError
固定: MoveMouse=True

## MouseAndKeyboard.SetKeyState [A]
```
MouseAndKeyboard.SetKeyState Key: MouseAndKeyboard.MultiStateKey.CapsLock State: MouseAndKeyboard.KeyState.ModeOn
```
入力: Key:MultiStateKey{CapsLock,NumLock,ScrollLock} State:KeyState{ModeOff,ModeOn}
ON ERROR可: SetKeyStateInNonInteractiveModeError

## MouseAndKeyboard.SetKeyboardLayout [A]
```
MouseAndKeyboard.SetKeyboardLayout KeyboardLayoutId: 1
```
入力: !KeyboardLayoutId:Int64
ON ERROR可: SetKeyboardLayoutError

### MouseAndKeyboard.WaitForMouse のセレクター: WaitForMouseToBecome, WaitForMouseToBecomeDifferentThan

## MouseAndKeyboard.WaitForMouse.WaitForMouseToBecome [W]
```
WAIT (MouseAndKeyboard.WaitForMouse.WaitForMouseToBecome MousePointerState: MouseAndKeyboard.MousePointerState.Arrow)
```
入力: !MousePointerState:MousePointerState{Arrow,AppStarting,Cross,Hand,Help,IBeam,WaitCursor}
ON ERROR可: (名前なし)
固定: MouseEvent=Become

## MouseAndKeyboard.WaitForMouse.WaitForMouseToBecomeDifferentThan [W]
```
WAIT (MouseAndKeyboard.WaitForMouse.WaitForMouseToBecomeDifferentThan MousePointerState: MouseAndKeyboard.MousePointerState.Arrow)
```
入力: !MousePointerState:MousePointerState{Arrow,AppStarting,Cross,Hand,Help,IBeam,WaitCursor}
ON ERROR可: (名前なし)
固定: MouseEvent=BecomeNot

### MouseAndKeyboard.WaitForShortcutKey のセレクター: WaitForShortcutKey, WaitForShortcutKeyAndProceedOnTimeout

## MouseAndKeyboard.WaitForShortcutKey.WaitForShortcutKey [A]
```
MouseAndKeyboard.WaitForShortcutKey.WaitForShortcutKey InputKeys: ['Ctrl+A'] IndexOfShortcutKeyPressed=> IndexOfShortcutKeyPressed
```
入力: InputKeys:List
出力: IndexOfShortcutKeyPressed:Int32=>
ON ERROR可: FailedToRegisterShortcutkeyError
固定: ProceedOnTimeout=False

## MouseAndKeyboard.WaitForShortcutKey.WaitForShortcutKeyAndProceedOnTimeout [A]
```
MouseAndKeyboard.WaitForShortcutKey.WaitForShortcutKeyAndProceedOnTimeout InputKeys: List ContinueAfter: 10 IndexOfShortcutKeyPressed=> IndexOfShortcutKeyPressed
```
入力: !InputKeys:List<String> !ContinueAfter:Int32
出力: IndexOfShortcutKeyPressed:Int32=>IndexOfShortcutKeyPressed
ON ERROR可: FailedToRegisterShortcutkeyError
固定: ProceedOnTimeout=True
