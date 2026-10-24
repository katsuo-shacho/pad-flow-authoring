# CyberArk actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/cyberark （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: CyberArk offers an identity security platform that secures human and machine identities from end-to-end. Power Automate enables you to retrieve credentials from CyberArk through the Get password from CyberArk action. To find the required information to populate the action, see the following instructions: - Application ID: To find the application ID, open CyberArk Password Vault on a web browser and navigate to the Applications tab. Select Components, open the Private Ark application, and then select the desired Vault. You can add Owners here. - Safe: Populate the name of the safe displayed in 

## Get password from CyberArk  `#getpasswordbase`
Retrieves a password for a specific application from CyberArk.
入力:
- Server address: Text value — The base URI for the web request to connect. For example, `https://yourservice.skytap.com:111`
- Application ID: Text value — The application ID to use for the web request. </br></br>To find the application ID, open CyberArk Password Vault on a web browser and navigate to the Applications tab. Select Components, open the Private Ark application, and then select the desired Vault. You can add Owners here.
- Safe: Text value — The safe on CyberArk in which the application belongs
- Folder: Text value — The folder necessary for the web request query
- Object: Text value — The object necessary for the web request query
- Extra data(任意): Text value — The extra data (if any) for the web request's query
- Accept untrusted certificates: Boolean value = False — Specifies whether to accept untrusted certificates
- Certificate location: Don't use certificate, Load certificate from Windows Store, Load certificate from file = Don't use certificate — Specifies how to load (if needed) the certificate for the request
- Use only valid certificates: Boolean value = False — Specifies whether to load only valid certificates from the store
- Store certificate path: Text value — The path of the certificate in the certificate store. The certificate is represented by its serial number. The path should use the following format:</br></br> (local path to certificate)/(certificate serial)
- Certificates path: File — The path of the certificate.
- Certificate password: Direct encrypted input or Text value — The password for the certificate file
- Timeout(任意): Numeric value = 30 — The waiting time (in seconds) to get results from CyberArk
出力:
- JSONResponse: Custom object — The API response result
- CyberArkPassword: Encrypted value — The password retrieved from CyberArk
例外: Failed to send web request; Timeout expired; Error response from web request
