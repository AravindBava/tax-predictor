def annual_property_tax(price, assessment_ratio=0.40, mills=26.95):
    annual_tax = price * assessment_ratio * (mills/1000)
    return annual_tax
