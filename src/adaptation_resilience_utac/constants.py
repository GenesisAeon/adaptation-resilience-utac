"""Verified constants for climate adaptation cost-benefit science."""

PACKAGE_ID = 95

ADAPTATION_RESILIENCE_NOTE = (
    "Climate adaptation measures (early warning systems, resilient "
    "infrastructure, nature-based coastal defenses, resilient "
    "agriculture) are not merely defensive spending -- the peer-reviewed "
    "and institutional literature finds they typically return several "
    "dollars of avoided loss and economic benefit per dollar invested, "
    "the 'triple dividend' of avoided losses, induced economic gains, "
    "and social/environmental co-benefits."
)

REGUERO_2018_CITATION = (
    "Reguero, B.G., Beck, M.W., Bresch, D.N., Calil, J., Meliane, I. "
    "(2018). Comparing the cost effectiveness of nature-based and "
    "coastal adaptation: A case study from the Gulf Coast of the United "
    "States. PLOS ONE, 13(4), e0192132. "
    "DOI: 10.1371/journal.pone.0192132"
)
REGUERO_2018_DOI = "10.1371/journal.pone.0192132"

# Total potential losses preventable by a cost-effective adaptation
# portfolio (benefit-to-cost ratio above 1) in the US Gulf Coast, USD billion
REGUERO_2018_PREVENTABLE_LOSSES_LOW_USD_BN = 57.0
REGUERO_2018_PREVENTABLE_LOSSES_HIGH_USD_BN = 101.0

# Losses averted by nature-based options specifically (wetlands, oyster
# reefs), USD billion, and their average benefit-to-cost ratio
REGUERO_2018_NATURE_BASED_AVERTED_USD_BN = 50.0
REGUERO_2018_NATURE_BASED_AVG_BCR = 3.5

GCA_2019_CITATION = (
    "Global Commission on Adaptation (2019). Adapt Now: A Global Call "
    "for Leadership on Climate Resilience. Global Center on Adaptation / "
    "World Resources Institute."
)

# GCA (2019): global investment proposed for 2020-2030 across 5 priority
# adaptation areas (early warning systems, resilient infrastructure,
# improved dryland agriculture, mangrove protection, resilient water
# resources), and the projected net benefit, USD trillion
GCA_2019_PROPOSED_INVESTMENT_USD_TRILLION = 1.8
GCA_2019_PROJECTED_NET_BENEFIT_USD_TRILLION = 7.1

# GCA (2019): typical range of benefit-to-cost ratios found across
# adaptation investment studies reviewed
GCA_2019_BCR_LOW = 2.0
GCA_2019_BCR_HIGH = 10.0

TRIPLE_DIVIDEND_NOTE = (
    "The 'triple dividend' framing (GCA 2019): (1) avoided future losses, "
    "(2) positive economic benefits through reduced risk and increased "
    "productivity, (3) additional social and environmental co-benefits. "
    "This package models dividend (1) and (2) quantitatively; dividend "
    "(3) is real but not reducible to a single comparable number across "
    "studies."
)

NOT_A_GUARANTEED_OUTCOME_NOTE = (
    "Benefit-cost ratios in this literature are modeled projections under "
    "stated assumptions (discount rates, hazard scenarios, avoided-loss "
    "methodology), not guaranteed outcomes. Implementation gaps are real: "
    "most published studies remain hazard-specific (often flood risk) "
    "and ex-post, not prospectively validated across all adaptation "
    "measure types."
)
