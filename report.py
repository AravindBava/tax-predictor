import textwrap
import matplotlib.pyplot as plt
from simulate import RISKS, run_simulation, summarize

# Plain-English names for the report
RISK_NAMES = {
    "appreciation": "Home value growth",
    "rent": "Rent",
    "repairs": "Repairs",
    "vacancy": "Vacancy",
    "tax": "Property tax",
}


def money(amount):
    # Formats -35374.2 as -$35,374
    if amount < 0:
        return f"-${abs(amount):,.0f}"
    return f"${amount:,.0f}"


def plot_profits(profits, path):
    plt.hist(profits, bins=50)
    plt.axvline(0, color="red")
    plt.title("Five-year profit across all simulations")
    plt.xlabel("Five-year profit ($)")
    plt.ylabel("Number of simulations")
    plt.savefig(path)
    plt.close()


def profit_with(deal, risks):
    profits, first_year = run_simulation(deal, n=1, risks=risks)
    return profits[0]


def rank_risks(deal, risks=RISKS):
    fixed = {}
    for k in risks:
        likely = risks[k][1]
        fixed[k] = (likely, likely, likely)

    swings = {}
    for name in risks:
        low, likely, high = risks[name]
        low_case = dict(fixed)
        low_case[name] = (low, low, low)
        high_case = dict(fixed)
        high_case[name] = (high, high, high)
        swings[name] = abs(profit_with(deal, high_case) - profit_with(deal, low_case))

    return sorted(swings.items(), key=lambda item: item[1], reverse=True)


def make_report(deal, path):
    # Get the numbers
    profits, first_year = run_simulation(deal)
    s = summarize(profits, first_year)
    ranked = rank_risks(deal)
    top_risk = RISK_NAMES[ranked[0][0]].lower()

    # A letter-size page
    fig = plt.figure(figsize=(8.5, 11))

    # Title and the one-sentence answer (Step 6)
    fig.text(0.08, 0.95, "Deal Risk Report", fontsize=22, weight="bold")
    answer = (f"This deal has about a {s['loss_chance']:.0%} chance of losing money "
              f"over five years, and its result depends most on {top_risk}.")
    fig.text(0.08, 0.89, textwrap.fill(answer, 75), fontsize=13)

    # Summary numbers
    fig.text(0.08, 0.83, "Five-year results from 10,000 simulations", fontsize=12, weight="bold")
    lines = [
        f"Chance of a five-year loss: {s['loss_chance']:.0%}",
        f"Median profit: {money(s['median'])}",
        f"Bad case (5th percentile): {money(s['bad_case'])}",
        f"Good case (95th percentile): {money(s['good_case'])}",
        f"Chance of negative year 1 cash flow: {s['neg_year1']:.0%}",
    ]
    y = 0.80
    for line in lines:
        fig.text(0.08, y, line, fontsize=11)
        y = y - 0.025

    # Histogram
    ax = fig.add_axes([0.10, 0.38, 0.82, 0.27])
    ax.hist(profits, bins=50)
    ax.axvline(0, color="red")
    ax.set_title("Five-year profit across all simulations")
    ax.set_xlabel("Five-year profit ($)")
    ax.set_ylabel("Number of simulations")

    # Top three risks
    fig.text(0.08, 0.30, "Biggest risks (profit swing from low to high)", fontsize=12, weight="bold")
    y = 0.27
    for name, swing in ranked[:3]:
        fig.text(0.08, y, f"{RISK_NAMES[name]}: {money(swing)}", fontsize=11)
        y = y - 0.025

    # Assumptions
    fig.text(0.08, 0.17, "Assumptions", fontsize=12, weight="bold")
    assumptions = [
        f"Price ${deal['price']:,.0f}, {deal['down_pct']:.0%} down, "
        f"{deal['rate']:.1%} loan for {deal['years']} years",
        f"Rent ${deal['monthly_rent']:,.0f}/month, property tax ${deal['annual_tax']:,.0f}/year, "
        f"insurance ${deal['insurance']:,.0f}/year",
        "Rent, tax, and insurance grow 3% a year; sold after 5 years with 6% selling costs",
    ]
    y = 0.14
    for line in assumptions:
        fig.text(0.08, y, line, fontsize=10)
        y = y - 0.022

    # Fine print (Step 7)
    fig.text(0.08, 0.04, "Estimate for educational purposes. Not an appraisal or investment advice.",
             fontsize=9, color="gray")

    fig.savefig(path)
    plt.close(fig)