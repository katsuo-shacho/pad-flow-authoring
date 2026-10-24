# Robin: Cryptography

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Cryptography.DecryptText のセレクター: DecryptTextWithAES, DecryptTextWithAESUseIV, DecryptTextWithAESUseSalt, DecryptTextWithAESUseSaltAndIV

## Cryptography.DecryptText.DecryptTextWithAES [A]
```
Cryptography.DecryptText.DecryptTextWithAES Encoding: Cryptography.EncryptionEncoding.Unicode TextToDecrypt: $fx'example' DecryptionKey: $fx'password' Padding: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 DecryptedText=> DecryptedText
```
入力: DecryptionKey:EncryptableObject Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} KeySize:AESKeySize{Bits128,Bits192,Bits256} Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} TextToDecrypt:String
出力: DecryptedText:String=>
ON ERROR可: DecryptTextError
固定: UseIV=False, UseSalt=False

## Cryptography.DecryptText.DecryptTextWithAESUseIV [A]
```
Cryptography.DecryptText.DecryptTextWithAESUseIV TextToDecrypt: $fx'example' Encoding: Cryptography.EncryptionEncoding.Unicode DecryptionKey: $fx'password' InitializationVector: $fx'example' Padding: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 DecryptedText=> DecryptedText
```
入力: !TextToDecrypt:String !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptionKey:EncryptableObject !InitializationVector:String !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: DecryptedText:String=>DecryptedText
ON ERROR可: DecryptTextError
固定: UseIV=True, UseSalt=False

## Cryptography.DecryptText.DecryptTextWithAESUseSalt [A]
```
Cryptography.DecryptText.DecryptTextWithAESUseSalt TextToDecrypt: $fx'example' HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 Salt: $fx'example' Encoding: Cryptography.EncryptionEncoding.Unicode DecryptionKey: $fx'password' Padding: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 DecryptedText=> DecryptedText
```
入力: !TextToDecrypt:String !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !Salt:String !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptionKey:EncryptableObject !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: DecryptedText:String=>DecryptedText
ON ERROR可: DecryptTextError
固定: UseIV=False, UseSalt=True

## Cryptography.DecryptText.DecryptTextWithAESUseSaltAndIV [A]
```
Cryptography.DecryptText.DecryptTextWithAESUseSaltAndIV TextToDecrypt: $fx'example' HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 Salt: $fx'example' Encoding: Cryptography.EncryptionEncoding.Unicode DecryptionKey: $fx'password' InitializationVector: $fx'example' Padding: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 DecryptedText=> DecryptedText
```
入力: !TextToDecrypt:String !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !Salt:String !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptionKey:EncryptableObject !InitializationVector:String !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: DecryptedText:String=>DecryptedText
ON ERROR可: DecryptTextError
固定: UseIV=True, UseSalt=True

### Cryptography.DecryptToFile のセレクター: DecryptToFileWithAES, DecryptToFileWithAESUseIV, DecryptToFileWithAESUseSalt, DecryptToFileWithAESUseSaltAndIV

## Cryptography.DecryptToFile.DecryptToFileWithAES [A]
```
Cryptography.DecryptToFile.DecryptToFileWithAES Encoding: Cryptography.EncryptionEncoding.Unicode TextToDecrypt: $fx'example' DecryptionKey: $fx'password' DecryptToFile: $fx'C:\temp\test.xlsx' IfFileExists: Cryptography.IfFileExists.AddSequentialSuffix Padding: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 DecryptedFile=> DecryptedFile
```
入力: DecryptionKey:EncryptableObject DecryptToFile:FileObject Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix} KeySize:AESKeySize{Bits128,Bits192,Bits256} Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} TextToDecrypt:String
出力: DecryptedFile:FileObject=>
ON ERROR可: DecryptToFileError
固定: UseIV=False, UseSalt=False

## Cryptography.DecryptToFile.DecryptToFileWithAESUseIV [A]
```
Cryptography.DecryptToFile.DecryptToFileWithAESUseIV TextToDecrypt: $fx'example' Padding: Cryptography.PaddingMode.PKCS7 Encoding: Cryptography.EncryptionEncoding.Unicode DecryptToFile: $fx'C:\temp\test.xlsx' DecryptionKey: $fx'password' KeySize: Cryptography.AESKeySize.Bits256 InitializationVector: $fx'example' IfFileExists: Cryptography.IfFileExists.AddSequentialSuffix DecryptedFile=> DecryptedFile
```
入力: !TextToDecrypt:String !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptToFile:FileObject !DecryptionKey:EncryptableObject !KeySize:AESKeySize{Bits128,Bits192,Bits256} !InitializationVector:String !IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix}
出力: DecryptedFile:FileObject=>DecryptedFile
ON ERROR可: DecryptToFileError
固定: UseSalt=False, UseIV=True

## Cryptography.DecryptToFile.DecryptToFileWithAESUseSalt [A]
```
Cryptography.DecryptToFile.DecryptToFileWithAESUseSalt TextToDecrypt: $fx'example' Salt: $fx'example' HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 Padding: Cryptography.PaddingMode.PKCS7 Encoding: Cryptography.EncryptionEncoding.Unicode DecryptToFile: $fx'C:\temp\test.xlsx' DecryptionKey: $fx'password' KeySize: Cryptography.AESKeySize.Bits256 IfFileExists: Cryptography.IfFileExists.AddSequentialSuffix DecryptedFile=> DecryptedFile
```
入力: !TextToDecrypt:String !Salt:String !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptToFile:FileObject !DecryptionKey:EncryptableObject !KeySize:AESKeySize{Bits128,Bits192,Bits256} !IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix}
出力: DecryptedFile:FileObject=>DecryptedFile
ON ERROR可: DecryptToFileError
固定: UseIV=False, UseSalt=True

## Cryptography.DecryptToFile.DecryptToFileWithAESUseSaltAndIV [A]
```
Cryptography.DecryptToFile.DecryptToFileWithAESUseSaltAndIV TextToDecrypt: $fx'example' Salt: $fx'example' HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 Padding: Cryptography.PaddingMode.PKCS7 Encoding: Cryptography.EncryptionEncoding.Unicode DecryptToFile: $fx'C:\temp\test.xlsx' DecryptionKey: $fx'password' KeySize: Cryptography.AESKeySize.Bits256 InitializationVector: $fx'example' IfFileExists: Cryptography.IfFileExists.AddSequentialSuffix DecryptedFile=> DecryptedFile
```
入力: !TextToDecrypt:String !Salt:String !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !Padding:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !DecryptToFile:FileObject !DecryptionKey:EncryptableObject !KeySize:AESKeySize{Bits128,Bits192,Bits256} !InitializationVector:String !IfFileExists:IfFileExists{Overwrite,DoNotModifyFiles,AddSequentialSuffix}
出力: DecryptedFile:FileObject=>DecryptedFile
ON ERROR可: DecryptToFileError
固定: UseSalt=True, UseIV=True

### Cryptography.EncryptFromFile のセレクター: EncryptFromFileWithAES, EncryptFromFileWithAESUseIV, EncryptFromFileWithAESUseSalt, EncryptFromFileWithAESUseSaltAndIV

## Cryptography.EncryptFromFile.EncryptFromFileWithAES [A]
```
Cryptography.EncryptFromFile.EncryptFromFileWithAES Encoding: Cryptography.EncryptionEncoding.Unicode FileToEncrypt: $fx'C:\temp\test.xlsx' EncryptionKey: $fx'password' PaddingMode: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 EncryptedText=> EncryptedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} EncryptionKey:EncryptableObject FileToEncrypt:FileObject KeySize:AESKeySize{Bits128,Bits192,Bits256} PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126}
出力: EncryptedText:String=>
ON ERROR可: EncryptFileError, FileNotFoundError
固定: UseIV=False, UseSalt=False

## Cryptography.EncryptFromFile.EncryptFromFileWithAESUseIV [A]
```
Cryptography.EncryptFromFile.EncryptFromFileWithAESUseIV PaddingMode: Cryptography.PaddingMode.PKCS7 EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode KeySize: Cryptography.AESKeySize.Bits256 FileToEncrypt: $fx'C:\temp\test.xlsx' InitializationVector=> InitializationVector EncryptedText=> EncryptedText
```
入力: !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !KeySize:AESKeySize{Bits128,Bits192,Bits256} !FileToEncrypt:FileObject
出力: InitializationVector:String=>InitializationVector EncryptedText:String=>EncryptedText
ON ERROR可: EncryptFileError, FileNotFoundError
固定: UseIV=True, UseSalt=False

## Cryptography.EncryptFromFile.EncryptFromFileWithAESUseSalt [A]
```
Cryptography.EncryptFromFile.EncryptFromFileWithAESUseSalt HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 PaddingMode: Cryptography.PaddingMode.PKCS7 EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode KeySize: Cryptography.AESKeySize.Bits256 FileToEncrypt: $fx'C:\temp\test.xlsx' Salt=> Salt EncryptedText=> EncryptedText
```
入力: !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !KeySize:AESKeySize{Bits128,Bits192,Bits256} !FileToEncrypt:FileObject
出力: Salt:String=>Salt EncryptedText:String=>EncryptedText
ON ERROR可: EncryptFileError, FileNotFoundError
固定: UseSalt=True, UseIV=False

## Cryptography.EncryptFromFile.EncryptFromFileWithAESUseSaltAndIV [A]
```
Cryptography.EncryptFromFile.EncryptFromFileWithAESUseSaltAndIV HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 PaddingMode: Cryptography.PaddingMode.PKCS7 EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode KeySize: Cryptography.AESKeySize.Bits256 FileToEncrypt: $fx'C:\temp\test.xlsx' Salt=> Salt InitializationVector=> InitializationVector EncryptedText=> EncryptedText
```
入力: !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !KeySize:AESKeySize{Bits128,Bits192,Bits256} !FileToEncrypt:FileObject
出力: Salt:String=>Salt InitializationVector:String=>InitializationVector EncryptedText:String=>EncryptedText
ON ERROR可: EncryptFileError, FileNotFoundError
固定: UseIV=True, UseSalt=True

### Cryptography.EncryptText のセレクター: EncryptTextWithAES, EncryptTextWithAESUseIV, EncryptTextWithAESUseSalt, EncryptTextWithAESUseSaltAndIV

## Cryptography.EncryptText.EncryptTextWithAES [A]
```
Cryptography.EncryptText.EncryptTextWithAES Encoding: Cryptography.EncryptionEncoding.Unicode TextToEncrypt: $fx'example' EncryptionKey: $fx'password' PaddingMode: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 EncryptedText=> EncryptedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} EncryptionKey:EncryptableObject KeySize:AESKeySize{Bits128,Bits192,Bits256} PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} TextToEncrypt:String
出力: EncryptedText:String=>
ON ERROR可: EncryptTextError
固定: UseIV=False, UseSalt=False

## Cryptography.EncryptText.EncryptTextWithAESUseIV [A]
```
Cryptography.EncryptText.EncryptTextWithAESUseIV TextToEncrypt: $fx'example' EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode PaddingMode: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 InitializationVector=> InitializationVector EncryptedText=> EncryptedText
```
入力: !TextToEncrypt:String !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: InitializationVector:String=>InitializationVector EncryptedText:String=>EncryptedText
ON ERROR可: EncryptTextError
固定: UseIV=True, UseSalt=False

## Cryptography.EncryptText.EncryptTextWithAESUseSalt [A]
```
Cryptography.EncryptText.EncryptTextWithAESUseSalt HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 TextToEncrypt: $fx'example' EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode PaddingMode: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 Salt=> Salt EncryptedText=> EncryptedText
```
入力: !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !TextToEncrypt:String !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: Salt:String=>Salt EncryptedText:String=>EncryptedText
ON ERROR可: EncryptTextError
固定: UseSalt=True, UseIV=False

## Cryptography.EncryptText.EncryptTextWithAESUseSaltAndIV [A]
```
Cryptography.EncryptText.EncryptTextWithAESUseSaltAndIV HashAlgorithm: Cryptography.EncryptionHashAlgorithm.SHA256 Iterations: 100000 TextToEncrypt: $fx'example' EncryptionKey: $fx'password' Encoding: Cryptography.EncryptionEncoding.Unicode PaddingMode: Cryptography.PaddingMode.PKCS7 KeySize: Cryptography.AESKeySize.Bits256 Salt=> Salt InitializationVector=> InitializationVector EncryptedText=> EncryptedText
```
入力: !HashAlgorithm:EncryptionHashAlgorithm{SHA1,SHA256,SHA384,SHA512} !Iterations:Int32 !TextToEncrypt:String !EncryptionKey:EncryptableObject !Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} !PaddingMode:PaddingMode{None,PKCS7,Zeros,ANSIX923,ISO10126} !KeySize:AESKeySize{Bits128,Bits192,Bits256}
出力: Salt:String=>Salt InitializationVector:String=>InitializationVector EncryptedText:String=>EncryptedText
ON ERROR可: EncryptTextError
固定: UseIV=True, UseSalt=True

## Cryptography.HashFromFile [A]
```
Cryptography.HashFromFile HashAlgorithm: Cryptography.HashAlgorithm.SHA256 Encoding: Cryptography.EncryptionEncoding.Unicode File: $fx'C:\temp\test.xlsx' HashedText=> HashedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} File:FileObject HashAlgorithm:HashAlgorithm{SHA256,SHA384,SHA512}
出力: HashedText:String=>
ON ERROR可: FileNotFoundError, HashFileError

## Cryptography.HashFromFileWithKey [A]
```
Cryptography.HashFromFileWithKey KeyedHashAlgorithm: Cryptography.KeyedHashAlgorithm.HMACSHA256 Encoding: Cryptography.EncryptionEncoding.Unicode FileToHash: $fx'C:\temp\test.xlsx' HashKey: $fx'password' HashedText=> HashedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} FileToHash:FileObject HashKey:EncryptableObject KeyedHashAlgorithm:KeyedHashAlgorithm{HMACSHA256,HMACSHA384,HMACSHA512}
出力: HashedText:String=>
ON ERROR可: FileNotFoundError, HashFileWithKeyError

## Cryptography.HashText [A]
```
Cryptography.HashText HashAlgorithm: Cryptography.HashAlgorithm.SHA256 Encoding: Cryptography.EncryptionEncoding.Unicode TextToHash: $fx'example' HashedText=> HashedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} HashAlgorithm:HashAlgorithm{SHA256,SHA384,SHA512} TextToHash:String
出力: HashedText:String=>
ON ERROR可: HashTextError

## Cryptography.HashTextWithKey [A]
```
Cryptography.HashTextWithKey HashAlgorithm: Cryptography.KeyedHashAlgorithm.HMACSHA256 Encoding: Cryptography.EncryptionEncoding.Unicode TextToHash: $fx'example' HashKey: $fx'password' HashedText=> HashedText
```
入力: Encoding:EncryptionEncoding{DefaultEncoding,ANSI,Unicode,BigEndianUnicode,UTF8} HashAlgorithm:KeyedHashAlgorithm{HMACSHA256,HMACSHA384,HMACSHA512} HashKey:EncryptableObject TextToHash:String
出力: HashedText:String=>
ON ERROR可: HashTextWithKeyError
