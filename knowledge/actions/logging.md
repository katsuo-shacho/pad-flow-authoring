# Logging actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/logging （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The Log message action enables you to log a custom text message with a severity level of Info, Warning or Error in the flow run action details. !Screenshot of the Log message action. At runtime, all action logs are uploaded to the Power Automate service, and are visible in the flow run action details view of the Power Automate portal.

## Log message  `#logmessage`
Adds a custom text message to the flow run action details.
入力:
- Message: Text value — The message to log
- Log level: Info, Warning, Error = Info — The severity level of the message
