# easy_delete
Deleting ( send to trash ) multiple files based on extension and file name in a given folder ( or within subfolders of the given folder as well).


There are 2 modes: Tree and Root

Tree mode means that it will delete the files in the root (given) folder and all of it's subfolders. 
Root mode means that it will delete the files in the root (given) folder only.

Any extension is accepted however given extension(s) should not include dot (' . ') in the input. Multiple extensions are separated by a comma (' , '). At least one (1) valid (exists) extension in the folder ( subfolders ) must be given.

Files are selected based on whether file name starts with, has or ends with the conditions given. Only one of the options can be used.

Multiple conditions of STARTSWITH, HAS or ENDSWITH should be separated by a comma (','). You can put only 'enter' as the condition to delete all files with the given extension(s). ENDSWITH condition must not include the extension of the file.

Multiple conditions means it will remove the files that match with any of the conditions.

Script start and end datetime, mode, condition(s), extension and deleted files are logged in C:\Users\USER\AppData\Local\easy_delete\logs.txt .

Only tested on Windows 10.
