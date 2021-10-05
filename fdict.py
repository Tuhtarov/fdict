import os.path
from fcore.worker import MainWorker
from fcore.filter import MinSymbolFilter, MaxSymbolFilter

delimiter = '==================================='
print('')
print(delimiter)
print("+=============RUNNING=============+")
print(delimiter)
#
# file_path = ''
# qty_symbols = 8
# DEFAULT_QTY_NUM = 8
#
#
# def get_file_path():
#     global file_path
#     file_path = str(input("\nType full path of file => "))
#
#
# get_file_path()
#
#
# def check_file_path(f_path):
#     if not os.path.exists(f_path):
#         return 'path not exists'
#     if not os.path.isfile(f_path):
#         return 'this not file'
#     return 'ok'
#
#
# while check_file_path(file_path) != 'ok':
#     print(check_file_path(file_path))
#     print("please, type the correct path")
#     get_file_path()
# else:
#     print('ok.. file is correct!\n')

file_path = '/home/aleksandr/Desktop/hs/filtered_rock.txt'

core = MainWorker(file_path, 'latin-1')
core.append_filter(MaxSymbolFilter(15))
core.append_filter(MinSymbolFilter(10))
core.run()

# def get_digit():
#     global qty_symbols
#     try:
#         qty_symbols = int(input("type min. qty symbols in lines => "))
#     except ValueError:
#         print('you entered incorrect value. Please type correct digit')
#         get_digit()
#     return qty_symbols
#
#
# get_digit()

# if not qty_symbols >= DEFAULT_QTY_NUM:
#     response = input(f'your qty symbols ({qty_symbols}) for lines is small (normal = {DEFAULT_QTY_NUM}). '
#                      f'you want change qty? y/n \n')
#     if response == 'Y' or response == 'y':
#         get_digit()



# filter_core = Filter(origin_path=file_path, qty_symbols=qty_symbols)
# filter_core.run()

print(delimiter)
print('---> The end. Bye :)\n')
print("---> developer: 'Tukhtarov Dynamic'")
print(delimiter)
