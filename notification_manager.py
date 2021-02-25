import smtplib
import datetime as dt

MY_EMAIL = "MY_EMAIL"
PASSWORD = "MY_PASSWORD"

today_raw = dt.datetime.now()
today_formatted = today_raw.strftime("%Y-%m-%d")

class NotificationManager:

    def __init__(self):
        self.client = smtplib.SMTP("smtp.gmail.com", port=587)

    def send_email(self, emails, message):
        # stock_name, stock_data
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Stock price!\n\n{message}".encode('utf-8')
                )
        print(message)
