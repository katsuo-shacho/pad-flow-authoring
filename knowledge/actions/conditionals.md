# Conditional actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/conditionals （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Conditional actions allow you to adjust which actions to run based on the outcomes of conditional statements. The following list displays some applications and features: * Use If conditionals to evaluate any type of condition. * Use Switch conditionals to compare a single variable with multiple possible values. * Cover multiple scenarios by employing nested conditionals. * Provide default and alternative behaviors to your desktop flows based on the available data. To find more information on how to use the conditionals,go to Use conditionals.

## Case  `#case`
An expression that, if met, a block of actions associated with that particular case runs.
入力:
- Operator: Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=), Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank = Equal to (=) — The comparison operator of this case
- Value to compare: * — Enter a value to compare with the switch-block value

## Default case  `#casedefault`
A block of actions that is run, if no case expression has been met in the switch body.

## Else  `#else`
Marks the beginning of a block of actions that ran if the condition specified in the preceding 'If' statements aren't met.

## Else if  `#elseif`
Marks the beginning of a block of actions that run if the conditions specified in the preceding 'If' statements aren't met, but the condition specified in this statement is met.
入力:
- Operator: Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=), Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank = Equal to (=) — Choose the relationship of first operand to the second operand.
- First operand: * — Enter a value name defined by a previous action, text, number or expression to compare with the second operand.
- Second operand: * — Enter a value name produced by a previous action, text, number or expression to compare with the first operand.

## If  `#if`
Marks the beginning of a block of actions that is run if the condition specified in this statement is met.

## Switch  `#switch`
Dispatches execution to different parts of the switch body based on the value of the expression.
入力:
- Value to check: * — Enter a value name, text, or number to compare with the following cases.
