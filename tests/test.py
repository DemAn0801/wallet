import unittest

from classes.FileManager import FileManager

class TestFileManager(unittest.TestCase):
    file_balance_read = "tests/test_files/for_read/test_balance.csv"
    file_test_append = "tests/test_files/for_append/append_test.csv"
    def test_read(self):
        fm = FileManager()
        result: list = [x for x in fm.read_file(self.file_balance)]
        self.assertEqual(result[0]["Баланс"], "7000")
        
    def test_append_row(self):
      fm = FileManager()
      data = [
              {
                  "Дата": "2022-12-01",
                  "Категория": "Расход",
                  "Описание": "Квартплата",
                  "Сумма": "1000",
              }
      ],
      fm.create_row(file_name=self.file_test_append, row=data, ) 
if __name__ == "__main__":
  unittest.main()