import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrels_count, black_squirrels_count, red_squirrels_count)

data_dict = {
  "Fur Color": ["Gray", "Red", "Black"],
  "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dataFrame = pandas.DataFrame(data_dict)
dataFrame.to_csv("SquirrelCount.csv")
