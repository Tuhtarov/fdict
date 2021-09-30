import os


class Filter:
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
        print('filtration started... \n')
        with open(self._origin) as origin:
            with open(self._destination, 'w') as destination:
                for line in origin:
                    if len(line) >= self._qty_symbols:
                        destination.writelines(line)

        origin.close()
        destination.close()
