# Loops actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/loops （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Use loops to automate repetitive sections of your desktop flows and avoid running the same actions multiple times. The following list presents some useful applications and features of loops: * Use simple loops to perform a specific number of repetitions and iterate through data. * Deploy Loop condition to repeat actions until a condition is met. * Iterate through the items of a list using For each loops. * Explicitly end loops when required. To find more information on how to use loops, go to Use loops.

## Exit loop  `#break`
Terminates the loop and the flow resumes at the next action or statement following the loop.

## For each  `#foreach`
Iterates over items in a list, data table or data row, allowing a block of actions to be executed repeatedly.
入力:
- Value to iterate: * — Enter a list, data row, or data table value to iterate through it.
出力:
- *: The value name that will store the current item value in each iteration. — 

## Loop  `#loop`
Iterates a block of actions for a specified number of times
入力:
- Start from: Numeric value — Set the starting point of the loop counter.
- Increment by: Numeric value — Set the increment that the loop counter variable is increased by.
- End to: Numeric value — Set the ending point of the loop counter.
出力:
- *: The value name that will store the current index, starting at the start from value. The value will change by the increment with each iteration. — 

## Loop condition  `#while`
Iterates a block of actions as long as a specified condition proves to be true.
入力:
- Operator: Equal to (=), Not equal to (<>), Greater than (>), Greater than or equal to (>=), Less than (<), Less than or equal to (<=) = Equal to (=) — Choose the relationship of first operand to second operand.
- First operand: * — Enter a value name defined by a previous action, text, number or expression to compare with the second operand.
- Second operand: * — Enter a value name produced by a previous action, text, number or expression to compare with the first operand.

## Next loop  `#continue`
Forces the next iteration of the block to take place, skipping any actions in between.
