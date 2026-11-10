from pytest import approx
from deal import TEST_DEAL
from returns import five_year_flows, total_profit, irr


def test_five_year_flows():
    assert five_year_flows(TEST_DEAL) == approx([-69000.0, -1327.51, -792.52, -241.47, 326.11, 101910.19], abs=0.01)


def test_total_profit():
    assert total_profit(five_year_flows(TEST_DEAL)) == approx(30874.79)

def test_irr_pct():
    assert irr(five_year_flows(TEST_DEAL)) == approx(0.0754, abs=0.0001)