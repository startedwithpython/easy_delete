import os
import shutil
import send2trash as s2t
from main import *  # LOG DIR, logging, Path

#  READS action.txt and mode.txt
with open(log_dir.joinpath('action.txt'), 'r') as f:
    action = f.read()
with open(log_dir.joinpath('mode.txt'), 'r') as f:
    mode = f.read()


class Condition:
    def __init__(self):
        pass

    # DELETES and logs files
    def deleting(self):
        file_list = self
        s2t.send2trash(str(file_list))
        print(f'Successfully removed {file_list}')
        logging.info(f'Successfully removed {file_list}')

    # MOVES and logs files - if file already exists, skip and log
    def moving(self, destination):
        source = self
        destination = destination
        try:
            shutil.move(source, destination)
            print(f'Successfully moved {source}')
            logging.info(f'Successfully moved {source}')
        except shutil.Error:
            print(f'File already exists: {source}')
            logging.info(f'FileExistError: {source}')

    """The next 3 function are used to find the matching files and call the action.
       The functions are called on the on the respective 'main' function.
       """
    def startswith_file(self, names_startswith, extensions_list, folder, destination):
        file = self
        folder = folder  # = folder_path in root mode, root_path in tree mode
        if any(file.startswith(p) for p in names_startswith):
            if any(file.endswith(e) for e in extensions_list):
                file_list = Path(folder, file)
                if action == 'delete' or action == 'd':
                    Condition.deleting(file_list)
                elif action == 'move' or action == 'm':
                    Condition.moving(file_list, destination)

    def has_file(self, names_has, extensions_list, folder, destination):
        file = self
        filename = file.split('.')
        folder = folder  # = folder_path in root mode, root_path in tree mode
        if any(p in filename[0] for p in names_has):
            if any(file.endswith(e) for e in extensions_list):
                file_list = Path(folder, file)
                if action == 'delete' or action == 'd':
                    Condition.deleting(file_list)
                elif action == 'move' or action == 'm':
                    Condition.moving(file_list, destination)

    def endswith_file(self, names_endswith, extensions_list, folder, destination):
        file = self
        filename = file.split('.')
        folder = folder  # = folder_path in root mode, root_path in tree mode
        if any(filename[0].endswith(p) for p in names_endswith):
            if any(file.endswith(e) for e in extensions_list):
                file_list = Path(folder, file)
                if action == 'delete' or action == 'd':
                    Condition.deleting(file_list)
                elif action == 'move' or action == 'm':
                    Condition.moving(file_list, destination)

    """Loops through each file in the source.
       Depending on the action and mode it will either delete or move the files using send2trash or shutil respectively.
       This applies to all 3 conditions.
       File is split on HAS and ENDSWITH so that only the file name is checked.
       """
    def name_startswith(self, folder_path, extensions_list, destination):
        names_startswith = self
        folder_path = folder_path   # = source when used for moving
        destination = destination   # ONLY used for moving
        if mode == 'tree' or mode == 't':
            logging.info(
                f'Mode: TREE | Condition is STARTSWITH: {names_startswith}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for root_folder, subfolders, files in os.walk(folder_path):
                for file in files:
                    Condition.startswith_file(file, names_startswith, extensions_list, root_folder, destination)
        elif mode == 'root' or mode == 'r':
            logging.info(
                f'Mode: ROOT | Condition is STARTSWITH: {names_startswith}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for file in os.listdir(folder_path):
                Condition.startswith_file(file, names_startswith, extensions_list, folder_path, destination)

    def name_has(self, folder_path, extensions_list, destination):
        names_has = self
        folder_path = folder_path   # = source when used for moving
        destination = destination   # ONLY used for moving
        if mode == 'tree' or mode == 't':
            logging.info(
                f'Mode: TREE | Condition is HAS: {names_has}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for root_folder, subfolders, files in os.walk(folder_path):
                for file in files:
                    Condition.has_file(file, names_has, extensions_list, root_folder, destination)
        elif mode == 'root' or mode == 'r':
            logging.info(
                f'Mode: ROOT | Condition is HAS: {names_has}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for file in os.listdir(folder_path):
                Condition.has_file(file, names_has, extensions_list, folder_path, destination)

    def name_endswith(self, folder_path, extensions_list, destination):
        names_endswith = self
        folder_path = folder_path   # = source when used for moving
        destination = destination   # ONLY used for moving
        if mode == 'tree' or mode == 't':
            logging.info(
                f'Mode: TREE | Condition is ENDSWITH: {names_endswith}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for root_folder, subfolders, files in os.walk(folder_path):
                for file in files:
                    Condition.endswith_file(file, names_endswith, extensions_list, root_folder, destination)
        elif mode == 'root' or mode == 'r':
            logging.info(
                f'Mode: ROOT | Condition is ENDSWITH: {names_endswith}. Extensions are: {extensions_list} | Source is: {folder_path} | Destination is: {destination}')
            for file in os.listdir(folder_path):
                Condition.endswith_file(file, names_endswith, extensions_list, folder_path, destination)
