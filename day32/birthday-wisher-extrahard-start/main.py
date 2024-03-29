import datetime as dt
import random
import smtplib

import pandas

MAIL = ""
PASSWORD = ""


today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("day32/birthday-wisher-extrahard-start/birthdays.csv")


birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    file_path = f"day32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read().replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL, PASSWORD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
