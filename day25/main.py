import pandas as pd

data = pd.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


# print(data["temp"].mean())
# print(data["temp"].max())

# get data in column
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])

# get the row of data where temp was max

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * (9 / 5) + 32
# print(monday.temp)
# print(monday_temp_F)

# Creating dataframe from scratch

data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
