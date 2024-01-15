import json
from datetime import datetime

import requests

MY_LAT = -25.296930
MY_LNG = 150.304062

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# print(longitude, latitude)


params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour

print(sunrise, time_now, sunset)
