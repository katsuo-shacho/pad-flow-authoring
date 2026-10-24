# Windows services actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/services （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate allows you to handle Windows services via the available Windows services actions. With these actions, you can maintain complete control of the operating system and limit the running services. These actions allow desktop flows to start, stop, pause, and resume Windows services. To use any action of this group, you need to enter only the service name. The following example starts the UIFlowService service.

## If service  `#ifserviceaction`
Marks the beginning of a conditional block of actions depending on whether a service is running, paused, stopped or installed on the computer.
入力:
- If service: Is stopped, Is installed, Isn't installed, Is running, Is paused = Is running — The state of the service to check
- Service name: Text value — The name of the service to check
例外: Service not found; Can't retrieve status for service

## Wait for service  `#waitforserviceaction`
Suspend the execution of the automation until a service is running, paused or stopped on the computer.
入力:
- Wait for service to: Stop, Start, Pause = Start — Specifies whether the flow pauses until a certain service starts, stops or pauses
- Service name: Text value — The name of the service to check
例外: Service not found; Can't retrieve status for service

## Start service  `#start`
Start a stopped Windows service.
入力:
- Service to start: Text value — The name of the service to start
例外: Service not found; Service is already running; Can't start service

## Stop service  `#stop`
Stop a running Windows service.
入力:
- Service to stop: Text value — The name of the service to stop
例外: Service not found; Service isn't running; Can't stop service

## Pause service  `#pause`
Pause a running Windows service.
入力:
- Service to pause: Text value — The name of the service to pause
例外: Service not found; Service isn't running; Can't pause service

## Resume service  `#resume`
Resume a paused Windows service.
入力:
- Service to resume: Text value — The name of the service to resume
例外: Service not found; Service isn't running; Can't resume service
