import sys
from ConditionClass import *                # ACTION, mode, Condition class, logging, Path, log file from main

logging.info(f'Action is : DELETE FILES')
print(f'Action: {action.upper()} \nMode: {mode.upper()}')

extensions_list = input('Extensions are: ').replace(' ', '').split(',')
folder_path = Path(input('Target is: ').replace('"', ''))

"""" Forces user to choose between the 3 conditions then prompts them for the sub conditions.
     calls the appropriate Condition. class function.
     """
while True:
    condition_choice = input('Condition is [startswith / has / endswith]: ').lower()
    if condition_choice == 'startswith' or condition_choice == 's':
        name_startswith = input('Startswith list: ').replace(' ', '').split(',')
        Condition.name_startswith(name_startswith, folder_path, extensions_list, 'NA')
        break
    elif condition_choice == 'has' or condition_choice == 'h':
        name_has = input('Has list: ').replace(' ', '').split(',')
        Condition.name_has(name_has, folder_path, extensions_list, 'NA')
        break
    elif condition_choice == 'endswith' or condition_choice == 'e':
        name_endswith = input('Endswith list: ').replace(' ', '').split(',')
        Condition.name_endswith(name_endswith, folder_path, extensions_list, 'NA')
        break
    else:
        print('Valid choices are: [startswith/has/endswith]')
        continue

# PRINTS log file location, ends and logs script upon user input
print(f'Log location is: {log_file}')
end = input('Press any key to exit\n')
sys.exit(logging.info('Script end.'))
