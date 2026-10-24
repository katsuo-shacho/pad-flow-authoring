# Date time actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/datetime （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Use the Get current date and time action to retrieve the current date and time (or date only, if selected) and store it in a variable. The date format depends on the Windows configuration. To find more information about the syntax of date and time values, go to Variable data types. To add various time units to date variables, deploy the Add to datetime action. To calculate the difference between two dates, use the Subtract dates action. You can retrieve the difference in seconds, minutes, hours, or days.

## Add to datetime  `#add`
Adds (or subtracts) a specific number of seconds, minutes, hours or days to a datetime value.
入力:
- Datetime: Datetime — The datetime value to alter
- Add: Numeric value — The numeric value to add. To subtract a time, the value should be negative. For example, add -7 days here to go back one week
- Time unit: Seconds, Minutes, Hours, Days, Months, Years = Seconds — The time unit the time to add represents
出力:
- ResultedDate: Datetime — The new, altered datetime value

## Subtract dates  `#subtract`
Finds the time difference between two given dates in days, hours, minutes, or seconds.
入力:
- From date: Datetime — The datetime to subtract the first datetime from. This will be the base datetime, so generally put the later date/time in this attribute
- Subtract date: Datetime — The datetime to subtract
- Get difference in: Seconds, Minutes, Hours, Days = Days — The unit of time to express the difference in
出力:
- TimeDifference: Numeric value — The difference in time as a numeric value

## Get current date and time  `#getcurrentdatetime`
Retrieves the current date or the current date and time.
入力:
- Retrieve: Current date and time, Current date only = Current date and time — Specify whether to get the date and time, or just the date. If the latter is chosen, the time value will be stored as midnight (0:00:00)
- Time zone: System time zone, Specific time zone (to be deprecated), Windows time zone, Custom input = System time zone — Specify whether to use the system's time zone or select a specific one or set up a time zone manually
- Country/region: Text value = Europe/Bucharest — The country/region to get the time of or add a numeric value as the hours that will be added in the UTC time zone
- Windows time zone: Available Windows time zones = (UTC) Coordinated Universal Time — Specify the country/region to obtain the time zone from
- Input Type: Offset, Windows time zone = Offset — Choose whether to set the offset via a numeric value or by providing a Windows format time zone
- Offset: Numeric value = N/A — Specify the number of hours the offset is going to be. Time format is UTC.
- Time zone: Text value = N/A — Specify the time zone (Windows time zone)
出力:
- CurrentDateTime: Datetime — The current datetime value
例外: Failed to get current date and time; Specified country/region not found
