import unittest

from classes.FileManager import FileManager


class TestFileManager(unittest.TestCase):
    file_test_wallet = "tests/test_files/for_read/test_wallet.csv"
    file_balance_read = "tests/test_files/for_read/test_balance.csv"
    file_test_append = "tests/test_files/for_append/append_test.csv"
    fm = FileManager()

    def test_read(self):
        result: list = [x for x in self.fm.read_file(self.file_balance_read)]
        self.assertEqual(result[0]["Баланс"], "7000")

    def test_append_row(self):
        data = [
            {
                "Дата": "2022-12-01",
                "Категория": "Расход",
                "Описание": "Квартплата",
                "Сумма": "1000",
            }
        ]
        self.fm.create_row(file_name=self.file_test_append, row=data)
        result = ""
        with open(self.file_test_append, "r") as f:
            result = f.read()
        with open(self.file_test_append, "w") as f:
            f.write("")
        self.assertEqual(result, "2022-12-01;Расход;Квартплата;1000\n")

    def test_find_record(self):
        data_correct = [
            "2024-12-05",
            "Расход",
            "Алименты",
        ]
        data_incorrect = [
            "2024-12-05",
            "Доход",
            "Алименты",
        ]
        succses = self.fm.find_record(self.file_test_wallet, data_correct)
        fallen = self.fm.find_record(self.file_test_wallet, data_incorrect)
        self.assertAlmostEqual(succses, 4)
        self.assertAlmostEqual(fallen, -1)


if __name__ == "__main__":
    unittest.main()
