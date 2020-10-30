import csv
with open('airtravel.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    next(reader)
    year_1958 = dict()
    for line in reader:
        year_1958[line[0]] = line[1]

    max_value = max(year_1958.values())
    for k,v in year_1958.items():
        if v == max_value:
            print(f"Bussiest Month: {k} and fligts: {v}")