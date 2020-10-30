import csv

devices = list()
with open("devices.txt", 'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=":")
    for line in reader:
        print(line)

with open("devices.txt", 'a', newline="") as csvfile:
    writer = csv.writer(csvfile,delimiter=":")
    writer.writerow(['A1','1.1.1.1','lab','lab'])

with open("devices.txt", 'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=":")
    for line in reader:
        print(line)