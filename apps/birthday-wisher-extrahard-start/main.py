##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd

data = pd.read_csv("birthdays.csv")
print(data)
data.loc[len(data.index)] = ["e", "e@", "1", "2", "3"]
print(data)
data.loc[len(data.index)] = ["d", "d@", "1", "2", "3"]
print(data)
data.to_csv("birthdays.csv", index=False)
# print(data.to_dict(orient="dict"))
# print(data.to_dict(orient="list"))
# print(data.to_dict(orient="series"))
# print(data.to_dict(orient="split"))
# print(data.to_dict(orient="split", index=False))
# print(data.to_dict(orient="tight"))
# print(data.to_dict(orient="tight", index=False))
# print(data.to_dict(orient="records"))
# print(data.to_dict(orient="index"))

data_dict = data.to_dict(orient="list")
# print(data_dict["email"][data_dict["name"].index("a")])
# print(data.loc[data["name"] == "a", "email"].values[0])

