import csv
import datetime
from typing import Any
from datetime import date


def get_transactions_data_from_csv(transaction_file: str) -> list[list[str]]:
    with open(transaction_file) as transactions_file:
        csv_reader = csv.reader(transactions_file, delimiter=',')
        transactions_data = list(csv_reader)[1:]
    return transactions_data


def get_transactions_data(transaction_from_csv: list[list[str]]) -> list[dict[str, Any]]:
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
