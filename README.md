# Lighthouse Scoring Calculator

Python package to calculate the Lighthouse scoring for a website

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![PyPI](https://img.shields.io/pypi/v/lighthouse-scoring-calculator)

## Authors

- [@fabiomanz](https://www.github.com/fabiomanz)

## Acknowledgements

- [lh-scorecalc](https://github.com/paulirish/lh-scorecalc)
- Inspired by this website: [https://googlechrome.github.io/lighthouse/scorecalc/](https://googlechrome.github.io/lighthouse/scorecalc/)
- [Awesome README](https://readme.so/)

## Features

- Python module to directly use the calculator in Python projects
- CLI to use the calculator directly from the command line
- Multiple Lighthouse version support
- Cross platform
- Support for Lighthouse mobile and desktop test

## Usage/Examples

```python
from lighthouse_scoring_calculator import LighthouseScoringCalculator

testData = {
    "FCP": 2130,
    "SI": 5800,
    "FMP": 4000,
    "TTI": 7300,
    "FCI": 6500,
    "LCP": 4000,
    "TBT": 600,
    "CLS": 0.25
}

calculator = LighthouseScoringCalculator(testData, "mobile", "v9")

print("Score:", calculator.calc_score())
print("Rating of FCP:", calculator.get_rating("FCP"))

```

### CLI Reference

```
usage: lighthouse_scoring_calculator.py [-h] [-d DEVICE] [-v VERSION] [--fcp FCP] [--si SI] [--fmp FMP] [--tti TTI] [--fci FCI] [--lcp LCP] [--tbt TBT] [--cls CLS]

Calculate the score and rating of each metric
Example: $ python3 -m lighthouse_scoring_calculator -d mobile -v v9 --fcp 2130 --si 5800 --fmp 4000 --tti 7300 --fci 6500 --lcp 4000 --tbt 600 --cls 0.25

options:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
                        The device type
  -v VERSION, --version VERSION
                        The lighthouse version
  --fcp FCP             The First Contentful Paint metric
  --si SI               The Speed Index metric
  --fmp FMP             The First Meaningful Paint metric
  --tti TTI             The Time to Interactive metric
  --fci FCI             The First CPU Idle metric
  --lcp LCP             The Largest Contentful Paint metric
  --tbt TBT             The Total Blocking Time metric
  --cls CLS             The Cumulative Layout Shift metric
```

## Installation

You can install the Lighthouse Scoring Calculator from [PyPI](https://pypi.org/project/lighthouse-scoring-calculator/):

    python -m pip install lighthouse-scoring-calculator

## Feedback

If you have any feedback, please reach out to us via GitHub