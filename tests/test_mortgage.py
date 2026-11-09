from pytest import approx
from mortgage import monthly_payment
from mortgage import remaining_balance


def test_monthly_payment():
    assert monthly_payment(240000, 0.07, 30) == approx(1596.73, abs=0.01)


def test_remaining_balance():
    assert remaining_balance(240000, 0.07, 30, 60) == approx(225915.82, abs=0.01)