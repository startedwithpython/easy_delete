import os
import sys
import time
import getpass
import datetime
import send2trash as s2t
import pyinputplus as pyip
from pathlib import Path

extension_list = []                     # EXTENSION list as per user input
file_name_startswith_list = []          # STARTSWITH list as per user input
file_name_has_list = []                 # HAS list as per user input
file_name_endswith_list = []            # ENDSWITH list as per user input

x = datetime.datetime.now()             # GETS date and time for logging
nl = '\n'                               # NEW line
username = getpass.getuser()            # GETS username of path
# APP dir
log_dir_path = Path(os.path.join('C:/users/', username, 'AppData/Local/easy_delete'))
# CREATES app dir
try:
    os.mkdir(log_dir_path)
except FileExistsError:
    pass

# CREATES log file, writes script start datetime, closes file
log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
log_file.write(f'{nl}Script has started on {x}{nl}')
log_file.close()

# TREE MODE deletes files in all subfolders of root folder
def tree_dir():
    # USER selects which condition they want to use and input folder path
    print('Current mode is TREE.')
    print('Pick the condition. [startswith / has / endswith]')
    condition_choice = pyip.inputStr()
    condition_choice = condition_choice.lower()
    folder_path = input('Folder path is: ')
    folder_path = folder_path.replace('"', '')
    folder_path = Path(folder_path)
    if condition_choice == 'startswith':
        # USER selects condition of STARTSWITH list and logs it
        file_name_startswith = input('File name starts with: ')
        file_name_startswith = file_name_startswith.split(',')
        file_name_startswith_list.append(file_name_startswith)
        print(file_name_startswith_list[0])
        log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
        log_file.write(f'MODE: TREE | Condition list is STARTSWITH: {file_name_startswith_list} | Extension is: {extension_list}  {nl}')
        log_file.close()
        # FINDS the files that match the given condition(s)
        for root_folder, subfolders, files in os.walk(Path(folder_path)):
            for file in files:
                for i in range(len(file_name_startswith_list[0])):
                    for y in range(len(extension_list[0])):
                        if file.startswith(file_name_startswith_list[0][i]):
                            if file.endswith(''.join(['.', str(extension_list[0][y])])):
                                # REMOVES the files
                                file_list = os.path.join(root_folder, file)
                                s2t.send2trash(str(file_list))
                                # PRINTS and logs removed files
                                log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                                log_file.write(f'{x} | {str(file_list)} {nl} ')
                                log_file.close()
                                print(f'Successfully removed {file_list}')
    elif condition_choice == 'has':
        # USER selects condition of ENDSWITH list and logs it
        file_name_has = input('File name has: ').replace(' ', '')
        file_name_has = file_name_has.split(',')
        file_name_has_list.append(file_name_has)
        print(file_name_has_list[0])
        log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
        log_file.write(f'MODE: TREE | Condition list is STARTSWITH: {file_name_has_list}. Extension is: {extension_list}. {nl}')
        log_file.close()
        # FINDS the files that match the given condition(s)
        for root_folder, subfolders, files in os.walk(Path(folder_path)):
            for file in files:
                for i in range(len(file_name_has_list[0])):
                    for y in range(len(extension_list[0])):
                        if file_name_has_list[0][i] in file:
                            if file.endswith(''.join(['.', str(extension_list[0][y])])):
                                # REMOVES the files
                                file_list = os.path.join(root_folder, file)
                                s2t.send2trash(str(file_list))
                                # PRINTS removed files
                                log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                                log_file.write(f'{x} | {str(file_list)} {nl} ')
                                log_file.close()
                                print(f'Successfully removed {file_list}')
    elif condition_choice == 'endswith':
        # USER selects condition of ENDSWITH list and logs it
        file_name_endswith = input('File name ends with: ').replace(' ', '')
        file_name_endswith = file_name_endswith.split(',')
        file_name_endswith_list.append(file_name_endswith)
        print(file_name_endswith_list[0])
        log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
        log_file.write(f'MODE: TREE | Condition list is STARTSWITH: {file_name_endswith_list}. Extension is: {extension_list}. {nl}')
        log_file.close()
        # FINDS the files that match the given condition(s)
        for root_folder, subfolders, files in os.walk(Path(folder_path)):
            for file in files:
                for i in range(len(file_name_endswith_list[0])):
                    for y in range(len(extension_list[0])):
                        # FINDS all files in the folder
                            # CONDITIONS to be met as per user input
                        if file.endswith('.'.join([str(file_name_endswith_list[0][i]), str(extension_list[0][y])])):
                            # REMOVES the files
                            file_list = os.path.join(root_folder, file)
                            s2t.send2trash(str(file_list))
                                # PRINTS removed files
                            log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                            log_file.write(f'{x} | {str(file_list)} {nl} ')
                            log_file.close()
                            print(f'Successfully removed {file_list}')


def if_startswith():
    # LOGS condition
    log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
    log_file.write(f'Condition list is STARTSWITH: {file_name_startswith_list}. Extension is: {extension_list}. {nl}')
    log_file.close()

    # GOES through each STARTSWITH condition and extension
    for i in range(len(file_name_startswith_list[0])):
        for y in range(len(extension_list[0])):
            # FINDS all files in the folder
            for file in os.listdir(folder_path):
                # GETS full file path
                file_list = Path(folder_path, file)
                # CONDITIONS to be met as per user input
                if file.startswith(file_name_startswith_list[0][i]):
                    if file.endswith(''.join(['.', str(extension_list[0][y])])):
                        # REMOVES the files
                        s2t.send2trash(str(file_list))
                        # PRINTS and logs removed files
                        log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                        log_file.write(f'{x} | {str(file_list)} {nl} ')
                        log_file.close()
                        print(f'Successfully removed {file_list}')


def if_has():
    # LOGS condition
    log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
    log_file.write(f'Condition list is HAS: {file_name_has_list}. Extension is: {extension_list}. {nl}')
    log_file.close()
    # GOES through each HAS condition and extension
    for i in range(len(file_name_has_list[0])):
        for y in range(len(extension_list[0])):
            # FINDS all files in the folder
            for file in os.listdir(folder_path):
                # GETS full file path
                file_list = Path(folder_path, file)
                # CONDITIONS to be met as per user input
                if file_name_has_list[0][i] in file:
                    if file.endswith(''.join(['.', str(extension_list[0][y])])):
                        # REMOVES the files
                        s2t.send2trash(str(file_list))
                        # PRINTS and logs removed files
                        log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                        log_file.write(f'{x} | {str(file_list)} {nl} ')
                        log_file.close()
                        print(f'Successfully removed {file_list}')


def if_endswith():
    # LOGS condition
    log_file = open(Path(''.join([str(log_dir_path), '/', 'logs.txt'])), 'a', encoding='UTF-8')
    log_file.write(f'Condition list is ENDSWITH: {file_name_endswith_list}. Extension is: {extension_list}. {nl}')
    log_file.close()
        # GOES through each ENDSWITH condition and extension
    for i in range(len(file_name_endswith_list[0])):
        for y in range(len(extension_list[0])):
            # FINDS all files in the folder
            for file in os.listdir(folder_path):
                # GETS full file path
                file_list = Path(folder_path, file)
                # CONDITIONS to be met as per user input
                if file.endswith('.'.join([str(file_name_endswith_list[0][i]), str(extension_list[0][y])])):
                    # REMOVES the files
                    s2t.send2trash(str(file_list))
                    # PRINTS and logs removed files
                    log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
                    log_file.write(f'{x} | {str(file_list)} {nl} ')
                    log_file.close()
                    print(f'Successfully removed {file_list}')


# SCRIPT starts and user inputs extension(s)
print('Script has started.')
# EXTENSIONS input is separated by a comma (','). At least one (1) valid extension must be given. Prints extensions.
extension = pyip.inputStr('Extensions are: ').replace(' ', '')
extension = extension.split(',')
extension_list.append(extension)
print(extension_list[0])

# USER picks delete mode
print('Please pick Easy Delete mode: [tree / root] ')
deletion_mode = input().lower()

# RUN TREE mode ( deletes files in subfolders as well )
if deletion_mode == 'tree':
    tree_dir()
    time.sleep(1)
    print(f'Log file location is {log_dir_path}\\logs.txt ')
    time.sleep(0.5)
    log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
    log_file.write(f'Script ended on {x}.{nl}')
    log_file.close()
    sys.exit(input(f'Press any key to exit. {nl}'))

# RUN ROOT mode if TREE mode isn't selected ( only deletes on the root folder given by user )
# USER inputs condition on how to select files to delete
condition_choice = input(f'Condition is [startswith / has / endswith]: ').lower()

if condition_choice == 'startswith':
    """ USER inputs STARTSWITH condition, appends to list, prints list. Conditions are separated by a comma (','). 
    User inputs folder path
    """
    file_name_startswith = input('File name starts with: ')
    file_name_startswith = file_name_startswith.split(',')
    file_name_startswith_list.append(file_name_startswith)
    print(file_name_startswith_list[0])
    folder_path = input('Folder path is: ')
    folder_path = folder_path.replace('"', '')
    folder_path = Path(folder_path)
    if_startswith()


elif condition_choice == 'has':
    """ USER inputs HAS condition, appends to list, prints list. Conditions are separated by a comma (','). 
        User inputs folder path
        """
    file_name_has = input('File name has: ').replace(' ', '')
    file_name_has = file_name_has.split(',')
    file_name_has_list.append(file_name_has)
    print(file_name_has_list[0])
    folder_path = input('Folder path is: ')
    folder_path = folder_path.replace('"', '')
    folder_path = Path(folder_path)
    if_has()

elif condition_choice == 'endswith':
    """ USER inputs ENDSWITH condition, appends to list, prints list. Conditions are separated by a comma (','). 
        User inputs folder path
        """
    file_name_endswith = input('File name ends with: ').replace(' ', '')
    file_name_endswith = file_name_endswith.split(',')
    file_name_endswith_list.append(file_name_endswith)
    print(file_name_endswith_list[0])
    folder_path = input('Folder path is: ')
    folder_path = folder_path.replace('"', '')
    folder_path = Path(folder_path)
    if_endswith()

else:
    # ENDS the script on invalid answer.
    print(f'Please choose between startswith / has / endswith only.{nl}Script ending in 3 seconds.')
    time.sleep(3)
    sys.exit()

# PRINTS log file location after all files are removed and logs the time script finished.
# Terminal remains open till a key is pressed by user
time.sleep(1)
print(f'Log file location is {log_dir_path}\\logs.txt ')
time.sleep(0.5)
log_file = open(Path(os.path.join(log_dir_path, 'logs.txt')), 'a', encoding='UTF-8')
log_file.write(f'Script ended on {x}.{nl}')
log_file.close()
sys.exit(input(f'Press any key to exit. {nl}'))
