# Robin: Triggers

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Triggers.WaitForTriggerAction のセレクター: WaitForTriggerAction, WaitForTriggerActionWithTimeout

## Triggers.WaitForTriggerAction.WaitForTriggerAction [L]
```
LOOP WHILE (Triggers.WaitForTriggerAction.WaitForTriggerAction Policy: Triggers.TriggerPolicy.OneTime TriggerEventInstanceHandle=> TriggerEventInstanceHandle)
```
入力: !Policy:TriggerPolicy{OneTime,Sequential}
出力: TriggerEventInstanceHandle:TriggerEventInstanceHandle=>TriggerEventInstanceHandle
ON ERROR可: WaitForTriggerError, WaitForTriggerTimeoutError
固定: FailWithTimeoutError=False

## Triggers.WaitForTriggerAction.WaitForTriggerActionWithTimeout [L]
```
LOOP WHILE (Triggers.WaitForTriggerAction.WaitForTriggerActionWithTimeout Timeout: 0 Policy: Triggers.TriggerPolicy.OneTime TriggerEventInstanceHandle=> TriggerEventInstanceHandle)
```
入力: !Timeout:Int32 !Policy:TriggerPolicy{OneTime,Sequential}
出力: TriggerEventInstanceHandle:TriggerEventInstanceHandle=>TriggerEventInstanceHandle
ON ERROR可: WaitForTriggerError, WaitForTriggerTimeoutError
固定: FailWithTimeoutError=True
