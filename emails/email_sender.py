import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


def generate_email_message(debit_average: float, credit_average: float, total_balance: float,
                           transactions_by_month: dict[str, int]) -> str:

    months = list(transactions_by_month.keys())
    transactions_by_month_list = []
    for month in months:
        transactions_by_month_list.append(f"<tr><td>Number of transactions in {month}: {transactions_by_month.get(month)}</td></tr>")

    transactions_by_month_text = "\n".join(transactions_by_month_list)

    html = f"""\
            <html>
            <body>
              <p>Hi,<br>
                Here's your account balance!<br>
                </p>
                <table>
                  <tr>
                    <td>Total balance is: {total_balance}</td>
                    <td>Average debit amount: {debit_average}</td>
                  </tr>
                  <tr>
                    <td></td>
                    <td>Average credit amount: {credit_average}</td>
                  </tr>
                  <tr>
                  </tr>
                  {transactions_by_month_text}
                </table>
            </body>
            </html>
            """

    return html


def send_email(to: str, subject: str, text: str) -> None:
    try:
        email_address = os.environ.get("EMAIL_ADDRESS")
        email_password = os.environ.get("EMAIL_PASSWORD")

        if email_address is None or email_password is None:
            raise ValueError("Password or email missing")

        # create email
        html_message = MIMEText(text, "html")
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = email_address
        message["To"] = to
        message.attach(html_message)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.sendmail(email_address, to, message.as_string())
    except Exception as e:
        raise e
