import csv
import json

with open('devices.txt', 'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=':')
    my_dict = dict()
    for line in reader:
        my_dict[line[0]] = line[1:]

# serialization: converting from python object to json object
with open("devices.json", 'w') as f:
    obj = json.dump(my_dict,f,indent=4)

# deserialization: converting from json to python object

with open("devices.json", 'r') as f:
    obj = json.load(f)
    print(type(obj))
print(obj)

for k,v in obj.items():
    print(f"key:{k} and value: {v}")



