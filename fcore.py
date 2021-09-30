import os


class Filter:
    _BREAK_LINE_SYMBOL = int(len('\n'))

    def __init__(self, origin_path: str, destination_path: str = '', qty_symbols: int = 8):
        self._origin = origin_path
        self._qty_symbols = qty_symbols
        sep = os.sep
        segments_origin_path = origin_path.split(sep)
        file_name_filtered = 'filtered_' + segments_origin_path.pop()
        if destination_path == '':
            self._destination = sep.join(segments_origin_path) + sep + file_name_filtered
        else:
            self._destination = destination_path + sep + file_name_filtered

    def run(self):
        self._run_specify_encode(encoding='utf-8')

    def _run_specify_encode(self, encoding: str):
        print('filtration started... \n')
        with open(self._origin, encoding=encoding) as origin:
            with open(self._destination, 'w', encoding=encoding) as destination:
                old_qty = 0
                new_qty = 0
                try:
                    for line in origin:
                        old_qty = old_qty + 1
                        if len(line) >= (self._qty_symbols + self._BREAK_LINE_SYMBOL):
                            destination.writelines(line)
                            new_qty = new_qty + 1
                    print(f'\nqty lines in source file == {old_qty}')
                    print(f'qty lines in new file == {new_qty}')
                    print("\nI'm tired, but I did my job\n")
                except UnicodeDecodeError:
                    print('\\ 0_0 /\n\ndanger word --> ' + str(line) + f'encoding error in {old_qty} line\n')
                    response_on_error = input('would you like to specify a different encoding? y/n\n')
                    if response_on_error.lower() == 'y':
                        user_encoding = str(input("\ntype your encoding (example: 'latin-1') => "))
                        user_encoding = user_encoding.replace("'", '').replace('"', '')
                        self._run_specify_encode(user_encoding)
                    else:
                        exit('\nBye :(')
        origin.close()
        destination.close()
