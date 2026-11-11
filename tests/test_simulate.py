from pytest import approx
from simulate import run_simulation
from deal import TEST_DEAL


NORMAL_VAL = {
    "rent": (0, 0, 0),
    "vacancy": (0.05, 0.05, 0.05),
    "repairs": (0.08, 0.08, 0.08),
    "tax": (1.0, 1.0, 1.0),
    "appreciation": (0.03, 0.03, 0.03)
}


def test_run_simulation():
    profits, first_year = run_simulation(TEST_DEAL, n=5, risks=NORMAL_VAL)

    assert profits == approx(30874.79, abs=0.01)
