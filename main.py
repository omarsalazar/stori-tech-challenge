from dotenv import load_dotenv
import os
from app.emails.email_sender import EmailSender
from app.file_readers.csv_reader import CSVReader
from app.transactions.data_processor import TransactionDataProcessor
from app.transactions.querier import TransactionQuerier, BalanceQuerier, MonthlyCountQuerier

load_dotenv()
db_name = os.environ.get("DB_NAME")
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_port = int(os.environ.get("DB_PORT"))
transactions_csv = os.environ.get("CVS_FILE")
row_names = os.environ.get("ROW_NAMES").split(",")
send_to = os.environ.get("SEND_TO")
subject = os.environ.get("SUBJECT")

if __name__ == '__main__':
    csv_reader = CSVReader()
    csv_data = csv_reader.get_csv_transactions_data(file_path=transactions_csv, row_names=row_names)
    transaction_data = TransactionDataProcessor().get_transactions_data(csv_data)

    transaction_querier = TransactionQuerier()
    transaction_querier.insert_into_table(csv_data)

    balance_querier = BalanceQuerier()
    balance_querier.insert_into_table(transaction_data)

    monthly_count_querier = MonthlyCountQuerier()
    monthly_count_querier.insert_into_table(transaction_data)

    email_sender = EmailSender(send_to, subject, transaction_data)
    email_sender.execute()
