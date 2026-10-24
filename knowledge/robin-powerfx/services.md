# Robin: Services

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Services.IfService のセレクター: IsInstalled, IsNotInstalled, IsPaused, IsRunning, IsStopped

## Services.IfService.IsInstalled [C]
```
IF (Services.IfService.IsInstalled Service: $fx'example') THEN
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: ServiceStatus=IsInstalled

## Services.IfService.IsNotInstalled [C]
```
IF (Services.IfService.IsNotInstalled Service: $fx'example') THEN
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: ServiceStatus=IsNotInstalled

## Services.IfService.IsPaused [C]
```
IF (Services.IfService.IsPaused Service: $fx'example') THEN
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: ServiceStatus=IsPaused

## Services.IfService.IsRunning [C]
```
IF (Services.IfService.IsRunning Service: $fx'example') THEN
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: ServiceStatus=IsRunning

## Services.IfService.IsStopped [C]
```
IF (Services.IfService.IsStopped Service: $fx'example') THEN
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: ServiceStatus=IsStopped

## Services.Pause [A]
```
Services.Pause ServiceName: $fx'example'
```
入力: ServiceName:String
ON ERROR可: PauseServiceError, ServiceNotFoundError, ServiceNotRunningError

## Services.Resume [A]
```
Services.Resume ServiceName: $fx'example'
```
入力: ServiceName:String
ON ERROR可: ResumeServiceError, ServiceNotFoundError, ServiceNotRunningError

## Services.Start [A]
```
Services.Start ServiceName: $fx'example'
```
入力: ServiceName:String
ON ERROR可: ServiceAlreadyRunningError, ServiceNotFoundError, StartServiceError

## Services.Stop [A]
```
Services.Stop ServiceName: $fx'example'
```
入力: ServiceName:String
ON ERROR可: ServiceNotFoundError, ServiceNotRunningError, StopServiceError

### Services.WaitForService のセレクター: Paused, Started, Stopped

## Services.WaitForService.Paused [W]
```
WAIT (Services.WaitForService.Paused Service: $fx'example')
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: WaitFor=ToPause

## Services.WaitForService.Started [W]
```
WAIT (Services.WaitForService.Started Service: $fx'example')
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: WaitFor=ToStart

## Services.WaitForService.Stopped [W]
```
WAIT (Services.WaitForService.Stopped Service: $fx'example')
```
入力: !Service:String
ON ERROR可: RetrieveStatusForServiceError, ServiceNotFoundError
固定: WaitFor=ToStop
