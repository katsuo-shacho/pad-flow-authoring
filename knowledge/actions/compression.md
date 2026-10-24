# Compression actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/compression （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: To compress (or zip) a file, use the ZIP files action and specify a path to archive. If the archive already exists, the action will add the selected files. The following example uses a variable to specify the path to archive. Best compression ensures maximum file size reduction, and a password adds a layer of security to the archive. The Unzip files action works similarly, requiring a path to archive and a destination folder. The following example uses the Include mask option to only unzip files with the extensions .txt and .xlsx.

## ZIP files  `#zipfiles`
Compress one or more files or folders into a ZIP archive.
入力:
- Archive path: File — The full path of ZIP file to create. If the file already exists, this action adds the new zipped files and/or to the existing ZIP file. If the ZIP file already contains a file or folder with the same name, it overwrites it.
- File(s) to zip: List of FileSystemObject — The full path of the file(s) or folder(s) to include in the ZIP file
- Compression level: None, Best speed, Best balance of speed and compression, Best compression = Best balance of speed and compression — The level of compression to use. The higher the compression the smaller the file, though it takes longer to create or access
- Password(任意): Direct encrypted input or Text value — The password to use for protecting the ZIP. Leave this attribute blank to create a non password-protected ZIP
- Archive comment(任意): Text value — The comment to include in the ZIP file as a file property
出力:
- ZipFile: File — The ZIP file created by this action
例外: File or folder doesn't exist; File or folder name is invalid; Archive already exists but it isn't a valid ZIP archive; Failed to zip files

## Unzip files  `#unzipfiles`
Uncompress one or more files or folders contained in a ZIP archive.
入力:
- Archive path: File — The full path of a ZIP file to extract
- Destination folder: Folder — The full path of the folder to extract the archive to. This action overwrites files in the folder with the same name as a file in the archive
- Password(任意): Direct encrypted input or Text value — The password, if any, that is used for this archive. If the ZIP file isn't password-protected, leave this blank
- Include mask(任意): Text value — The filter to limit the files extracted to the files entered here. This parameter allows wild cards, for example '*.txt' or 'document?.doc' (without the quotes). To allow multiple file filters, separate the choices with a semi-colon, for instance, '*.txt;*.exe'
- Exclude mask(任意): Text value — The filter to limit the files extracted by excluding the file entered here. This parameter allows wild cards, for example, '*.txt' or 'document?.doc' (without the quotes). To allow multiple file filters, separate the choices with a semi-colon, for instance, '*.txt;*.exe'
例外: Can't create destination folder; Archive not found; Archive isn't a valid ZIP file; Failed to unzip files
