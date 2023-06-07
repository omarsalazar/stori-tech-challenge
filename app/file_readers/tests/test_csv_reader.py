import os
import csv
import unittest
import datetime
from datetime import date
from dotenv import load_dotenv
from app.file_readers.csv_reader import CSVReader

load_dotenv()

test_file = 'test.csv'
wrong_file = "nonexistent.csv"
row_names = os.environ.get("ROW_NAMES").split(",")

rows = [
    ["Id", "Date", "Transaction"],
    ["0", "7/15", "+60.5"],
    ["1", "12/1", "-8000"]
]

wrong_rows = [
    ["Id", "bar", "foo"],
    ["0p0", "adfasdf", "asdf"],
    ["1", "asdfadf", ""]
]


class TestCsvReader(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CSVReader()
        self.fail_csv_reader = CSVReader()
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(rows)

    def tearDown(self):
        os.remove(test_file)

    def test_get_info_from_file(self):
        result = self.csv_reader.get_info_from_file(file_path=test_file, row_names=row_names)
        expected_result = rows[1:]
        assert result is not None
        assert result == expected_result

    def test_get_info_from_file_dont_exists(self):
        with self.assertRaises(FileExistsError):
            self.csv_reader.get_info_from_file(file_path=wrong_file, row_names=["Id, bar, foo"])

    def test_get_transactions_data_from_csv_file_wrong_rows(self):
        with open(wrong_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(wrong_rows)

        with self.assertRaises(ValueError):
            self.csv_reader.get_info_from_file(file_path=wrong_file, row_names=["Id, bar, foo"])

        os.remove(wrong_file)

    def test_parse_csv_transactions_data(self):
        transaction_from_test_rows = rows[1:]
        expected_result = [{
            "id": int(row[0]),
            "date": date(
                day=int(row[1].split("/")[1]), month=int(row[1].split("/")[0]), year=datetime.date.today().year
            ),
            "transaction": float(row[2].replace("+", ""))
        } for row in transaction_from_test_rows]
        result = self.csv_reader.format_csv_data(transaction_from_test_rows)
        assert result == expected_result


if __name__ == "__main__":
    unittest.main()
