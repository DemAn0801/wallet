class FileManager:
    
    def read_file(self, file_name: str) -> str:
        with open(file_name, "r") as f:
            balance = f.read()
            return balance
        
    def append_row(self, file_name: str, row: str, open_parametr: str="a") -> None:
        with open(file_name, open_parametr) as f:
            f.write(row)
            f.write("\n")
    
    def update_file(self, file_name: str, row: str, open_parametr: str="w+"):
        self.append_row(file_name, row, open_parametr)
            