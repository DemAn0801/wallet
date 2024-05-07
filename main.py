from classes.UserActions import UserActions
from classes.FileManager import FileManager

from constans import WALLET_FILE_NAME, BALANCE_FILE_NAME


def make_choice(response: int, fm: FileManager, user_actions: UserActions) -> None:
    match response:
        case "1":
            print(f"Сейчас на баллансе {user_actons.get_ballance()}")
        case "2":
            checked_data: list = user_actons.user_input_data_for_create_record()
            file_manager.create_row(
                WALLET_FILE_NAME,
                [
                    {
                        "Дата": checked_data[0],
                        "Категория": checked_data[1],
                        "Описание": checked_data[2],
                        "Сумма": checked_data[3],
                    }
                ],
            )
            balance: int = int(user_actons.get_ballance())
            change_sum = (
                int(checked_data[3])
                if checked_data[1] == "Доход"
                else -abs(int(checked_data[3]))
            )
            new_ballance: str = str(balance + change_sum)
            file_manager.update_file(
                BALANCE_FILE_NAME, [{"Баланс": new_ballance}], "w+"
            )
        case "3":
            checked_data: list = user_actons.user_input_data_for_change_record()
            row_index: int = file_manager.find_record(WALLET_FILE_NAME, checked_data)
            if not row_index == -1:
                wallet: list = [x for x in file_manager.read_file(WALLET_FILE_NAME)]
                new_sum: int = int(input("Ведите новую сумму\n"))
                wallet[row_index]["Сумма"] = str(new_sum)
                file_manager.update_record(wallet)
                new_ballance = 0
                for row in wallet:
                    if row["Категория"] == "Доход":
                        new_ballance += int(row["Сумма"])
                    else:
                        new_ballance -= int(row["Сумма"])
                file_manager.update_file(
                    BALANCE_FILE_NAME, [{"Баланс": str(new_ballance)}]
                )

            else:
                print("Запись не найдена")
        case _:
            print("Выберите один из предложенных вариантов")


def main(file_manager: FileManager, user_actions: UserActions):
    while True:
        response: str = input(
            "Выберите действие по номеру пункта:\n\
                1. Посмотреть балланс\n\
                2. Изменить балланс\n\
                3. Изменить сумму в одной из записей\n"
        )
        make_choice(response, file_manager, user_actions)


if __name__ == "__main__":
    user_actons = UserActions()
    file_manager = FileManager()
    file_manager.prepare_files()
    main(file_manager, user_actons)
