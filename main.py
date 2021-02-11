import logging
import getpass
from pathlib import Path

# GETS username of path and creates log dir if doesn't exist, else pass - if permission denied exit on user input
username = getpass.getuser()
log_dir = Path('C:/users/', username, 'AppData/Local/easy_delete_move')
try:
    Path.mkdir(log_dir)
except FileExistsError:
    pass
except PermissionError:
    input(f'Permission denied: Unable to create log dir in {log_dir} \nPress any key to exit \n')
# CREATES log file and logging format - logs script start
log_file = log_dir.joinpath('logs.log')
logging.basicConfig(filename=log_file, format='%(asctime)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S %z | ', level=logging.INFO)
logging.info('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
logging.info(f'Script start.')


# FORCES user between tree or root mode
def mode_choice(action):
    while True:
        mode = input().lower()
        if mode == 'tree' or mode == 't':
            action_mode(action, mode)
            if action == 'delete' or action == 'd':
                import easy_delete
            elif action == 'move' or action == 'm':
                import easy_move
            break
        elif mode == 'root' or mode == 'r':
            action_mode(action, mode)
            if action == 'delete' or action == 'd':
                import easy_delete
            elif action == 'move' or action == 'm':
                import easy_move
            break
        else:
            print('Valid mode is tree or root')
            continue


# USED to store action and mode
def action_mode(action, mode):
    with open(log_dir.joinpath('action.txt'), 'w') as f:
        f.write(action)
    with open(log_dir.joinpath('mode.txt'), 'w') as f:
        f.write(mode)


""" main function
    User is forced to select between delete/move action and tree/root mode
    Action and mode are saved in a .txt file to be read by the Condition class"""


def main():
    print('Script has started.')
    print('What do you want to do with the files? [delete / move]')

# LOOPS to force user pick between move or delete only
    while True:
        action = input().lower()
        if action == 'delete' or action == 'd':
            print('Pick the mode: [ tree / root]')
            mode_choice(action)
        elif action == 'move' or action == 'm':
            print('Pick the mode: [ tree / root]')
            mode_choice(action)
        else:
            print('Valid choices are [delete] or [move]')
            continue
        break


# RUNS main function otherwise only logs script start and gets log dir & file variable
if __name__ == '__main__':
    main()
else:
    log_file = log_file
    log_dir = log_dir
