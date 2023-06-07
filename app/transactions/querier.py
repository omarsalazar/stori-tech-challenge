from datetime import datetime

from app.databases.postgresql_connection import PostgresConnector


class TransactionQuerier(PostgresConnector):
    def __init__(self):
        super().__init__()

    def insert_into_table(self, data):
        for transaction_cvs_data in data:
            try:
                query = f"INSERT INTO public.transactions (\"id\", \"transaction\", \"transaction_date\") VALUES({transaction_cvs_data.get('id')}, {transaction_cvs_data.get('transaction')}, \'{transaction_cvs_data.get('date')}\');"
                self.cursor.execute(query)
                self.connection.commit()
                count = self.cursor.rowcount
                print(count, "Record inserted successfully into transactions table")
            except Exception as e:
                print(e)

        self.close_db_connection()


class BalanceQuerier(PostgresConnector):
    def __init__(self):
        super().__init__()

    def insert_into_table(self, data):
        try:
            query = f"INSERT INTO public.balance (\"total\", \"debit_average\", \"credit_average\") VALUES({data.get('total_balance')}, {data.get('debit_average')}, {data.get('credit_average')});"
            self.cursor.execute(query)
            self.connection.commit()
            count = self.cursor.rowcount
            print(count, "Record inserted successfully into balance table")
        except Exception as e:
            print(e)
        finally:
            self.close_db_connection()


class MonthlyCountQuerier(PostgresConnector):
    def __init__(self):
        super().__init__()

    def insert_into_table(self, data):
        transactions_by_month = data.get("transactions_by_month")
        months = list(transactions_by_month.keys())
        try:
            for month_name in months:
                monthly_count = transactions_by_month.get(month_name)
                query = f"INSERT INTO public.monthly_count (\"month\", \"year\", \"transaction_count\") VALUES(\'{month_name}\', {datetime.today().year}, {monthly_count});"
                self.cursor.execute(query)
                self.connection.commit()
                count = self.cursor.rowcount
                print(count, "Record inserted successfully into monthly_count table")
        except Exception as e:
            print(e)

        self.close_db_connection()

