from pytest import approx
from tax import annual_property_tax

def test_fulton_example():
    assert annual_property_tax(300000) == approx(3234)

def test_fulton_exapmle2():
    assert annual_property_tax(500000) == approx(5390)

