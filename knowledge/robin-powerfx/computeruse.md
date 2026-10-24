# Robin: ComputerUse

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## ComputerUse.InvokeComputerUse [A]
```
ComputerUse.InvokeComputerUse ReasoningEffort: $fx'example' InteractionMode: ComputerUse.ComputerUseInteractionMode.AutomationFramework TimeoutSeconds: 300 Prompt: $fx'example' Endpoint: $fx'example' Provider: ComputerUse.ComputerUseProvider.AzureAI Model: $fx'example' ApiKey: $fx'password' ExtractedData=> ComputerUseExtractedData TotalTokens=> ComputerUseTotalTokens Steps=> ComputerUseSteps Status=> ComputerUseStatus
```
入力: !ReasoningEffort:String !InteractionMode:ComputerUseInteractionMode{AutomationFramework,PureVision} !TimeoutSeconds:Int32 !Prompt:String !Endpoint:String !Provider:ComputerUseProvider{AzureAI,OpenAI} !Model:String ApiKey:EncryptableObject
出力: ExtractedData:List<CustomObject>=>ComputerUseExtractedData TotalTokens:Int64=>ComputerUseTotalTokens Steps:List<CustomObject>=>ComputerUseSteps Status:ComputerUseRunStatus=>ComputerUseStatus
ON ERROR可: AlreadyRunningError, ConnectionError, ModelNotFoundError, RateLimitedError, TimeoutError
