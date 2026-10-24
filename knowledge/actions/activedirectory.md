# Active Directory actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/activedirectory （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Active Directory actions require a connection to an Active Directory server. Establish the connection using the Connect to server action and an LDAP path. The LDAP path specifies the domain controllers and should have the following format: ```LDAP path LDAP://DC=contoso,DC=demo ``` If you work with groups, objects, or users, you need to specify also their location. The Location field specifies the container and the domain controller, and should have the following format: ```LDAP path CN=Users,DC=contoso,DC=demo ``` After getting all the distinguished names using the dsquery user command, enter

## Create group  `#creategroup`
Creates a group in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Group name: Text value — The name of the newly created group
- Location(任意): Text value — The location that the group will be created in
- Description(任意): Text value — The description for the group
- Group scope: Local, Global, Universal = Global — The scope of the group in the Active Directory
- Group type: Security, Distribution = Security — The type of the group
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object already exists; Active Directory error

## Get group info  `#getgroupinfo`
Gets information about a group from the Active Directory server.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
出力:
- GroupInfo: Group info — The group's info
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error

## Get group members  `#getgroupmembers`
Gets the members of a group in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
出力:
- GroupMembers: List of Group members — The variable that holds the members of the group
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error

## Modify group  `#modifygroupaction`
Modifies a group in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
- Operation: Rename group, Delete group, Add user, Remove user = Rename group — Select the operation to perform
- New name: Text value — The new name for the group
- User distinguished name: Text value — Specify the user's distinguished name
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Object already exists; Active Directory error

## Create object  `#createobject`
Creates an object in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Location(任意): Text value — The location that the group will be created in
- Object type: Computer, Organizational unit = Computer — The type of the object
- Object name: Text value — The name of the newly created object
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object already exists; Invalid attribute syntax; Active Directory error

## Delete object  `#deleteobject`
Deletes an object in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error

## Move object  `#moveobject`
Moves an object in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
- Move to location: Text value — The location for the object to be moved to
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error; Location can't be empty

## Rename object  `#renameobject`
Renames an object in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
- New name: Text value — Type the new name for the group
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Object already exists; Active Directory error

## Create user  `#createuser`
Creates a user in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Location(任意): Text value — The location that the group will be created in
- First name: Text value — The first name of the user
- Initials(任意): Text value — The initials of the user
- Last name(任意): Text value — The last name of the user
- Username: Text value — The username of the user
- Password: Direct encrypted input or Text value — The password of the user
- Password never expires: Boolean value = False — Specify whether the password of the user will expire
- Disabled account: Boolean value = False — Specify whether the account will be disabled
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object already exists; Couldn't set or update password; Active Directory error

## Get user info  `#getuserinfo`
Gets a user's information in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
出力:
- UserInfo: User info — The user's info
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error

## Modify user  `#modifyuseraction`
Modify a user in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
- Operation: Enable/disable user, Rename user, Delete user, Reset password = Enable/disable user — Select the operation to be performed
- Enable user: Boolean value = False — Enable or disable the user
- New name: Text value — Type the new name for the group
- New password: Direct encrypted input or Text value — Type the new password for the group
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Object already exists; Invalid attribute syntax; Active Directory error; Couldn't set or update password

## Unlock user  `#unlockuser`
Unlocks an Active Directory user.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Active Directory error

## Update user info  `#updateuserinfo`
Updates a user's information in the Active Directory.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
- Distinguished name: Text value — The distinguished name of the Active Directory entry
- Display name(任意): Text value — The display name of the user
- First name(任意): Text value — The first name of the user
- Initials(任意): Text value — The initials of the user
- Last name(任意): Text value — The last name of the user
- Title(任意): Text value — The title of the user
- The email of the user(任意): Text value — The email of the user
- The company of the user(任意): Text value — The company of the user
- Telephone number(任意): Text value — The telephone number of the user
- Extension(任意): Text value — The extension of the user
- City(任意): Text value — The city of the user
- Postal code(任意): Text value — The postal code of the user
- State(任意): Text value — The state of the user
- Country: Afghanistan, Åland Islands, Albania, Algeria, American Samoa, Andorra, Angola, Anguilla, Antarctica, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bermuda, Bhutan, State of Bolivia Plurinational, Bonaire, Bosnia and Herzegovina, Botswana, Bouvet Island, Brazil, British Indian Ocean Territory, Brunei Darussalam, Bulgaria, Burkina Faso, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Cayman Islands, Central African Republic, Chad, Chile, China, Christmas Island, Cocos (Keeling) Islands, Colombia, Comoros, Congo, Democratic Republic of the Congo, Cook Islands, Costa Rica, Côte d'Ivoire, Croatia, Cuba, Curaçao, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Ethiopia, Falkland Islands, Faroe Islands, Fiji, Finland, France, French Guiana, French Polynesia, French Southern Territories, Gabon, Gambia, Georgia, Germany, Ghana, Gibraltar, Greece, Greenland, Grenada, Guadeloupe, Guam, Guatemala, Guernsey, Guinea, Guinea-Bissau, Guyana, Haiti, Heard Island and McDonald Islands, Holy See, Honduras, Hong Kong Special Administrative Region, Hungary, Iceland, India, Indonesia, Islamic Republic of Iran, Iraq, Ireland, Isle of Man, Israel, Italy, Jamaica, Japan, Jersey, Jordan, Kazakhstan, Kenya, Kiribati, Democratic Peoples Republic of Korea, Republic of Korea, Kuwait, Kyrgyzstan, Lao People's Democratic Republic, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, Luxembourg, Macao Special Administrative Region, North Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Martinique, Mauritania, Mauritius, Mayotte, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Montserrat, Morocco, Mozambique, Myanmar, Namibia, Nauru, Nepal, Netherlands, New Caledonia, New Zealand, Nicaragua, Niger, Nigeria, Niue, Norfolk Island, Northern Mariana Islands, Norway, Oman, Pakistan, Palau, Palestinian Authority, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Pitcairn, Poland, Portugal, Puerto Rico, Qatar, Réunion, Romania, Russia, Rwanda, Saint Barthélemy, Saint Helena, Ascension, Tristan da Cunha, Saint Kitts and Nevis, Saint Lucia, Saint Martin (French part), Saint Pierre and Miquelon, Saint Vincent and the Grenadines, Samoa, San Marino, São Tomé and Príncipe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Sint Maarten (Dutch part), Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Georgia and the South Sandwich Islands, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Svalbard and Jan Mayen, Swaziland, Sweden, Switzerland, Syrian Arab Republic, Taiwan, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Tokelau, Tonga, Trinidad and Tobago, Tunisia, Türkiye, Turkmenistan, Turks and Caicos Islands, Tuvalu, Uganda, Ukraine, United Arab Emirates, United Kingdom of Great Britain and Northern Ireland, United States of America, United States Minor Outlying Islands, Uruguay, Uzbekistan, Vanuatu, Bolivarian Republic of Venezuela, Vietnam, Virgin Islands (British), Virgin Islands (U.S.), Wallis and Futuna, Yemen, Zambia, Zimbabwe, None = None — The country of the user as a two-letter code (ISO 3166-1 alpha-2)
例外: Authentication error; Invalid operation; The server isn't operational; Unauthorized access; Active Directory entry not found; Object doesn't exist on server; Couldn't set or update password; Active Directory error

## Connect to server  `#connecttoserveraction`
Connects to an Active Directory server.
入力:
- LDAP path: Text value — The LDAP path of the Active Directory server
- Use authentication: Boolean value = False — Specify whether authentication is needed to connect to the server
- Username: Text value — The user's username
- Password: Direct encrypted input or Text value — The user's password
- Authentication type: None, Secure, Encryption, Secure sockets layer, Read-only server, Anonymous, Fast bind, Signing, Sealing, Delegation, Server bind = Secure — Specify the type of authentication to be used
出力:
- ParentDirectoryEntry: Active Directory entry — The parent of the Active Directory entry for use with later Active Directory actions
例外: Authentication error; Unauthorized access; The server isn't operational; Invalid operation; Active Directory error

## Close connection  `#closeconnection`
Closes the connection with the Active Directory server.
入力:
- Parent directory entry: Active Directory entry — The parent entry of the Active Directory server
