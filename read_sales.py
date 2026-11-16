print("---Exercise 2---")

import csv

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")

import csv

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

print("---Exercise 4---")

import csv

total_revenue = 0

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        line_total = price * quantity
        total_revenue += line_total

        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("---Exercise 5---")

import csv

original_count = 0
written_count = 0

with open("data/sales.csv", newline="") as infile, \
     open("data/cleaned.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)  # skip the original header
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        original_count += 1

        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            written_count += 1

print(f"Original rows: {original_count}")
print(f"Rows written to cleaned.csv: {written_count}")

print("---Exercise 6---")

