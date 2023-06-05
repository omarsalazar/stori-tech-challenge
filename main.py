from dotenv import load_dotenv
import os
from transactions import transactions_reader
from transactions import transactions_data_processor
from emails import email_sender


if __name__ == '__main__':
    load_dotenv()
    transactions_csv = os.environ.get("CVS_FILE")
    send_to = os.environ.get("SEND_TO")

    csv_data = transactions_reader.get_transactions_data_from_csv(transactions_csv)
    transactions_data = transactions_reader.get_transactions_data(csv_data)
    total = transactions_data_processor.get_total_balance(transactions_data)
    date_sorted = transactions_data_processor.group_transaction_by_month(transactions_data)
    debit = transactions_data_processor.get_debit_average_amount(transactions_data)
    credit = transactions_data_processor.get_credit_average_amount(transactions_data)

    message = email_sender.generate_email_message(credit, debit, total, date_sorted)
    email_sender.send_email(send_to, "Your Balance is Here!", message)

