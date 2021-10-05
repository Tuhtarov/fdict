from fcore.worker import *
from fcore.filter import *


class Functional:
    __delimiter = '-----------------------------------'
    _MIN = 1
    _MAX = 2
    _POSITIVE = 3
    _NEGATIVE = 4
    _EXIT = 0
    _PRINT_MENU = 9

    _menu = {
        _MIN: 'Set filter "minimum number of characters"',
        _MAX: 'Set filter "maximum number of characters"',
        _POSITIVE: 'Set filter "include words in strings"',
        _NEGATIVE: 'Set filter "exclude words in strings"',
        _PRINT_MENU: '<--- Show menu',
        _EXIT: '---> Save and continue'
    }

    _worker: MainWorker

    def __init__(self, worker: MainWorker):
        self._worker = worker

    def run(self):
        return self.show_menu()

    def show_menu(self):
        self.print_menu()
        worker = self.choose_loop()
        return worker

    def print_menu(self):
        print(f'\n---> MENU\n{self.__delimiter}')
        for line in self._menu:
            print(f'{line} = {self._menu[line]}')

    def choose_loop(self):
        number: int = None
        while not number == self._EXIT:
            try:
                number = int(input('\nSpecify number for continue => '))
                if number == self._MIN:
                    min = int(input('* min. value => '))
                    self._worker.append_filter(MinSymbolFilter(min))
                if number == self._MAX:
                    max = int(input('* max. value => '))
                    self._worker.append_filter(MaxSymbolFilter(max))
                if number == self._POSITIVE:
                    word = str(input('* positive word => '))
                    self._worker.append_filter(WordPositiveFilter(word))
                if number == self._NEGATIVE:
                    word = str(input('* negative word => '))
                    self._worker.append_filter(WordPositiveFilter(word))
                if number == self._PRINT_MENU:
                    self.print_menu()
                if number == self._EXIT:
                    if not self._worker.is_ready():
                        print('* ERROR: you have not specified any filters')
                        self.choose_loop()
                        return
                if not number in self._menu:
                    print('* unknown number')
            except ValueError:
                print('* ERROORRRRRR: please, type number')
                self.choose_loop()
                return
        print(f'{self.__delimiter}')
        print('---> CONTINUE\n')
        return self._worker
