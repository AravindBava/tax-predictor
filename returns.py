import mortgage
from deal import analyze_year
import numpy_financial as npf


def five_year_flows(deal, growth=0.03, appreciation=0.03, sale_cost=0.06):
    yrs_so_far = 5
    # Cash invested
    flows = [-analyze_year(deal)["cash_in"]]

    for year in range(1, 6):
        grow = (1 + growth) ** (year - 1)
        this_year = dict(deal)
        this_year["monthly_rent"] = deal["monthly_rent"] * grow
        this_year["annual_tax"] = deal["annual_tax"] * grow
        this_year["insurance"] = deal["insurance"] * grow

        flows.append(analyze_year(this_year)["cash_flow"])

    loan = deal["price"] * (1 - deal["down_pct"])
    sale_price = deal["price"] * (1 + appreciation) ** yrs_so_far
    money_from_sale = sale_price * (1 - sale_cost) - mortgage.remaining_balance(loan, deal["rate"], deal["years"], yrs_so_far * 12)
    flows[5] = flows[5] + money_from_sale

    return flows


def total_profit(flows):
    profit = sum(flows)
    return profit


def irr(flows):
    irr_pct = npf.irr(flows)
    return irr_pct
