
from classes.FileManager import FileManager
from constans import BALANCE_FILE_NAME, WALLET_FILE_NAME


class WalletExecutor:
    
    file_manager = FileManager()
    
    def get_ballance(self) -> str:
        return "wallet_records.csv"
            
    def top_up_ballance(self, data: list):
        self.make_record(data)
        balance: int = int(self.file_manager.read_file(BALANCE_FILE_NAME))
        change_sum = int(data[3]) if data[1] == "Доход" else -abs(int(data[1]))
        new_ballance = str(balance + change_sum)
        self.update_balance(BALANCE_FILE_NAME, new_ballance, "w+" )
        
    def update_balance(self, file_name: str, row: str, open_parametr: str):
        self.file_manager.update_file(file_name, row, open_parametr)
        
    def make_record(self, data):
         self.file_manager.write_row(WALLET_FILE_NAME, ";".join(data), "a")
    
    def buy(self):
        pass