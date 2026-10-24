# Robin: TerminalEmulation

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## TerminalEmulation.CloseSession [A]
```
TerminalEmulation.CloseSession Session: TerminalSession
```
入力: Session:TerminalSessionHandle
ON ERROR可: EmulatorCommunicationError

## TerminalEmulation.FindTextFromTerminalSession [A]
```
TerminalEmulation.FindTextFromTerminalSession Session: TerminalSession Text: $fx'example' IsRegEx: False ColumnSize: 80 Results=> FindResults
```
入力: Session:TerminalSessionHandle Text:String IsRegEx:Boolean ColumnSize:Int32
出力: Results:DataTable=>
ON ERROR可: EmulatorCommunicationError, InvalidRegexError, TextNotFoundError

### TerminalEmulation.GetTextFromTerminalSession のセレクター: GetTextFromCursorPosition, GetTextFromFieldAtPosition, GetTextFromFieldWithIndex, GetTextFromFieldWithLabel, GetTextFromPosition, GetTextFromScreen

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromCursorPosition [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromCursorPosition TextLength: 1 Session: TerminalSession Text=> TerminalText
```
入力: !TextLength:Int32 !Session:TerminalSessionHandle
出力: Text:String=>TerminalText
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=CursorPosition

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldAtPosition [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldAtPosition Row: 1 Session: TerminalSession Column: 1 Text=> TerminalText
```
入力: !Row:Int32 !Session:TerminalSessionHandle !Column:Int32
出力: Text:String=>TerminalText
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=Field, GetFieldBy=Position

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldWithIndex [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldWithIndex Index: 1 Session: TerminalSession Text=> TerminalText
```
入力: !Index:Int32 !Session:TerminalSessionHandle
出力: Text:String=>TerminalText
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=Field, GetFieldBy=Index

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldWithLabel [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromFieldWithLabel Session: TerminalSession FieldLabel: $fx'example' Text=> TerminalText
```
入力: FieldLabel:String Session:TerminalSessionHandle
出力: Text:String=>
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=Field, GetFieldBy=FieldLabel

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromPosition [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromPosition Row: 1 TextLength: 1 Session: TerminalSession Column: 1 Text=> TerminalText
```
入力: !Row:Int32 !TextLength:Int32 !Session:TerminalSessionHandle !Column:Int32
出力: Text:String=>TerminalText
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=SpecificPosition

## TerminalEmulation.GetTextFromTerminalSession.GetTextFromScreen [A]
```
TerminalEmulation.GetTextFromTerminalSession.GetTextFromScreen Session: TerminalSession Text=> TerminalText
```
入力: !Session:TerminalSessionHandle
出力: Text:String=>TerminalText
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: GetTextFrom=EntireScreen

## TerminalEmulation.MoveCursor [A]
```
TerminalEmulation.MoveCursor Session: TerminalSession Row: 1 Column: 1
```
入力: Column:Int32 Row:Int32 Session:TerminalSessionHandle
ON ERROR可: EmulatorCommunicationError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError

### TerminalEmulation.OpenTerminalSession のセレクター: OpenSession, OpenSessionUsingReflection, OpenSessionUsingReflectionProfile

## TerminalEmulation.OpenTerminalSession.OpenSession [A]
```
TerminalEmulation.OpenTerminalSession.OpenSession SessionName: $fx'example' HllapiPath: $fx'C:\temp\test.xlsx' Session=> TerminalSession
```
入力: !SessionName:String !HllapiPath:FileObject
出力: Session:TerminalSessionHandle=>TerminalSession
ON ERROR可: EmulatorCommunicationError, ProfileError
固定: Provider=HLLAPI

## TerminalEmulation.OpenTerminalSession.OpenSessionUsingReflection [A]
```
TerminalEmulation.OpenTerminalSession.OpenSessionUsingReflection Port: 1 InstallationPath: $fx'C:\temp' Attach: False HostType: TerminalEmulation.HostType.IBM3270 Host: $fx'example' Session=> TerminalSession
```
入力: !Port:Int32 !InstallationPath:FolderObject !Attach:Boolean !HostType:HostType{IBM3270,IBM5250} !Host:String
出力: Session:TerminalSessionHandle=>TerminalSession
ON ERROR可: EmulatorCommunicationError, ProfileError
固定: Provider=Reflection, Configuration=SpecifyConnection

## TerminalEmulation.OpenTerminalSession.OpenSessionUsingReflectionProfile [A]
```
TerminalEmulation.OpenTerminalSession.OpenSessionUsingReflectionProfile InstallationPath: $fx'C:\temp' Profile: $fx'C:\temp\test.xlsx' Attach: False Session=> TerminalSession
```
入力: Attach:Boolean InstallationPath:FolderObject Profile:FileObject
出力: Session:TerminalSessionHandle=>
ON ERROR可: EmulatorCommunicationError, ProfileError
固定: Provider=Reflection, Configuration=ExistingProfile

## TerminalEmulation.SendKey [A]
```
TerminalEmulation.SendKey Session: TerminalSession ControlKey: TerminalEmulation.ControlKey.Transmit
```
入力: ControlKey:ControlKey{Transmit,AltCursor,Attention,BackSpace,BackTab,BlockToggle,Break,Cancel,Center,Clear,ClearComm,ClearDisplay,ClearLine,ClearPage,ClearPartition,Comma,CommandLine,CommandWindow,Compose,CtrlF1,CtrlF2,CtrlF3,CtrlF4,CtrlF5,CtrlF6,CtrlF7,CtrlF8,CtrlF9,CtrlF10,CtrlF11,CtrlF12,CtrlShiftF1,CtrlShiftF2,CtrlShiftF3,CtrlShiftF4,CtrlShiftF5,CtrlShiftF6,CtrlShiftF7,CtrlShiftF8,CtrlShiftF9,CtrlShiftF10,CtrlShiftF11,CtrlShiftF12,CursorBlink,CursorSelect,Decimal,Delete,DeleteChar,DeleteLine,DeleteWord,DestructiveBackSpace,Disconnect,DoKey,Down,DownDouble,Dup,Duplicate,EditScript,KeyEnd,EndOfField,Erase_Eof,EraseEOL,EraseEOP,EraseInput,Escape,ExtGr,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,FieldDelimiter,FieldExit,FieldMark,FieldMinus,FieldPlus,Find,HardReset,Help,Hex,Hex00,Hex01,Hex02,Hex03,Hex04,Hex05,Hex06,Hex07,Hex08,Hex09,Hex0A,Hex0B,Hex0C,Hex0D,Hex0E,Hex0F,Hex10,Hex11,Hex12,Hex13,Hex14,Hex15,Hex16,Hex17,Hex18,Hex19,Hex1A,Hex1B,Hex1C,Hex1D,Hex1E,Hex1F,Hex7F,Hold,HoldClear,HoldSet,Home,HomeDown,HomeUp,Insert,InsertChar,InsertHere,InsertLine,InsertMode,InvalidKey,KeyPad0,KeyPad1,KeyPad2,KeyPad3,KeyPad4,KeyPad5,KeyPad6,KeyPad7,KeyPad8,KeyPad9,Left,LeftDouble,LineFeed,Minus,MonitorToggle,NewLine,NextPage,NextScreen,NextWord,Nul,NumLock,PA1,PA2,PA3,Page,PageDown,PageUp,PanLeft,PanRight,PartitionJump,PF1,PF2,PF3,PF4,PlusCr,PreviousWord,PrevPage,PrevScreen,Print,PrintLine,PrintMsg,PrintScreen,Remove,Replace,Reset,Return,ReverseField,Right,RightDouble,RollDown,RollUp,RuleLine,RunScript,ScrollDown,ScrollLeft,ScrollRight,ScrollUp,Select,Send,SendAnswerBack,SendDelete,SendLine,SendMsg,ShiftBackspace,ShiftDelete,ShiftDown,ShiftF1,ShiftF2,ShiftF3,ShiftF4,ShiftF5,ShiftF6,ShiftF7,ShiftF8,ShiftF9,ShiftF10,ShiftF11,ShiftF12,ShiftF13,ShiftF14,ShiftF15,ShiftF16,ShiftF17,ShiftF18,ShiftF19,ShiftF20,ShiftHome,ShiftInsert,ShiftLeft,ShiftPrintScreen,ShiftRight,ShiftUp,SoftReset,SystemRequest,Tab,TekZoom,TermNextPage,TermPrevPage,Test,TextAssistBeginBold,TextAssistBeginOfLine,TextAssistBeginUnderline,TextAssistBottomOfPage,TextAssistCarrierReturn,TextAssistCenter,TextAssistEndBold,TextAssistEndOfLine,TextAssistHalfIndexDown,TextAssistHalfIndexUp,TextAssistInsertSymbols,TextAssistNextStop,TextAssistNextTextColumn,TextAssistPageEnd,TextAssistRequiredSpace,TextAssistRequiredTab,TextAssistStop,TextAssistTextTabAdvance,TextAssistTopOfPage,TextAssistWordUnderline,TraceToggle,Udk10,Udk6,Udk7,Udk8,Udk9,Udk11,Udk12,Udk13,Udk14,Udk15,Udk16,Udk17,Udk18,Udk19,Udk20,Up,UpDouble} Session:TerminalSessionHandle
ON ERROR可: EmulatorCommunicationError, KeyNotSupportedError

### TerminalEmulation.SetTextOnTerminalSession のセレクター: SetTextOnCursorPosition, SetTextOnFieldAtPosition, SetTextOnFieldWithIndex, SetTextOnFieldWithLabel

## TerminalEmulation.SetTextOnTerminalSession.SetTextOnCursorPosition [A]
```
TerminalEmulation.SetTextOnTerminalSession.SetTextOnCursorPosition Session: TerminalSession TreatAtCharacterAsLiteral: False Text: $fx'password'
```
入力: !Session:TerminalSessionHandle !TreatAtCharacterAsLiteral:Boolean !Text:EncryptableObject
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, InputTextRejectedError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: SetTextOn=CursorPosition

## TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldAtPosition [A]
```
TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldAtPosition Session: TerminalSession TreatAtCharacterAsLiteral: False Text: $fx'password' Row: 1 Column: 1
```
入力: !Session:TerminalSessionHandle !TreatAtCharacterAsLiteral:Boolean !Text:EncryptableObject !Row:Int32 !Column:Int32
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, InputTextRejectedError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: SetTextOn=Field, GetFieldBy=Position

## TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldWithIndex [A]
```
TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldWithIndex Session: TerminalSession TreatAtCharacterAsLiteral: False Text: $fx'password' Index: 1
```
入力: !Session:TerminalSessionHandle !TreatAtCharacterAsLiteral:Boolean !Text:EncryptableObject !Index:Int32
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, InputTextRejectedError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: SetTextOn=Field, GetFieldBy=Index

## TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldWithLabel [A]
```
TerminalEmulation.SetTextOnTerminalSession.SetTextOnFieldWithLabel Session: TerminalSession Text: $fx'password' FieldLabel: $fx'example' TreatAtCharacterAsLiteral: False
```
入力: FieldLabel:String Session:TerminalSessionHandle Text:EncryptableObject TreatAtCharacterAsLiteral:Boolean
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, InputTextRejectedError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, UnformattedTerminalScreenError
固定: SetTextOn=Field, GetFieldBy=FieldLabel

### TerminalEmulation.WaitForTextOnTerminalSession のセレクター: WaitForTextOnFieldAtPosition, WaitForTextOnFieldWithIndex, WaitForTextOnFieldWithLabel, WaitForTextOnScreen

## TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldAtPosition [A]
```
TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldAtPosition Session: TerminalSession Row: 1 Text: $fx'example' Timeout: 0 Column: 1 IsRegEx: False
```
入力: !Session:TerminalSessionHandle !Row:Int32 !Text:String !Timeout:Int32 !Column:Int32 !IsRegEx:Boolean
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, TimeOutExpiredError, UnformattedTerminalScreenError
固定: WaitForTextOn=Field, GetFieldBy=Position

## TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldWithIndex [A]
```
TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldWithIndex Session: TerminalSession Text: $fx'example' Timeout: 0 IsRegEx: False Index: 1
```
入力: !Session:TerminalSessionHandle !Text:String !Timeout:Int32 !IsRegEx:Boolean !Index:Int32
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, TimeOutExpiredError, UnformattedTerminalScreenError
固定: WaitForTextOn=Field, GetFieldBy=Index

## TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldWithLabel [A]
```
TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnFieldWithLabel Session: TerminalSession Text: $fx'example' Timeout: 0 FieldLabel: $fx'example' IsRegEx: False
```
入力: !Session:TerminalSessionHandle !Text:String !Timeout:Int32 !FieldLabel:String !IsRegEx:Boolean
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, TimeOutExpiredError, UnformattedTerminalScreenError
固定: WaitForTextOn=Field, GetFieldBy=FieldLabel

## TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnScreen [A]
```
TerminalEmulation.WaitForTextOnTerminalSession.WaitForTextOnScreen Session: TerminalSession Text: $fx'example' IsRegEx: False Timeout: 0
```
入力: IsRegEx:Boolean Session:TerminalSessionHandle Text:String Timeout:Int32
ON ERROR可: EmulatorCommunicationError, FieldIndexOutOfBoundsError, FieldLabelNotFoundError, NoFieldFoundAtGivenPositionError, OperationUnavailableForSessionTypeError, PositionCommandsNotSupportedByEmulatorError, ScreenPositionOutOfBoundsError, TimeOutExpiredError, UnformattedTerminalScreenError
固定: WaitForTextOn=Screen
