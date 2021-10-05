class AbstractFilter:
    _increment: int

    def __init__(self):
        self._increment = 0

    def inc(self):
        self._increment = self._increment + 1

    def info(self):
        pass

    def run(self, line: str):
        pass

    def send_result(self):
        print('--- removed ' + f'{self._increment}' + ' lines\n')
        return self._increment


class MinSymbolFilter(AbstractFilter):
    def __init__(self, min_symbol: int = 8):
        super().__init__()
        self._min_symbol = min_symbol

    def info(self):
        print('>>> filtration by minimal qty of symbols (' + f'{self._min_symbol})')

    def run(self, line: str):
        if len(line) >= (self._min_symbol + 1):
            return line
        else:
            self.inc()
            return False


class MaxSymbolFilter(AbstractFilter):
    def __init__(self, max_symbol: int):
        super().__init__()
        self._max_symbol = max_symbol

    def info(self):
        print('>>> filtration by maximum qty of symbols (' + f'{self._max_symbol})')

    def run(self, line: str):
        if len(line) < (self._max_symbol + 1):
            return line
        else:
            self.inc()
            return False


class WordPositiveFilter(AbstractFilter):
    def __init__(self, words: [str]):
        super().__init__()
        self._words = words

    def run(self, line: str):
        if line in self._words:
            self.inc()
            return line


class WordNegativeFilter(AbstractFilter):
    def __init__(self, words: [str]):
        super().__init__()
        self._words = words

    def run(self, line: str):
        if line not in self._words:
            return line
        else:
            return False
