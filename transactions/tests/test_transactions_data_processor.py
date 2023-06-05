import unittest
import datetime
import collections
import calendar

from transactions import transactions_data_processor

transactions_dict = [
    {'id': 0, 'date': datetime.date(2023, 7, 15), 'transaction': 60.5},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': 100.0},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': -80.0},
    {'id': 1, 'date': datetime.date(2023, 12, 1), 'transaction': -8.0},
    {'id': 1, 'date': datetime.date(2023, 7, 1), 'transaction': -15.0}
]


class TestDataProcessor(unittest.TestCase):
    def test_get_transactions_data_from_csv(self):
        expected_result = sum([transaction.get("transaction") for transaction in transactions_dict])
        result = transactions_data_processor.get_total_balance(transactions_dict)
        assert result == expected_result

    def test_group_transaction_by_month(self):
        amount_by_month = collections.Counter()
        for transaction in transactions_dict:
            amount_by_month[calendar.month_name[transaction.get("date").month]] += transaction.get("transaction")
        expected_result = dict(amount_by_month)
        result = transactions_data_processor.group_transaction_by_month(transactions_dict)
        assert result == expected_result

    def test_get_credit_average_amount(self):
        expected_result = sum(
            transaction.get("transaction") for transaction in transactions_dict if transaction.get("transaction") > 0)
        result = transactions_data_processor.get_credit_average_amount(transactions_dict)
        assert result == expected_result

    def test_get_debit_average_amount(self):
        expected_result = abs(sum(
            transaction.get("transaction") for transaction in transactions_dict if transaction.get("transaction") < 0))
        result = transactions_data_processor.get_debit_average_amount(transactions_dict)
        assert result == expected_result


if __name__ == "__main__":
    unittest.main()
