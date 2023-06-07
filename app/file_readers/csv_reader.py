import csv
import datetime
from typing import Any
from datetime import date
from os.path import exists
from dotenv import load_dotenv

load_dotenv()


class CSVReader:

    @staticmethod
    def get_info_from_file(file_path: str, row_names: list[str]) -> list[list[str]]:
        if exists(file_path):
            with open(file_path) as transactions_file:
                csv_reader = csv.reader(transactions_file, delimiter=',')
                csv_data = list(csv_reader)
                if csv_data[0] == row_names:
                    transactions_data = csv_data[1:]
                else:
                    row_names_to_str = ", ".join(row_names)
                    raise ValueError(f"Please provide a csv file with the correct row names ({row_names_to_str})")
            return transactions_data
        else:
            raise FileExistsError(f"{file_path} does not exists")

    @staticmethod
    def format_csv_data(transactions_from_csv: list[list[str]]) -> list[dict[str, Any]]:
        parsed_transactions_data = [
            {
                "id": int(row[0]),
                "date": date(
                    day=int(row[1].split("/")[1]), month=int(row[1].split("/")[0]), year=datetime.date.today().year
                ),
                "transaction": float(row[2].replace("+", ""))
            }
            for row in transactions_from_csv]
        return parsed_transactions_data

    def get_csv_transactions_data(self, file_path: str, row_names: list[str]) -> list[dict[str, Any]]:
        info_from_file = self.get_info_from_file(file_path=file_path, row_names=row_names)
        return self.format_csv_data(transactions_from_csv=info_from_file)
