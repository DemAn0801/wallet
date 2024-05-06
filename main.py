

import csv
from classes.UserActions import UserActions
from classes.FileManager import FileManager

from constans import WALLET_FILE_NAME, BALANCE_FILE_NAME

def make_choice(response: int) -> None:
    user_actons: UserActions = UserActions()
    file_manager: FileManager = FileManager()
    match response:
        case "1":
            print(user_actons.get_ballance())
        case "2":
            checked_data: list = user_actons.user_input_data_for_create_record()
            file_manager.append_row(WALLET_FILE_NAME, ";".join(checked_data))
            balance: int = int(file_manager.read_file(BALANCE_FILE_NAME))
            change_sum = int(checked_data[3]) if checked_data[1] == "Доход" else -abs(int(checked_data[3]))
            new_ballance = str(balance + change_sum)
            file_manager.update_file(BALANCE_FILE_NAME, new_ballance, "w+")
        case "3":
            checked_data: list = user_actons.user_input_data_for_change_record()
            row_index: int = file_manager.find_record(checked_data)
            if not row_index == -1:
                wallet: list = [ x for x in file_manager.read_file(WALLET_FILE_NAME)]
                new_sum: int = int(input("Ведите новую сумму\n"))
                wallet[row_index]["Сумма"] = str(new_sum)
                with open(WALLET_FILE_NAME, "w+", newline="") as f:
                    x = ["Дата","Категория","Описание","Сумма"]
                    www = csv.DictWriter(f, fieldnames=x,delimiter=";")
                    www.writeheader()
                    www.writerows(wallet)
                new_ballance = 0
                for w in wallet:
                    if w["Категория"] == "Доход":
                        new_ballance += int(w["Сумма"])
                    else:
                        new_ballance -= int(w["Сумма"])
                file_manager.update_file(BALANCE_FILE_NAME, str(new_ballance))
                        
            else:
                print("Запись не найдена")
        case _:
            print("Выберите один из предложенных вариантов")
            
def main():
    while True:
        response: str = input("Выберите действие по номеру пункта:\n\
                1. Посмотреть балланс\n\
                2. Изменить балланс\n\
                3. Изменить сумму в одной из записей\n"
            )
        make_choice(response)

if __name__ == "__main__":
    main()