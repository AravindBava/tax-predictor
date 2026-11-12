from loaders import load_deals, load_comps
from report import make_report

for deal in load_deals("deals.csv"):
    comps = load_comps("comps.csv", deal["address"])
    path = "reports/" + deal["address"].replace(" ", "_") + ".pdf"
    make_report(deal, comps, path)
    print("Saved", path, "with", len(comps), "comps")