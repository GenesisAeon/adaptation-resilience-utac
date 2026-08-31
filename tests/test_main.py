"""Tests for adaptation-resilience-utac."""

from adaptation_resilience_utac import (
    ALL_MEASURES,
    PACKAGE_ID,
    __version__,
    gca_global_bcr,
    gca_global_net_benefit_usd_trillion,
    is_cost_effective,
    nature_based_share_of_preventable_losses,
)


def test_version():
    assert __version__ == "1.0.1"


def test_package_id():
    assert PACKAGE_ID == 95


def test_all_measures_has_two_entries():
    assert len(ALL_MEASURES) == 2


def test_all_measures_are_cost_effective():
    for measure in ALL_MEASURES:
        assert is_cost_effective(measure.bcr_low)
        assert is_cost_effective(measure.bcr_high)


def test_is_cost_effective_boundary():
    assert is_cost_effective(1.0) is False
    assert is_cost_effective(1.01) is True


def test_gca_global_net_benefit_positive():
    assert gca_global_net_benefit_usd_trillion() > 0.0


def test_gca_global_bcr_matches_expected_ratio():
    bcr = gca_global_bcr()
    assert 3.5 < bcr < 4.5


def test_nature_based_share_default_midpoint():
    share = nature_based_share_of_preventable_losses()
    assert 0.5 < share < 1.0


def test_nature_based_share_with_explicit_total():
    share = nature_based_share_of_preventable_losses(total_usd_bn=100.0)
    assert share == 0.5


def test_at_least_one_measure_is_nature_based():
    assert any(m.is_nature_based for m in ALL_MEASURES)
