import os
import csv
import unittest
import datetime
from datetime import date


from transactions import transactions_reader

test_file = 'test.csv'
rows = [
    ["Id", "Date", "Transaction"],
    ["0", "7/15", "+60.5"],
    ["1", "12/1", "-8000"]
]


class TestCsv(unittest.TestCase):

    def setUp(self):
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(rows)

    def tearDown(self):
        os.remove(test_file)

    def test_get_transactions_data_from_csv(self):
        transactions_data = transactions_reader.get_transactions_data_from_csv(test_file)
        transaction_from_test_rows = rows[1:]
        assert transactions_data is not None
        assert transactions_data == transaction_from_test_rows

    def test_parse_csv_transactions_data(self):
        transaction_from_test_rows = rows[1:]
        expected_result = [{
            "id": int(row[0]),
            "date": date(
                day=int(row[1].split("/")[1]), month=int(row[1].split("/")[0]), year=datetime.date.today().year
            ),
            "transaction": float(row[2].replace("+", ""))
        } for row in transaction_from_test_rows]
        result = transactions_reader.get_transactions_data(transaction_from_test_rows)
        assert result == expected_result


if __name__ == "__main__":
    unittest.main()
