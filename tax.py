import csv


def annual_property_tax(price, assessment_ratio=0.40, mills=26.95):
    annual_tax = price * assessment_ratio * (mills/1000)
    return annual_tax


def load_mills(county, city):
    with open("rates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["county"] == county and row["city"] == city:
                return float(row["total_mills"])
