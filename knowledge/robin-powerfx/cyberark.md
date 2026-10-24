# Robin: Cyberark

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Cyberark.GetPassword のセレクター: GetPassword, GetPasswordWithFileCertificate, GetPasswordWithStoreCertificate

## Cyberark.GetPassword.GetPassword [A]
```
Cyberark.GetPassword.GetPassword Safe: $fx'example' Object: $fx'example' ServerAddress: $fx'example' Timeout: 30 AuthApp: $fx'example' ApplicationId: $fx'example' AcceptUntrustedCertificates: False Folder: $fx'example' ExtraData: $fx'example' Response=> JSONResponse PlainTextPassword=> CyberArkPassword Password=> CyberArkPassword
```
入力: !Safe:String !Object:String !ServerAddress:String !Timeout:Int32 !AuthApp:String !ApplicationId:String !AcceptUntrustedCertificates:Boolean !Folder:String ExtraData:String
出力: Response:CustomObject=>JSONResponse PlainTextPassword:String=>CyberArkPassword Password:EncryptableObject=>CyberArkPassword
ON ERROR可: ResponseFromWebRequestError, SendWebRequestError, TimeoutExpiredError
固定: LoadCertificationFrom=None

## Cyberark.GetPassword.GetPasswordWithFileCertificate [A]
```
Cyberark.GetPassword.GetPasswordWithFileCertificate Safe: $fx'example' Object: $fx'example' ServerAddress: $fx'example' Timeout: 30 AuthApp: $fx'example' ApplicationId: $fx'example' AcceptUntrustedCertificates: False CertificateFilePassword: $fx'password' Folder: $fx'example' ExtraData: $fx'example' CertificateFilePath: $fx'C:\temp\test.xlsx' Response=> JSONResponse PlainTextPassword=> CyberArkPassword Password=> CyberArkPassword
```
入力: !Safe:String !Object:String !ServerAddress:String !Timeout:Int32 !AuthApp:String !ApplicationId:String !AcceptUntrustedCertificates:Boolean !CertificateFilePassword:EncryptableObject !Folder:String ExtraData:String !CertificateFilePath:FileObject
出力: Response:CustomObject=>JSONResponse PlainTextPassword:String=>CyberArkPassword Password:EncryptableObject=>CyberArkPassword
ON ERROR可: ResponseFromWebRequestError, SendWebRequestError, TimeoutExpiredError
固定: LoadCertificationFrom=File

## Cyberark.GetPassword.GetPasswordWithStoreCertificate [A]
```
Cyberark.GetPassword.GetPasswordWithStoreCertificate Safe: $fx'example' Object: $fx'example' ServerAddress: $fx'example' UseOnlyValidCertificate: False Timeout: 30 StoreCertificatesPaths: $fx'example' AuthApp: $fx'example' ApplicationId: $fx'example' AcceptUntrustedCertificates: False Folder: $fx'example' ExtraData: $fx'example' Response=> JSONResponse PlainTextPassword=> CyberArkPassword Password=> CyberArkPassword
```
入力: !Safe:String !Object:String !ServerAddress:String !UseOnlyValidCertificate:Boolean !Timeout:Int32 !StoreCertificatesPaths:String !AuthApp:String !ApplicationId:String !AcceptUntrustedCertificates:Boolean !Folder:String ExtraData:String
出力: Response:CustomObject=>JSONResponse PlainTextPassword:String=>CyberArkPassword Password:EncryptableObject=>CyberArkPassword
ON ERROR可: ResponseFromWebRequestError, SendWebRequestError, TimeoutExpiredError
固定: LoadCertificationFrom=Store
