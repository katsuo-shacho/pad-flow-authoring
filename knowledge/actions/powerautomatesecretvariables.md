# Power Automate secret variables actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/powerautomatesecretvariables （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: In this module, you find actions that allow you to safely retrieve sensitive data that are available in your environment, offering direct integration with the corresponding components. You can securely retrieve CyberArk-based credentials and use them in desktop flows, or retrieve Azure Key Vault-based credentials and use them in desktop flows. The credential values are only retrieved at runtime and aren't logged. Credential type variables are enforced to be sensitive.

## Get credential  `#getcredentialaction`
Retrieves the values of a credential created through Power Automate's portal page for this environment.
入力:
- Credential: Text value — The credential whose values are retrieved
- Timeout: Numeric value = 0 — The maximum waiting time (in seconds) to get the credential
出力:
- Credential: Credential — The content of the retrieved credential
例外: Failed to get credential; Invalid credentials configuration; Credential timed out; Failed to contact credentials vault
