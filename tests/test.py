import unittest

from classes.FileManager import FileManager

class TestFileManager(unittest.TestCase):
    file_balance = "tests/test_balance.csv"
    def test_read(self):
        fm = FileManager()
        result: list = [x for x in fm.read_file(self.file_balance)]
        self.assertEqual(result[0]["Баланс"], "7000")
        
if __name__ == "__main__":
  unittest.main()