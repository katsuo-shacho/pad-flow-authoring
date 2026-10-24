# Robin: System

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Scripting.RunDOSCommand のセレクター: RunDOSCommand, RunDOSCommandAndFailOnTimeout, RunDOSCommandWithCodePage, RunDOSCommandWithCodePageAndFailOnTimeout

## Scripting.RunDOSCommand.RunDOSCommand [A]
```
Scripting.RunDOSCommand.RunDOSCommand DOSCommandOrApplication: $'''C:\temp\test.xlsx''' WorkingDirectory: $'''C:\temp''' StandardOutput=> CommandOutput StandardError=> CommandErrorOutput ExitCode=> CommandExitCode
```
入力: DOSCommandOrApplication:FileObject WorkingDirectory:FolderObject
出力: ExitCode:Int32=> StandardError:String=> StandardOutput:String=>
ON ERROR可: ExecuteCommandOrConsoleApplicationError, ScriptTimeoutError
固定: ChangeCodePage=False, FailOnTimeout=False

## Scripting.RunDOSCommand.RunDOSCommandAndFailOnTimeout [A]
```
Scripting.RunDOSCommand.RunDOSCommandAndFailOnTimeout WorkingDirectory: $'''C:\temp''' Timeout: 10 DOSCommandOrApplication: $'''C:\temp\test.xlsx''' StandardOutput=> CommandOutput StandardError=> CommandErrorOutput ExitCode=> CommandExitCode
```
入力: WorkingDirectory:FolderObject !Timeout:Int32 !DOSCommandOrApplication:FileObject
出力: StandardOutput:String=>CommandOutput StandardError:String=>CommandErrorOutput ExitCode:Int32=>CommandExitCode
ON ERROR可: ExecuteCommandOrConsoleApplicationError, ScriptTimeoutError
固定: ChangeCodePage=False, FailOnTimeout=True

## Scripting.RunDOSCommand.RunDOSCommandWithCodePage [A]
```
Scripting.RunDOSCommand.RunDOSCommandWithCodePage WorkingDirectory: $'''C:\temp''' DOSCommandOrApplication: $'''C:\temp\test.xlsx''' Encoding: System.Encoding.utf_8 StandardOutput=> CommandOutput StandardError=> CommandErrorOutput ExitCode=> CommandExitCode
```
入力: WorkingDirectory:FolderObject !DOSCommandOrApplication:FileObject !Encoding:Encoding{IBM037,IBM437,IBM500,ASMO_708,DOS_720,ibm737,ibm775,ibm850,ibm852,IBM855,ibm857,IBM00858,IBM860,ibm861,DOS_862,IBM863,IBM864,IBM865,cp866,ibm869,IBM870,windows_874,cp875,shift_jis,gb2312,ks_c_5601_1987,big5,IBM1026,IBM01047,IBM01140,IBM01141,IBM01142,IBM01143,IBM01144,IBM01145,IBM01146,IBM01147,IBM01148,IBM01149,utf_16,utf_16BE,windows_1250,windows_1251,Windows_1252,windows_1253,windows_1254,windows_1255,windows_1256,windows_1257,windows_1258,Johab,macintosh,x_mac_japanese,x_mac_chinesetrad,x_mac_korean,x_mac_arabic,x_mac_hebrew,x_mac_greek,x_mac_cyrillic,x_mac_chinesesimp,x_mac_romanian,x_mac_ukrainian,x_mac_thai,x_mac_ce,x_mac_icelandic,x_mac_turkish,x_mac_croatian,utf_32,utf_32BE,x_Chinese_CNS,x_cp20001,x_Chinese_Eten,x_cp20003,x_cp20004,x_cp20005,x_IA5,x_IA5_German,x_IA5_Swedish,x_IA5_Norwegian,us_ascii,x_cp20261,x_cp20269,IBM273,IBM277,IBM278,IBM280,IBM284,IBM285,IBM290,IBM297,IBM420,IBM423,IBM424,x_EBCDIC_KoreanExtended,IBM_Thai,koi8_r,IBM871,IBM880,IBM905,IBM00924,EUC_JP_20932,x_cp20936,x_cp20949,cp1025,koi8_u,iso_8859_1,iso_8859_2,iso_8859_3,iso_8859_4,iso_8859_5,iso_8859_6,iso_8859_7,iso_8859_8,iso_8859_9,iso_8859_13,iso_8859_15,x_Europa,iso_8859_8_i,iso_2022_jp_50220,csISO2022JP,iso_2022_jp_50222,iso_2022_kr,x_cp50227,euc_jp_51932,EUC_CN,euc_kr,hz_gb_2312,GB18030,x_iscii_de,x_iscii_be,x_iscii_ta,x_iscii_te,x_iscii_as,x_iscii_or,x_iscii_ka,x_iscii_ma,x_iscii_gu,x_iscii_pa,utf_7,utf_8}
出力: StandardOutput:String=>CommandOutput StandardError:String=>CommandErrorOutput ExitCode:Int32=>CommandExitCode
ON ERROR可: ExecuteCommandOrConsoleApplicationError, ScriptTimeoutError
固定: ChangeCodePage=True, FailOnTimeout=False

## Scripting.RunDOSCommand.RunDOSCommandWithCodePageAndFailOnTimeout [A]
```
Scripting.RunDOSCommand.RunDOSCommandWithCodePageAndFailOnTimeout WorkingDirectory: $'''C:\temp''' Timeout: 10 DOSCommandOrApplication: $'''C:\temp\test.xlsx''' Encoding: System.Encoding.utf_8 StandardOutput=> CommandOutput StandardError=> CommandErrorOutput ExitCode=> CommandExitCode
```
入力: WorkingDirectory:FolderObject !Timeout:Int32 !DOSCommandOrApplication:FileObject !Encoding:Encoding{IBM037,IBM437,IBM500,ASMO_708,DOS_720,ibm737,ibm775,ibm850,ibm852,IBM855,ibm857,IBM00858,IBM860,ibm861,DOS_862,IBM863,IBM864,IBM865,cp866,ibm869,IBM870,windows_874,cp875,shift_jis,gb2312,ks_c_5601_1987,big5,IBM1026,IBM01047,IBM01140,IBM01141,IBM01142,IBM01143,IBM01144,IBM01145,IBM01146,IBM01147,IBM01148,IBM01149,utf_16,utf_16BE,windows_1250,windows_1251,Windows_1252,windows_1253,windows_1254,windows_1255,windows_1256,windows_1257,windows_1258,Johab,macintosh,x_mac_japanese,x_mac_chinesetrad,x_mac_korean,x_mac_arabic,x_mac_hebrew,x_mac_greek,x_mac_cyrillic,x_mac_chinesesimp,x_mac_romanian,x_mac_ukrainian,x_mac_thai,x_mac_ce,x_mac_icelandic,x_mac_turkish,x_mac_croatian,utf_32,utf_32BE,x_Chinese_CNS,x_cp20001,x_Chinese_Eten,x_cp20003,x_cp20004,x_cp20005,x_IA5,x_IA5_German,x_IA5_Swedish,x_IA5_Norwegian,us_ascii,x_cp20261,x_cp20269,IBM273,IBM277,IBM278,IBM280,IBM284,IBM285,IBM290,IBM297,IBM420,IBM423,IBM424,x_EBCDIC_KoreanExtended,IBM_Thai,koi8_r,IBM871,IBM880,IBM905,IBM00924,EUC_JP_20932,x_cp20936,x_cp20949,cp1025,koi8_u,iso_8859_1,iso_8859_2,iso_8859_3,iso_8859_4,iso_8859_5,iso_8859_6,iso_8859_7,iso_8859_8,iso_8859_9,iso_8859_13,iso_8859_15,x_Europa,iso_8859_8_i,iso_2022_jp_50220,csISO2022JP,iso_2022_jp_50222,iso_2022_kr,x_cp50227,euc_jp_51932,EUC_CN,euc_kr,hz_gb_2312,GB18030,x_iscii_de,x_iscii_be,x_iscii_ta,x_iscii_te,x_iscii_as,x_iscii_or,x_iscii_ka,x_iscii_ma,x_iscii_gu,x_iscii_pa,utf_7,utf_8}
出力: StandardOutput:String=>CommandOutput StandardError:String=>CommandErrorOutput ExitCode:Int32=>CommandExitCode
ON ERROR可: ExecuteCommandOrConsoleApplicationError, ScriptTimeoutError
固定: ChangeCodePage=True, FailOnTimeout=True

## Scripting.RunDotNetScript [A]
```
Scripting.RunDotNetScript Language: System.DotNetActionLanguageType.CSharp Imports: $'''example''' ReferenceRootPath: $'''C:\temp''' Script: $'''example'''
```
入力: Imports:String ReferenceRootPath:FolderObject Script:String Language:DotNetActionLanguageType{CSharp,VisualBasic}
ON ERROR可: RunDotNetScriptError

### Scripting.RunJavascript のセレクター: RunJavascript, RunJavascriptAndFailOnTimeout

## Scripting.RunJavascript.RunJavascript [A]
```
Scripting.RunJavascript.RunJavascript JavascriptCode: $'''''' ScriptOutput=> JavascriptOutput ScriptError=> ScriptError
```
入力: JavascriptCode:String
出力: ScriptError:String=> ScriptOutput:String=>
ON ERROR可: ScriptTimeoutError
固定: FailOnTimeout=False

## Scripting.RunJavascript.RunJavascriptAndFailOnTimeout [A]
```
Scripting.RunJavascript.RunJavascriptAndFailOnTimeout Timeout: 10 JavascriptCode: $'''example''' ScriptOutput=> JavascriptOutput ScriptError=> ScriptError
```
入力: !Timeout:Int32 !JavascriptCode:String
出力: ScriptOutput:String=>JavascriptOutput ScriptError:String=>ScriptError
ON ERROR可: ScriptTimeoutError
固定: FailOnTimeout=True

### Scripting.RunPowershellScript のセレクター: RunScript, RunScriptAndFailOnTimeout

## Scripting.RunPowershellScript.RunScript [A]
```
Scripting.RunPowershellScript.RunScript Script: $'''''' ScriptOutput=> PowershellOutput ScriptError=> ScriptError
```
入力: Script:String
出力: ScriptError:String=> ScriptOutput:String=>
ON ERROR可: RunPowershellScriptError, ScriptTimeoutError
固定: FailOnTimeout=False

## Scripting.RunPowershellScript.RunScriptAndFailOnTimeout [A]
```
Scripting.RunPowershellScript.RunScriptAndFailOnTimeout Timeout: 10 Script: $'''example''' ScriptOutput=> PowershellOutput ScriptError=> ScriptError
```
入力: !Timeout:Int32 !Script:String
出力: ScriptOutput:String=>PowershellOutput ScriptError:String=>ScriptError
ON ERROR可: RunPowershellScriptError, ScriptTimeoutError
固定: FailOnTimeout=True

### Scripting.RunPythonScript のセレクター: RunPythonScript, RunPythonScript34, RunPythonScriptCPython

## Scripting.RunPythonScript.RunPythonScript [A]
```
Scripting.RunPythonScript.RunPythonScript PythonCode: $'''example''' ModuleFolderPaths: List ScriptOutput=> PythonScriptOutput ScriptError=> ScriptError
```
入力: !PythonCode:String ModuleFolderPaths:List<FolderObject>
出力: ScriptOutput:String=>PythonScriptOutput ScriptError:String=>ScriptError
ON ERROR可: DirectoryNotFoundError, RunPythonScriptError
固定: PythonEngine=IronPython2

## Scripting.RunPythonScript.RunPythonScript34 [A]
```
Scripting.RunPythonScript.RunPythonScript34 PythonCode: $'''example''' ModuleFolderPaths: List ScriptOutput=> PythonScriptOutput ScriptError=> ScriptError
```
入力: !PythonCode:String ModuleFolderPaths:List<FolderObject>
出力: ScriptOutput:String=>PythonScriptOutput ScriptError:String=>ScriptError
ON ERROR可: DirectoryNotFoundError, RunPythonScriptError
固定: PythonEngine=IronPython3

## Scripting.RunPythonScript.RunPythonScriptCPython [A]
```
Scripting.RunPythonScript.RunPythonScriptCPython PythonPath: $'''C:\temp''' PythonCode: $'''example''' ModuleFolderPaths: List ScriptOutput=> PythonScriptOutput ScriptError=> ScriptError
```
入力: !PythonPath:FolderObject !PythonCode:String ModuleFolderPaths:List<FolderObject>
出力: ScriptOutput:String=>PythonScriptOutput ScriptError:String=>ScriptError
ON ERROR可: DirectoryNotFoundError, RunPythonScriptError
固定: PythonEngine=CPython

### Scripting.RunVBScript のセレクター: RunVBScript, RunVBScriptAndFailOnTimeout

## Scripting.RunVBScript.RunVBScript [A]
```
Scripting.RunVBScript.RunVBScript VBScriptCode: $'''''' ScriptOutput=> VBScriptOutput ScriptError=> ScriptError
```
入力: VBScriptCode:String
出力: ScriptError:String=> ScriptOutput:String=>
ON ERROR可: ScriptTimeoutError
固定: FailOnTimeout=False

## Scripting.RunVBScript.RunVBScriptAndFailOnTimeout [A]
```
Scripting.RunVBScript.RunVBScriptAndFailOnTimeout Timeout: 10 VBScriptCode: $'''example''' ScriptOutput=> VBScriptOutput ScriptError=> ScriptError
```
入力: !Timeout:Int32 !VBScriptCode:String
出力: ScriptOutput:String=>VBScriptOutput ScriptError:String=>ScriptError
ON ERROR可: ScriptTimeoutError
固定: FailOnTimeout=True

## System.DeleteEnvironmentVariable [A]
```
System.DeleteEnvironmentVariable Name: $'''example''' Type: System.EnvironmentVariableType.User
```
入力: Name:String Type:EnvironmentVariableType{User,System}
ON ERROR可: DeleteEnvironmentVariableError, InsufficientPermissionsError

### System.GetEnvironmentVariable のセレクター: GetEnvironmentVariable, GetEnvironmentVariableFromScope

## System.GetEnvironmentVariable.GetEnvironmentVariable [A]
```
System.GetEnvironmentVariable.GetEnvironmentVariable Name: $'''example''' Value=> EnvironmentVariableValue
```
入力: Name:String
出力: Value:String=>
ON ERROR可: EnvironmentVariableNotFoundError, InsufficientPermissionsError
固定: SearchOnlyInScope=False

## System.GetEnvironmentVariable.GetEnvironmentVariableFromScope [A]
```
System.GetEnvironmentVariable.GetEnvironmentVariableFromScope Scope: System.EnvironmentVariableType.User Name: $'''example''' Value=> EnvironmentVariableValue
```
入力: !Scope:EnvironmentVariableType{User,System} !Name:String
出力: Value:String=>EnvironmentVariableValue
ON ERROR可: EnvironmentVariableNotFoundError, InsufficientPermissionsError
固定: SearchOnlyInScope=True

### System.IfProcess のセレクター: ProcessIsNotRunning, ProcessIsRunning, ProcessWithNameIsNotRunning, ProcessWithNameIsRunning

## System.IfProcess.ProcessIsNotRunning [C]
```
IF (System.IfProcess.ProcessIsNotRunning ProcessName: $'''example''') THEN
```
入力: !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: CheckMode=IsNotRunning, UseProcessUser=False

## System.IfProcess.ProcessIsRunning [C]
```
IF (System.IfProcess.ProcessIsRunning ProcessName: $'''example''') THEN
```
入力: !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: CheckMode=IsRunning, UseProcessUser=False

## System.IfProcess.ProcessWithNameIsNotRunning [C]
```
IF (System.IfProcess.ProcessWithNameIsNotRunning ProcessUser: $'''example''' ProcessName: $'''example''') THEN
```
入力: !ProcessUser:String !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: CheckMode=IsNotRunning, UseProcessUser=True

## System.IfProcess.ProcessWithNameIsRunning [C]
```
IF (System.IfProcess.ProcessWithNameIsRunning ProcessUser: $'''example''' ProcessName: $'''example''') THEN
```
入力: !ProcessUser:String !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: CheckMode=IsRunning, UseProcessUser=True

## System.Ping [A]
```
System.Ping HostName: $'''example''' Timeout: 5000 PingResult=> PingResult RoundTripTime=> RoundTripTime
```
入力: HostName:String Timeout:Int32
出力: PingResult:String=> RoundTripTime:Int32=>
ON ERROR可: PingError

### System.RunApplication のセレクター: RunApplication, RunApplicationAndWaitToComplete, RunApplicationAndWaitToLoad

## System.RunApplication.RunApplication [A]
```
System.RunApplication.RunApplication WindowStyle: System.ProcessWindowStyle.Normal WorkingDirectory: $'''C:\temp''' ApplicationPath: $'''C:\temp\test.xlsx''' CommandLineArguments: $'''example''' ProcessId=> AppProcessId
```
入力: !WindowStyle:ProcessWindowStyle{Normal,Hidden,Minimized,Maximized} WorkingDirectory:FolderObject !ApplicationPath:FileObject CommandLineArguments:String
出力: ProcessId:Int32=>AppProcessId
ON ERROR可: ExecuteApplicationOrOpenFileError, FileOrApplicationAccessDeniedError, FileOrApplicationNotFoundError, RetrieveWindowHandleError
固定: WaitApplication=DoNotWait

## System.RunApplication.RunApplicationAndWaitToComplete [A]
```
System.RunApplication.RunApplicationAndWaitToComplete WindowStyle: System.ProcessWindowStyle.Normal WorkingDirectory: $'''C:\temp''' ApplicationPath: $'''C:\temp\test.xlsx''' CommandLineArguments: $'''example''' Timeout: 0 ProcessId=> AppProcessId ExitCode=> AppExitCode
```
入力: !WindowStyle:ProcessWindowStyle{Normal,Hidden,Minimized,Maximized} WorkingDirectory:FolderObject !ApplicationPath:FileObject CommandLineArguments:String !Timeout:Int32
出力: ProcessId:Int32=>AppProcessId ExitCode:Int32=>AppExitCode
ON ERROR可: ExecuteApplicationOrOpenFileError, FileOrApplicationAccessDeniedError, FileOrApplicationNotFoundError, RetrieveWindowHandleError
固定: WaitApplication=WaitToComplete

## System.RunApplication.RunApplicationAndWaitToLoad [A]
```
System.RunApplication.RunApplicationAndWaitToLoad WindowStyle: System.ProcessWindowStyle.Normal WorkingDirectory: $'''C:\temp''' ApplicationPath: $'''C:\temp\test.xlsx''' CommandLineArguments: $'''example''' Timeout: 0 WindowHandle=> WindowHandle ProcessId=> AppProcessId
```
入力: !WindowStyle:ProcessWindowStyle{Normal,Hidden,Minimized,Maximized} WorkingDirectory:FolderObject !ApplicationPath:FileObject CommandLineArguments:String !Timeout:Int32
出力: WindowHandle:Int32=>WindowHandle ProcessId:Int32=>AppProcessId
ON ERROR可: ExecuteApplicationOrOpenFileError, FileOrApplicationAccessDeniedError, FileOrApplicationNotFoundError, RetrieveWindowHandleError
固定: WaitApplication=WaitToLoad

## System.SetEnvironmentVariable [A]
```
System.SetEnvironmentVariable Name: $'''example''' Value: $'''example''' Type: System.EnvironmentVariableType.User
```
入力: Name:String Type:EnvironmentVariableType{User,System} Value:String
ON ERROR可: InsufficientPermissionsError, SetEnvironmentVariableError

### System.TerminateProcess のセレクター: TerminateProcessById, TerminateProcessByIdWithUserName, TerminateProcessByName, TerminateProcessByNameWithUserName

## System.TerminateProcess.TerminateProcessById [A]
```
System.TerminateProcess.TerminateProcessById ProcessId: 1
```
入力: !ProcessId:Int32
ON ERROR可: InvalidProcessIdError, TerminateProcessError
固定: SpecifyProcessBy=Id, UseProcessUser=False

## System.TerminateProcess.TerminateProcessByIdWithUserName [A]
```
System.TerminateProcess.TerminateProcessByIdWithUserName ProcessUser: $'''example''' ProcessId: 1
```
入力: !ProcessUser:String !ProcessId:Int32
ON ERROR可: InvalidProcessIdError, TerminateProcessError
固定: SpecifyProcessBy=Id, UseProcessUser=True

## System.TerminateProcess.TerminateProcessByName [A]
```
System.TerminateProcess.TerminateProcessByName ProcessName: $'''example'''
```
入力: ProcessName:String
ON ERROR可: InvalidProcessIdError, TerminateProcessError
固定: SpecifyProcessBy=Name, UseProcessUser=False

## System.TerminateProcess.TerminateProcessByNameWithUserName [A]
```
System.TerminateProcess.TerminateProcessByNameWithUserName ProcessUser: $'''example''' ProcessName: $'''example'''
```
入力: !ProcessUser:String !ProcessName:String
ON ERROR可: InvalidProcessIdError, TerminateProcessError
固定: SpecifyProcessBy=Name, UseProcessUser=True

### System.WaitForProcess のセレクター: ProcessToStart, ProcessToStop, ProcessWithNameToStart, ProcessWithNameToStop

## System.WaitForProcess.ProcessToStart [W]
```
WAIT (System.WaitForProcess.ProcessToStart ProcessName: $'''example''')
```
入力: !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: WaitFor=Start, UseProcessUser=False

## System.WaitForProcess.ProcessToStop [W]
```
WAIT (System.WaitForProcess.ProcessToStop ProcessName: $'''example''')
```
入力: !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: WaitFor=Stop, UseProcessUser=False

## System.WaitForProcess.ProcessWithNameToStart [W]
```
WAIT (System.WaitForProcess.ProcessWithNameToStart ProcessUser: $'''example''' ProcessName: $'''example''')
```
入力: !ProcessUser:String !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: WaitFor=Start, UseProcessUser=True

## System.WaitForProcess.ProcessWithNameToStop [W]
```
WAIT (System.WaitForProcess.ProcessWithNameToStop ProcessUser: $'''example''' ProcessName: $'''example''')
```
入力: !ProcessUser:String !ProcessName:String
ON ERROR可: RetrieveProcessesError
固定: WaitFor=Stop, UseProcessUser=True

## Workstation.ControlScreenSaver [A]
```
Workstation.ControlScreenSaver ScreenSaverAction: System.ScreenSaverAction.Enable
```
入力: ScreenSaverAction:ScreenSaverAction{Enable,Disabled,Start,Stop}
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Workstation.EmptyRecycleBin [A]
```
Workstation.EmptyRecycleBin _
```
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Workstation.GetDefaultPrinter [A]
```
Workstation.GetDefaultPrinter PrinterName=> PrinterName
```
出力: PrinterName:String=>DefaultPrinterName
ON ERROR可: GetDefaultPrinterError

## Workstation.GetScreenResolution [A]
```
Workstation.GetScreenResolution MonitorNumber: 1 MonitorWidth=> MonitorWidth MonitorHeight=> MonitorHeight MonitorBitCount=> MonitorBitCount MonitorFrequency=> MonitorFrequency
```
入力: MonitorNumber:Int32
出力: MonitorBitCount:Int32=> MonitorFrequency:Int32=> MonitorHeight:Int32=> MonitorWidth:Int32=>
ON ERROR可: GetScreenResolutionError

## Workstation.LockWorkstation [A]
```
Workstation.LockWorkstation _
```
ON ERROR可: LockWorkstationError, LockWorkstationInNonInteractiveModeError

### Workstation.PlaySound のセレクター: PlaySound, PlaySystemSound

## Workstation.PlaySound.PlaySound [A]
```
Workstation.PlaySound.PlaySound WavFile: $'''C:\temp\test.xlsx'''
```
入力: !WavFile:FileObject
ON ERROR可: InvalidSoundFileError, SoundFileNotFoundError
固定: PlaySoundFrom=File

## Workstation.PlaySound.PlaySystemSound [A]
```
Workstation.PlaySound.PlaySystemSound SystemSound: System.SystemSound.Asterisk
```
入力: !SystemSound:SystemSound{Asterisk,Beep,Exclamation,Hand,Question}
ON ERROR可: InvalidSoundFileError, SoundFileNotFoundError
固定: PlaySoundFrom=System

## Workstation.PrintDocument [A]
```
Workstation.PrintDocument DocumentPath: $'''C:\temp\test.xlsx'''
```
入力: DocumentPath:FileObject
ON ERROR可: DocumentAccessDeniedError, DocumentNotFoundError, PrintDocumentError

## Workstation.SetDefaultPrinter [A]
```
Workstation.SetDefaultPrinter PrinterName: $'''example'''
```
入力: PrinterName:String
ON ERROR可: SetDefaultPrinterError

## Workstation.SetScreenResolution [A]
```
Workstation.SetScreenResolution MonitorNumber: 1 MonitorWidth: 1 MonitorHeight: 1 MonitorBitCount: 1 MonitorFrequency: 1
```
入力: MonitorBitCount:Int32 MonitorFrequency:Int32 MonitorHeight:Int32 MonitorNumber:Int32 MonitorWidth:Int32
ON ERROR可: SetScreenResolutionError

## Workstation.ShowDesktop [A]
```
Workstation.ShowDesktop DesktopOperation: System.DesktopOperation.Show
```
入力: DesktopOperation:DesktopOperation{Show,Hide}
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Workstation.TakeScreenshot のセレクター: TakeScreenshot, TakeScreenshotAndSaveToFile, TakeScreenshotOfForegroundWindow, TakeScreenshotOfForegroundWindowAndSaveToFile, TakeScreenshotOfPrimaryScreen, TakeScreenshotOfPrimaryScreenAndSaveToFile, TakeScreenshotOfScreen, TakeScreenshotOfScreenAndSaveToFile

## Workstation.TakeScreenshot.TakeScreenshot [A]
```
Workstation.TakeScreenshot.TakeScreenshot
```
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=Clipboard, CaptureOption=AllScreens

## Workstation.TakeScreenshot.TakeScreenshotAndSaveToFile [A]
```
Workstation.TakeScreenshot.TakeScreenshotAndSaveToFile ImageFormat: System.ImageFormat.Bmp File: $'''C:\temp\test.xlsx'''
```
入力: !ImageFormat:ImageFormat{Bmp,Gif,Jpg,Png,Tiff} !File:FileObject
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=File, CaptureOption=AllScreens

## Workstation.TakeScreenshot.TakeScreenshotOfForegroundWindow [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfForegroundWindow
```
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=Clipboard, CaptureOption=ForegroundWindow

## Workstation.TakeScreenshot.TakeScreenshotOfForegroundWindowAndSaveToFile [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfForegroundWindowAndSaveToFile ImageFormat: System.ImageFormat.Bmp File: $'''C:\temp\test.xlsx'''
```
入力: !ImageFormat:ImageFormat{Bmp,Gif,Jpg,Png,Tiff} !File:FileObject
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=File, CaptureOption=ForegroundWindow

## Workstation.TakeScreenshot.TakeScreenshotOfPrimaryScreen [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfPrimaryScreen
```
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=Clipboard, CaptureOption=PrimaryScreen

## Workstation.TakeScreenshot.TakeScreenshotOfPrimaryScreenAndSaveToFile [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfPrimaryScreenAndSaveToFile ImageFormat: System.ImageFormat.Bmp File: $'''C:\temp\test.xlsx'''
```
入力: !ImageFormat:ImageFormat{Bmp,Gif,Jpg,Png,Tiff} !File:FileObject
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=File, CaptureOption=PrimaryScreen

## Workstation.TakeScreenshot.TakeScreenshotOfScreen [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfScreen ScreenToCapture: 1
```
入力: !ScreenToCapture:Int32
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=Clipboard, CaptureOption=SelectScreen

## Workstation.TakeScreenshot.TakeScreenshotOfScreenAndSaveToFile [A]
```
Workstation.TakeScreenshot.TakeScreenshotOfScreenAndSaveToFile ScreenToCapture: 1 ImageFormat: System.ImageFormat.Bmp File: $'''C:\temp\test.xlsx'''
```
入力: !ScreenToCapture:Int32 !ImageFormat:ImageFormat{Bmp,Gif,Jpg,Png,Tiff} !File:FileObject
ON ERROR可: GetScreenError, SaveScreenshotToClipboardError, SaveScreenshotToFileError, TakeScreenshotError
固定: StoreScreenshotInto=File, CaptureOption=SelectScreen
