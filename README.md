# easy_delete_move
* Deleting ( send to trash ) files based on extension(s) and file name in a given folder (or and subfolders of the given folder ). "Any match" logic.
* Movind files based on extension(s) and file name in a given folder (or and subfolders of the given source folder). "Any match" logic. - skips if file already exists

# Instructions
There are 2 modes: Tree and Root

* Tree mode: It will delete the files in the root (given) folder and all of it's subfolders.
* Root mode: It will delete the files in the root (given) folder only.


Any extension is accepted. They are seperated by a comma (',') e.g " jpg, epub, pdf, gif"

Files are selected based on whether file name starts with, has or ends with the conditions given. Only one of the options can be used.

Multiple conditions of STARTSWITH, HAS or ENDSWITH should be separated by a comma (','). e.g "A, C, Image". You can put only 'enter' as the condition to delete all files with the given extension(s). 

First letter of action/mode/condition is considered a valid choice as well.

#### "Enter" = all . You can use it to delete or move every file regardless of extensions or name.

Logs in: C:\Users\USER\AppData\Local\easy_delete_move\logs.log 

# Extras
If anyone wants to use the .exe directly it can be found [here](https://github.com/startedwithpython/easy_delete/releases/tag/2.00). It might be blocked by AVs so you might need to exclude it.
# Notes
Only works on W10.
