# Testing actions

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/testing （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: In this module, you find actions that let you create and run test cases directly within Power Automate for desktop. This capability improves the reliability of desktop flows by enabling structured validation and integration into automated pipelines.

## Test a desktop flow  `#runtestflow`
Test a desktop flow that receives input variables and might produce output variables. The parent flow run pauses until the called desktop flow completes.
入力:
- Desktop flow: Desktop flow — Select the desktop flow to run within this flow. The called flow runs in the same Windows session as the parent flow.

## Assert  `#assertaction`
Validates output against expected results using operators like equals, contains, or greater than.
入力:
- Assert expression(任意): Text value — Expression that verifies the actual result of your desktop flow matches the result you expect
- Assert message(任意): Text value — Message displayed if the test fails
