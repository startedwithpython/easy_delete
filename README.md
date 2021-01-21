# easy_delete
Deleting ( send to trash ) multiple files based on extension(s) and file name in a given folder ( or within subfolders of the given folder as well ). It works on "any match" logic.

# Instructions
There are 2 modes: Tree and Root

* Tree mode: It will delete the files in the root (given) folder and all of it's subfolders.
* Root mode: It will delete the files in the root (given) folder only.


Any extension is accepted. They are seperated by a comma (',') e.g " jpg, epub, pdf, gif"

Files are selected based on whether file name starts with, has or ends with the conditions given. Only one of the options can be used.

Multiple conditions of STARTSWITH, HAS or ENDSWITH should be separated by a comma (','). e.g "A, C, Image". You can put only 'enter' as the condition to delete all files with the given extension(s). 

Script start and end datetime, mode, condition(s), extension(s), target and deleted files are logged in C:\Users\USER\AppData\Local\easy_delete\logs.log .

# Extras
If anyone wants to use the .exe directly it can be found [here](https://github.com/startedwithpython/easy_delete/releases/tag/1.0.0). It will be blocked by AVs so you'll need to exclude it. Only works on W10.

# Notes
#### BE CAREFUL WITH USAGE OF "ENTER". e.g YOU COULD REMOVE EVERY FILE IN THE FOLDER(subfolders) BY USING "ENTER" FOR EXTENSIONS AND CONDITION.
