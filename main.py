

from classes.DataHandler import DataHandler
from classes.DtataChecker import DataChecker
from classes.FileManager import FileManager
from exceptions.InputExeptions import NotEnoughtArgs

from constans import WALLET_FILE_NAME, BALANCE_FILE_NAME

def user_input_data():
    checker: DataChecker = DataChecker()
    data_handler: DataHandler = DataHandler()
    data: list = data_handler.get_data("Введите через запятую, без пробелов, дату,сумму,описание\n\
                    например: 2024-12-01,Доход,Зарплата,3000\n\
                         или: 2024-12-01,Расход,Квартплата,3000")
    response = []
    try:
        checked_data: list = checker.check_data(data)
        response = checked_data
    except NotEnoughtArgs as e:
        print(e)
        response = user_input_data()
    return response

def make_choice(response: int) -> None:
    file_manager: FileManager = FileManager()
    
    match response:
        case "1":
            print(file_manager.read_file(BALANCE_FILE_NAME))
        case "2":
            checked_data = user_input_data()
            print("🐍 File: wallet/main.py | Line: 31 | make_choice ~ checked_data",checked_data)
            file_manager.append_row(WALLET_FILE_NAME, ";".join(checked_data), "a")
            balance: int = int(file_manager.read_file(BALANCE_FILE_NAME))
            change_sum = int(checked_data[3]) if checked_data[1] == "Доход" else -abs(int(checked_data[3]))
            new_ballance = str(balance + change_sum)
            file_manager.update_file(BALANCE_FILE_NAME, new_ballance, "w+")
        case "3":
            pass
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