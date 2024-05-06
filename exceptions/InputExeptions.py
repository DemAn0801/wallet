class NotEnoughtArgs(Exception):
    def __init__(self, message="Недостаточно аргументов"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n"