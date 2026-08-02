"""adaptation-resilience-utac -- real climate adaptation cost-benefit science.

GenesisAeon Package 95. Deliberately has no UTAC/CREP/AFET bridge -- see DISCLAIMER.md.
"""

from .constants import (
    ADAPTATION_RESILIENCE_NOTE,
    GCA_2019_BCR_HIGH,
    GCA_2019_BCR_LOW,
    GCA_2019_CITATION,
    GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION,
    GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION,
    NOT_A_GUARANTEED_OUTCOME_NOTE,
    PACKAGE_ID,
    REGUERO_2018_CITATION,
    REGUERO_2018_DOI,
    REGUERO_2018_NATURE_BASED_AVERTED_USD_BN,
    REGUERO_2018_NATURE_BASED_AVG_BCR,
    REGUERO_2018_PREVENTABLE_LOSSES_HIGH_USD_BN,
    REGUERO_2018_PREVENTABLE_LOSSES_LOW_USD_BN,
    TRIPLE_DIVIDEND_NOTE,
)
from .cost_benefit import (
    ALL_MEASURES,
    AdaptationMeasure,
    gca_global_bcr,
    gca_global_net_benefit_usd_trillion,
    is_cost_effective,
    nature_based_share_of_preventable_losses,
)

__version__ = "1.0.0"

__all__ = [
    "ADAPTATION_RESILIENCE_NOTE",
    "GCA_2019_BCR_HIGH",
    "GCA_2019_BCR_LOW",
    "GCA_2019_CITATION",
    "GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION",
    "GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION",
    "NOT_A_GUARANTEED_OUTCOME_NOTE",
    "PACKAGE_ID",
    "REGUERO_2018_CITATION",
    "REGUERO_2018_DOI",
    "REGUERO_2018_NATURE_BASED_AVERTED_USD_BN",
    "REGUERO_2018_NATURE_BASED_AVG_BCR",
    "REGUERO_2018_PREVENTABLE_LOSSES_HIGH_USD_BN",
    "REGUERO_2018_PREVENTABLE_LOSSES_LOW_USD_BN",
    "TRIPLE_DIVIDEND_NOTE",
    "ALL_MEASURES",
    "AdaptationMeasure",
    "gca_global_bcr",
    "gca_global_net_benefit_usd_trillion",
    "is_cost_effective",
    "nature_based_share_of_preventable_losses",
]
