import re
from exceptions.InputExeptions import (
    WrongArgumentsQuantity,
    NotValidSum,
    WrongOperationType,
)
from constans import TYPES_OF_RECORD


class DataChecker:
    def check_date_format(self, date: str) -> str:
        if not re.match(r"\d{4}\-\d{2}\-\d{2}", date):
            new_date = input(
                "Неверный формат даты.\n\
                Введите дату в формате ГГГГ-ММ-ДД. Например: 2024-12-01\n"
            )
            checked_new_date = self.check_date_format(new_date)
            return checked_new_date
        return date

    def check_data_for_new_record(self, data: list) -> list:
        if not len(data) == 4:
            raise WrongArgumentsQuantity()
        if data[1] not in TYPES_OF_RECORD:
            raise WrongOperationType()
        try:
            int(data[3])
        except ValueError:
            raise NotValidSum()
        date: str = self.check_date_format(data[0])
        return [date, data[1], data[2], data[3]]

    def check_data_for_change_record(self, data: list) -> list:
        if not len(data) == 3:
            raise WrongArgumentsQuantity()
        if data[1] not in TYPES_OF_RECORD:
            raise WrongOperationType()
        date: str = self.check_date_format(data[0])
        return [date, data[1], data[2]]
