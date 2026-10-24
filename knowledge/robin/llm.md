# Robin: LLM

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## LLM.InvokeLLM [A]
```
LLM.InvokeLLM MaxTokens: 2048 Temperature: 0.8 ResponseFormat: LLM.ResponseFormatType.Text ApiKey: $'''password''' Timeout: 300 ModelConfiguration: $'''example''' EndpointUrl: $'''example''' SystemPrompt: $'''example''' AttachFiles: SelectedFiles UserPrompt: $'''example''' ToolBindings: $'''[]''' CompletionTokens=> CompletionTokens PromptTokens=> PromptTokens Response=> Response
```
入力: !MaxTokens:Int32 !Temperature:Double !ResponseFormat:ResponseFormatType{Text,Json} ApiKey:EncryptableObject !Timeout:Int32 !AttachFiles:List<FileObject> !EndpointUrl:String ToolBindings:String !ModelConfiguration:String !UserPrompt:String !SystemPrompt:String
出力: CompletionTokens:Int32=>CompletionTokens PromptTokens:Int32=>PromptTokens Response:String=>Response
ON ERROR可: ConnectionError, FailedToInvokeModelError, FileNotFoundError, InvalidInputError, InvalidResponseError, ModelNotFoundError, RequestTimedOutError
