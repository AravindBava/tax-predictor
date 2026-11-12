from pytest import approx
from report import rank_risks
from deal import TEST_DEAL
from simulate import RISKS


def test_rank_risks():
    ranks = rank_risks(TEST_DEAL, risks=RISKS)
    names = [name for name, swing in ranks]
    assert names == ["appreciation", "rent", "repairs", "vacancy", "tax"]