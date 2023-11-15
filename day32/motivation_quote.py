import datetime as dt
import random
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""


weekday = dt.datetime.now().weekday()
if weekday == 2:
    with open(file="day32/quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Weekly Quote\n\n{random_quote}",
        )
