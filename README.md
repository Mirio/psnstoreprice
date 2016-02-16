## PsnStorePrice
This module find the price from url given

Compatible with all amazon store

[![Build Status](https://travis-ci.org/Mirio/psnstoreprice.svg?branch=0.1)](https://travis-ci.org/Mirio/psnstoreprice) [![PyPI](https://img.shields.io/pypi/dm/psnstoreprice.svg)]() [![Github All Releases](https://img.shields.io/github/downloads/mirio/psnstoreprice/total.svg)]() [![Documentation Status](https://readthedocs.org/projects/psnstoreprice/badge/?version=0.1)](http://psnstoreprice.readthedocs.org/en/latest/?badge=0.1)
[![Coverage Status](https://coveralls.io/repos/github/Mirio/psnstoreprice/badge.svg?branch=0.1)](https://coveralls.io/github/Mirio/psnstoreprice?branch=0.1)


## Link
Documentation: http://psnstoreprice.readthedocs.org/

Bug Tracker: https://github.com/Mirio/psnstoreprice/issues

GitHub: https://github.com/Mirio/psnstoreprice


## Requirement
Python 3.x

Python Library = [ 'dryscrape', 'beautifulsoup4' ]

## How to install
```
pip install psnstoreprice
```

## Install from source
```
git clone https://github.com/Mirio/psnstoreprice.git
cd psnstoreprice
python setup.py install
```

## Getting Started

Example:
```
from psnstoreprice import PsnStorePrice

url = "https://store.playstation.com/#!/en-ie/games/earth-defense-force-41-the-shadow-of-new-despair/" \
      "cid=EP4293-CUSA03467_00-EARTHDEFENSEFO41"
pricelib = PsnStorePrice()
print(pricelib.getprice(url))
```

Output:
```
$ python example_getprice.py
64.99
```