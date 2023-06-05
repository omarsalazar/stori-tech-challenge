from typing import Any
import collections
import calendar


def get_total_balance(transactions_dict: list[dict[str, Any]]) -> float:
    transactions_amount = [transaction.get("transaction") for transaction in transactions_dict]
    return sum(transactions_amount)


def group_transaction_by_month(transactions_dict: list[dict[str, Any]]) -> dict[str, int]:
    amount_by_month = collections.Counter()
    for transaction in transactions_dict:
        amount_by_month[calendar.month_name[transaction.get("date").month]] += 1
    return dict(amount_by_month)


def get_credit_average_amount(transactions_dict: list[dict[str, Any]]) -> float:
    credit_transactions_amount = [transaction.get("transaction")
                                  for transaction in transactions_dict
                                  if transaction.get("transaction") > 0]
    return sum(credit_transactions_amount)


def get_debit_average_amount(transactions_dict: list[dict[str, Any]]) -> float:
    credit_transactions_amount = [transaction.get("transaction")
                                  for transaction in transactions_dict
                                  if transaction.get("transaction") < 0]
    return abs(sum(credit_transactions_amount))

