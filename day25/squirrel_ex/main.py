import pandas as pd

squirrel_data = pd.read_csv(
    "day25/squirrel_ex/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels, black_squirrels, red_squirrels],
}

data_to_export = pd.DataFrame(data_dict)
data_to_export.to_csv("day25/squirrel_ex/color_count.csv")
