import csv

status_data = []
with open("data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    for row in data:
        status_data.append(row[1])
    status_data.pop(0)
    # print(status_data)


import pandas as pd

data = pd.read_csv("data.csv")
# data2018 = pd.to_numeric(data["2018"])
# print(data["2018"].to_list())
print(data["2018"].mean())
print(data["2018"].max())
print(data[data["Nationality"] == "Indonesia"])
print(data[data["2018"] == data["2018"].max()])

# over1000_2017 = data[pd.to_numeric(data["2017"], errors="coerce") >= 1000]
# print(over1000_2017)
# print(len(over1000_2017))
# print(over1000_2017.size)

year = []
over1000 = []
for _year in range(2017, 2020, 1):
    year.append(_year)
    over1000.append(len(data[pd.to_numeric(data[str(_year)], errors="coerce") >= 1000]))
    print(_year)
print(over1000)

data_dict = {
    "year": year,
    "count": over1000
}
_data = pd.DataFrame(data_dict)
_data.to_csv("resume.csv")