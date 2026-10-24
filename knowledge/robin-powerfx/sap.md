# Robin: SAP

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### SAP.AttachToRunning のセレクター: AttachToRunningSapByActiveSession, AttachToRunningSapByWindowTitle

## SAP.AttachToRunning.AttachToRunningSapByActiveSession [A]
```
SAP.AttachToRunning.AttachToRunningSapByActiveSession SapInstance=> SapInstance
```
出力: SapInstance:SapInstanceHandle=>SapInstance
ON ERROR可: AttachToRunningSapActionError
固定: AttachMode=Active

## SAP.AttachToRunning.AttachToRunningSapByWindowTitle [A]
```
SAP.AttachToRunning.AttachToRunningSapByWindowTitle WindowTitle: $fx'example' SapInstance=> SapInstance2
```
入力: WindowTitle:String
出力: SapInstance:SapInstanceHandle=>
ON ERROR可: AttachToRunningSapActionError
固定: AttachMode=WindowTitle

### SAP.ClickSapGuiElement のセレクター: BasicElementSelected, CheckBoxSelected, ComboBoxSelected, GridCellCheckboxSelected, GridCellListSelected, GridCellSelected, LabelSelected

## SAP.ClickSapGuiElement.BasicElementSelected [A]
```
SAP.ClickSapGuiElement.BasicElementSelected SapInstance: SapInstance ElementId: $fx'example'
```
入力: ElementId:String SapInstance:SapInstanceHandle
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=BasicSapElement

## SAP.ClickSapGuiElement.CheckBoxSelected [A]
```
SAP.ClickSapGuiElement.CheckBoxSelected SapInstance: SapInstance2 ElementId: $fx'example' SapCheckBoxAction: SAP.SapCheckBoxAction.Check
```
入力: !SapInstance:SapInstanceHandle !ElementId:String !SapCheckBoxAction:SapCheckBoxAction{Check,Uncheck}
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=CheckBox

## SAP.ClickSapGuiElement.ComboBoxSelected [A]
```
SAP.ClickSapGuiElement.ComboBoxSelected SapInstance: SapInstance2 ComboboxValue: $fx'example' ElementId: $fx'example'
```
入力: !SapInstance:SapInstanceHandle !ComboboxValue:String !ElementId:String
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=SapComboBox

## SAP.ClickSapGuiElement.GridCellCheckboxSelected [A]
```
SAP.ClickSapGuiElement.GridCellCheckboxSelected SapInstance: SapInstance2 ElementId: $fx'example' SapCheckBoxAction: SAP.SapCheckBoxAction.Check
```
入力: !SapInstance:SapInstanceHandle !ElementId:String !SapCheckBoxAction:SapCheckBoxAction{Check,Uncheck}
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=SapGridElement, SapGridElementType=Checkbox

## SAP.ClickSapGuiElement.GridCellListSelected [A]
```
SAP.ClickSapGuiElement.GridCellListSelected SapInstance: SapInstance2 ComboboxValue: $fx'example' ElementId: $fx'example'
```
入力: !SapInstance:SapInstanceHandle !ComboboxValue:String !ElementId:String
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=SapGridElement, SapGridElementType=ValueList

## SAP.ClickSapGuiElement.GridCellSelected [A]
```
SAP.ClickSapGuiElement.GridCellSelected SapGridElementType: SAP.SapGridElementType.Normal SapInstance: SapInstance2 ElementId: $fx'example'
```
入力: !SapGridElementType:SapGridElementType{Normal,Row,Header,ValueList,Button,ToolbarButton,Checkbox,RadioButton} !SapInstance:SapInstanceHandle !ElementId:String
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=SapGridElement

## SAP.ClickSapGuiElement.LabelSelected [A]
```
SAP.ClickSapGuiElement.LabelSelected SapInstance: SapInstance2 SapLabelAction: SAP.SapLabelAction.Expand ElementId: $fx'example'
```
入力: !SapInstance:SapInstanceHandle !SapLabelAction:SapLabelAction{Expand,Collapse,Choose} !ElementId:String
ON ERROR可: ClickSapGuiElementActionError
固定: SapElementType=SapLabel

## SAP.CloseSapConnection [A]
```
SAP.CloseSapConnection SapInstance: SapInstance CloseSapLogonOnLastConnection: True
```
入力: CloseSapLogonOnLastConnection:Boolean SapInstance:SapInstanceHandle
ON ERROR可: CloseSapConnectionActionError

## SAP.CreateNewSession [A]
```
SAP.CreateNewSession SapInstance: SapInstance SapInstanceOutput=> SapInstance
```
入力: SapInstance:SapInstanceHandle
出力: SapInstanceOutput:SapInstanceHandle=>
ON ERROR可: CreateNewSapSession

## SAP.EndTransaction [A]
```
SAP.EndTransaction SapInstance: SapInstance
```
入力: SapInstance:SapInstanceHandle
ON ERROR可: EndTransactionActionError

## SAP.GetSapElementDetail [A]
```
SAP.GetSapElementDetail SapInstance: SapInstance ElementId: $fx'example' AttributeName: $fx'Own Text' AttributeValue=> SAPAttributeValue
```
入力: SapInstance:SapInstanceHandle ElementId:String AttributeName:String
出力: AttributeValue:String=>
ON ERROR可: GetSapElementDetailActionError

## SAP.PopulateTextField [A]
```
SAP.PopulateTextField SapInstance: SapInstance ElementId: $fx'example' TextValue: $fx'example' PopulateTextFieldMode: SAP.PopulateTextFieldMode.Replace
```
入力: SapInstance:SapInstanceHandle ElementId:String TextValue:String PopulateTextFieldMode:PopulateTextFieldMode{Replace,Append}
ON ERROR可: PopulateTextFieldActionError

### SAP.SapLogin のセレクター: SapLogInAdvancedConnectionOptionMultiple, SapLogInAdvancedConnectionOptionSingle, SapLogInAdvancedConnectionOptionTerminate, SapLogInOptionMultiple, SapLogInOptionSingle, SapLogInOptionTerminate, SapSSOLogInAdvancedConnectionOptionMultiple, SapSSOLogInAdvancedConnectionOptionSingle, SapSSOLogInAdvancedConnectionOptionTerminate, SapSSOLogInOptionMultiple, SapSSOLogInOptionSingle, SapSSOLogInOptionTerminate

## SAP.SapLogin.SapLogInAdvancedConnectionOptionMultiple [A]
```
SAP.SapLogin.SapLogInAdvancedConnectionOptionMultiple Password: $fx'password' Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance
```
入力: !Password:EncryptableObject !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Multiple, LoginMode=Normal

## SAP.SapLogin.SapLogInAdvancedConnectionOptionSingle [A]
```
SAP.SapLogin.SapLogInAdvancedConnectionOptionSingle Password: $fx'password' Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance OtherSapLoginTerminated=> OtherSapLoginTerminated
```
入力: !Password:EncryptableObject !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance OtherSapLoginTerminated:Boolean=>OtherSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Single, LoginMode=Normal

## SAP.SapLogin.SapLogInAdvancedConnectionOptionTerminate [A]
```
SAP.SapLogin.SapLogInAdvancedConnectionOptionTerminate Password: $fx'password' Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance CurrentSapLoginTerminated=> CurrentSapLoginTerminated
```
入力: !Password:EncryptableObject !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance CurrentSapLoginTerminated:Boolean=>CurrentSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Terminate, LoginMode=Normal

## SAP.SapLogin.SapLogInOptionMultiple [A]
```
SAP.SapLogin.SapLogInOptionMultiple Password: $fx'password' Username: $fx'example' Client: $fx'example' Language: $fx'example' Description: $fx'example' SapInstance=> SapInstance
```
入力: !Password:EncryptableObject !Username:String !Client:String !Language:String !Description:String
出力: SapInstance:SapInstanceHandle=>SapInstance
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Multiple, LoginMode=Normal

## SAP.SapLogin.SapLogInOptionSingle [A]
```
SAP.SapLogin.SapLogInOptionSingle Password: $fx'password' Username: $fx'example' Client: $fx'example' Language: $fx'example' Description: $fx'example' SapInstance=> SapInstance OtherSapLoginTerminated=> OtherSapLoginTerminated
```
入力: !Password:EncryptableObject !Username:String !Client:String !Language:String !Description:String
出力: SapInstance:SapInstanceHandle=>SapInstance OtherSapLoginTerminated:Boolean=>OtherSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Single, LoginMode=Normal

## SAP.SapLogin.SapLogInOptionTerminate [A]
```
SAP.SapLogin.SapLogInOptionTerminate Description: $fx'example' Client: $fx'example' Username: $fx'example' Password: $fx'password' Language: $fx'example' SapInstance=> SapInstance CurrentSapLoginTerminated=> CurrentSapLoginTerminated
```
入力: Client:String Description:String Language:String Password:EncryptableObject Username:String
出力: CurrentSapLoginTerminated:Boolean=> SapInstance:SapInstanceHandle=>
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Terminate, LoginMode=Normal

## SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionMultiple [A]
```
SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionMultiple Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance
```
入力: !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Multiple, LoginMode=SSO

## SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionSingle [A]
```
SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionSingle Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance OtherSapLoginTerminated=> OtherSapLoginTerminated
```
入力: !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance OtherSapLoginTerminated:Boolean=>OtherSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Single, LoginMode=SSO

## SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionTerminate [A]
```
SAP.SapLogin.SapSSOLogInAdvancedConnectionOptionTerminate Username: $fx'example' Server: $fx'example' Client: $fx'example' Language: $fx'example' SapInstance=> SapInstance CurrentSapLoginTerminated=> CurrentSapLoginTerminated
```
入力: !Username:String !Server:String !Client:String !Language:String
出力: SapInstance:SapInstanceHandle=>SapInstance CurrentSapLoginTerminated:Boolean=>CurrentSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=ConnectionString, LogInOption=Terminate, LoginMode=SSO

## SAP.SapLogin.SapSSOLogInOptionMultiple [A]
```
SAP.SapLogin.SapSSOLogInOptionMultiple Username: $fx'example' Client: $fx'example' Language: $fx'example' Description: $fx'example' SapInstance=> SapInstance
```
入力: !Username:String !Client:String !Language:String !Description:String
出力: SapInstance:SapInstanceHandle=>SapInstance
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Multiple, LoginMode=SSO

## SAP.SapLogin.SapSSOLogInOptionSingle [A]
```
SAP.SapLogin.SapSSOLogInOptionSingle Username: $fx'example' Client: $fx'example' Language: $fx'example' Description: $fx'example' SapInstance=> SapInstance OtherSapLoginTerminated=> OtherSapLoginTerminated
```
入力: !Username:String !Client:String !Language:String !Description:String
出力: SapInstance:SapInstanceHandle=>SapInstance OtherSapLoginTerminated:Boolean=>OtherSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Single, LoginMode=SSO

## SAP.SapLogin.SapSSOLogInOptionTerminate [A]
```
SAP.SapLogin.SapSSOLogInOptionTerminate Username: $fx'example' Client: $fx'example' Language: $fx'example' Description: $fx'example' SapInstance=> SapInstance CurrentSapLoginTerminated=> CurrentSapLoginTerminated
```
入力: !Username:String !Client:String !Language:String !Description:String
出力: SapInstance:SapInstanceHandle=>SapInstance CurrentSapLoginTerminated:Boolean=>CurrentSapLoginTerminated
ON ERROR可: SAPLoginActionError
固定: ConnectionMode=Description, LogInOption=Terminate, LoginMode=SSO

## SAP.SapSelectMenuItem [A]
```
SAP.SapSelectMenuItem SapInstance: SapInstance MenuItemName: $fx'example'
```
入力: SapInstance:SapInstanceHandle MenuItemName:String
ON ERROR可: SapSelectMenuItemActionError

## SAP.SelectNavigationBarItem [A]
```
SAP.SelectNavigationBarItem SapInstance: SapInstance ItemName: $fx'example'
```
入力: ItemName:String SapInstance:SapInstanceHandle
ON ERROR可: SapSelectNavigationItemActionError

## SAP.StartTransaction [A]
```
SAP.StartTransaction SapInstance: SapInstance TransactionCode: $fx'example'
```
入力: SapInstance:SapInstanceHandle TransactionCode:String
ON ERROR可: StartTransactionActionError
