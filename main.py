from dotenv import load_dotenv
import os

from emails.email_sender import EmailSender
from file_readers.csv_reader import CSVReader

from transactions.data_processor import TransactionDataProcessor

if __name__ == '__main__':
    load_dotenv()
    transactions_csv = os.environ.get("CVS_FILE")
    row_names = os.environ.get("ROW_NAMES").split(",")
    send_to = os.environ.get("SEND_TO")
    subject = os.environ.get("SUBJECT")

    csv_reader = CSVReader(file_path=transactions_csv, row_names=row_names)
    csv_data = csv_reader.get_csv_transactions_data()

    transaction_data = TransactionDataProcessor().get_transactions_data(csv_data)

    email_sender = EmailSender(send_to, subject, transaction_data)
    email_sender.execute()
