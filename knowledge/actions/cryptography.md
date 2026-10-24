# Cryptography actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/cryptography （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Cryptography actions enable you to encrypt and decrypt plain text and text from files providing a key and an encoding format. The Encrypt text with AES action encrypts a text using the AES algorithm and a user-specified encryption key. You can provide the encryption key directly or through a variable. To encrypt the text of a file directly, use the Encrypt from file with AES action. This action works similarly to the Encrypt text with AES action but requires a source file instead of a text value. To decrypt a text, use the Decrypt text with AES, and enter the encrypted text and the encryption 

## Encrypt text with AES  `#encrypttextaction`
Encrypt a string with AES, using a key and a specified encoding format.
入力:
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the text to encrypt
- Text to encrypt: Text value — The text to encrypt
- Encryption key: Direct encrypted input or Text value — The encryption key to use
- Padding: None, PKCS7, Zeros, ANSIX923, ISO10126 = PKCS7 — The padding to use for the selected encryption algorithm
- Key size: 128 bits, 192 bits, 256 bits = 256 bits — The size of the key in bits to use for the encryption
- Use salt: Boolean value = False — Specifies whether to use salt for encryption. When this option is enabled, the randomly generated salt becomes an output in the form of a base64 string.
- Use initialization vector: Boolean value = False — Specifies whether to use an initialization vector. When this option is enabled, the randomly generated initialization vector becomes an output in the form of a base64 string
出力:
- EncryptedText: Text value — The encrypted text for later processing
- Salt: Text value — The randomly generated salt value for later processing
- InitializationVector: Text value — The randomly generated initialization vector value for later processing
例外: Failed to encrypt text

## Decrypt text with AES  `#decrypttextaction`
Decrypt a string with AES based on a specified key and an encoding format.
入力:
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding for the decrypted text
- Text to decrypt: Text value — The text to decrypt in the form of a base64 string
- Decryption key: Direct encrypted input or Text value — The decryption key to use
- Padding: None, PKCS7, Zeros, ANSIX923, ISO10126 = PKCS7 — The padding to use for the selected decryption algorithm
- Key size: 128 bits, 192 bits, 256 bits = 256 bits — The size of the key in bits to use for the decryption
- Use salt: Boolean value = False — Specifies whether to use salt for the decryption
- Salt: Text value — The salt to use for decryption in the form of a base64 string
- Use initialization vector: Boolean value = False — Specifies whether to use an initialization vector
- Initialization vector: Text value — The initialization vector to use for decryption in the form of a base64 string
出力:
- DecryptedText: Text value — The decrypted text for later processing
例外: Failed to decrypt text

## Encrypt from file with AES  `#encryptfromfileaction`
Encrypt the contents of a file with AES, using a key and a specified encoding format.
入力:
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the file to encrypt
- File to encrypt: File — The text file that stores the contents to encrypt
- Encryption key: Direct encrypted input or Text value — The encryption key to use
- Padding: None, PKCS7, Zeros, ANSIX923, ISO10126 = PKCS7 — The padding to use for the selected encryption algorithm
- Key size: 128 bits, 192 bits, 256 bits = 256 bits — The size of the key in bits to use for the encryption
- Use salt: Boolean value = False — Specifies whether to use salt for encryption. When this option is enabled, the randomly generated salt becomes an output in the form of a base64 string.
- Use initialization vector: Boolean value = False — Specifies whether to use an initialization vector. When this option is enabled, the randomly generated initialization vector becomes an output in the form of a base64 string
出力:
- EncryptedText: Text value — The text of the encrypted file for later processing
- Salt: Text value — The randomly generated salt value for later processing
- InitializationVector: Text value — The randomly generated initialization vector value for later processing
例外: File not found; Failed to encrypt the contents of the file

## Decrypt to file with AES  `#decrypttofileaction`
Decrypt a string to a file with AES based on a specified key and an encoding format.
入力:
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the text to decrypt
- Text to decrypt: Text value — The text to decrypt in the form of a base64 string
- Decryption key: Direct encrypted input or Text value — The decryption key to use
- Decrypt to file: File — The file to save the decrypted text into
- If file exists: Overwrite, Don't decrypt to file, Add sequential suffix = Add sequential suffix — Specifies what to do in case the destination file already exists
- Padding: None, PKCS7, Zeros, ANSIX923, ISO10126 = PKCS7 — The padding to use for the selected decryption algorithm
- Key size: 128 bits, 192 bits, 256 bits = 256 bits — The size of the key in bits to use for decryption
- Use salt: Boolean value = False — Specifies whether to use salt for decryption
- Salt: Text value — The salt to use for decryption in the form of a base64 string
- Use initialization vector: Boolean value = False — Specifies whether to use an initialization vector. Enter the initialization vector in the form of a base64 string
- Initialization vector: Text value — The initialization vector to use for decryption
出力:
- DecryptedFile: File — The decrypted file for later processing
例外: Failed to decrypt and store the contents to a file

## Hash text  `#hashtext`
Hash a string, using a specified algorithm and an encoding format.
入力:
- Hash algorithm: SHA256, SHA384, SHA512 = SHA256 — The algorithm to use for hashing
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the text to hash
- Text to hash: Text value — The text to hash
出力:
- HashedText: Text value — The hashed text for later processing
例外: Failed to hash text

## Hash from file  `#hashfromfile`
Hash the contents of a file, using a specified algorithm and an encoding format.
入力:
- Hash algorithm: SHA256, SHA384, SHA512 = SHA256 — The algorithm to use for hashing
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the file to hash
- File to hash: File — The file to hash the contents of
出力:
- HashedText: Text value — The hashed text for later processing
例外: File not found; Failed to hash the file

## Hash text with key  `#hashtextwithkey`
Hash a string with a key, using a specified algorithm and an encoding format.
入力:
- Hash algorithm: HMAC SHA256, HMAC SHA384, HMAC SHA512 = HMAC SHA256 — The algorithm to use for hashing
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the text to hash
- Text to hash: Text value — The text to hash
- Hash key: Direct encrypted input or Text value — The key to hash the text with
出力:
- HashedText: Text value — The hashed text for later processing
例外: Failed to hash text with key

## Hash from file with key  `#hashfromfilewithkey`
Hash the contents of a file with a key, using a specified algorithm and an encoding format.
入力:
- Hash algorithm: HMAC SHA256, HMAC SHA384, HMAC SHA512 = HMAC SHA256 — The algorithm to use for hashing
- Encoding: System default, ASCII, Unicode, Big-endian Unicode, UTF-8 = Unicode — The encoding of the file to hash
- File to hash: File — The file to hash the contents of
- Hash key: Direct encrypted input or Text value — The hash key to hash the text with
出力:
- HashedText: Text value — The hashed text for later processing
例外: File not found; Failed to hash the file with key
