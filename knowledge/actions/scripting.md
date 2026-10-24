# Scripting actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/scripting （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Scripting actions enable you to run blocks of code and implement custom behavior in your desktop flows. All scripting actions follow the basic structure of the respective programming or scripting language: PowerShell, Python, VBScript, JavaScript, and C#/VB.NET.

## Run DOS command  `#rundoscommand`
Executes a DOS command or console application in invisible mode and retrieves its output upon completion.
入力:
- DOS command or application: File — The name of DOS command or a console application, with arguments if applicable
- Working folder(任意): Folder — The full path of the folder to work out of, if applicable
- Fail after timeout(任意): Boolean value — Specify whether the DOS command or application will run indefinitely or fail after a set period of time
- Timeout: Numeric value = 10 — The maximum number of seconds to wait for the script to complete (-1 for indefinitely)
- Change code page: Boolean value = False — Specifies whether to change the session's current code page
- Encoding: ASMO-708: Arabic (ASMO 708), big5: Chinese Traditional (Big5), cp1025: IBM EBCDIC (Cyrillic Serbian-Bulgarian), cp866: Cyrillic (DOS), cp875: IBM EBCDIC (Greek Modern), csISO2022JP: Japanese (JIS-Allow 1 byte Kana), DOS-720: Arabic (DOS), DOS-862: Hebrew (DOS), EUC-CN: Chinese Simplified (EUC), EUC-JP: Japanese (JIS 0208-1990 and 0212-1990), euc-jp: Japanese (EUC), euc-kr: Korean (EUC), GB18030: Chinese Simplified (GB18030), gb2312: Chinese Simplified (GB2312), hz-gb-2312: Chinese Simplified (HZ), IBM-Thai: IBM EBCDIC (Thai), IBM00858: OEM Multilingual Latin I, IBM00924: IBM Latin-1, IBM01047: IBM Latin-1, IBM01140: IBM EBCDIC (US-Canada-Euro), IBM01141: IBM EBCDIC (Germany-Euro), IBM01142: IBM EBCDIC (Denmark-Norway-Euro), IBM01143: IBM EBCDIC (Finland-Sweden-Euro), IBM01144: IBM EBCDIC (Italy Euro), IBM01145: IBM EBCDIC (Spain-Euro), IBM01146: IBM EBCDIC (UK-Euro), IBM01147: IBM EBCDIC (France-Euro), IBM01148: IBM EBCDIC (International-Euro), IBM01149: IBM EBCDIC (Icelandic-Euro), IBM037: IBM EBCDIC (US-Canada), IBM1026: IBM EBCDIC (Turkish Latin-5), IBM273: IBM EBCDIC (Germany), IBM277: IBM EBCDIC (Denmark-Norway), IBM278: IBM EBCDIC (Finland-Sweden), IBM280: IBM EBCDIC (Italy), IBM284: IBM EBCDIC (Spain), IBM285: IBM EBCDIC (UK), IBM290: IBM EBCDIC (Japanese katakana), IBM297: IBM EBCDIC (France), IBM420: IBM EBCDIC (Arabic), IBM423: IBM EBCDIC (Greek), IBM424: IBM EBCDIC (Hebrew), IBM437: OEM United States, IBM500: IBM EBCDIC (International), ibm737: Greek (DOS), ibm775: Baltic (DOS), ibm850: Western European (DOS), ibm852: Central European (DOS), IBM855: OEM Cyrillic, ibm857: Turkish (DOS), IBM860: Portuguese (DOS), ibm861: Icelandic (DOS), IBM863: French Canadian (DOS), IBM864: Arabic (864), IBM865: Nordic (DOS), ibm869: Greek, Modern (DOS), IBM870: IBM EBCDIC (Multilingual Latin-2), IBM871: IBM EBCDIC (Icelandic), IBM880: IBM EBCDIC (Cyrillic Russian), IBM905: IBM EBCDIC (Turkish), iso-2022-jp: Japanese (JIS), iso-2022-jp: Japanese (JIS-Allow 1 byte Kana - SO/SI), iso-2022-kr: Korean (ISO), iso-8859-1: Western European (ISO), iso-8859-13: Estonian (ISO), iso-8859-15: Latin 9 (ISO), iso-8859-2: Central European (ISO), iso-8859-3: Latin 3 (ISO), iso-8859-4: Baltic (ISO), iso-8859-5: Cyrillic (ISO), iso-8859-6: Arabic (ISO), iso-8859-7: Greek (ISO), iso-8859-8: Hebrew (ISO-Visual), iso-8859-8-i: Hebrew (ISO-Logical), iso-8859-9: Turkish (ISO), Johab: Korean (Johab), koi8-r: Cyrillic (KOI8-R), koi8-u: Cyrillic (KOI8-U), ks_c_5601-1987: Korean, macintosh: Western European (Mac), shift_jis: Japanese (Shift-JIS), us-ascii: US-ASCII, utf-16: Unicode, utf-16BE: Unicode (Big-Endian), utf-32: Unicode (UTF-32), utf-32BE: Unicode (UTF-32 Big-Endian), utf-7: Unicode (UTF-7), utf-8: Unicode (UTF-8), windows-1250: Central European (Windows), windows-1251: Cyrillic (Windows), Windows-1252: Western European (Windows), windows-1253: Greek (Windows), windows-1254: Turkish (Windows), windows-1255: Hebrew (Windows), windows-1256: Arabic (Windows), windows-1257: Baltic (Windows), windows-1258: Vietnamese (Windows), windows-874: Thai (Windows), x-Chinese-CNS: Chinese Traditional (CNS), x-Chinese-Eten: Chinese Traditional (Eten), x-cp20001: TCA Taiwan, x-cp20003: IBM5550 Taiwan, x-cp20004: TeleText Taiwan, x-cp20005: Wang Taiwan, x-cp20261: T.61, x-cp20269: ISO-6937, x-cp20936: Chinese Simplified (GB2312-80), x-cp20949: Korean Wansung, x-cp50227: Chinese Simplified (ISO-2022), x-EBCDIC-KoreanExtended: IBM EBCDIC (Korean Extended), x-Europa: Europa, x-IA5: Western European (IA5), x-IA5-German: German (IA5), x-IA5-Norwegian: Norwegian (IA5), x-IA5-Swedish: Swedish (IA5), x-iscii-as: ISCII Assamese, x-iscii-be: ISCII Bengali, x-iscii-de: ISCII Devanagari, x-iscii-gu: ISCII Gujarati, x-iscii-ka: ISCII Kannada, x-iscii-ma: ISCII Malayalam, x-iscii-or: ISCII Oriya, x-iscii-pa: ISCII Punjabi, x-iscii-ta: ISCII Tamil, x-iscii-te: ISCII Telugu, x-mac-arabic: Arabic (Mac), x-mac-ce: Central European (Mac), x-mac-chinesesimp: Chinese Simplified (Mac), x-mac-chinesetrad: Chinese Traditional (Mac), x-mac-croatian: Croatian (Mac), x-mac-cyrillic: Cyrillic (Mac), x-mac-greek: Greek (Mac), x-mac-hebrew: Hebrew (Mac), x-mac-icelandic: Icelandic (Mac), x-mac-japanese: Japanese (Mac), x-mac-korean: Korean (Mac), x-mac-romanian: Romanian (Mac), x-mac-thai: Thai (Mac), x-mac-turkish: Turkish (Mac), x-mac-ukrainian: Ukrainian (Mac)` = utf-8: Unicode (UTF-8) — The encoding to use when reading the output
出力:
- CommandOutput: Text value — The text output from the DOS command or application
- CommandErrorOutput: Text value — The text describing the errors occurred (if any) during the execution of the DOS command or application
- CommandExitCode: Numeric value — The command or application exit code. This value is numeric
例外: Can't execute command or console application; Failed to run script in the allotted time

## Run VBScript  `#runvbscript`
Executes some custom VBScript code and retrieves its output into a variable.
入力:
- VBScript to run(任意): Text value — The VBScript code to execute. Variables might be included within the script since they evaluate before the execution of the VBScript
- Fail after timeout(任意): Boolean value = N/A — Specify whether the VBScript script will run indefinitely or fail after a set period of time
- Timeout: Numeric value = 10 — The maximum number of seconds to wait for the script to complete (-1 for indefinitely)
出力:
- VBScriptOutput: Text value — The script's output
- ScriptError: Text value — The errors that might occur during the execution of the VBScript code
例外: Failed to run script in the allotted time

## Run JavaScript  `#runjavascript`
Executes some custom JavaScript code and retrieves its output into a variable.
入力:
- JavaScript to run(任意): Text value — The JavaScript code to execute. Variables might be included within the script since they evaluate before the JavaScript code's execution
- Fail after timeout(任意): Boolean value — Specify whether the JavaScript script will run indefinitely or fail after a set period of time
- Timeout: Numeric value = 10 — The maximum number of seconds to wait for the script to complete (-1 for indefinitely)
出力:
- JavascriptOutput: Text value — The script's output
- ScriptError: Text value — The errors that might occur during the execution of the JavaScript code
例外: Failed to run script in the allotted time

## Run PowerShell script  `#runpowershellscript`
Executes some custom PowerShell script and retrieves its output into a variable.
入力:
- PowerShell code to run(任意): Text value — The PowerShell code to execute. Variables can be included within the script since they evaluate before the execution of the PowerShell code
- Fail after timeout(任意): Boolean value — Specify whether the PowerShell script will run indefinitely or fail after a set period of time
- Timeout: Numeric value = 10 — The maximum number of seconds to wait for the script to complete (-1 for indefinitely)
出力:
- PowershellOutput: Text value — The script's output
- ScriptError: Text value — The errors that might occur during the execution of the PowerShell code
例外: Failed to run PowerShell script; Failed to run script in the allotted time

## Run Python script  `#runpythonscript`
Executes Python script code and retrieves its output.
入力:
- Python script to run: Text value — The Python script code to execute
- Python version: Python 2.7, Python 3.4 = Python 2.7 — Specify which version of Python to use when executing the script
- Module folder paths(任意): List of Folders — The paths of folders where external Python modules lie
出力:
- PythonScriptOutput: Text value — The script's output
- ScriptError: Text value — The errors that might occur during the execution of the Python script code
例外: Failed to run Python script; Directory not found

## Run .NET script  `#rundotnetscript`
Executes .NET (C#/VB.NET) script code and retrieves its output.
入力:
- Language: C#/ VB.NET = C# — The language of the script
- .NET script imports(任意): Text value — The .NET script imports to be included in the script
- References to be loaded(任意): Folder — The root path where .NET dynamic link libraries (.dll files) references are located
- Script parameters(任意): Script Parameters as defined by the user — Setting the values of the parameters that are defined in the script
- .NET code to run: Text value — The .NET code to run
例外: Failed to run the .NET script
