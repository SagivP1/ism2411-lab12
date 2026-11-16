import csv

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
