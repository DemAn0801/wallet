import csv
from constans import BALANCE_FILE_NAME, WALLET_FILE_NAME


class FileManager:
    def prepare_files(self):
        try:
            with open(BALANCE_FILE_NAME, "x+") as f:
                f.write("Баланс\n")
                f.write("0")
        except FileExistsError:
            pass
        try:
            with open(WALLET_FILE_NAME, "x+") as f:
                f.write("Дата;Категория;Описание;Сумма\n")
        except FileExistsError:
            pass

    def read_file(self, file_name: str) -> iter:
        with open(file_name, "r") as f:
            spamreader = csv.DictReader(f, delimiter=";")
            for line in spamreader:
                yield line

    def create_row(
        self,
        file_name: str,
        row: list[dict],
        open_parametr: str = "a",
        headers: list = ["Дата", "Категория", "Описание", "Сумма"],
    ) -> None:
        with open(file_name, open_parametr, newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=headers, delimiter=";")
            if open_parametr == "w+":
                dict_writer.writeheader()
            dict_writer.writerows(row)

    def update_file(
        self,
        file_name: str,
        row: list,
        open_parametr: str = "w+",
        headers: list = ["Баланс"],
    ) -> None:
        self.create_row(file_name, row, open_parametr, headers)

    def find_record(self, file_name: str, data: list) -> int:
        searching_tuple: tuple = (data[0], data[1], data[2])
        counter: int = 0
        for line in self.read_file(file_name):
            if (line["Дата"], line["Категория"], line["Описание"]) == searching_tuple:
                return counter
            counter += 1
        return -1

    def update_record(self, wallet):
        with open(WALLET_FILE_NAME, "w+", newline="") as f:
            dict_writer = csv.DictWriter(
                f, fieldnames=["Дата", "Категория", "Описание", "Сумма"], delimiter=";"
            )
            dict_writer.writeheader()
            dict_writer.writerows(wallet)
