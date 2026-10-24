# Robin: Display

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Display.InputDialog [A]
```
Display.InputDialog InputType: Display.InputType.SingleLine IsTopMost: False DefaultValue: $'''example''' Message: $'''example''' Title: $'''example''' UserInput=> UserInput ButtonPressed=> ButtonPressed
```
入力: DefaultValue:String InputType:InputType{SingleLine,Password,Multiline} IsTopMost:Boolean Message:String Title:String
出力: ButtonPressed:String=> UserInput:String=>
ON ERROR可: DisplayInputDialogError, DisplayInputDialogInNonInteractiveModeError

### Display.SelectDateDialog のセレクター: SelectDate, SelectDateRange

## Display.SelectDateDialog.SelectDate [A]
```
Display.SelectDateDialog.SelectDate DateDialogFormat: Display.DateDialogFormat.DateOnly IsTopMost: False DefaultValue: $'''2025-01-01''' Message: $'''example''' Title: $'''example''' SelectedDate=> SelectedDate ButtonPressed=> ButtonPressed
```
入力: DateDialogFormat:DateDialogFormat{DateOnly,DateAndTime} DefaultValue:Nullable IsTopMost:Boolean Message:String Title:String
出力: ButtonPressed:String=> SelectedDate:DateTime=>
ON ERROR可: SelectDateDialogError, SelectDateDialogInNonInteractiveModeError
固定: DateDialogType=SingleDate

## Display.SelectDateDialog.SelectDateRange [A]
```
Display.SelectDateDialog.SelectDateRange IsTopMost: False Message: $'''example''' Title: $'''example''' DefaultValueForSecondDate: $'''2025-01-01''' DateDialogFormat: Display.DateDialogFormat.DateOnly DefaultValue: $'''2025-01-01''' SelectedDate=> SelectedDate SecondSelectedDate=> SecondSelectedDate ButtonPressed=> ButtonPressed
```
入力: !IsTopMost:Boolean Message:String Title:String DefaultValueForSecondDate:Nullable<DateTime> !DateDialogFormat:DateDialogFormat{DateOnly,DateAndTime} DefaultValue:Nullable<DateTime>
出力: SelectedDate:DateTime=>SelectedDate SecondSelectedDate:DateTime=>SecondSelectedDate ButtonPressed:String=>ButtonPressed
ON ERROR可: SelectDateDialogError, SelectDateDialogInNonInteractiveModeError
固定: DateDialogType=DateRange

### Display.SelectFileDialog のセレクター: SelectFile, SelectFiles

## Display.SelectFileDialog.SelectFile [A]
```
Display.SelectFileDialog.SelectFile IsTopMost: False CheckIfFileExists: False FileFilter: $'''example''' InitialDirectory: $'''C:\temp''' Title: $'''example''' SelectedFile=> SelectedFile ButtonPressed=> ButtonPressed
```
入力: CheckIfFileExists:Boolean FileFilter:String InitialDirectory:FolderObject IsTopMost:Boolean Title:String
出力: ButtonPressed:String=> SelectedFile:FileObject=>
ON ERROR可: SelectFileDialogError, SelectFileDialogInNonInteractiveModeError
固定: AllowMultiple=False

## Display.SelectFileDialog.SelectFiles [A]
```
Display.SelectFileDialog.SelectFiles InitialDirectory: $'''C:\temp''' IsTopMost: False Title: $'''example''' CheckIfFileExists: False FileFilter: $'''example''' SelectedFiles=> SelectedFiles ButtonPressed=> ButtonPressed
```
入力: InitialDirectory:FolderObject !IsTopMost:Boolean Title:String !CheckIfFileExists:Boolean FileFilter:String
出力: SelectedFiles:List<FileObject>=>SelectedFiles ButtonPressed:String=>ButtonPressed
ON ERROR可: SelectFileDialogError, SelectFileDialogInNonInteractiveModeError
固定: AllowMultiple=True

## Display.SelectFolder [A]
```
Display.SelectFolder IsTopMost: False Description: $'''example''' InitialDirectory: $'''C:\temp''' SelectedFolder=> SelectedFolder ButtonPressed=> ButtonPressed
```
入力: Description:String InitialDirectory:FolderObject IsTopMost:Boolean
出力: ButtonPressed:String=> SelectedFolder:FolderObject=>
ON ERROR可: SelectFolderDialogError, SelectFolderDialogInNonInteractiveModeError

### Display.SelectFromListDialog のセレクター: SelectFromList, SelectFromListOrInsertValue, SelectItemsFromList

## Display.SelectFromListDialog.SelectFromList [A]
```
Display.SelectFromListDialog.SelectFromList List: $'''sample''' IsTopMost: False AllowEmpty: False Message: $'''example''' Title: $'''example''' SelectedItem=> SelectedItem SelectedIndex=> SelectedIndex ButtonPressed=> ButtonPressed
```
入力: AllowEmpty:Boolean IsTopMost:Boolean List:Object Message:String Title:String
出力: ButtonPressed:String=> SelectedIndex:Int32=> SelectedItem:String=>
ON ERROR可: SelectDialogError, SelectDialogInNonInteractiveModeError
固定: LimitToList=True, AllowMultiple=False

## Display.SelectFromListDialog.SelectFromListOrInsertValue [A]
```
Display.SelectFromListDialog.SelectFromListOrInsertValue Message: $'''example''' List: $'''sample''' Title: $'''example''' IsTopMost: False SelectedItem=> SelectedItem ButtonPressed=> ButtonPressed SelectedIndex=> SelectedIndex
```
入力: Message:String !List:Object Title:String !IsTopMost:Boolean
出力: SelectedItem:String=>SelectedItem ButtonPressed:String=>ButtonPressed SelectedIndex:Int32=>SelectedIndex
ON ERROR可: SelectDialogError, SelectDialogInNonInteractiveModeError
固定: LimitToList=False

## Display.SelectFromListDialog.SelectItemsFromList [A]
```
Display.SelectFromListDialog.SelectItemsFromList Message: $'''example''' List: $'''sample''' Title: $'''example''' PreSelectItemsWithPlus: False AllowEmpty: False IsTopMost: False SelectedItems=> SelectedItems SelectedIndexes=> SelectedIndexes ButtonPressed=> ButtonPressed
```
入力: Message:String !List:Object Title:String !PreSelectItemsWithPlus:Boolean !AllowEmpty:Boolean !IsTopMost:Boolean
出力: SelectedItems:List<String>=>SelectedItems SelectedIndexes:List<Int32>=>SelectedIndexes ButtonPressed:String=>ButtonPressed
ON ERROR可: SelectDialogError, SelectDialogInNonInteractiveModeError
固定: LimitToList=True, AllowMultiple=True

## Display.ShowCustomDialog [A]
```
Display.ShowCustomDialog CardTemplateJson: $'''example''' CustomFormData=> CustomFormData ButtonPressed=> ButtonPressed
```
入力: !CardTemplateJson:String
出力: CustomFormData:CustomObject=>CustomFormData ButtonPressed:String=>ButtonPressed
ON ERROR可: ShowCustomDialogError

### Display.ShowMessageDialog のセレクター: ShowMessage, ShowMessageWithTimeout

## Display.ShowMessageDialog.ShowMessage [A]
```
Display.ShowMessageDialog.ShowMessage Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False Message: $'''example''' Title: $'''example''' ButtonPressed=> ButtonPressed
```
入力: Buttons:Buttons{OK,OKCancel,YesNo,YesNoCancel,AbortRetryIgnore,RetryCancel} DefaultButton:DefaultButton{Button1,Button2,Button3} Icon:Icon{None,Information,Question,Warning,ErrorIcon} IsTopMost:Boolean Message:String Title:String
出力: ButtonPressed:String=>
ON ERROR可: ShowMessageDialogError, ShowMessageDialogInNonInteractiveModeError
固定: CloseAutomatically=False

## Display.ShowMessageDialog.ShowMessageWithTimeout [A]
```
Display.ShowMessageDialog.ShowMessageWithTimeout Message: $'''example''' IsTopMost: False Title: $'''example''' Timeout: 3 Buttons: Display.Buttons.OK Icon: Display.Icon.None DefaultButton: Display.DefaultButton.Button1 ButtonPressed=> ButtonPressed
```
入力: Message:String !IsTopMost:Boolean Title:String !Timeout:Int32 !Buttons:Buttons{OK,OKCancel,YesNo,YesNoCancel,AbortRetryIgnore,RetryCancel} !Icon:Icon{None,Information,Question,Warning,ErrorIcon} !DefaultButton:DefaultButton{Button1,Button2,Button3}
出力: ButtonPressed:String=>ButtonPressed
ON ERROR可: ShowMessageDialogError, ShowMessageDialogInNonInteractiveModeError
固定: CloseAutomatically=True
