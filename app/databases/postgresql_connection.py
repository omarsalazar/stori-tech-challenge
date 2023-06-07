import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class PostgresConnector:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.db_name: str = os.environ.get("DB_NAME")
        self.db_host: str = os.environ.get("DB_HOST")
        self.db_user: str = os.environ.get("DB_USER")
        self.db_pass: str = os.environ.get("DB_PASS")
        self.db_port: int = int(os.environ.get("DB_PORT"))
        self.set_up_db_connection()

    def set_up_db_connection(self) -> None:
        try:
            connection = psycopg2.connect(host=self.db_host,
                                          database=self.db_name,
                                          user=self.db_user,
                                          password=self.db_pass)
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as e:
            print(e)

    def close_db_connection(self) -> None:
        self.cursor.close()
        self.connection.close()
        print("PostgreSQL connection is closed")

    def insert_into_table(self, **params) -> None:
        pass
