

from classes.DataHandler import DataHandler
from classes.DtataChecker import DataChecker
from classes.FileManager import FileManager
from classes.WalletExecutor import WalletExecutor
import re

from constans import WALLET_FILE_NAME, BALANCE_FILE_NAME

def make_choice(response: int) -> None:
    executor: WalletExecutor = WalletExecutor()
    data_handler: DataHandler = DataHandler()
    file_manager: FileManager = FileManager()
    checker: DataChecker = DataChecker()
    match response:
        case "1":
            print(file_manager.read_file(BALANCE_FILE_NAME))
        case "2":
            data: list = data_handler.input_data("Введите через запятую без пробелов дату,сумму,описание\n\
                    например: 2024-12-01,Доход,Зарплата,3000")
            checked_data: str = checker.check_data(data)
            executor.top_up_ballance(checked_data)
        case "3":
            executor.buy()
        case _:
            print("Выберите один из предложенных вариантов")
            
def main():
    while True:
        print("Выберите действие по номеру пункта:\n\
                1. Посмотреть балланс\n\
                2. Пополнить балланс\n\
                3. Сделать покупку")
        response: str = input()
        make_choice(response)

if __name__ == "__main__":
    main()