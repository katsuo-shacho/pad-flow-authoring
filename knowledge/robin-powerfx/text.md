# Robin: Text

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## Text.AppendLine [A]
```
Text.AppendLine Text: OutputText LineToAppend: CellValue Result=> OutputText
```
入力: LineToAppend:String Text:String
出力: Result:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Text.ChangeCase [A]
```
Text.ChangeCase Text: $fx'' NewCase: Text.CaseOption.UpperCase Result=> TextWithNewCase
```
入力: NewCase:CaseOption{UpperCase,LowerCase,TitleCase,SentenceCase} Text:String
出力: Result:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.ConvertDateTimeToText のセレクター: FromCustomDateTime, FromDateTime

## Text.ConvertDateTimeToText.FromCustomDateTime [A]
```
Text.ConvertDateTimeToText.FromCustomDateTime CustomFormat: $fx'example' DateTime: $fx'2025-01-01' Result=> FormattedDateTime
```
入力: !CustomFormat:String !DateTime:DateTime
出力: Result:String=>FormattedDateTime
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Format=Custom

## Text.ConvertDateTimeToText.FromDateTime [A]
```
Text.ConvertDateTimeToText.FromDateTime DateTime: $fx'2025-01-01' StandardFormat: Text.WellKnownDateTimeFormat.ShortDate Result=> FormattedDateTime
```
入力: DateTime:DateTime StandardFormat:WellKnownDateTimeFormat{ShortDate,LongDate,ShortTime,LongTime,FullDateTimeShortTime,FullDateTimeLongTime,GeneralDateTimeShortTime,GeneralDateTimeLongTime,SortableDateTime}
出力: Result:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Format=Standard

### Text.ConvertTextToDateTime のセレクター: ToDateTime, ToDateTimeCustomFormat

## Text.ConvertTextToDateTime.ToDateTime [A]
```
Text.ConvertTextToDateTime.ToDateTime Text: $fx'example' DateTime=> TextAsDateTime
```
入力: Text:String
出力: DateTime:DateTime=>
ON ERROR可: TextNotValidDateTimeError
固定: DateIsInCustomFormat=False

## Text.ConvertTextToDateTime.ToDateTimeCustomFormat [A]
```
Text.ConvertTextToDateTime.ToDateTimeCustomFormat Text: $fx'example' CustomFormat: $fx'example' DateTime=> TextAsDateTime
```
入力: !Text:String !CustomFormat:String
出力: DateTime:DateTime=>TextAsDateTime
ON ERROR可: TextNotValidDateTimeError
固定: DateIsInCustomFormat=True

## Text.CreateHTMLContent [A]
```
Text.CreateHTMLContent HtmlEditor: $fx'example' HtmlContent=> HtmlContent
```
入力: HtmlEditor:String
出力: HtmlContent:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.CropText のセレクター: CropTextAfterFlag, CropTextBeforeFlag, CropTextBetweenFlags

## Text.CropText.CropTextAfterFlag [A]
```
Text.CropText.CropTextAfterFlag IgnoreCase: False FromFlag: $fx'example' Text: $fx'example' IsFlagFound=> IsFlagFound CroppedText=> CroppedText
```
入力: !IgnoreCase:Boolean !FromFlag:String !Text:String
出力: IsFlagFound:Boolean=>IsFlagFound CroppedText:String=>CroppedText
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Mode=GetTextAfterFlag

## Text.CropText.CropTextBeforeFlag [A]
```
Text.CropText.CropTextBeforeFlag Text: $fx'example' ToFlag: $fx'example' IgnoreCase: False CroppedText=> CroppedText IsFlagFound=> IsFlagFound
```
入力: Text:String ToFlag:String IgnoreCase:Boolean
出力: CroppedText:String=> IsFlagFound:Boolean=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Mode=GetTextBeforeFlag

## Text.CropText.CropTextBetweenFlags [A]
```
Text.CropText.CropTextBetweenFlags ToFlag: $fx'example' IgnoreCase: False FromFlag: $fx'example' Text: $fx'example' IsFlagFound=> IsFlagFound CroppedText=> CroppedText
```
入力: !ToFlag:String !IgnoreCase:Boolean !FromFlag:String !Text:String
出力: IsFlagFound:Boolean=>IsFlagFound CroppedText:String=>CroppedText
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: Mode=GetTextBetweenFlags

## Text.EscapeForRegularExpression [A]
```
Text.EscapeForRegularExpression Text: $fx'example' EscapedText=> EscapedText
```
入力: Text:String
出力: EscapedText:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Text.FromNumber [A]
```
Text.FromNumber Number: 1.0 DecimalPlaces: 2 UseThousandsSeparator: True FormattedNumber=> FormattedNumber
```
入力: DecimalPlaces:Int32 Number:Decimal UseThousandsSeparator:Boolean
出力: FormattedNumber:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.GetSubtext のセレクター: GetSubtext, GetSubtextFrom, GetSubtextFromStartTo, GetText

## Text.GetSubtext.GetSubtext [A]
```
Text.GetSubtext.GetSubtext Text: $fx'example' CharacterPosition: 1 NumberOfChars: 1 Subtext=> Subtext
```
入力: CharacterPosition:Int32 NumberOfChars:Int32 Text:String
出力: Subtext:String=>
ON ERROR可: StartIndexOrLengthOutOfRangeError
固定: StartIndex=CharacterPosition, Length=NumberOfChars

## Text.GetSubtext.GetSubtextFrom [A]
```
Text.GetSubtext.GetSubtextFrom Text: $fx'example' CharacterPosition: 1 Subtext=> Subtext
```
入力: !Text:String !CharacterPosition:Int32
出力: Subtext:String=>Subtext
ON ERROR可: StartIndexOrLengthOutOfRangeError
固定: StartIndex=CharacterPosition, Length=EndOfText

## Text.GetSubtext.GetSubtextFromStartTo [A]
```
Text.GetSubtext.GetSubtextFromStartTo Text: $fx'example' NumberOfChars: 1 Subtext=> Subtext
```
入力: !Text:String !NumberOfChars:Int32
出力: Subtext:String=>Subtext
ON ERROR可: StartIndexOrLengthOutOfRangeError
固定: StartIndex=StartOfText, Length=NumberOfChars

## Text.GetSubtext.GetText [A]
```
Text.GetSubtext.GetText Text: $fx'example' Subtext=> Subtext
```
入力: !Text:String
出力: Subtext:String=>Subtext
ON ERROR可: StartIndexOrLengthOutOfRangeError
固定: StartIndex=StartOfText, Length=EndOfText

### Text.JoinText のセレクター: Join, JoinWithCustomDelimiter, JoinWithDelimiter

## Text.JoinText.Join [A]
```
Text.JoinText.Join List: FileList Result=> JoinedText
```
入力: List:List
出力: Result:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: DelimiterType=None

## Text.JoinText.JoinWithCustomDelimiter [A]
```
Text.JoinText.JoinWithCustomDelimiter List: List CustomDelimiter: $fx'example' Result=> JoinedText
```
入力: !List:List<String> !CustomDelimiter:String
出力: Result:String=>JoinedText
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: DelimiterType=Custom

## Text.JoinText.JoinWithDelimiter [A]
```
Text.JoinText.JoinWithDelimiter List: List StandardDelimiter: Text.StandardDelimiter.Space DelimiterTimes: 1 Result=> JoinedText
```
入力: !List:List<String> !StandardDelimiter:StandardDelimiter{Space,Tab,NewLine} !DelimiterTimes:Int32
出力: Result:String=>JoinedText
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: DelimiterType=Standard

## Text.Pad [A]
```
Text.Pad Text: $fx'' PadPosition: Text.PadPosition.Left TotalLength: 10 PaddingText: $fx'example' PaddedText=> PaddedText
```
入力: PaddingText:String PadPosition:PadPosition{Left,Right} Text:String TotalLength:Int32
出力: PaddedText:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.ParseText のセレクター: Parse, ParseForFirstOccurrence, RegexParse, RegexParseForFirstOccurrence

## Text.ParseText.Parse [A]
```
Text.ParseText.Parse StartingPosition: 0 Text: $fx'example' TextToFind: $fx'example' IgnoreCase: False OccurrencePositions=> Positions
```
入力: !StartingPosition:Int32 !Text:String !TextToFind:String !IgnoreCase:Boolean
出力: OccurrencePositions:List<Int32>=>Positions
ON ERROR可: InvalidRegexError
固定: IsRegEx=False, FirstOccurrenceOnly=False

## Text.ParseText.ParseForFirstOccurrence [A]
```
Text.ParseText.ParseForFirstOccurrence Text: $fx'example' TextToFind: $fx'example' StartingPosition: 0 IgnoreCase: False OccurrencePosition=> Position
```
入力: IgnoreCase:Boolean StartingPosition:Int32 Text:String TextToFind:String
出力: OccurrencePosition:Int32=>
ON ERROR可: InvalidRegexError
固定: IsRegEx=False, FirstOccurrenceOnly=True

## Text.ParseText.RegexParse [A]
```
Text.ParseText.RegexParse StartingPosition: 0 Text: $fx'example' TextToFind: $fx'example' IgnoreCase: False OccurrencePositions=> Positions Matches=> Matches
```
入力: !StartingPosition:Int32 !Text:String !TextToFind:String !IgnoreCase:Boolean
出力: OccurrencePositions:List<Int32>=>Positions Matches:List<String>=>Matches
ON ERROR可: InvalidRegexError
固定: IsRegEx=True, FirstOccurrenceOnly=False

## Text.ParseText.RegexParseForFirstOccurrence [A]
```
Text.ParseText.RegexParseForFirstOccurrence StartingPosition: 0 Text: $fx'example' TextToFind: $fx'example' IgnoreCase: False OccurrencePosition=> Position Match=> Match
```
入力: !StartingPosition:Int32 !Text:String !TextToFind:String !IgnoreCase:Boolean
出力: OccurrencePosition:Int32=>Position Match:String=>Match
ON ERROR可: InvalidRegexError
固定: IsRegEx=True, FirstOccurrenceOnly=True

## Text.Random [A]
```
Text.Random UseUpperCaseLetters: True UseLowerCaseLetters: True UseDigits: True UseSymbols: True MinimumLength: 6 MaximumLength: 10 RandomText=> RandomText
```
入力: MaximumLength:Int32 MinimumLength:Int32 UseDigits:Boolean UseLowerCaseLetters:Boolean UseSymbols:Boolean UseUpperCaseLetters:Boolean
出力: RandomText:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## Text.RecognizeEntitiesInText [A]
```
Text.RecognizeEntitiesInText Text: $fx'example' Mode: Text.RecognizerMode.DateTime Language: Text.RecognizerLanguage.English RecognizedEntities=> RecognizedEntities
```
入力: Language:RecognizerLanguage{English,Chinese,Spanish,SpanishMexican,Portuguese,French,German,Italian,Japanese,Dutch,Korean,Swedish,Turkish,Hindi} Mode:RecognizerMode{DateTime,Dimension,Temperature,Currency,NumberRange,Number,Ordinal,Percentage,PhoneNumber,Email,IpAddress,Mention,Hashtag,Url,Guid,QuotedText} Text:String
出力: RecognizedEntities:DataTable=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.Replace のセレクター: ReplaceText, ReplaceTextWithRegex

## Text.Replace.ReplaceText [A]
```
Text.Replace.ReplaceText Text: $fx'example' TextToFind: $fx'example' IgnoreCase: False ReplaceWith: $fx'example' ActivateEscapeSequences: False ComparisonType: Text.TextComparisonType.CultureSensitive Result=> Replaced
```
入力: ActivateEscapeSequences:Boolean ComparisonType:TextComparisonType{CultureSensitive,Ordinal} IgnoreCase:Boolean ReplaceWith:String Text:String TextToFind:String
出力: Result:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: IsRegEx=False

## Text.Replace.ReplaceTextWithRegex [A]
```
Text.Replace.ReplaceTextWithRegex Text: $fx'example' TextToFind: $fx'example' ReplaceWith: $fx'example' ActivateEscapeSequences: False IgnoreCase: False Result=> Replaced
```
入力: !Text:String !TextToFind:String !ReplaceWith:String !ActivateEscapeSequences:Boolean !IgnoreCase:Boolean
出力: Result:String=>Replaced
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
固定: IsRegEx=True

## Text.Reverse [A]
```
Text.Reverse Text: $fx'example' ReversedText=> ReversedText
```
入力: Text:String
出力: ReversedText:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Text.SplitText のセレクター: Split, SplitAtNumberOfCharacters, SplitWithDelimiter

## Text.SplitText.Split [A]
```
Text.SplitText.Split Text: $fx'example' StandardDelimiter: Text.StandardDelimiter.Space DelimiterTimes: 1 Result=> TextList
```
入力: DelimiterTimes:Int32 StandardDelimiter:StandardDelimiter{Space,Tab,NewLine} Text:String
出力: Result:List=>
ON ERROR可: InvalidRegexError
固定: DelimiterType=Standard

## Text.SplitText.SplitAtNumberOfCharacters [A]
```
Text.SplitText.SplitAtNumberOfCharacters SplitInterval: 1 Text: $fx'example' Result=> TextList
```
入力: !SplitInterval:Int32 !Text:String
出力: Result:List<String>=>TextList
ON ERROR可: InvalidRegexError
固定: DelimiterType=NumberOfCharacters

## Text.SplitText.SplitWithDelimiter [A]
```
Text.SplitText.SplitWithDelimiter Text: $fx'example' IsRegEx: False CustomDelimiter: $fx'example' Result=> TextList
```
入力: !Text:String !IsRegEx:Boolean !CustomDelimiter:String
出力: Result:List<String>=>TextList
ON ERROR可: InvalidRegexError
固定: DelimiterType=Custom

## Text.ToNumber [A]
```
Text.ToNumber Text: $fx'example' Number=> TextAsNumber
```
入力: Text:String
出力: Number:Decimal=>
ON ERROR可: TextNotValidNumberError

## Text.Trim [A]
```
Text.Trim Text: $fx'' TrimOption: Text.TrimOption.Both TrimmedText=> TrimmedText
```
入力: Text:String TrimOption:TrimOption{FromStart,ToEnd,Both}
出力: TrimmedText:String=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
