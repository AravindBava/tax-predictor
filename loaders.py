import csv
from tax import annual_property_tax, load_mills

# Columns in deals.csv that hold numbers
NUMBER_COLUMNS = {"price", "monthly_rent", "insurance", "rate", "down_pct",
                  "closing_pct", "vacancy", "repairs_pct", "mgmt_pct"}


def load_deals(path):
    deals = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for col in NUMBER_COLUMNS:
                row[col] = float(row[col])
            row["years"] = int(row["years"])
            mills = load_mills(row["county"], row["city"])
            row["annual_tax"] = annual_property_tax(row["price"], mills=mills)
            deals.append(row)
    return deals


def load_comps(path, address):
    comps = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["property"] == address:
                row["rent"] = float(row["rent"])
                comps.append(row)
    return comps