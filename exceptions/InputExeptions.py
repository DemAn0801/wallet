class NotEnoughtArgs(Exception):
    def __init__(self, message="Недостаточно аргументов"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n"
    
    
class WrongOperationType(Exception):
    def __init__(self, message="Неверный тип операции.\n Допустимые варианты:\n Доход, Расход"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n"


class NotValidSum(Exception):
    def __init__(self, message="Некорректно введена сумма\n"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n"