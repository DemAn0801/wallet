import csv
from constans import WALLET_FILE_NAME


class FileManager:

    def read_file(self, file_name: str) -> iter:
        with open(file_name, "r") as f:
            spamreader = csv.DictReader(f, delimiter=";")
            for line in spamreader:
                yield line

    def append_row(self, file_name: str, row: str, open_parametr: str = "a") -> None:
        with open(file_name, open_parametr) as f:
            f.write(row)
            f.write("\n")

    def update_file(self, file_name: str, row: str, open_parametr: str = "w+") -> None:
        self.append_row(file_name, row, open_parametr)

    def find_record(self, data: list) -> int:
        searching_tuple: tuple = (data[0], data[1], data[2])
        counter: int = 0
        for line in self.read_file(WALLET_FILE_NAME):
            if (line["Дата"], line["Категория"], line["Описание"]) == searching_tuple:
                print(counter)
                return counter
            counter += 1
        return -1
