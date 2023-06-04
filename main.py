from transactions import transactions_reader
from transactions import transactions_data_processor


if __name__ == '__main__':
    # TODO: use env variables
    transactions_csv = "transactions.csv"
    csv_data = transactions_reader.get_transactions_data_from_csv(transactions_csv)
    transactions_data = transactions_reader.get_transactions_data(csv_data)
    total = transactions_data_processor.get_total_balance(transactions_data)
    date_sorted = transactions_data_processor.group_transaction_by_month(transactions_data)
    debit = transactions_data_processor.get_debit_average_amount(transactions_data)
    credit = transactions_data_processor.get_credit_average_amount(transactions_data)
    print(date_sorted)
    print(total)
    print(credit)
    print(debit)
    print(transactions_data)
