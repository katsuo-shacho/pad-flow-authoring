# Robin: Cmd

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Cmd.Close [A]
```
Cmd.Close Session: CmdSession
```
入力: Session:CmdSessionHandle
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Cmd.Open のセレクター: Open, OpenWithCodePage

## Cmd.Open.Open [A]
```
Cmd.Open.Open Directory: $'''C:\temp''' Session=> CmdSession
```
入力: Directory:FolderObject
出力: Session:CmdSessionHandle=>
ON ERROR可: OpenCmdError, WorkingDirectoryDoesNotExist
固定: ChangeCodePage=False

## Cmd.Open.OpenWithCodePage [A]
```
Cmd.Open.OpenWithCodePage Encoding: Cmd.Encoding.utf_8 Directory: $'''C:\temp''' Session=> CmdSession
```
入力: !Encoding:Encoding{IBM037,IBM437,IBM500,ASMO_708,DOS_720,ibm737,ibm775,ibm850,ibm852,IBM855,ibm857,IBM00858,IBM860,ibm861,DOS_862,IBM863,IBM864,IBM865,cp866,ibm869,IBM870,windows_874,cp875,shift_jis,gb2312,ks_c_5601_1987,big5,IBM1026,IBM01047,IBM01140,IBM01141,IBM01142,IBM01143,IBM01144,IBM01145,IBM01146,IBM01147,IBM01148,IBM01149,utf_16,utf_16BE,windows_1250,windows_1251,Windows_1252,windows_1253,windows_1254,windows_1255,windows_1256,windows_1257,windows_1258,Johab,macintosh,x_mac_japanese,x_mac_chinesetrad,x_mac_korean,x_mac_arabic,x_mac_hebrew,x_mac_greek,x_mac_cyrillic,x_mac_chinesesimp,x_mac_romanian,x_mac_ukrainian,x_mac_thai,x_mac_ce,x_mac_icelandic,x_mac_turkish,x_mac_croatian,utf_32,utf_32BE,x_Chinese_CNS,x_cp20001,x_Chinese_Eten,x_cp20003,x_cp20004,x_cp20005,x_IA5,x_IA5_German,x_IA5_Swedish,x_IA5_Norwegian,us_ascii,x_cp20261,x_cp20269,IBM273,IBM277,IBM278,IBM280,IBM284,IBM285,IBM290,IBM297,IBM420,IBM423,IBM424,x_EBCDIC_KoreanExtended,IBM_Thai,koi8_r,IBM871,IBM880,IBM905,IBM00924,EUC_JP_20932,x_cp20936,x_cp20949,cp1025,koi8_u,iso_8859_1,iso_8859_2,iso_8859_3,iso_8859_4,iso_8859_5,iso_8859_6,iso_8859_7,iso_8859_8,iso_8859_9,iso_8859_13,iso_8859_15,x_Europa,iso_8859_8_i,iso_2022_jp_50220,csISO2022JP,iso_2022_jp_50222,iso_2022_kr,x_cp50227,euc_jp_51932,EUC_CN,euc_kr,hz_gb_2312,GB18030,x_iscii_de,x_iscii_be,x_iscii_ta,x_iscii_te,x_iscii_as,x_iscii_or,x_iscii_ka,x_iscii_ma,x_iscii_gu,x_iscii_pa,utf_7,utf_8} Directory:FolderObject
出力: Session:CmdSessionHandle=>CmdSession
ON ERROR可: OpenCmdError, WorkingDirectoryDoesNotExist
固定: ChangeCodePage=True

### Cmd.ReadFromCmdSession のセレクター: Read, ReadAndSplit

## Cmd.ReadFromCmdSession.Read [A]
```
Cmd.ReadFromCmdSession.Read Session: CmdSession CmdOutput=> CmdOutput
```
入力: Session:CmdSessionHandle
出力: CmdOutput:String=>
ON ERROR可: SessionClosedError
固定: SplitOutputAndError=False

## Cmd.ReadFromCmdSession.ReadAndSplit [A]
```
Cmd.ReadFromCmdSession.ReadAndSplit Session: CmdSession CmdOutput=> CmdOutput CmdError=> CmdError
```
入力: !Session:CmdSessionHandle
出力: CmdOutput:String=>CmdOutput CmdError:String=>CmdError
ON ERROR可: SessionClosedError
固定: SplitOutputAndError=True

## Cmd.WaitForText [A]
```
Cmd.WaitForText Session: CmdSession Text: $'''example''' IsRegex: False Timeout: 0
```
入力: IgnoreCase:Boolean IsRegEx:Boolean Session:CmdSessionHandle Text:String Timeout:Int32
ON ERROR可: SessionClosedError, TimeoutExpiredError

## Cmd.Write [A]
```
Cmd.Write Session: CmdSession Command: $'''example''' SendEnter: True
```
入力: Command:String SendEnter:Boolean Session:CmdSessionHandle
ON ERROR可: SessionClosedError, WriteCmdError
