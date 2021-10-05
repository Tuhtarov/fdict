import os

from fcore.filter import AbstractFilter


class AbstractWorker:
    def __init__(self, file: str, encode: str):
        self._file = file
        self._encode = encode
        sep = os.sep
        segments_origin_path = file.split(sep)
        self._file_name_origin = segments_origin_path.pop()
        self._file_buffer = sep.join(segments_origin_path) + sep + 'buffer_' + self._file_name_origin
        self._file_filtered = sep.join(segments_origin_path) + sep + 'filtered_' + self._file_name_origin

    def run(self):
        pass


class MainWorker(AbstractWorker):
    _filters = []

    def __init__(self, file: str, encode: str):
        super().__init__(file, encode)

    def append_filter(self, filter: AbstractFilter):
        self._filters.append(filter)

    def run(self):
        with open(self._file, encoding=self._encode) as origin:
            with open(self._file_buffer, 'w+', encoding=self._encode) as buffer:
                print(f'\n>>> copy {self._file_name_origin} in buffer')
                amount_old_lines = 0
                amount_removed_lines = 0

                # скопировал данные в буфер
                for line in origin:
                    buffer.writelines(line)
                    amount_old_lines += 1
                print(f'--- copy is successful ({amount_old_lines} lines)\n')

                for filtration in self._filters:
                    buffer.seek(0)
                    filtration.info()

                    # прочитал буфер, отфильтровал данные, занёс в конечный файл
                    with open(self._file_filtered, 'w', encoding=self._encode) as filtered:
                        for line in buffer:
                            result = filtration.run(line)
                            if result:
                                filtered.writelines(result)
                    buffer.seek(0)

                    # сохранил отфильтрованные строки для нового перебора
                    with open(self._file_filtered, 'r', encoding=self._encode) as filtered:
                        with open(self._file_buffer, 'w', encoding=self._encode) as buffer2:
                            for line in filtered:
                                buffer2.writelines(line)

                    amount_removed_lines = amount_removed_lines + filtration.send_result()

        # на всякий случай закрыл всё, ибо не уверен в том, что with всегда закрывает соединение сам
        for connection in [origin, buffer, filtered]:
            connection.close()
        os.remove(self._file_buffer)

        print(f'>>> result')
        print(f'--- {amount_removed_lines} removed')
        print(f'--- {amount_old_lines - amount_removed_lines} saved \n')
