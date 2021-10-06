from os import path
from fcore.worker import *
from fcore.functional import Functional
from fcore.filter import MinSymbolFilter, MaxSymbolFilter


class Controller:
    _file_path: str = None
    _worker: MainWorker
    _functional: Functional

    def set_file_path(self, file: str):
        if self.check_file_path(file):
            self._file_path = file
            return True
        else:
            return False

    def file_is_available(self):
        if self._file_path is not None:
            return True
        else:
            return False

    def check_file_path(self, file: str):
        if path.exists(file):
            return True
        if path.isfile(file):
            return True
        return False

    def run(self):
        core = MainWorker(self._file_path, 'latin-1')
        self._functional = Functional(core)
        core = self._functional.build_worker()
        core.run()

    # def get_digit(self):
    #     global qty_symbols
    #     try:
    #         qty_symbols = int(input("type min. qty symbols in lines => "))
    #     except ValueError:
    #         print('you entered incorrect value. Please type correct digit')
    #         get_digit()
    #     return qty_symbols

# if not qty_symbols >= DEFAULT_QTY_NUM:
#     response = input(f'your qty symbols ({qty_symbols}) for lines is small (normal = {DEFAULT_QTY_NUM}). '
#                      f'you want change qty? y/n \n')
#     if response == 'Y' or response == 'y':
#         get_digit()
