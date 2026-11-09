from pytest import approx
from tax import annual_property_tax
from tax import load_mills


def test_fulton_example():
    assert annual_property_tax(300000) == approx(3234)


def test_fulton_example2():
    assert annual_property_tax(500000) == approx(5390)


def test_load_mills():
    assert load_mills("Fulton", "Atlanta") == approx(40.709)
