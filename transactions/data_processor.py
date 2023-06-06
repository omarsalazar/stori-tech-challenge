from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Any
import collections
import calendar
import datetime
from datetime import date

load_dotenv()


@dataclass
class TransactionDataProcessor:
    @staticmethod
    def format_csv_data(transaction_from_csv: list[list[str]]) -> list[dict[str, Any]]:
        parsed_transactions_data = [
            {
                "id": int(row[0]),
                "date": date(
                    day=int(row[1].split("/")[1]), month=int(row[1].split("/")[0]), year=datetime.date.today().year
                ),
                "transaction": float(row[2].replace("+", ""))
            }
            for row in transaction_from_csv]
        return parsed_transactions_data

    @staticmethod
    def get_total_balance(transactions_dict: list[dict[str, Any]]) -> float:
        total_balance = [transaction.get("transaction") for transaction in transactions_dict]
        return sum(total_balance)

    @staticmethod
    def group_transactions_by_month(transactions_dict: list[dict[str, Any]]) -> dict[Any, int]:
        amount_by_month = collections.Counter()
        for transaction in transactions_dict:
            amount_by_month[calendar.month_name[transaction.get("date").month]] += 1
        return dict(amount_by_month)

    @staticmethod
    def get_credit_average(transactions_dict: list[dict[str, Any]]) -> float:
        credit_transactions = [transaction.get("transaction")
                               for transaction in transactions_dict
                               if transaction.get("transaction") > 0]
        return sum(credit_transactions)

    @staticmethod
    def get_debit_average(transactions_dict: list[dict[str, Any]]) -> float:
        debit_transactions = [transaction.get("transaction")
                              for transaction in transactions_dict
                              if transaction.get("transaction") < 0]
        return abs(sum(debit_transactions))

    def get_transactions_data(self, csv_data) -> dict:
        return {
            "total_balance": self.get_total_balance(csv_data),
            "transactions_by_month": self.group_transactions_by_month(csv_data),
            "debit_average": self.get_debit_average(csv_data),
            "credit_average": self.get_credit_average(csv_data)
        }
