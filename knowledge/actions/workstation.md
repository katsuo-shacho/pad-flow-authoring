# Workstation actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/workstation （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The workstation group of actions provides a collection of actions that automate some essential functionalities of your workstation. To print a document, deploy the Print document action and populate the path of the file you want to print. To change the default printer of the workstation, use the Set default printer action. To check which is the current default printer, use the Get default printer action. If you want to sign out of your Windows account, use the Log off user action. Additionally, you can use the Shutdown computer and Lock workstation actions to shut down or lock your workstation

## Print document  `#printdocument`
Prints a document on the default printer.
入力:
- Document to print: File — The path of the document to print
例外: Document not found; Access denied for document; Can't print document

## Get default printer  `#getdefaultprinter`
Gets the name of the default printer.
出力:
- PrinterName: Text value — The name of the default printer
例外: Can't get default printer

## Set default printer  `#setdefaultprinter`
Sets a printer as the default printer.
入力:
- Printer name: Text value — The name of the printer to set as default
例外: Can't set default printer

## Show desktop  `#showdesktop`
Shows the desktop.
入力:
- Operation: Minimize all windows (show desktop), Restore all windows (undo show desktop) = Minimize all windows (show desktop) — Specify whether to minimize all windows to reveal the desktop or restore all windows to their original respective states

## Lock workstation  `#lockworkstation`
Locks the workstation's display to protect it from unauthorized use.
例外: Can't lock the computer in non interactive mode; Can't lock the computer

## Play sound  `#playsoundbase`
Plays a system sound or a wav file.
入力:
- Play sound from: System, WAV file = System — The type of sound to play
- Sound to play: Asterisk, Beep, Exclamation, Hand, Question = Asterisk — The specific sound to play
- File to play: File — The full path of the specific WAV file to play
例外: Can't find sound file; Invalid sound file

## Empty recycle bin  `#emptyrecyclebin`
Deletes all files from the windows recycle bin.

## Take screenshot  `#takescreenshotbase`
Takes a screenshot of the foreground window or the specified screen and saves the image in a file or to the clipboard.
入力:
- Capture: All screens, Primary screen, Select screen, Foreground window = All screens — The area to capture
- Screen to capture: Numeric value — Specify which screen to capture
- Save screenshot to: Clipboard, File = Clipboard — The location to save the screenshot to
- Image file: File — The full path of the file name where the captured image will be saved
- Image format: BMP, EMF, EXIF, GIF, JPG, PNG, TIFF, WMF = BMP — The format for the image file to save
例外: Failed to take screenshot; Failed to save screenshot to file; Failed to set screenshot to clipboard; Failed to get specified screen

## Control screen saver  `#controlscreensaver`
Enables, disables, starts or stops the screensaver.
入力:
- Screen saver action: Enable, Disable, Start, Stop = Enable — The function of the screensaver

## Get screen resolution  `#getscreenresolution`
Gets the width, height, bit count and frequency of a selected monitor.
入力:
- Monitor number: Numeric value — The number of the monitor to get the resolution of
出力:
- MonitorWidth: Numeric value — The width of the monitor
- MonitorHeight: Numeric value — The height of the monitor
- MonitorBitCount: Numeric value — The monitor bit count
- MonitorFrequency: Numeric value — The monitor frequency
例外: Failed to get the screen's resolution

## Set screen resolution  `#setscreenresolution`
Sets the width, height, bit count and frequency of a selected monitor during an attended desktop flow run.
入力:
- Monitor number: Numeric value — The number of monitor to set the resolution of
- Monitor width: Numeric value — The value to set the monitor width to
- Monitor height: Numeric value — The value to set the monitor height to
- Monitor bit count: Numeric value — The value to set the monitor bit count to
- Monitor frequency: Numeric value — The value to set the monitor frequency to
例外: Failed to set the screen's resolution

## Log off user  `#logoffuser`
Logs off the current user.
入力:
- Force log off: Boolean value = False — Specify whether to force the user account to log off, regardless of unsaved files or programs that won't close
例外: Can't log off user in non interactive mode; Can't log off the current user

## Shutdown computer  `#shutdowncomputer`
Instructs the computer to shut down.
入力:
- Action to perform: Shutdown, Restart, Suspend, Hibernate = Shutdown — Specify which shutdown option the computer will perform
- Force: Boolean value = False — Specify whether to force the computer to shut down, regardless of unsaved files or programs that won't close
例外: Can't shut down the computer
