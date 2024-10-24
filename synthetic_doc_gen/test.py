# Python program to read
# json file

import json

# Opening JSON file
f = open('configuration.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# for i in data["check"]:
# 	print(i["generator"])


# position_xy = (int(data["check"]["payee"]["x"]),int(data["check"]["payee"]["y"]))
# print(type(position_xy))

# position = (30,40)
# print(type(position))

for i in data:
    for j in data[i]:
        for object in j:
            print(f"Key = {object}")
            print(f"Value = {j[object]}")

# Closing file
f.close()
