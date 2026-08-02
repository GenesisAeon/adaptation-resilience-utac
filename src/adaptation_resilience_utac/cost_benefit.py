"""Adaptation cost-benefit modeling helpers."""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    GCA_2019_BCR_HIGH,
    GCA_2019_BCR_LOW,
    GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION,
    GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION,
    REGUERO_2018_NATURE_BASED_AVERTED_USD_BN,
    REGUERO_2018_NATURE_BASED_AVG_BCR,
    REGUERO_2018_PREVENTABLE_LOSSES_HIGH_USD_BN,
    REGUERO_2018_PREVENTABLE_LOSSES_LOW_USD_BN,
)


@dataclass(frozen=True)
class AdaptationMeasure:
    """A modeled adaptation measure with a benefit-to-cost ratio estimate."""

    label: str
    bcr_low: float
    bcr_high: float
    citation: str
    is_nature_based: bool


ALL_MEASURES: tuple[AdaptationMeasure, ...] = (
    AdaptationMeasure(
        label="global portfolio (5 priority areas, 2020-2030)",
        bcr_low=GCA_2019_BCR_LOW,
        bcr_high=GCA_2019_BCR_HIGH,
        citation="Global Commission on Adaptation 2019",
        is_nature_based=False,
    ),
    AdaptationMeasure(
        label="Gulf Coast nature-based (wetlands, oyster reefs)",
        bcr_low=REGUERO_2018_NATURE_BASED_AVG_BCR,
        bcr_high=REGUERO_2018_NATURE_BASED_AVG_BCR,
        citation="Reguero et al. 2018",
        is_nature_based=True,
    ),
)


def is_cost_effective(bcr: float) -> bool:
    """A benefit-to-cost ratio above 1.0 means the measure is cost-effective."""
    return bcr > 1.0


def gca_global_net_benefit_usd_trillion() -> float:
    """Net benefit ($7.1T) minus investment ($1.8T) per the GCA (2019) global scenario."""
    return GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION - GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION


def gca_global_bcr() -> float:
    """Overall benefit-to-cost ratio of the GCA (2019) global adaptation scenario."""
    return GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION / GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION


def nature_based_share_of_preventable_losses(total_usd_bn: float | None = None) -> float:
    """Fraction of preventable Gulf Coast losses attributable to nature-based options.

    Defaults to the midpoint of Reguero et al. (2018)'s $57-101bn preventable-loss
    range if no value is supplied.
    """
    if total_usd_bn is None:
        low = REGUERO_2018_PREVENTABLE_LOSSES_LOW_USD_BN
        high = REGUERO_2018_PREVENTABLE_LOSSES_HIGH_USD_BN
        total_usd_bn = (low + high) / 2
    return REGUERO_2018_NATURE_BASED_AVERTED_USD_BN / total_usd_bn
