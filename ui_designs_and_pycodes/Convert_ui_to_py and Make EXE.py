import os
import sys
import colorama

global icon
icon_path = os.path.abspath("Pheonix.ico")

global files_dict
files_dict = {}

global py_files
py_files = []


def gui_maker(selection):
    print(colorama.Fore.GREEN+f'making {files_dict[selection]} executable'+colorama.Style.RESET_ALL)
    file_name = files_dict[selection]
    os.system(f'pyinstaller -w -F -i {icon_path} {file_name}')


def gui_maker_choice():
    global files_dict
    global py_files

    i = 1
    for file_name in py_files:
        file_name = file_name + str('.py')
        files_dict[str(i)] = file_name
        i += 1

    print(f'file dict = {files_dict} ')

    cnt = 0
    condition = input("Turn into a GUI? (y / n) ")
    if condition == 'y' or 'yes':
        for file in files_dict.items():
            if cnt % 2 == 0:
                print(colorama.Fore.LIGHTBLUE_EX+f'{file[0]} '+colorama.Style.RESET_ALL+f'for file '+colorama.Fore.LIGHTBLUE_EX+f'{file[1]}' +colorama.Style.RESET_ALL)
            else:
                print(
                    colorama.Fore.CYAN + f'{file[0]} ' + colorama.Style.RESET_ALL + f'for file ' + colorama.Fore.CYAN + f'{file[1]}' + colorama.Style.RESET_ALL)
            cnt += 1
        select = input('which file number would you like to render? ')
        return select
    elif condition == 'n' or 'no':
        sys.exit()


def convert_to_py():

    global py_files

    names = os.listdir()
    names = [name for name in names if '.ui' in name]
    print(f'files found:\n {names}')

    py_files = (input("Which '.ui' file would you like to convert to '.py' ? (SPACE to separate) ")).split(" ")
    py_files = [item.split(".ui")[0] if '.ui' in item else item for item in py_files]

    print(py_files)

    for file in py_files:
        print(file)
        try:
            if os.path.isfile(os.path.abspath(f"{file}+.py")):
                print(colorama.Fore.RED + f'{file}.py already exists, skipping.' + colorama.Style.RESET_ALL)
            else:
                os.system(f'pyuic5 -x {file} -o {file}.py')
                print(colorama.Fore.BLUE + f'rendering: {file}' + colorama.Style.RESET_ALL)
                print (colorama.Fore.GREEN+f'{file}.ui ------------>> {file}.py'+colorama.Style.RESET_ALL)

        except:
            pass


if __name__ == '__main__':
    convert_to_py()
    selection = gui_maker_choice()
    gui_maker(selection)

