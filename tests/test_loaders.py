from pytest import approx
from loaders import load_deals, load_comps


def test_polar_rock_tax():
    deals = load_deals("deals.csv")
    assert deals[0]["annual_tax"] == approx(3093.88, abs=0.01)


def test_polar_rock_comps():
    assert len(load_comps("comps.csv", "166 Polar Rock Rd SW")) == 4
