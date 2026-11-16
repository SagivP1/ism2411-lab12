import csv

total_revenue = 0

with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity
        total_revenue += line_total

        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")
