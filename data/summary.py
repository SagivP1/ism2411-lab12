import csv

summary = {}

with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])

        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")
