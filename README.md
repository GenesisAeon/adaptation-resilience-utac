# adaptation-resilience-utac

[![GenesisAeon](https://img.shields.io/badge/GenesisAeon-P95-blue)](https://github.com/GenesisAeon)
[![CI](https://github.com/GenesisAeon/adaptation-resilience-utac/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/adaptation-resilience-utac/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21798240.svg)](https://doi.org/10.5281/zenodo.21798240)

GenesisAeon Package 95 — real climate adaptation cost-benefit science.
**Deliberately has no UTAC/CREP/AFET bridge** — see
[DISCLAIMER.md](DISCLAIMER.md).

For a plain-language explanation of the same topic (German, no jargon,
written for general audiences), see [WHITEPAPER.md](WHITEPAPER.md).

## What's real here

- Reguero et al. (2018, *PLOS ONE*): Gulf Coast nature-based adaptation
  (wetlands, oyster reefs) averts $50B+ in losses at an average
  benefit-to-cost ratio above 3.5.
- Global Commission on Adaptation (2019): $1.8T global adaptation
  investment (2020-2030) projected to generate $7.1T in net benefits.
- Documents the real "triple dividend" of adaptation: avoided losses,
  economic gains, and social/environmental co-benefits — see
  [DISCLAIMER.md](DISCLAIMER.md).

## Quickstart

```bash
pip install adaptation-resilience-utac
```

```python
from adaptation_resilience_utac import gca_global_bcr

print(gca_global_bcr())  # ~3.94
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
