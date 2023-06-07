import unittest
import datetime
import collections
import calendar
from datetime import date

from app.transactions.data_processor import TransactionDataProcessor


rows = [
    ["Id", "Date", "Transaction"],
    ["0", "7/15", "+60.5"],
    ["1", "12/1", "-8000"]
]

transactions_dict = [
    {'id': 0, 'date': datetime.date(2023, 7, 15), 'transaction': 60.5},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': 100.0},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': -80.0},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': -8.0},
    {'id': 1, 'date': datetime.date(2023, 7, 1), 'transaction': -15.0}
]


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.data_processor = TransactionDataProcessor()

    def test_format_csv_data(self):
        transaction_from_test_rows = rows[1:]
        expected_result = [{
            "id": int(row[0]),
            "date": date(
                day=int(row[1].split("/")[1]), month=int(row[1].split("/")[0]), year=datetime.date.today().year
            ),
            "transaction": float(row[2].replace("+", ""))
        } for row in transaction_from_test_rows]
        result = self.data_processor.format_csv_data(transaction_from_test_rows)
        assert result == expected_result

    def test_get_total_balance(self):
        expected_result = sum([transaction.get("transaction") for transaction in transactions_dict])
        result = self.data_processor.get_total_balance(transactions_dict)
        assert result == expected_result

    def test_group_transaction_by_month(self):
        amount_by_month = collections.Counter()
        for transaction in transactions_dict:
            amount_by_month[calendar.month_name[transaction.get("date").month]] += 1
        expected_result = dict(amount_by_month)
        result = self.data_processor.group_transactions_by_month(transactions_dict)
        assert result == expected_result

    def test_get_credit_average_amount(self):
        credit_transactions = [transaction.get("transaction")
                               for transaction in transactions_dict
                               if transaction.get("transaction") > 0]
        total = sum(credit_transactions) / len(credit_transactions)
        expected_result = float("{:.2f}".format(total))
        result = self.data_processor.get_credit_average(transactions_dict)
        assert result == expected_result

    def test_get_debit_average_amount(self):
        debit_transactions = [transaction.get("transaction")
                              for transaction in transactions_dict
                              if transaction.get("transaction") < 0]
        total = sum(debit_transactions) / len(debit_transactions)
        expected_result = float("{:.2f}".format(total))
        result = self.data_processor.get_debit_average(transactions_dict)
        assert result == expected_result


if __name__ == "__main__":
    unittest.main()
