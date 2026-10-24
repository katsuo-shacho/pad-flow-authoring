# Power Automate environment actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/powerautomateenvironment （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: In this module, you find actions that allow you to retrieve environment variables that are available in your environment, offering direct integration with the corresponding components. You can retrieve environment variables of the following types: Text values, numeric values, Boolean values, JSON as text values, and secrets as sensitive values (text values that are enforced to be sensitive). The secret values are only retrieved at runtime and aren't logged.

## Retrieve environment variable  `#retrieveenvironmentvariable`
Retrieves a Power Automate environment variable.
入力:
- Environment variable: Text value — Select the environment variable whose value will be retrieved
出力:
- EnvironmentVariableValue: *Depends on the selected environment variable type* — Retrieve the Power Automate environment variable value
例外: Retrieve environment variable failed
