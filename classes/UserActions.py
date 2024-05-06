# from main import main
import re

from classes.DtataChecker import DataChecker
from classes.FileManager import FileManager
from constans import BALANCE_FILE_NAME
from exceptions.InputExeptions import NotEnoughtArgs, NotValidSum, WrongOperationType

class UserActions:
    
    def get_data(self: str) -> list:
        print("Введите через запятую, без пробелов, дату, тип операции, описание, сумму,\n\
                    например: 2024-12-01,Доход,Зарплата,3000\n\
                         или: 2024-12-01,Расход,Квартплата,3000")
        return input().split(",")
    
    
    def user_input_data(self) -> str:
        checker: DataChecker = DataChecker()
        user_actions: UserActions = UserActions()
        data: list = user_actions.get_data()
        response: list = []
        try:
            checked_data: list = checker.check_data(data)
            response: str = checked_data
        except NotEnoughtArgs:
            print(NotEnoughtArgs())
            response = self.user_input_data()
        except WrongOperationType:
            print(WrongOperationType())
            response: str = self.user_input_data()
        except NotValidSum:
            print(NotValidSum())
            response: str = self.user_input_data()
        return response
        

    def get_ballance(self) -> str:
        file_manager: FileManager = FileManager()
        balance = [x for x in file_manager.read_file(BALANCE_FILE_NAME)]
        return f"Сейчас на баллансе: {balance[0]}"
        

            

