import csv
import json

# with open('data.csv') as f:
#     data = csv.reader(f)
#     print(data)
#     for i in data:
#         print(i)

upload = [["560", "epsiten", "island"], ["666", "diddy", "Baitadi"]]

with open('data.csv', "a", newline="") as f:
    data = csv.writer(f)
    data.writerows(upload)

with open('data.json') as f:
    data = json.load(f)
    print(type(data))

data = {"name": "Sudan(HM)", "age": "31"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)