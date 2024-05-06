

from classes.UserActions import UserActions
from classes.FileManager import FileManager

from constans import WALLET_FILE_NAME, BALANCE_FILE_NAME

def make_choice(response: int) -> None:
    user_actons: UserActions = UserActions()
    file_manager: FileManager = FileManager()
    match response:
        case "1":
            print(file_manager.read_file(BALANCE_FILE_NAME))
        case "2":
            checked_data: str = user_actons.user_input_data()
            file_manager.append_row(WALLET_FILE_NAME, ";".join(checked_data))
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
                2. Изменить балланс\n\
                3. Изменить запись"
            )
        response: str = input()
        make_choice(response)

if __name__ == "__main__":
    main()