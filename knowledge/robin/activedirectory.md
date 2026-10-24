# Robin: ActiveDirectory

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## ActiveDirectory.CloseConnection [A]
```
ActiveDirectory.CloseConnection ParentDirectoryEntry: ParentDirectoryEntry
```
入力: !ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### ActiveDirectory.ConnectToServer のセレクター: ConnectToServer, ConnectToServerWithAuthentication

## ActiveDirectory.ConnectToServer.ConnectToServer [A]
```
ActiveDirectory.ConnectToServer.ConnectToServer LdapPath: $'''example''' ParentDirectoryEntry=> ParentDirectoryEntry
```
入力: LdapPath:String
出力: ParentDirectoryEntry:ActiveDirectoryEntry=>
ON ERROR可: ActiveDirectoryError, AuthenticationError, InvalidOperationError, ServerNotOperationalError, UnauthorizedAccessError
固定: UseAuthentication=False

## ActiveDirectory.ConnectToServer.ConnectToServerWithAuthentication [A]
```
ActiveDirectory.ConnectToServer.ConnectToServerWithAuthentication Username: $'''example''' Password: $'''password''' AuthenticationType: ActiveDirectory.AuthenticationTypes.Secure LdapPath: $'''example''' ParentDirectoryEntry=> ParentDirectoryEntry
```
入力: !Username:String !Password:EncryptableObject !AuthenticationType:AuthenticationTypes{None,Secure,Encryption,SecureSocketsLayer,ReadonlyServer,Anonymous,FastBind,Signing,Sealing,Delegation,ServerBind} !LdapPath:String
出力: ParentDirectoryEntry:ActiveDirectoryEntry=>ParentDirectoryEntry
ON ERROR可: ActiveDirectoryError, AuthenticationError, InvalidOperationError, ServerNotOperationalError, UnauthorizedAccessError
固定: UseAuthentication=True

## ActiveDirectory.CreateGroup [A]
```
ActiveDirectory.CreateGroup ParentDirectoryEntry: ParentDirectoryEntry GroupName: $'''example''' Location: $'''''' GroupScope: ActiveDirectory.GroupScope.GlobalScope GroupType: ActiveDirectory.GroupType.Security Description: $'''example'''
```
入力: Description:String GroupName:String GroupScope:GroupScope{LocalScope,GlobalScope,UniversalScope} GroupType:GroupType{Security,Distribution} Location:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.CreateObject [A]
```
ActiveDirectory.CreateObject ParentDirectoryEntry: ParentDirectoryEntry ObjectType: ActiveDirectory.ObjectType.Computer ObjectName: $'''example''' Location: $'''example'''
```
入力: Location:String ObjectName:String ObjectType:ObjectType{Computer,OrganizationalUnit} ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.CreateUser [A]
```
ActiveDirectory.CreateUser ParentDirectoryEntry: ParentDirectoryEntry FirstName: $'''example''' Username: $'''example''' Password: $'''password''' PasswordNeverExpires: False DisabledAccount: False Initials: $'''example''' LastName: $'''example''' Location: $'''example'''
```
入力: DisabledAccount:Boolean FirstName:String Initials:String LastName:String Location:String Password:EncryptableObject PasswordNeverExpires:Boolean Username:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError

## ActiveDirectory.DeleteObject [A]
```
ActiveDirectory.DeleteObject ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.GetGroupInfo [A]
```
ActiveDirectory.GetGroupInfo ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' GroupInfo=> GroupInfo
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
出力: GroupInfo:GroupInfo=>
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.GetGroupMembers [A]
```
ActiveDirectory.GetGroupMembers ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' GroupMembers=> GroupMembers
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
出力: GroupMembers:List=>
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.GetUserInfo [A]
```
ActiveDirectory.GetUserInfo ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' UserInfo=> UserInfo
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
出力: UserInfo:UserInfo=>
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

### ActiveDirectory.ModifyGroup のセレクター: AddUserToGroup, DeleteGroup, RemoveUserFromGroup, RenameGroup

## ActiveDirectory.ModifyGroup.AddUserToGroup [A]
```
ActiveDirectory.ModifyGroup.AddUserToGroup UserDistinguishedName: $'''example''' ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !UserDistinguishedName:String !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError
固定: Operation=AddUser

## ActiveDirectory.ModifyGroup.DeleteGroup [A]
```
ActiveDirectory.ModifyGroup.DeleteGroup ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError
固定: Operation=Delete

## ActiveDirectory.ModifyGroup.RemoveUserFromGroup [A]
```
ActiveDirectory.ModifyGroup.RemoveUserFromGroup UserDistinguishedName: $'''example''' ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !UserDistinguishedName:String !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError
固定: Operation=RemoveUser

## ActiveDirectory.ModifyGroup.RenameGroup [A]
```
ActiveDirectory.ModifyGroup.RenameGroup ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' NewName: $'''example'''
```
入力: DistinguishedName:String NewName:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError
固定: Operation=Rename

### ActiveDirectory.ModifyUser のセレクター: DeleteUser, DisableUser, EnableUser, RenameUser, ResetUserPassword

## ActiveDirectory.ModifyUser.DeleteUser [A]
```
ActiveDirectory.ModifyUser.DeleteUser ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
固定: Operation=Delete

## ActiveDirectory.ModifyUser.DisableUser [A]
```
ActiveDirectory.ModifyUser.DisableUser ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
固定: Operation=EnableDisable, EnableUser=False

## ActiveDirectory.ModifyUser.EnableUser [A]
```
ActiveDirectory.ModifyUser.EnableUser ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
固定: Operation=EnableDisable, EnableUser=True

## ActiveDirectory.ModifyUser.RenameUser [A]
```
ActiveDirectory.ModifyUser.RenameUser ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' NewName: $'''example'''
```
入力: !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String !NewName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
固定: Operation=Rename

## ActiveDirectory.ModifyUser.ResetUserPassword [A]
```
ActiveDirectory.ModifyUser.ResetUserPassword NewPassword: $'''password''' ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: !NewPassword:EncryptableObject !ParentDirectoryEntry:ActiveDirectoryEntry !DistinguishedName:String
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidAttributeSyntaxError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
固定: Operation=ResetPassword

## ActiveDirectory.MoveObject [A]
```
ActiveDirectory.MoveObject ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' MoveToLocation: $'''example'''
```
入力: DistinguishedName:String MoveToLocation:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, LocationCannotBeEmpty, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.RenameObject [A]
```
ActiveDirectory.RenameObject ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' NewName: $'''example'''
```
入力: DistinguishedName:String NewName:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectAlreadyExistsError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.UnlockUser [A]
```
ActiveDirectory.UnlockUser ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example'''
```
入力: DistinguishedName:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, UnauthorizedAccessError

## ActiveDirectory.UpdateUserInfo [A]
```
ActiveDirectory.UpdateUserInfo ParentDirectoryEntry: ParentDirectoryEntry DistinguishedName: $'''example''' Country: ActiveDirectory.Countries.None City: $'''example''' Company: $'''example''' DisplayName: $'''example''' Email: $'''example''' Extension: $'''example''' FirstName: $'''example''' Initials: $'''example''' LastName: $'''example''' PostalCode: $'''example''' State: $'''example''' TelephoneNumber: $'''example''' Title: $'''example'''
```
入力: City:String Company:String Country:Countries{None,Afghanistan,AlandIslands,Albania,Algeria,AmericanSamoa,Andorra,Angola,Anguilla,Antarctica,AntiguaandBarbuda,Argentina,Armenia,Aruba,Australia,Austria,Azerbaijan,Bahamas,Bahrain,Bangladesh,Barbados,Belarus,Belgium,Belize,Benin,Bermuda,Bhutan,BolivarianRepublicOfVenezuela,Bonaire,BosniaandHerzegovina,Botswana,BouvetIsland,Brazil,BritishIndianOceanTerritory,BruneiDarussalam,Bulgaria,BurkinaFaso,Burundi,CaboVerde,Cambodia,Cameroon,Canada,CaymanIslands,CentralAfricanRepublic,Chad,Chile,China,ChristmasIsland,CocosKeelingIslands,Colombia,Comoros,Congo,CookIslands,CostaRica,Croatia,Cuba,Curacao,Cyprus,CzechRepublic,IvoryCoast,DemocraticPeoplesRepublicOfKorea,DemocraticRepublicOftheCongo,Denmark,Djibouti,Dominica,DominicanRepublic,Ecuador,Egypt,ElSalvador,EquatorialGuinea,Eritrea,Estonia,Ethiopia,FalklandIslandsMalvinas,FaroeIslands,Fiji,Finland,France,FrenchGuiana,FrenchPolynesia,FrenchSouthernTerritories,Gabon,Gambia,Georgia,Germany,Ghana,Gibraltar,Greece,Greenland,Grenada,Guadeloupe,Guam,Guatemala,Guernsey,Guinea,GuineaBissau,Guyana,Haiti,HeardIslandandMcDonaldIslands,HolySee,Honduras,HongKong,Hungary,Iceland,India,Indonesia,Iraq,Ireland,IslamicRepublicOfIran,IsleOfMan,Israel,Italy,Jamaica,Japan,Jersey,Jordan,Kazakhstan,Kenya,Kiribati,Kuwait,Kyrgyzstan,LaoPeoplesDemocraticRepublic,Latvia,Lebanon,Lesotho,Liberia,Libya,Liechtenstein,Lithuania,Luxembourg,Macao,Madagascar,Malawi,Malaysia,Maldives,Mali,Malta,MarshallIslands,Martinique,Mauritania,Mauritius,Mayotte,Mexico,Micronesia,Moldova,Monaco,Mongolia,Montenegro,Montserrat,Morocco,Mozambique,Myanmar,Namibia,Nauru,Nepal,Netherlands,NewCaledonia,NewZealand,Nicaragua,Niger,Nigeria,Niue,NorfolkIsland,RepublicOfMacedoniatheformerYugoslav,NorthernMarianaIslands,Norway,Oman,Pakistan,Palau,Palestine,Panama,PapuaNewGuinea,Paraguay,Peru,Philippines,Pitcairn,Poland,Portugal,PuertoRico,Qatar,RepublicOfKorea,Reunion,Romania,Russia,Rwanda,SaintBarthelemy,SaintHelena,SaintKittsandNevis,SaintLucia,SaintMartinFrenchpart,SaintPierreandMiquelon,SaintVincentandtheGrenadines,Samoa,SanMarino,SaoTomeandPrincipe,SaudiArabia,Senegal,Serbia,Seychelles,SierraLeone,Singapore,SintMaartenDutchpart,Slovakia,Slovenia,SolomonIslands,Somalia,SouthAfrica,SouthGeorgiaandtheSouthSandwichIslands,SouthSudan,Spain,SriLanka,StateOfBoliviaPlurinational,Sudan,Suriname,SvalbardandJanMayen,Swaziland,Sweden,Switzerland,SyrianArabRepublic,Taiwan,Tajikistan,Tanzania,Thailand,TimorLeste,Togo,Tokelau,Tonga,TrinidadandTobago,Tunisia,Turkey,Turkmenistan,TurksandCaicosIslands,Tuvalu,Uganda,Ukraine,UnitedArabEmirates,UnitedKingdomOfGreatBritainandNorthernIreland,UnitedStatesMinorOutlyingIslands,UnitedStatesOfAmerica,Uruguay,Uzbekistan,Vanuatu,Vietnam,VirginIslandsBritish,VirginIslandsUS,WallisandFutuna,Yemen,Zambia,Zimbabwe} DisplayName:String DistinguishedName:String Email:String Extension:String FirstName:String Initials:String LastName:String PostalCode:String State:String TelephoneNumber:String Title:String ParentDirectoryEntry:ActiveDirectoryEntry
ON ERROR可: ActiveDirectoryEntryNotFound, ActiveDirectoryError, AuthenticationError, InvalidOperationError, ObjectDoesNotExistOnServerError, ServerNotOperationalError, SetOrUpdatePasswordError, UnauthorizedAccessError
