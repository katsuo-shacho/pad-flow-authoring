# Flow control actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/flowcontrol （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Flow control is the act of controlling the order in which actions and subflows run. Power Automate enables you to implement flow control through the flow control actions. In conjunction with the safe stop capability available in the Power Automate portal, you can trigger the If safe stop is requested action in the desktop flow run details page or directly within the flow designer for debugging purposes. This action enables controlled termination of a running flow. For more information, see Safe stop. To intentionally raise user-defined errors during a desktop flow's execution, you can use the 

## If safe stop requested  `#ifsafestopaction`
Checks whether safe stop is requested for the specific flow.
入力:
- Stop the flow: Boolean value = False — Indicates whether the flow's execution should be terminated after the completion of the specific block of actions or if the execution should continue. Note that if you choose to continue execution, you need to manually add a Stop Flow action to terminate the flow.

## Comment  `#comment`
User comment.
入力:
- Comment(任意): Text value — User comment

## End  `#end`
Signifies the end of a block.

## End region  `#endregion`
Marks the end of a group of actions.

## Exit subflow  `#exitfunction`
Exits current subflow and returns to the point it was called from.

## Get last error  `#getlasterror`
Retrieves the last error that occurred in the flow.
入力:
- Clear error: Boolean value = False — After the action stores the error in the variable, it clears the error so that the next time the action retrieves an error, it doesn't retrieve the same error value
出力:
- LastError: Error — The details of the error that last occurred in the flow

## Go to  `#goto`
Transfers the flow of execution to another point, indicated by a label.
入力:
- Go to label: Text value — Label in the flow

## Label  `#label`
Acts as the destination of a 'go to' statement.
入力:
- Label name: Text value — Label in the program

## Throw custom error
Raises a user-defined error by using a specified error name and message. By using this action, the flow can intentionally trigger a custom exception during runtime. You must place this action inside an On block error action, where you configure and handle its corresponding custom error entry.
入力:
- Error name: Text value = None — The name of the custom error.
- Error message: Text value = None — The description of the custom error.

## On block error  `#block`
Marks the beginning of a block to handle actions errors.
入力:
- Name: Text value — The name of the Exception Block for Visual purposes only.
- Retry policy: None, Fixed, Exponential = None — The rules based on which retries are performed. Delays are estimated in seconds.
- Handle flow terminating errors: Boolean value = False — Expand the scope of error handling, also capturing logical errors in the flow, such as dividing a number by zero or trying to access an item from an out of bounds position.

## Region  `#region`
Marks the beginning of a group of actions.
入力:
- Name(任意): Text value — The name of the region.

## Run subflow  `#callfunction`
Runs a subflow and specifies any required arguments.
入力:
- Subflow name: Subflow — The name of the subflow to call
- Input as expression: Boolean value = False — Define whether the input should be handled as an expression. If enabled, use variables and expressions to dynamically determine the subflow during runtime.

## Stop flow  `#exit`
Terminates the flow.
入力:
- End flow: Successfully, With error message = Successfully — Terminate the execution of the flow, either successfully or with an error
- Error message: Text value — The error message to return to the flow caller upon exit

## Wait  `#wait`
Suspends the execution of the flow for a specified number of seconds.
入力:
- Duration: Numeric value — Time duration in seconds
