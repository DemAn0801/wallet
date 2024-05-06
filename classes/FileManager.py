class FileManager:
    
    def read_file(self, file_name: str) -> str:
        with open(file_name, "r") as f:
            balance = f.read()
            return balance
        
    def write_row(self, file_name: str, row: str, open_parametr: str) -> None:
        with open(file_name, open_parametr) as f:
            f.write(row)
            f.write("\n")
    
    def update_file(self, file_name: str, row: str, open_parametr: str):
        self.write_row(file_name, row, open_parametr)
            