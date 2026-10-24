# System actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/system （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Use the system actions to automate tasks fundamental to the Windows operating system. Launch any of your installed applications with the Run application action. You must enclose any command line arguments in double quotes and separate them by space. The following example opens a specific Word document in quiet mode. !Screenshot of the Run application action. Additionally, desktop flows enable you to terminate processes by name or ID through the Terminate process action, and wait for processes to start or stop through the Wait for process action. You can also use user context if a process runs 

## If process  `#ifprocessaction`
Marks the beginning of a conditional block of actions depending on whether a process is running or not.
入力:
- If process: Is running, Isn't running = Is running — State of the process to check
- Process name: Text value — The name of the process to check
- From User: Boolean value = False — Determine whether the process runs under a specific user or not
- User name: Text value — Specify the name of the user running the process. The format is either domain\username or username.
例外: Can't retrieve list of processes

## Wait for process  `#waitprocessaction`
Suspends the execution until a process starts or stops.
入力:
- Process name: Text value — The name of the process to check
- From User: Boolean value = False — Determine whether the process runs under a specific user or not
- User name: Text value — Specify the name of the user running the process. The format is either domain\username or username.
- Wait for process to: Start, Stop = Start — Whether to wait until a certain process starts or stops
- Fail with timeout error: Boolean value = False — Specify whether you want the action to wait indefinitely or fail after a set time period
例外: Can't retrieve list of processes; Timeout error

## Run application  `#runapplicationbase`
Executes an application or opens a document by executing the associated application.
入力:
- Application path: File — The executable file as a complete file path
- Command line arguments(任意): Text value — Add extra arguments that would go after the executable file name. For example, enter notepad.exe in the application path and a specific text file in the command line arguments
- Working folder(任意): Folder — The full path of the folder to work out of, if applicable.
- Window style: Normal, Hidden, Minimized, Maximized = Normal — Choose the appearance and size of the application window when it opens
- After application launch: Continue immediately, Wait for application to load, Wait for application to complete = Continue immediately — Whether the next action executes immediately, or waits until the program loads or completes
- Timeout(任意): Numeric value = 0 — The maximum wait time, and how long before forcing a continue
出力:
- AppProcessId: Numeric value — The process ID output
- AppExitCode: Numeric value — The application exit code
- WindowHandle: Numeric value — The window handle. When opening a new window, this variable will catch the value of the window handle, and store it in this variable. A window handle is useful to specifically identify a window in a later action
例外: File or application not found; Access denied for application or File; Can't retrieve application's main window handle; Can't execute application or open file

## Terminate process  `#terminateprocess`
Immediately stops a running process.
入力:
- Specify process by: Process ID, Process name = Process name — Specify whether the process to terminate is specified by its name, or by its ID
- Process ID: Numeric value — The ID of the process to terminate
- Process name: Text value — The name of the process to terminate. If more than one process with the same name is running, all of them are terminated
- From User: Boolean value = False — Determine whether the process runs under a specific user or not
- User name: Text value — Specify the name of the user running the process. The format is either domain\username or username.
例外: Process with specified ID not running; Failed to terminate process

## Ping  `#ping`
Sends a message to determine whether a remote computer is accessible over the network.
入力:
- Host name: Text value — The name of the remote computer or an IP address
- Timeout(任意): Numeric value = 5000 — The maximum number of milliseconds to wait for the Ping reply message
出力:
- PingResult: Text value — The status of the ping message (success or failure)
- RoundTripTime: Numeric value — The number of milliseconds taken for the Ping to complete
例外: Can't complete ping action

## Set Windows environment variable  `#setenvironmentvariable`
Sets an environment variable to a given value.
入力:
- Environment variable name: Text value — The name of the environment variable
- New environment variable value: Text value — The value that is set to the environment variable
- Type: User, System = User — The type of the environment variable
例外: Indicates a problem setting the environment variable's value; Insufficient permissions

## Get Windows environment variable  `#getenvironmentvariable`
Retrieves the value of an environment variable.
入力:
- Environment variable name: Text value — The name of the environment variable whose value will be retrieved
- Search for variable only in scope: Boolean value = False — Specify whether to search for the variable only in a specific scope
- Scope: User, System = User — The scope from which the environment variable should be retrieved
出力:
- EnvironmentVariableValue: Text value — The environment variable's value
例外: Environment variable doesn't exist; Insufficient permissions

## Delete Windows environment variable  `#deleteenvironmentvariable`
Deletes an environment variable from a given scope.
入力:
- Environment variable name: Text value — The name of the environment variable to delete
- Type: User, System = User — The type of the environment variable to delete
例外: Failed to delete environment variable; Insufficient permissions
