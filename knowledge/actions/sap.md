# SAP GUI automation actions reference for Power Automate for desktop

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/sap （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Our group of actions for SAP automation provides a set of tools to help streamline and automate your SAP workflows. With these actions, you can easily launch the SAP GUI app, create new sessions, select menu items, start and end transactions, and more. With the actions of the SAP automation group, you can easily interact with SAP UI elements by clicking on them, filling in text fields, and extracting their data. Just enter the SAP UI element ID attribute value. If you don't know the ID value, you can use the Power Automate for desktop UI element picker to capture the required SAP element and r

## Launch SAP  `#saplogin`
Open the SAP GUI application and connect to an SAP system.
入力:
- Connection mode: Server description and server connection string = Server description — Specify how to connect to the SAP GUI server.
- Login mode: Manual login and single sign-on (SSO) = Manual login — Specify how to log in to the SAP GUI server, either log in to the server by manually entering your username and password or using single sign-on (SSO).
- Server description(任意): Text value — Specifies SAP system name or IP address for connection.
- Connection string(任意): Text value — Specifies the connection string for the SAP GUI server. The connection string is a unique identifier that specifies the server's name, system number, and other connection details.
- Client: Text value — Specifies the SAP client number for connection.
- Username: Text value — Specifies the SAP user ID for login.
- Password(任意): Text value — Specifies the SAP user password for login.
- Language: Text value — Specifies the SAP login language for the user interface.
- Multiple logon options: Terminate this logon, continue this logon and end any other logons, Continue this logon without ending any other logons in the system = Terminate this logon — Multiple logon options specify how the SAP system behaves when the user tries to log in when they're already logged in.
出力:
- `SAPInstance`: SAP instance — The SAP instance to use with SAP automation actions. The SAP instance refers to the specific SAP window.
- `CurrentSAPLoginTerminated`: Boolean value — Whether the SAP login being performed with the specific action is terminated or not.
- `OtherSAPLoginTerminated`: Boolean value — Whether the other SAP logins are terminated or not.
例外: SAP GUI login action fails

## Attach  `#attachtorunning`
Attach the running SAP GUI application to an SAP instance.
入力:
- Attach mode: Foreground or last activated, Window title = Window title — Specifies the mode for attaching the SAP instance to a window. If Foreground or last activated option is selected, the SAP instance is attached to the SAP session in the foreground. If there's no SAP session in the foreground, it attaches to the last SAP session that was launched and isn't closed yet.
- Window title(任意): Text — Specifies the title of the SAP window to which the instance is attached. The window title can be selected from the drop-down list of existing SAP sessions or entered manually.
出力:
- `SAPInstance`: SAP instance — The SAP instance to use with SAP automation actions. The SAP instance refers to the specific SAP window.
例外: Attach to SAP error

## Create new SAP session  `#createnewsession`
Creates a new SAP session based on the same SAP instance.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
出力:
- `SAPInstance`: SAP instance — The SAP instance to use with SAP automation actions. The SAP instance refers to the specific SAP window.
例外: Create new SAP session action fails

## Select SAP navigation item  `#selectnavigationbaritem`
Select an SAP menu item in the application toolbar of the SAP window.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. Define this variable in a previous SAP login action.
- Navigation item name: Text value — The name of the item in the navigation toolbar to select, such as 'System'. You can also specify an option from a submenu by using the '>' symbol to indicate the parent-child relationship. For example, 'Program > Execute' means that the 'Execute' option, which is part of the submenu under 'Program', is selected.
例外: SAP GUI select navigation toolbar item error

## Select SAP menu item  `#sapselectmenuitem`
Select an SAP menu item in the window tool bar. Enter the name of the item in the respective input parameter manually, in the same language as the SAP GUI screen is being displayed.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
- Menu item name: Text value — The name of the menu item in the toolbar to be selected, such as ‘Save’. Insert the name of the menu item as it's displayed in the machine’s SAP installation.
例外: Select SAP menu item action fails

## Close SAP connection  `#closesapconnection`
Close the SAP connection of the selected SAP instance. Note that all instances related to the specific connection will be terminated.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
例外: Close SAP session action fails

## Start SAP transaction  `#starttransaction`
Opens a specific transaction code in existing session.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
- Transaction code: Text value — The transaction code that you desire to execute.
例外: Start SAP transaction action fails

## End SAP transaction  `#endtransaction`
Closes the SAP transaction in a specific SAP instance and returns to the SAP easy access menu. An SAP transaction must be started before for the specific SAP session.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
例外: End SAP transaction action fails

## Click SAP UI element  `#clicksapguielement`
Interacts through click action on any UI element of an SAP window.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
- Element type: Basic SAP element, Checkbox, Label, Drop-down list, Grid element = Basic SAP element — Select the SAP element type you want to interact with. The ‘Click SAP element’ option performs a click action on any SAP element like buttons, radio buttons, tabs, text fields, or trees.
- SAP element ID: Numeric — The SAP element’s ID. This parameter determines the UI element in SAP that action interacts with. You can use the below button for indication the SAP UI element in the SAP screen or insert the value manually.
- SAP element ID: Numeric — The SAP element’s ID. This parameter determines the UI element in SAP that action interacts with. You can use the below button for indication the SAP UI element in the SAP screen or insert the value manually.
- Set SAP checkbox state to(任意): Checked, Unchecked = Checked — Specify whether the checkbox becomes checked or unchecked.
- SAP label operation(任意): Expand, Collapse, Choose = Expand — Specify whether to expand or collapse the SAP label.
- Drop-down option value(任意): Text value — Specify the drop-down option is selected.
- SAP grid element(任意): Cell, Row, Header, List, Button, Toolbar Button, Checkbox, Radio Button = Cell — Select the SAP grid element type you want to interact with.
例外: Click Sap GUI Element error

## Get details of SAP UI element  `#getsapelementdetail`
Gets the value of an SAP UI element's attribute in an SAP window.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
- SAP element ID: Numeric — The SAP element’s ID. This parameter determines the UI element in SAP that action interacts with. You can use the below button for indication the SAP UI element in the SAP screen or insert the value manually.
- Attribute name: Text value = Own text — The attribute whose value is retrieved.
出力:
- AttributeValue: Text value — The value of the SAP UI element's attribute.
例外: Get SAP element detail error

## Populate SAP text field in element  `#populatetextfield`
Fills a text box in an SAP window with the specified text.
入力:
- `SAPInstance`: SAP instance — Select the variable that holds the SAP instance you want to work with. This variable should be defined in a previous SAP login action.
- SAP element ID: Numeric — The SAP element’s ID. This parameter determines the UI element in SAP that action interacts with. You can use the below button for indication the SAP UI element in the SAP screen or insert the value manually.
- Text to fill in: Direct encrypted input or Text value — The text to fill in the SAP text field
- If field isn't empty(任意): Replace text, Append text = Replace text — Specify whether to replace existing content, or to append.
例外: Populate Sap Text Field Value error
