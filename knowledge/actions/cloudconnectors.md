# Cloud Connectors in Power Automate for desktop

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/cloudconnectors （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Cloud connectors available for Power Automate are now available for desktop flows as well.

## Prerequisites and limitations
- To use premium connectors, you need an Attended RPA license. If you have a free work or school account, you can access standard connectors.

## Use files in cloud connector actions
To pass a file as an input to a cloud connector action, first convert the file to binary data by using the Convert file to binary data action.

## Embed connection references on a desktop flow
By using connection reference embedding, you can give other co-owners access to your connection references and their underlying resources. You can only do this process in the scope of the respective shared desktop flow.

## Bring your own connection in console runs
If you're a co-owner, bring your own connection (BYOC) in console runs for connection references that aren't embedded. If you're a run-only user, bring your own connection, even if the connection references are embedded.

## List of cloud connectors
Power Automate for desktop adds these cloud connectors to desktop flows by default. You always see them in the actions pane:
