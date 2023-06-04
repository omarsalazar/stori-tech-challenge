import csv
import datetime
from typing import Any
from datetime import date
from os.path import exists

row_names = ["Id", "Date", "Transaction"]


def get_transactions_data_from_csv(transaction_file: str) -> list[list[str]]:
    if exists(transaction_file):
        with open(transaction_file) as transactions_file:
            csv_reader = csv.reader(transactions_file, delimiter=',')
            csv_data = list(csv_reader)
            if csv_data[0] == row_names:
                transactions_data = csv_data[1:]
            else:
                row_names_to_str = ", ".join(row_names)
                raise ValueError(f"Please provide a csv file with the correct row names ({row_names_to_str})")
        return transactions_data
    else:
        raise FileExistsError(f"{transaction_file} does not exists")


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
