# Run desktop flow actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/runflow （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: The *Run desktop flow* action enables you to call other desktop flows while running a specific desktop flow. To use the action, add it to the workspace and select the desktop flow you want to call. If the called flow contains input variables, the action will prompt you to enter their values. In the context menu of the Run desktop flow action, the option Go to flow, allows you to quickly launch the designer of the selected flow and avoid navigating to the flows list in the console. You can disable the toggle property Wait for flow to complete, which is enabled by default. If disabled, the invok

## Run desktop flow  `#runflow`
Runs a desktop flow that can receive input variables and might produce output variables. The parent flow run will be paused until the called desktop flow completes.
入力:
- Desktop flow: Desktop flow — Select the desktop flow to run from within this flow. The called flow always runs in the same Windows session as the parent flow.
- Wait for flow to complete: Boolean value = True — If enabled, this desktop flow waits for the invoked desktop flow to complete before resuming. The invoked desktop flow's output variables are available to the current flow. If disabled, the invoked desktop flow runs concurrently, and its output variables are ignored.
例外: Run desktop flow failed; Desktop flow timed out
