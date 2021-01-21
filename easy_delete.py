import os
import sys
import getpass
import logging
import send2trash as s2t
from pathlib import Path

username = getpass.getuser()            # GETS username of path
# APP dir
log_dir = Path('C:/users/', username, 'AppData/Local/easy_delete')

# CREATES app dir
try:
    Path.mkdir(log_dir)
except FileExistsError:
    pass

# CREATES log file, writes script start datetime and timezone offset (on all logging)

log_file = log_dir.joinpath('logs.log')
logging.basicConfig(filename=log_file, format='%(asctime)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S %z', level=logging.INFO)
logging.info('--------------------------------------------------------------------------------------------------------')
logging.info(f'| Script start.')


def tree_dir():
    # USER selects which condition they want to use and input folder path
    print(f'Mode is TREE. \nCondition is [startswith / has / endswith]:')
    condition_choice = input().lower()

    folder_path = input('Folder path is: ')
    folder_path = Path(folder_path.replace('"', ''))
    if condition_choice == 'startswith':
        # USER selects condition of STARTSWITH and logs it
        file_name_startswith = input('File name starts with: ').replace(' ', '')
        names_startswith = file_name_startswith.split(',')
        logging.info(f'| MODE: TREE | Condition is STARTSWITH: {names_startswith} | Extension is: {extensions_inputs} | Target is: {folder_path}')
        # FINDS the files that match the given condition(s), removes, prints and logs
        for root_folder, subfolders, files in os.walk(folder_path):
            for file in files:
                file_list = Path(root_folder, file)
                if any(file.startswith(p) for p in names_startswith):
                    if any(file.endswith(e) for e in extensions_inputs):
                        s2t.send2trash(str(file_list))
                        print(f'Successfully removed {file_list}')
                        logging.info(f'| Successfully removed {file_list}')
    elif condition_choice == 'has':
        # USER selects condition of HAS and logs it
        file_name_has = input('File name has: ').replace(' ', '')
        names_has = file_name_has.split(',')
        logging.info(f'| MODE: TREE | Condition is STARTSWITH: {names_has}. Extension is: {extensions_inputs} | Target is: {folder_path}')
        # FINDS the files that match the given condition(s), removes, prints and logs
        for root_folder, subfolders, files in os.walk(folder_path):
            for file in files:
                file_list = Path(root_folder, file)
                if any(p in file for p in names_has):
                    if any(file.endswith(e) for e in extensions_inputs):
                        s2t.send2trash(str(file_list))
                        print(f'Successfully removed {file_list}')
                        logging.info(f'| Successfully removed {file_list}')
    elif condition_choice == 'endswith':
        # USER selects condition of ENDSWITH and logs it
        file_name_endswith = input('File name ends with: ').replace(' ', '')
        names_endswith = file_name_endswith.split(',')
        logging.info(f'| MODE: TREE | Condition is ENDSWITH: {names_endswith} | Extension is: {extensions_inputs} | Target is: {folder_path}')
        # FINDS the files that match the given condition(s), removes, prints and logs
        for root_folder, subfolders, files in os.walk(folder_path):
            for file in files:
                filename = file.split('.')
                file_list = Path(root_folder, file)
                if any(filename[0].endswith(p) for p in names_endswith):
                    if any(file.endswith(e) for e in extensions_inputs):
                        s2t.send2trash(str(file_list))
                        print(f'Successfully removed {file_list}')
                        logging.info(f'| Successfully removed {file_list}')


def if_startswith():
    logging.info(f'| Mode: ROOT | Condition is STARTSWITH: {names_startswith}. Extensions are: {extensions_inputs} | Target is: {folder_path}')
    # FINDS files that match the given conditions, removes, prints, logs
    for file in os.listdir(folder_path):
        if any(file.startswith(p) for p in names_startswith):
            if any(file.endswith(e) for e in extensions_input):
                file_list = Path(folder_path, file)
                s2t.send2trash(str(file_list))
                print(f'Successfully removed {file_list}')
                logging.info(f'| Successfully removed {file_list}')


def if_has():
    logging.info(f'| Mode: ROOT | Condition is HAS: {names_has}. Extensions are: {extensions_inputs} | Target is: {folder_path}')
    # FINDS files that match the given conditions, removes, prints, logs
    for file in os.listdir(folder_path):
        file_list = Path(folder_path, file)
        if any(p in file for p in names_has):
            if any(file.endswith(e) for e in extensions_inputs):
                s2t.send2trash(str(file_list))
                print(f'Successfully removed {file_list}')
                logging.info(f'| Successfully removed {file_list}')


def if_endswith():
    logging.info(f'| Mode: ROOT | Condition is ENDSWITH: {names_endswith}. Extensions are: {extensions_inputs} | Target is: {folder_path}')
    # FINDS files that match the given conditions, removes, prints, logs
    for file in os.listdir(folder_path):
        file_list = Path(folder_path, file)
        filename = file.split('.')
        if any(filename[0].endswith(p) for p in names_endswith):
            if any(file.endswith(e) for e in extensions_inputs):
                s2t.send2trash(str(file_list))
                print(f'Successfully removed {file_list}')
                logging.info(f'| Successfully removed {file_list}')


# SCRIPT start and user selects extensions separated by commas followed by mode selection
print('Script has started.')
extensions_input = input('Extensions are: ').replace(' ', '')
extensions_inputs = extensions_input.split(',')
print('Please pick easy delete mode [tree / root]')
deletion_mode = input().lower()

# IF tree is TREE it calls tree_dir() and then logs script end
if deletion_mode == 'tree':
    tree_dir()
    print(f'Log file location is {log_file}')
    input('Press any key to exit')
    sys.exit(logging.info('| Script has ended.'))

# USER inputs absolute folder path then picks the condition
print('Mode is ROOT.')
folder_input = input('Folder path is: ')
folder_path = Path(folder_input.replace('"', ''))
condition_choice = input(f'Condition is [startswith / has / endswith]: ').lower()

if condition_choice == 'startswith':
    # USER inputs STARTSWITH conditions and calls if_startswith()
    file_name_startswith = input('File name starts with: ').replace(' ', '')
    names_startswith = file_name_startswith.split(',')
    if_startswith()
elif condition_choice == 'has':
    # USER inputs HAS conditions and calls if_has()
    file_name_has = input('File name has: ').replace(' ', '')
    names_has = file_name_has.split(',')
    if_has()
elif condition_choice == 'endswith':
    # USER inputs ENDSWITH conditions and calls if_endswith()
    file_name_endswith = input('File name endswith: ').replace(' ', '')
    names_endswith = file_name_endswith.split(',')
    if_endswith()
else:
    sys.exit()

# PRINTS log file location and prompts user to press any key to exit, logging script end
print(f'Log file location is {log_file}')
input('Press any key to exit')
sys.exit(logging.info('| Script end.'))
