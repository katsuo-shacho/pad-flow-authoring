# Robin: PGP

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### PGP.PgpDecryptFile のセレクター: PgpDecryptFile, PgpDecryptFilePrivateKeyAsText

## PGP.PgpDecryptFile.PgpDecryptFile [A]
```
PGP.PgpDecryptFile.PgpDecryptFile PrivateKeyFilePath: $'''C:\temp\test.xlsx''' Passphrase: $'''password''' InputFilePath: $'''C:\temp\test.xlsx''' OutputFilePath: $'''C:\temp\test.xlsx'''
```
入力: !PrivateKeyFilePath:FileObject Passphrase:EncryptableObject !InputFilePath:FileObject !OutputFilePath:FileObject
ON ERROR可: FileNotFoundError, IncorrectPassphraseError, InvalidKeyError, KeyFileNotFoundError, PgpDecryptFileError
固定: PrivateKeySource=File

## PGP.PgpDecryptFile.PgpDecryptFilePrivateKeyAsText [A]
```
PGP.PgpDecryptFile.PgpDecryptFilePrivateKeyAsText PrivateKeyText: $'''example''' Passphrase: $'''password''' InputFilePath: $'''C:\temp\test.xlsx''' OutputFilePath: $'''C:\temp\test.xlsx'''
```
入力: !PrivateKeyText:String Passphrase:EncryptableObject !InputFilePath:FileObject !OutputFilePath:FileObject
ON ERROR可: FileNotFoundError, IncorrectPassphraseError, InvalidKeyError, KeyFileNotFoundError, PgpDecryptFileError
固定: PrivateKeySource=Text

### PGP.PgpEncryptFile のセレクター: PgpEncryptFile, PgpEncryptFilePublicKeyAsText

## PGP.PgpEncryptFile.PgpEncryptFile [A]
```
PGP.PgpEncryptFile.PgpEncryptFile EncryptionAlgorithm: PGP.PgpEncryptionAlgorithm.AES256 PublicKeyFilePath: $'''C:\temp\test.xlsx''' IsAsciiArmored: False CompressionAlgorithm: PGP.PgpCompressionAlgorithm.ZIP OutputFilePath: $'''C:\temp\test.xlsx''' InputFilePath: $'''C:\temp\test.xlsx'''
```
入力: !EncryptionAlgorithm:PgpEncryptionAlgorithm{AES256,AES192,AES128,TripleDES,CAST5} !PublicKeyFilePath:FileObject !IsAsciiArmored:Boolean !CompressionAlgorithm:PgpCompressionAlgorithm{None,ZIP,ZLIB,BZIP2} !OutputFilePath:FileObject !InputFilePath:FileObject
ON ERROR可: FileNotFoundError, InvalidKeyError, KeyFileNotFoundError, PgpEncryptFileError
固定: PublicKeySource=File

## PGP.PgpEncryptFile.PgpEncryptFilePublicKeyAsText [A]
```
PGP.PgpEncryptFile.PgpEncryptFilePublicKeyAsText EncryptionAlgorithm: PGP.PgpEncryptionAlgorithm.AES256 IsAsciiArmored: False CompressionAlgorithm: PGP.PgpCompressionAlgorithm.ZIP OutputFilePath: $'''C:\temp\test.xlsx''' InputFilePath: $'''C:\temp\test.xlsx''' PublicKeyText: $'''example'''
```
入力: !EncryptionAlgorithm:PgpEncryptionAlgorithm{AES256,AES192,AES128,TripleDES,CAST5} !IsAsciiArmored:Boolean !CompressionAlgorithm:PgpCompressionAlgorithm{None,ZIP,ZLIB,BZIP2} !OutputFilePath:FileObject !InputFilePath:FileObject !PublicKeyText:String
ON ERROR可: FileNotFoundError, InvalidKeyError, KeyFileNotFoundError, PgpEncryptFileError
固定: PublicKeySource=Text
