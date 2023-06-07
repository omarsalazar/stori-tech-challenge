import unittest
import os

from dotenv import load_dotenv
from app.emails.email_sender import EmailSender

load_dotenv()
send_to = os.environ.get("SEND_TO")
subject = os.environ.get("SUBJECT")
balance_data = {'total_balance': 57.5, 'transactions_by_month': {'July': 2, 'December': 3}, 'debit_average': -34.33, 'credit_average': 80.25}


class TestEmailSender(unittest.TestCase):

    def setUp(self):
        self.email_sender = EmailSender(send_to=send_to, subject=subject, balance_data=balance_data)

    def test_generate_email_message(self):
        expected_result = f"""\
                <html>
                <body>
                  <p>Hi,<br>
                    Here's your account balance!<br>
                    </p>
                    <table>
                      <tr>
                        <td>Total balance is: 57.5</td>
                        <td>Average debit amount: -34.33</td>
                      </tr>
                      <tr>
                        <td></td>
                        <td>Average credit amount: 80.25</td>
                      </tr>
                      <tr>
                      </tr>
                      <tr><td>Number of transactions in July: 2</td></tr>
<tr><td>Number of transactions in December: 3</td></tr>
                    </table>
                </body>
                </html>
                """
        result = self.email_sender.generate_email_message()
        assert expected_result == result
