import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = json.dumps(data)
print(json)
with open("data.json", "w") as fWrite:
    fWrite.write(json)
