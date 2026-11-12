from mortgage import monthly_payment

TEST_DEAL = {
    "address": "Practice deal",
    "price": 300000,
    "down_pct": 0.20,
    "closing_pct": 0.03,
    "rate": 0.07,
    "years": 30,
    "monthly_rent": 2400,
    "vacancy": 0.05,
    "repairs_pct": 0.08,
    "mgmt_pct": 0.08,
    "insurance": 1800,
    "annual_tax": 3234,
}


def analyze_year(deal):
    # Rent if the home is full all year
    gross = deal["monthly_rent"] * 12

    # Rent you actually collect after empty months
    collected = gross * (1 - deal["vacancy"])

    # Yearly costs of owning the home (not the loan)
    repairs = gross * deal["repairs_pct"]
    management = collected * deal["mgmt_pct"]
    operating_costs = deal["annual_tax"] + deal["insurance"] + repairs + management

    # Net operating income: what the property earns before the loan
    noi = collected - operating_costs

    # Yearly loan payments
    loan = deal["price"] * (1 - deal["down_pct"])
    debt = monthly_payment(loan, deal["rate"], deal["years"]) * 12

    # What is left for you after the loan
    cash_flow = noi - debt

    # Cash you put in on day one
    cash_in = deal["price"] * (deal["down_pct"] + deal["closing_pct"])

    return {
        "gross": gross,
        "collected": collected,
        "operating_costs": operating_costs,
        "noi": noi,
        "debt": debt,
        "cash_flow": cash_flow,
        "dscr": noi / debt,
        "cap_rate": noi / deal["price"],
        "cash_in": cash_in,
        "coc": cash_flow / cash_in,
    }
