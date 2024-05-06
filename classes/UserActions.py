# from main import main
import re

from classes.DtataChecker import DataChecker
from classes.FileManager import FileManager
from constans import BALANCE_FILE_NAME
from exceptions.InputExeptions import (
    WrongArgumentsQuantity,
    NotValidSum,
    WrongOperationType,
)


class UserActions:

    def get_data(self, text: str) -> list:
        return input(text).split(",")

    def user_input_data_for_create_record(self) -> list:
        checker: DataChecker = DataChecker()
        user_actions: UserActions = UserActions()
        data: list = user_actions.get_data(
            "Введите через запятую, без пробелов, дату, тип операции, описание, сумму,\n\
                        например: 2024-12-01,Доход,Зарплата,3000\n\
                        или: 2024-12-01,Расход,Квартплата,3000\n"
        )
        response: list = []
        try:
            checked_data: list = checker.check_data_for_new_record(data)
            response: list = checked_data
        except WrongArgumentsQuantity:
            print(WrongArgumentsQuantity())
            response = self.user_input_data_for_create_record()
        except WrongOperationType:
            print(WrongOperationType())
            response: list = self.user_input_data_for_create_record()
        except NotValidSum:
            print(NotValidSum())
            response: list = self.user_input_data_for_create_record()
        return response

    def user_input_data_for_change_record(self) -> list:
        checker: DataChecker = DataChecker()
        user_actions: UserActions = UserActions()
        data: list = user_actions.get_data(
            "Введите через запятую, без пробелов, дату, тип операции, описание, сумму,\n\
                        например: 2024-12-01,Доход,Зарплата\n\
                        или: 2024-12-01,Расход,Квартплата\n"
        )
        response: list = []
        try:
            checked_data: list = checker.check_data_for_change_record(data)
            response: list = checked_data
        except WrongArgumentsQuantity:
            print(WrongArgumentsQuantity())
            response = self.user_input_data_for_change_record()
        except WrongOperationType:
            print(WrongOperationType())
            response: list = self.user_input_data_for_change_record()
        except NotValidSum:
            print(NotValidSum())
            response: list = self.user_input_data_for_change_record()
        return response

    def get_ballance(self) -> str:
        file_manager: FileManager = FileManager()
        balance = [x for x in file_manager.read_file(BALANCE_FILE_NAME)]
        return balance[0]['Баланс']
