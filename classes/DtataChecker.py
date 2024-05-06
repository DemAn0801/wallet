import re


class DataChecker:
    
    def check_date_format(self, date: str) -> str:
        if not re.match(r"\d{4}\-\d{2}\-\d{2}", date): 
            print("Неверный формат даты.\n\
                Введите дату в формате ГГГГ-ММ-ДД. Например: 2024-12-01")
            new_date = input()
            checked_new_date = self.check_date_format(new_date)
            return checked_new_date
        return date
    
    def check_data(self, data: list) -> list:
        date = self.check_date_format(data[0])
        return [date, data[1], data[2], data[3]]