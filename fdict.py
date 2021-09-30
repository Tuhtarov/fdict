import os.path
from fcore import Filter

# это пэт проект начинающего разраба
# вся суть данной приложухи заключается в фильтрации словаря (файла с паролями) по заданным критериям
#
# пример использования: есть большой файл > 1000 строк, стандартные пароли для WPA-2 сетей начинаются с 8 символов,
# но зачастую, в словарях с интернета много строк, где количество символов < 8, что затрудняет работу утилиты "hashcat"
#
# алгоритм фильтрации таков: открывается словарь, создаётся дополнительный файл в родительском каталоге открытого файла
# в этот дополнительный файл, строчкой за строчкой, помеющатся строки с указанной длинной символов.

delimiter = '==========================='
print('')
print(delimiter)
print("+========+RUNNING=========+")
print(delimiter)

file_path = ''
qty_symbols = 8
DEFAULT_QTY_NUM = 8


def get_file_path():
    global file_path
    file_path = str(input("\nType full path of file => "))



get_file_path()


def check_file_path(f_path):
    if not os.path.exists(f_path):
        return 'path not exists'
    if not os.path.isfile(f_path):
        return 'this not file'
    return 'ok'


while check_file_path(file_path) != 'ok':
    print(check_file_path(file_path))
    print("please, type the correct path")
    get_file_path()
else:
    print('ok.. file is correct!\n')


def get_digit():
    global qty_symbols
    try:
        qty_symbols = int(input("type min. qty symbols in lines => "))
    except ValueError:
        print('you entered incorrect value. Please type correct digit')
        get_digit()
    return qty_symbols


get_digit()

if not qty_symbols >= DEFAULT_QTY_NUM:
    response = input(f'your qty symbols ({qty_symbols}) for lines is small (normal = {DEFAULT_QTY_NUM}). '
                     f'you want change qty? y/n \n')
    if response == 'Y' or response == 'y':
        get_digit()

filter_core = Filter(origin_path=file_path, qty_symbols=qty_symbols)
filter_core.run()

print(delimiter)
print('---> The end. Bye :)')
print(delimiter)
