"""
1. ex
"""

# sentence = input()
# result = {word: len(word) for word in sentence.split(" ")}
# print(result)

"""
2. ex convert temp from c to f
"""
from pprint import pprint

week_temp = {
    "Monday": 23.4,
    "Tuesday": 18.9,
    "Wednesday": 15.7,
    "Thursday": 27.1,
    "Friday": 21.3,
    "Saturday": 12.5,
    "Sunday": 28.8,
}
weather_f = {day: round(temp * 5 / 9 + 32, 1) for (day, temp) in week_temp.items()}
pprint(weather_f)
