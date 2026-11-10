from pytest import approx
from deal import analyze_year, TEST_DEAL


def test_full_year_rent():
    assert analyze_year(TEST_DEAL)["gross"] == approx(28800)


def test_collected_rent():
    assert analyze_year(TEST_DEAL)["collected"] == approx(27360)


def test_operating_costs():
    assert analyze_year(TEST_DEAL)["operating_costs"] == approx(9526.80, abs=0.01)


def test_noi():
    assert analyze_year(TEST_DEAL)["noi"] == approx(17833.20, abs=0.01)


def test_debt():
    assert analyze_year(TEST_DEAL)["debt"] == approx(19160.71, abs=0.01)


def test_cash_flow():
    assert analyze_year(TEST_DEAL)["cash_flow"] == approx(-1327.51, abs=0.01)


def test_dscr():
    assert analyze_year(TEST_DEAL)["dscr"] == approx(0.93, abs=0.005)


def test_cap_rate():
    assert analyze_year(TEST_DEAL)["cap_rate"] == approx(.0594, abs=0.00005)


def test_cash_in():
    assert analyze_year(TEST_DEAL)["cash_in"] == approx(69000, abs=0.01)


def test_coc():
    assert analyze_year(TEST_DEAL)["coc"] == approx(-.0192, abs=0.0001)

