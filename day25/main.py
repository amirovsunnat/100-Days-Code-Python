# import csv
#
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for info in data:
#         if info[1] != "temp":
#             temperatures.append(int(info[1]))
#
#     print(temperatures)

import pandas


# data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# print(data["temp"])

data_2018 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cin_squ_number = len(data_2018[data_2018["Primary Fur Color"] == "Cinnamon"])
grey_suq_number = len(data_2018[data_2018["Primary Fur Color"] == "Gray"])
black_suq_number = len(data_2018[data_2018["Primary Fur Color"] == "Black"])

data_in_dict = {
    "Primary Fur Color": ["Cinnamon", "Gray", "Black"],
    "Numbers": [cin_squ_number, grey_suq_number, black_suq_number]
}

data_frame = pandas.DataFrame(data_in_dict)
data_frame.to_csv("squirrel colors")

