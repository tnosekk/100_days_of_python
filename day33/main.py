import json
import smtplib
import time
from datetime import datetime

import requests

MY_EMAIL = "my_mail@mail.com"
MY_PASS = "abcd1234"


MY_LAT = -25.296930
MY_LNG = 150.304062


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
    ):
        return True


def is_night():
    params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            mss="Subject:Look up\n\nThe ISS is above you in the sky.",
        )
