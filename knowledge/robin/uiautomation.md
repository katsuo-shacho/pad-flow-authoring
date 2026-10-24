# Robin: UIAutomation

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### UIAutomation.Click のセレクター: Click, SimulateClick

## UIAutomation.Click.Click [A UI]
```
UIAutomation.Click.Click OffsetX: 0 OffsetY: 0 Element: appmask['Window \'KB Test Window\'']['Button \'OK\''] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter
```
入力: !OffsetX:Int32 !OffsetY:Int32 !Element:UIControl !ClickType:ClickType{LeftClick,RightClick,DoubleClick,LeftButtonDown,LeftButtonUp,RightButtonDown,RightButtonUp,MiddleClick} !MousePositionRelativeToElement:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight}
ON ERROR可: ClickFailedError
固定: Simulate=False

## UIAutomation.Click.SimulateClick [A UI]
```
UIAutomation.Click.SimulateClick Element: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !Element:UIControl
ON ERROR可: ClickFailedError
固定: Simulate=True

### UIAutomation.CloseWindow のセレクター: Close, CloseByInstanceOrHandle, CloseByTitleClass

## UIAutomation.CloseWindow.Close [A UI]
```
UIAutomation.CloseWindow.Close Window: appmask['Window \'KB Test Window\'']
```
入力: !Window:UIControl
ON ERROR可: CloseWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.CloseWindow.CloseByInstanceOrHandle [A]
```
UIAutomation.CloseWindow.CloseByInstanceOrHandle WindowInstance: 1
```
入力: !WindowInstance:Int32
ON ERROR可: CloseWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.CloseWindow.CloseByTitleClass [A]
```
UIAutomation.CloseWindow.CloseByTitleClass Title: $'''example''' Class: $'''example'''
```
入力: !Title:String !Class:String
ON ERROR可: CloseWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

## UIAutomation.DragAndDropElement [A UI]
```
UIAutomation.DragAndDropElement MouseUpOffsetY: 0 MouseUpOffsetX: 0 RectangleEdgePointForMouseUp: UIAutomation.RectangleEdgePoint.MiddleCenter RectangleEdgePointForMouseDown: UIAutomation.RectangleEdgePoint.MiddleCenter MouseDownOffsetY: 0 ClickType: UIAutomation.DragAndDropClickType.LeftClick ControlToDrag: appmask['Window \'KB Test Window\'']['Button \'OK\''] MouseDownOffsetX: 0 ControlToDropOver: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !MouseUpOffsetY:Int32 !MouseUpOffsetX:Int32 !RectangleEdgePointForMouseUp:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !RectangleEdgePointForMouseDown:RectangleEdgePoint{TopLeft,TopCenter,TopRight,MiddleLeft,MiddleCenter,MiddleRight,BottomLeft,BottomCenter,BottomRight} !MouseDownOffsetY:Int32 !ClickType:DragAndDropClickType{LeftClick,RightClick} !ControlToDrag:UIControl !MouseDownOffsetX:Int32 !ControlToDropOver:UIControl
ON ERROR可: DragAndDropError, DragElementNotFoundError, DropTargetNotFoundError

## UIAutomation.ExpandCollapseTreeNode [A UI]
```
UIAutomation.ExpandCollapseTreeNode Control: $'''body''' UseRegex: False Operation: UIAutomation.TreeNodeOperation.Expand FoldersPath: $'''example'''
```
入力: FoldersPath:String Operation:TreeNodeOperation{Expand,Collapse} UseRegex:Boolean Control:UIControl
ON ERROR可: SetTreeNodeStateError

### UIAutomation.ExtractDataFromTable のセレクター: ExtractDataFromTable, ExtractDataFromTableInExcelSpreadsheet

## UIAutomation.ExtractDataFromTable.ExtractDataFromTable [A UI]
```
UIAutomation.ExtractDataFromTable.ExtractDataFromTable Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringToFront: True ExtractedData=> DataFromTable
```
入力: !Control:UIControl !BringToFront:Boolean
出力: ExtractedData:Object=>DataFromTable
ON ERROR可: ExtractDataFromTableError
固定: StoreExtractedDataIn=Variable

## UIAutomation.ExtractDataFromTable.ExtractDataFromTableInExcelSpreadsheet [A UI]
```
UIAutomation.ExtractDataFromTable.ExtractDataFromTableInExcelSpreadsheet Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringToFront: True ExcelInstance=> ExcelInstance
```
入力: !Control:UIControl !BringToFront:Boolean
出力: ExcelInstance:ExcelInstanceHandle=>ExcelInstance
ON ERROR可: ExtractDataFromTableError
固定: StoreExtractedDataIn=ExcelSpreadsheet

### UIAutomation.ExtractDataFromWindow のセレクター: ExtractData, ExtractDataInExcelSpreadsheet

## UIAutomation.ExtractDataFromWindow.ExtractData [A UI]
```
UIAutomation.ExtractDataFromWindow.ExtractData Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringToFront: True ExtractedData=> DataFromWindow
```
入力: !Control:UIControl !BringToFront:Boolean
出力: ExtractedData:Object=>DataFromWindow
ON ERROR可: ExtractWindowDataError
固定: StoreExtractedDataIn=Variable

## UIAutomation.ExtractDataFromWindow.ExtractDataInExcelSpreadsheet [A UI]
```
UIAutomation.ExtractDataFromWindow.ExtractDataInExcelSpreadsheet Control: $'''body''' BringToFront: True ExcelInstance=> ExcelInstance
```
入力: BringToFront:Boolean Control:UIControl
出力: ExcelInstance:ExcelInstanceHandle=>
ON ERROR可: ExtractWindowDataError
固定: StoreExtractedDataIn=ExcelSpreadsheet

## UIAutomation.FocusTextField [A UI]
```
UIAutomation.FocusTextField TextField: appmask['Window \'KB Test Window\'']['Edit \'Name\'']
```
入力: !TextField:UIControl
ON ERROR可: FocusTextFieldError

### UIAutomation.FocusWindow のセレクター: Focus, FocusByInstanceOrHandle, FocusByTitleClass

## UIAutomation.FocusWindow.Focus [A UI]
```
UIAutomation.FocusWindow.Focus Window: appmask['Window \'KB Test Window\'']
```
入力: !Window:UIControl
ON ERROR可: FocusWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.FocusWindow.FocusByInstanceOrHandle [A]
```
UIAutomation.FocusWindow.FocusByInstanceOrHandle WindowInstance: 1
```
入力: !WindowInstance:Int32
ON ERROR可: FocusWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.FocusWindow.FocusByTitleClass [A]
```
UIAutomation.FocusWindow.FocusByTitleClass Title: $'''example''' Class: $'''example'''
```
入力: !Title:String !Class:String
ON ERROR可: FocusWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

## UIAutomation.GetElementDetails [A UI]
```
UIAutomation.GetElementDetails BringToFront: True AttributeName: $'''example''' Element: appmask['Window \'KB Test Window\'']['Button \'OK\''] AttributeValue=> AttributeValue
```
入力: !BringToFront:Boolean !AttributeName:String !Element:UIControl
出力: AttributeValue:String=>AttributeValue
ON ERROR可: RetrieveElementAttributeError

### UIAutomation.GetSelectedCheckboxesInWindow のセレクター: GetCheckboxState, GetSelectedCheckboxes

## UIAutomation.GetSelectedCheckboxesInWindow.GetCheckboxState [A UI]
```
UIAutomation.GetSelectedCheckboxesInWindow.GetCheckboxState Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringToFront: True CheckboxState=> IsChecked
```
入力: !Control:UIControl !BringToFront:Boolean
出力: CheckboxState:Boolean=>IsChecked
ON ERROR可: RetrieveCheckboxStateError
固定: Operation=GetStateOfCheckbox

## UIAutomation.GetSelectedCheckboxesInWindow.GetSelectedCheckboxes [A UI]
```
UIAutomation.GetSelectedCheckboxesInWindow.GetSelectedCheckboxes Control: $'''body''' BringToFront: True SelectedCheckboxes=> SelectedCheckboxes
```
入力: BringToFront:Boolean Control:UIControl
出力: SelectedCheckboxes:List=>
ON ERROR可: RetrieveCheckboxStateError
固定: Operation=GetSelectedCheckboxesInGroup

### UIAutomation.GetSelectedRadiobuttonInWindow のセレクター: GetRadioButtonState, GetSelectedRadiobutton

## UIAutomation.GetSelectedRadiobuttonInWindow.GetRadioButtonState [A UI]
```
UIAutomation.GetSelectedRadiobuttonInWindow.GetRadioButtonState Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringToFront: True RadiobuttonState=> IsSelected
```
入力: !Control:UIControl !BringToFront:Boolean
出力: RadiobuttonState:Boolean=>IsSelected
ON ERROR可: RetrieveRadioButtonStateError
固定: Operation=GetRadiobuttonState

## UIAutomation.GetSelectedRadiobuttonInWindow.GetSelectedRadiobutton [A UI]
```
UIAutomation.GetSelectedRadiobuttonInWindow.GetSelectedRadiobutton Control: $'''body''' BringToFront: True SelectedRadiobutton=> SelectedRadiobutton
```
入力: BringToFront:Boolean Control:UIControl
出力: SelectedRadiobutton:String=>
ON ERROR可: RetrieveRadioButtonStateError
固定: Operation=GetSelectedRadiobuttonInGroup

## UIAutomation.GetUIControl [A UI]
```
UIAutomation.GetUIControl Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] UIControl=> UIControl
```
入力: !Control:UIControl
出力: UIControl:UIControl=>UIControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### UIAutomation.GetWindow のセレクター: Get, GetForegroundWindow, GetUseTimeout

## UIAutomation.GetWindow.Get [A UI]
```
UIAutomation.GetWindow.Get Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] BringWindowToFront: False WindowInstance=> AutomationWindow
```
入力: !Control:UIControl !BringWindowToFront:Boolean
出力: WindowInstance:WindowInstanceHandle=>AutomationWindow
ON ERROR可: GetWindowError
固定: GetWindowMode=SpecificWindow, UseTimeout=False

## UIAutomation.GetWindow.GetForegroundWindow [A]
```
UIAutomation.GetWindow.GetForegroundWindow WindowTitle=> WindowTitle WindowInstance=> AutomationWindow
```
出力: WindowTitle:String=>WindowTitle WindowInstance:WindowInstanceHandle=>AutomationWindow
ON ERROR可: GetWindowError
固定: GetWindowMode=ForegroundWindow

## UIAutomation.GetWindow.GetUseTimeout [A UI]
```
UIAutomation.GetWindow.GetUseTimeout Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] Timeout: 5 BringWindowToFront: False WindowInstance=> AutomationWindow
```
入力: !Control:UIControl !Timeout:Int32 !BringWindowToFront:Boolean
出力: WindowInstance:WindowInstanceHandle=>AutomationWindow
ON ERROR可: GetWindowError
固定: GetWindowMode=SpecificWindow, UseTimeout=True

## UIAutomation.GetWindowDetails [A UI]
```
UIAutomation.GetWindowDetails BringToFront: True ExtractionOperation: UIAutomation.WindowProperties.Title Window: appmask['Window \'KB Test Window\''] Property=> WindowProperty
```
入力: !BringToFront:Boolean !ExtractionOperation:WindowProperties{Title,Text,Bounds,ProcessName} !Window:UIControl
出力: Property:Object=>WindowProperty
ON ERROR可: RetrieveWindowPropertyError

## UIAutomation.HoverOnElement [A UI]
```
UIAutomation.HoverOnElement Element: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !Element:UIControl
ON ERROR可: HoverOverFailedError

## UIAutomation.IfRemoteDesktopIsAvailable [C UI]
```
IF (UIAutomation.IfRemoteDesktopIsAvailable Mode: UIAutomation.CheckRemoteDesktopAvailabilityMode.IsAvailable Control: $'''body''') THEN
```
入力: Mode:CheckRemoteDesktopAvailabilityMode{IsAvailable,IsNotAvailable} Control:UIControl
ON ERROR可: CheckRemoteDesktopAvailabilityError

### UIAutomation.IfWindow のセレクター: IsFocused, IsFocusedByInstanceOrHandle, IsFocusedByTitleClass, IsNotFocused, IsNotFocusedByInstanceOrHandle, IsNotFocusedByTitleClass, IsNotOpen, IsNotOpenByInstanceOrHandle, IsNotOpenByTitleClass, IsOpen, IsOpenByInstanceOrHandle, IsOpenByTitleClass

## UIAutomation.IfWindow.IsFocused [C UI]
```
IF (UIAutomation.IfWindow.IsFocused InstantCheck: False Window: appmask['Window \'KB Test Window\'']) THEN
```
入力: !InstantCheck:Boolean !Window:UIControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=Control, WindowMode=IsFocused

## UIAutomation.IfWindow.IsFocusedByInstanceOrHandle [C]
```
IF (UIAutomation.IfWindow.IsFocusedByInstanceOrHandle WindowInstance: 1 InstantCheck: False) THEN
```
入力: !WindowInstance:Int32 !InstantCheck:Boolean
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=InstanceOrHandle, WindowMode=IsFocused

## UIAutomation.IfWindow.IsFocusedByTitleClass [C]
```
IF (UIAutomation.IfWindow.IsFocusedByTitleClass InstantCheck: False Title: $'''example''' Class: $'''example''') THEN
```
入力: !InstantCheck:Boolean !Title:String !Class:String
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=TitleAndClass, WindowMode=IsFocused

## UIAutomation.IfWindow.IsNotFocused [C UI]
```
IF (UIAutomation.IfWindow.IsNotFocused InstantCheck: False Window: appmask['Window \'KB Test Window\'']) THEN
```
入力: !InstantCheck:Boolean !Window:UIControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=Control, WindowMode=IsNotFocused

## UIAutomation.IfWindow.IsNotFocusedByInstanceOrHandle [C]
```
IF (UIAutomation.IfWindow.IsNotFocusedByInstanceOrHandle WindowInstance: 1 InstantCheck: False) THEN
```
入力: !WindowInstance:Int32 !InstantCheck:Boolean
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=InstanceOrHandle, WindowMode=IsNotFocused

## UIAutomation.IfWindow.IsNotFocusedByTitleClass [C]
```
IF (UIAutomation.IfWindow.IsNotFocusedByTitleClass InstantCheck: False Title: $'''example''' Class: $'''example''') THEN
```
入力: !InstantCheck:Boolean !Title:String !Class:String
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=TitleAndClass, WindowMode=IsNotFocused

## UIAutomation.IfWindow.IsNotOpen [C UI]
```
IF (UIAutomation.IfWindow.IsNotOpen InstantCheck: False Window: appmask['Window \'KB Test Window\'']) THEN
```
入力: !InstantCheck:Boolean !Window:UIControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=Control, WindowMode=IsNotOpen

## UIAutomation.IfWindow.IsNotOpenByInstanceOrHandle [C]
```
IF (UIAutomation.IfWindow.IsNotOpenByInstanceOrHandle WindowInstance: 1 InstantCheck: False) THEN
```
入力: !WindowInstance:Int32 !InstantCheck:Boolean
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=InstanceOrHandle, WindowMode=IsNotOpen

## UIAutomation.IfWindow.IsNotOpenByTitleClass [C]
```
IF (UIAutomation.IfWindow.IsNotOpenByTitleClass InstantCheck: False Title: $'''example''' Class: $'''example''') THEN
```
入力: !InstantCheck:Boolean !Title:String !Class:String
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=TitleAndClass, WindowMode=IsNotOpen

## UIAutomation.IfWindow.IsOpen [C UI]
```
IF (UIAutomation.IfWindow.IsOpen InstantCheck: False Window: appmask['Window \'KB Test Window\'']) THEN
```
入力: !InstantCheck:Boolean !Window:UIControl
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=Control, WindowMode=IsOpen

## UIAutomation.IfWindow.IsOpenByInstanceOrHandle [C]
```
IF (UIAutomation.IfWindow.IsOpenByInstanceOrHandle WindowInstance: 1 InstantCheck: False) THEN
```
入力: !WindowInstance:Int32 !InstantCheck:Boolean
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=InstanceOrHandle, WindowMode=IsOpen

## UIAutomation.IfWindow.IsOpenByTitleClass [C]
```
IF (UIAutomation.IfWindow.IsOpenByTitleClass InstantCheck: False Title: $'''example''' Class: $'''example''') THEN
```
入力: !InstantCheck:Boolean !Title:String !Class:String
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: FindWindowMode=TitleAndClass, WindowMode=IsOpen

### UIAutomation.IfWindowContains のセレクター: WindowContainsElement, WindowContainsElementInState, WindowContainsText, WindowDoesNotContainElement, WindowDoesNotContainText

## UIAutomation.IfWindowContains.WindowContainsElement [C UI]
```
IF (UIAutomation.IfWindowContains.WindowContainsElement InstantCheck: False Element: appmask['Window \'KB Test Window\'']['Button \'OK\'']) THEN
```
入力: !InstantCheck:Boolean !Element:UIControl
ON ERROR可: IfWindowContainsError
固定: CheckElementState=False, ContainsMode=ContainsElement

## UIAutomation.IfWindowContains.WindowContainsElementInState [C UI]
```
IF (UIAutomation.IfWindowContains.WindowContainsElementInState State: UIAutomation.State.Enabled InstantCheck: False Element: appmask['Window \'KB Test Window\'']['Button \'OK\'']) THEN
```
入力: !State:State{Enabled,Disabled} !InstantCheck:Boolean !Element:UIControl
ON ERROR可: IfWindowContainsError
固定: CheckElementState=True, ContainsMode=ContainsElement

## UIAutomation.IfWindowContains.WindowContainsText [C UI]
```
IF (UIAutomation.IfWindowContains.WindowContainsText Text: $'''example''' Window: appmask['Window \'KB Test Window\''] InstantCheck: False) THEN
```
入力: !Text:String !Window:UIControl !InstantCheck:Boolean
ON ERROR可: IfWindowContainsError
固定: ContainsMode=ContainsText

## UIAutomation.IfWindowContains.WindowDoesNotContainElement [C UI]
```
IF (UIAutomation.IfWindowContains.WindowDoesNotContainElement InstantCheck: False Element: appmask['Window \'KB Test Window\'']['Button \'OK\'']) THEN
```
入力: !InstantCheck:Boolean !Element:UIControl
ON ERROR可: IfWindowContainsError
固定: ContainsMode=DoesNotContainElement

## UIAutomation.IfWindowContains.WindowDoesNotContainText [C UI]
```
IF (UIAutomation.IfWindowContains.WindowDoesNotContainText Text: $'''example''' Window: appmask['Window \'KB Test Window\''] InstantCheck: False) THEN
```
入力: !Text:String !Window:UIControl !InstantCheck:Boolean
ON ERROR可: IfWindowContainsError
固定: ContainsMode=DoesNotContainText

### UIAutomation.MoveWindow のセレクター: Move, MoveByInstanceOrHandle, MoveByTitleClass

## UIAutomation.MoveWindow.Move [A UI]
```
UIAutomation.MoveWindow.Move X: 1 Y: 1 Window: appmask['Window \'KB Test Window\'']
```
入力: !X:Int32 !Y:Int32 !Window:UIControl
ON ERROR可: MoveWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.MoveWindow.MoveByInstanceOrHandle [A]
```
UIAutomation.MoveWindow.MoveByInstanceOrHandle WindowInstance: 1 X: 1 Y: 1
```
入力: !WindowInstance:Int32 !X:Int32 !Y:Int32
ON ERROR可: MoveWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.MoveWindow.MoveByTitleClass [A]
```
UIAutomation.MoveWindow.MoveByTitleClass X: 1 Y: 1 Title: $'''example''' Class: $'''example'''
```
入力: !X:Int32 !Y:Int32 !Title:String !Class:String
ON ERROR可: MoveWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

### UIAutomation.PopulateTextField のセレクター: PopulateTextField, SimulatePopulateTextField

## UIAutomation.PopulateTextField.PopulateTextField [A UI]
```
UIAutomation.PopulateTextField.PopulateTextField Text: $'''password''' Mode: UIAutomation.PopulateTextMode.Replace TextField: appmask['Window \'KB Test Window\'']['Edit \'Name\''] ClickType: UIAutomation.PopulateMouseClickType.SingleClick
```
入力: !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append} !TextField:UIControl !ClickType:PopulateMouseClickType{SingleClick,DoubleClick,None}
ON ERROR可: PopulateTextFieldError
固定: Simulate=False

## UIAutomation.PopulateTextField.SimulatePopulateTextField [A UI]
```
UIAutomation.PopulateTextField.SimulatePopulateTextField Text: $'''password''' Mode: UIAutomation.PopulateTextMode.Replace TextField: appmask['Window \'KB Test Window\'']['Edit \'Name\'']
```
入力: !Text:EncryptableObject !Mode:PopulateTextMode{Replace,Append} !TextField:UIControl
ON ERROR可: PopulateTextFieldError
固定: Simulate=True

## UIAutomation.PressButton [A UI]
```
UIAutomation.PressButton Simulate: False Button: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !Simulate:Boolean !Button:UIControl
ON ERROR可: PressButtonError

### UIAutomation.ResizeWindow のセレクター: Resize, ResizeByInstanceOrHandle, ResizeByTitleClass

## UIAutomation.ResizeWindow.Resize [A UI]
```
UIAutomation.ResizeWindow.Resize Width: 1 Height: 1 Window: appmask['Window \'KB Test Window\'']
```
入力: !Width:Int32 !Height:Int32 !Window:UIControl
ON ERROR可: ResizeWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.ResizeWindow.ResizeByInstanceOrHandle [A]
```
UIAutomation.ResizeWindow.ResizeByInstanceOrHandle Width: 1 WindowInstance: 1 Height: 1
```
入力: !Width:Int32 !WindowInstance:Int32 !Height:Int32
ON ERROR可: ResizeWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.ResizeWindow.ResizeByTitleClass [A]
```
UIAutomation.ResizeWindow.ResizeByTitleClass Title: $'''example''' Width: 1 Height: 1 Class: $'''example'''
```
入力: !Title:String !Width:Int32 !Height:Int32 !Class:String
ON ERROR可: ResizeWindowError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

## UIAutomation.SelectMenuOption [A UI]
```
UIAutomation.SelectMenuOption Control: $'''body'''
```
入力: Control:UIControl
ON ERROR可: SelectMenuOptionError

## UIAutomation.SelectRadioButton [A UI]
```
UIAutomation.SelectRadioButton RadioButton: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !RadioButton:UIControl
ON ERROR可: SelectRadioButtonError

## UIAutomation.SelectTab [A UI]
```
UIAutomation.SelectTab Tab: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !Tab:UIControl
ON ERROR可: SelectTabError

## UIAutomation.SetCheckboxState [A UI]
```
UIAutomation.SetCheckboxState CheckboxState: UIAutomation.CheckboxState.Checked Checkbox: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !CheckboxState:CheckboxState{Checked,Unchecked} !Checkbox:UIControl
ON ERROR可: SetCheckboxStateError

### UIAutomation.SetDropDownListValueInWindow のセレクター: ClearDropDownListValue, SetDropDownListValueByIndex, SetDropDownListValueByName

## UIAutomation.SetDropDownListValueInWindow.ClearDropDownListValue [A UI]
```
UIAutomation.SetDropDownListValueInWindow.ClearDropDownListValue DropDownList: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !DropDownList:UIControl
ON ERROR可: SelectOptionInDropDownError
固定: Operation=ClearAllOptions

## UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByIndex [A UI]
```
UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByIndex OptionsIndeces: $'''example''' DropDownList: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !OptionsIndeces:String !DropDownList:UIControl
ON ERROR可: SelectOptionInDropDownError
固定: Operation=SelectOptionsByIndex

## UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByName [A UI]
```
UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByName OptionsNames: $'''example''' UseRegularExpressions: False DropDownList: appmask['Window \'KB Test Window\'']['Button \'OK\'']
```
入力: !OptionsNames:String !UseRegularExpressions:Boolean !DropDownList:UIControl
ON ERROR可: SelectOptionInDropDownError
固定: Operation=SelectOptionsByName

### UIAutomation.SetWindowState のセレクター: SetState, SetStateByInstanceOrHandle, SetStateByTitleClass

## UIAutomation.SetWindowState.SetState [A UI]
```
UIAutomation.SetWindowState.SetState State: UIAutomation.WindowState.Restored Window: appmask['Window \'KB Test Window\'']
```
入力: !State:WindowState{Restored,Maximized,Minimized} !Window:UIControl
ON ERROR可: SetWindowStateError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.SetWindowState.SetStateByInstanceOrHandle [A]
```
UIAutomation.SetWindowState.SetStateByInstanceOrHandle State: UIAutomation.WindowState.Restored WindowInstance: 1
```
入力: !State:WindowState{Restored,Maximized,Minimized} !WindowInstance:Int32
ON ERROR可: SetWindowStateError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.SetWindowState.SetStateByTitleClass [A]
```
UIAutomation.SetWindowState.SetStateByTitleClass State: UIAutomation.WindowState.Restored Title: $'''example''' Class: $'''example'''
```
入力: !State:WindowState{Restored,Maximized,Minimized} !Title:String !Class:String
ON ERROR可: SetWindowStateError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

### UIAutomation.SetWindowVisibility のセレクター: SetVisibility, SetVisibilityByInstanceOrHandle, SetVisibilityByTitleClass

## UIAutomation.SetWindowVisibility.SetVisibility [A UI]
```
UIAutomation.SetWindowVisibility.SetVisibility Visibility: UIAutomation.Visibility.Hidden Window: appmask['Window \'KB Test Window\'']
```
入力: !Visibility:Visibility{Visible,Hidden} !Window:UIControl
ON ERROR可: SetWindowVisibilityError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control

## UIAutomation.SetWindowVisibility.SetVisibilityByInstanceOrHandle [A]
```
UIAutomation.SetWindowVisibility.SetVisibilityByInstanceOrHandle Visibility: UIAutomation.Visibility.Hidden WindowInstance: 1
```
入力: !Visibility:Visibility{Visible,Hidden} !WindowInstance:Int32
ON ERROR可: SetWindowVisibilityError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle

## UIAutomation.SetWindowVisibility.SetVisibilityByTitleClass [A]
```
UIAutomation.SetWindowVisibility.SetVisibilityByTitleClass Title: $'''example''' Visibility: UIAutomation.Visibility.Hidden Class: $'''example'''
```
入力: !Title:String !Visibility:Visibility{Visible,Hidden} !Class:String
ON ERROR可: SetWindowVisibilityError, WindowNotFoundError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass

### UIAutomation.TakeScreenshotOfUIElement のセレクター: TakeScreenshotOfUIElement, TakeScreenshotOfUIElementAndSaveToFile

## UIAutomation.TakeScreenshotOfUIElement.TakeScreenshotOfUIElement [A UI]
```
UIAutomation.TakeScreenshotOfUIElement.TakeScreenshotOfUIElement Control: $'''body'''
```
入力: Control:UIControl
ON ERROR可: SaveImageError, TakeScreenshotError, UIElementNotFoundError
固定: SaveMode=Clipboard

## UIAutomation.TakeScreenshotOfUIElement.TakeScreenshotOfUIElementAndSaveToFile [A UI]
```
UIAutomation.TakeScreenshotOfUIElement.TakeScreenshotOfUIElementAndSaveToFile ImageFormat: UIAutomation.ImageFormat.Bmp Control: appmask['Window \'KB Test Window\'']['Button \'OK\''] ImageFilePath: $'''C:\temp\test.xlsx''' ImageFile=> ImageFile
```
入力: !ImageFormat:ImageFormat{Bmp,Gif,Jpeg,Png,Tiff} !Control:UIControl !ImageFilePath:FileObject
出力: ImageFile:FileObject=>ImageFile
ON ERROR可: SaveImageError, TakeScreenshotError, UIElementNotFoundError
固定: SaveMode=File

## UIAutomation.UseDesktop [A UI]
```
UIAutomation.UseDesktop Control: $'''body''' ClickType: UIAutomation.DesktopClickType.LeftClick LaunchNewApplication: True
```
入力: ClickType:DesktopClickType{LeftClick,RightClick,DoubleClick} LaunchNewApplication:Boolean Control:UIControl
ON ERROR可: TaskbarOperationFailed

## UIAutomation.WaitForRemoteDesktop [W UI]
```
WAIT (UIAutomation.WaitForRemoteDesktop Mode: UIAutomation.CheckRemoteDesktopAvailabilityMode.IsAvailable Control: $'''body''')
```
入力: Mode:CheckRemoteDesktopAvailabilityMode{IsAvailable,IsNotAvailable} Control:UIControl
ON ERROR可: CheckRemoteDesktopAvailabilityError

### UIAutomation.WaitForWindow のセレクター: ToBecomeFocused, ToBecomeFocusedByInstanceOrHandle, ToBecomeFocusedByTitleClass, ToClose, ToCloseByInstanceOrHandle, ToCloseByTitleClass, ToLoseFocus, ToLoseFocusByInstanceOrHandle, ToLoseFocusByTitleClass, ToOpen, ToOpenByInstanceOrHandle, ToOpenByTitleClass

## UIAutomation.WaitForWindow.ToBecomeFocused [W UI]
```
WAIT (UIAutomation.WaitForWindow.ToBecomeFocused Window: appmask['Window \'KB Test Window\''])
```
入力: !Window:UIControl
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control, WindowMode=BecomeFocused

## UIAutomation.WaitForWindow.ToBecomeFocusedByInstanceOrHandle [W]
```
WAIT (UIAutomation.WaitForWindow.ToBecomeFocusedByInstanceOrHandle WindowInstance: 1)
```
入力: !WindowInstance:Int32
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle, WindowMode=BecomeFocused

## UIAutomation.WaitForWindow.ToBecomeFocusedByTitleClass [W]
```
WAIT (UIAutomation.WaitForWindow.ToBecomeFocusedByTitleClass Title: $'''example''' Class: $'''example''')
```
入力: !Title:String !Class:String
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass, WindowMode=BecomeFocused

## UIAutomation.WaitForWindow.ToClose [W UI]
```
WAIT (UIAutomation.WaitForWindow.ToClose Window: appmask['Window \'KB Test Window\''])
```
入力: !Window:UIControl
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control, WindowMode=Close

## UIAutomation.WaitForWindow.ToCloseByInstanceOrHandle [W]
```
WAIT (UIAutomation.WaitForWindow.ToCloseByInstanceOrHandle WindowInstance: 1)
```
入力: !WindowInstance:Int32
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle, WindowMode=Close

## UIAutomation.WaitForWindow.ToCloseByTitleClass [W]
```
WAIT (UIAutomation.WaitForWindow.ToCloseByTitleClass Title: $'''example''' Class: $'''example''')
```
入力: !Title:String !Class:String
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass, WindowMode=Close

## UIAutomation.WaitForWindow.ToLoseFocus [W UI]
```
WAIT (UIAutomation.WaitForWindow.ToLoseFocus Window: appmask['Window \'KB Test Window\''])
```
入力: !Window:UIControl
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control, WindowMode=LoseFocus

## UIAutomation.WaitForWindow.ToLoseFocusByInstanceOrHandle [W]
```
WAIT (UIAutomation.WaitForWindow.ToLoseFocusByInstanceOrHandle WindowInstance: 1)
```
入力: !WindowInstance:Int32
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle, WindowMode=LoseFocus

## UIAutomation.WaitForWindow.ToLoseFocusByTitleClass [W]
```
WAIT (UIAutomation.WaitForWindow.ToLoseFocusByTitleClass Title: $'''example''' Class: $'''example''')
```
入力: !Title:String !Class:String
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass, WindowMode=LoseFocus

## UIAutomation.WaitForWindow.ToOpen [W UI]
```
WAIT (UIAutomation.WaitForWindow.ToOpen FocusWindow: False Window: appmask['Window \'KB Test Window\''])
```
入力: !FocusWindow:Boolean !Window:UIControl
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=Control, WindowMode=Open

## UIAutomation.WaitForWindow.ToOpenByInstanceOrHandle [W]
```
WAIT (UIAutomation.WaitForWindow.ToOpenByInstanceOrHandle WindowInstance: 1 FocusWindow: False)
```
入力: !WindowInstance:Int32 !FocusWindow:Boolean
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=InstanceOrHandle, WindowMode=Open

## UIAutomation.WaitForWindow.ToOpenByTitleClass [W]
```
WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''example''' FocusWindow: False Class: $'''example''')
```
入力: !Title:String !FocusWindow:Boolean !Class:String
ON ERROR可: FocusWindowError, WaitForWindowError, WindowOperationInNonInteractiveModeError
固定: FindWindowMode=TitleAndClass, WindowMode=Open

### UIAutomation.WaitForWindowContent のセレクター: WindowToContainElement, WindowToContainElementInState, WindowToContainText, WindowToNotContainElement, WindowToNotContainText

## UIAutomation.WaitForWindowContent.WindowToContainElement [W UI]
```
WAIT (UIAutomation.WaitForWindowContent.WindowToContainElement Element: appmask['Window \'KB Test Window\'']['Button \'OK\''])
```
入力: !Element:UIControl
ON ERROR可: WaitForWindowContentError
固定: CheckElementState=False, ContainsMode=ContainsElement

## UIAutomation.WaitForWindowContent.WindowToContainElementInState [W UI]
```
WAIT (UIAutomation.WaitForWindowContent.WindowToContainElementInState State: UIAutomation.State.Enabled Element: appmask['Window \'KB Test Window\'']['Button \'OK\''])
```
入力: !State:State{Enabled,Disabled} !Element:UIControl
ON ERROR可: WaitForWindowContentError
固定: CheckElementState=True, ContainsMode=ContainsElement

## UIAutomation.WaitForWindowContent.WindowToContainText [W UI]
```
WAIT (UIAutomation.WaitForWindowContent.WindowToContainText Text: $'''example''' Window: appmask['Window \'KB Test Window\''])
```
入力: !Text:String !Window:UIControl
ON ERROR可: WaitForWindowContentError
固定: ContainsMode=ContainsText

## UIAutomation.WaitForWindowContent.WindowToNotContainElement [W UI]
```
WAIT (UIAutomation.WaitForWindowContent.WindowToNotContainElement Element: appmask['Window \'KB Test Window\'']['Button \'OK\''])
```
入力: !Element:UIControl
ON ERROR可: WaitForWindowContentError
固定: ContainsMode=DoesNotContainElement

## UIAutomation.WaitForWindowContent.WindowToNotContainText [W UI]
```
WAIT (UIAutomation.WaitForWindowContent.WindowToNotContainText Text: $'''example''' Window: appmask['Window \'KB Test Window\''])
```
入力: !Text:String !Window:UIControl
ON ERROR可: WaitForWindowContentError
固定: ContainsMode=DoesNotContainText
