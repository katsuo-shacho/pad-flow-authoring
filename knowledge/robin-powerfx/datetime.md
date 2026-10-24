# Robin: DateTime

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## DateTime.Add [A]
```
DateTime.Add DateTime: $fx'2025-01-01' TimeToAdd: 0 TimeUnit: DateTime.TimeUnit.Days ResultedDate=> ResultedDate
```
入力: DateTime:DateTime TimeToAdd:Int32 TimeUnit:TimeUnit{Seconds,Minutes,Hours,Days,Months,Years}
出力: ResultedDate:DateTime=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### DateTime.GetCurrentDateTime のセレクター: Current, CustomOffset, CustomTimeZone, Local, Windows

## DateTime.GetCurrentDateTime.Current [A]
```
DateTime.GetCurrentDateTime.Current DateTimeFormat: DateTime.DateTimeFormat.DateAndTime Offset: $fx'example' CurrentDateTime=> CurrentDateTime
```
入力: !DateTimeFormat:DateTimeFormat{DateAndTime,DateOnly} !Offset:String
出力: CurrentDateTime:DateTime=>CurrentDateTime
ON ERROR可: CountryOrRegionNotFoundError, GetCurrentDateTimeError
固定: TimeZoneMode=Specific

## DateTime.GetCurrentDateTime.CustomOffset [A]
```
DateTime.GetCurrentDateTime.CustomOffset CustomOffset: 1.0 DateTimeFormat: DateTime.DateTimeFormat.DateAndTime CurrentDateTime=> CurrentDateTime
```
入力: !CustomOffset:Double !DateTimeFormat:DateTimeFormat{DateAndTime,DateOnly}
出力: CurrentDateTime:DateTime=>CurrentDateTime
ON ERROR可: CountryOrRegionNotFoundError, GetCurrentDateTimeError
固定: TimeZoneMode=Custom, InputType=Offset

## DateTime.GetCurrentDateTime.CustomTimeZone [A]
```
DateTime.GetCurrentDateTime.CustomTimeZone CustomTimeZone: $fx'example' DateTimeFormat: DateTime.DateTimeFormat.DateAndTime CurrentDateTime=> CurrentDateTime
```
入力: !CustomTimeZone:String !DateTimeFormat:DateTimeFormat{DateAndTime,DateOnly}
出力: CurrentDateTime:DateTime=>CurrentDateTime
ON ERROR可: CountryOrRegionNotFoundError, GetCurrentDateTimeError
固定: TimeZoneMode=Custom, InputType=Windows

## DateTime.GetCurrentDateTime.Local [A]
```
DateTime.GetCurrentDateTime.Local DateTimeFormat: DateTime.DateTimeFormat.DateAndTime CurrentDateTime=> CurrentDateTime
```
入力: DateTimeFormat:DateTimeFormat{DateAndTime,DateOnly}
出力: CurrentDateTime:DateTime=>
ON ERROR可: CountryOrRegionNotFoundError, GetCurrentDateTimeError
固定: TimeZoneMode=System

## DateTime.GetCurrentDateTime.Windows [A]
```
DateTime.GetCurrentDateTime.Windows TimeZoneLocation: DateTime.TimeZoneLocation.UTC DateTimeFormat: DateTime.DateTimeFormat.DateAndTime CurrentDateTime=> CurrentDateTime
```
入力: !TimeZoneLocation:TimeZoneLocation{DatelineStandardTime,UTC11,AleutianStandardTime,HawaiianStandardTime,MarquesasStandardTime,AlaskanStandardTime,UTC09,PacificStandardTimeMexico,UTC08,PacificStandardTime,USMountainStandardTime,MountainStandardTimeMexico,MountainStandardTime,YukonStandardTime,CentralAmericaStandardTime,CentralStandardTime,EasterIslandStandardTime,CentralStandardTimeMexico,CanadaCentralStandardTime,SAPacificStandardTime,EasternStandardTimeMexico,EasternStandardTime,HaitiStandardTime,CubaStandardTime,USEasternStandardTime,TurksAndCaicosStandardTime,ParaguayStandardTime,AtlanticStandardTime,VenezuelaStandardTime,CentralBrazilianStandardTime,SAWesternStandardTime,PacificSAStandardTime,NewfoundlandStandardTime,TocantinsStandardTime,ESouthAmericaStandardTime,SAEasternStandardTime,ArgentinaStandardTime,GreenlandStandardTime,MontevideoStandardTime,MagallanesStandardTime,SaintPierreStandardTime,BahiaStandardTime,UTC02,MidAtlanticStandardTime,AzoresStandardTime,CapeVerdeStandardTime,UTC,GMTStandardTime,GreenwichStandardTime,SaoTomeStandardTime,MoroccoStandardTime,WEuropeStandardTime,CentralEuropeStandardTime,RomanceStandardTime,CentralEuropeanStandardTime,WCentralAfricaStandardTime,GTBStandardTime,MiddleEastStandardTime,EgyptStandardTime,EEuropeStandardTime,SyriaStandardTime,WestBankStandardTime,SouthAfricaStandardTime,FLEStandardTime,IsraelStandardTime,SouthSudanStandardTime,KaliningradStandardTime,SudanStandardTime,LibyaStandardTime,NamibiaStandardTime,JordanStandardTime,ArabicStandardTime,TurkeyStandardTime,ArabStandardTime,BelarusStandardTime,RussianStandardTime,EAfricaStandardTime,VolgogradStandardTime,IranStandardTime,ArabianStandardTime,AstrakhanStandardTime,AzerbaijanStandardTime,RussiaTimeZone3,MauritiusStandardTime,SaratovStandardTime,GeorgianStandardTime,CaucasusStandardTime,AfghanistanStandardTime,WestAsiaStandardTime,EkaterinburgStandardTime,PakistanStandardTime,QyzylordaStandardTime,IndiaStandardTime,SriLankaStandardTime,NepalStandardTime,BangladeshStandardTime,CentralAsiaStandardTime,OmskStandardTime,MyanmarStandardTime,SEAsiaStandardTime,AltaiStandardTime,WMongoliaStandardTime,NorthAsiaStandardTime,NCentralAsiaStandardTime,TomskStandardTime,ChinaStandardTime,NorthAsiaEastStandardTime,SingaporeStandardTime,WAustraliaStandardTime,TaipeiStandardTime,UlaanbaatarStandardTime,AusCentralWStandardTime,TransbaikalStandardTime,TokyoStandardTime,NorthKoreaStandardTime,KoreaStandardTime,YakutskStandardTime,CenAustraliaStandardTime,AUSCentralStandardTime,EAustraliaStandardTime,AUSEasternStandardTime,WestPacificStandardTime,TasmaniaStandardTime,VladivostokStandardTime,LordHoweStandardTime,BougainvilleStandardTime,RussiaTimeZone10,MagadanStandardTime,NorfolkStandardTime,SakhalinStandardTime,CentralPacificStandardTime,RussiaTimeZone11,NewZealandStandardTime,UTC12,FijiStandardTime,KamchatkaStandardTime,ChathamIslandsStandardTime,UTC13,TongaStandardTime,SamoaStandardTime,LineIslandsStandardTime} !DateTimeFormat:DateTimeFormat{DateAndTime,DateOnly}
出力: CurrentDateTime:DateTime=>CurrentDateTime
ON ERROR可: CountryOrRegionNotFoundError, GetCurrentDateTimeError
固定: TimeZoneMode=Windows

## DateTime.Subtract [A]
```
DateTime.Subtract FromDate: $fx'2025-01-01' SubstractDate: $fx'2025-01-01' TimeUnit: DateTime.DifferenceTimeUnit.Days TimeDifference=> TimeDifference
```
入力: FromDate:DateTime SubstractDate:DateTime TimeUnit:DifferenceTimeUnit{Seconds,Minutes,Hours,Days}
出力: TimeDifference:Decimal=>
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）
