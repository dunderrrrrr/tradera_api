# TraderaAPI

[![PyPI version](https://img.shields.io/pypi/v/tradera_api?style=for-the-badge)](https://pypi.org/project/tradera_api/) [![License](https://img.shields.io/badge/license-WTFPL-green?style=for-the-badge)](https://github.com/dunderrrrrr/tradera_api/blob/main/LICENSE) [![Python versions](https://img.shields.io/pypi/pyversions/tradera-api?style=for-the-badge)](https://pypi.org/project/tradera_api/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/tradera_api?style=for-the-badge&color=%23dbce58)

This is an unofficial Python wrapper for the [Tradera](https://tradera.com/) API, Sweden’s largest online marketplace. It simplifies interaction with Tradera's services, such as searching and filtering listings in all categories, returning all data in raw json format.

>Tradera is Sweden's largest online marketplace, offering a platform for buying and selling new and second-hand items through auctions and fixed-price listings. It hosts millions of listings across categories like fashion, electronics, home goods, and collectibles, serving both private individuals and professional sellers.

## ✨ Features

- Make searches across all of Tradera
- Filters for region, categories, price range, and more.

## 🧑‍💻️ Install

TraderaAPI is available on PyPI.

```sh
pip install tradera-api
```

## 💁‍♀️ Usage

This will search for term "ESP32" across all categories using `AuctionType.all` and `Sorting.best_hit`, which is the default Tradera search behavior.

```py
>>> from tradera_api import TraderaAPI
>>> print(TraderaAPI().search("ESP32"))
```

### 🔎 Filtering


Use `Sorting`, `AuctionType`, `Category` and `price` to filter your search. For all available options, see each Enum respectively.


```py
>>> from TraderaAPI import Sorting, AuctionType, Category
>>> TraderaAPI().search(
   query="ESP32", 
   category=Category.hobby,
   price=(50, 200), # from 50 SEK to 200 SEK
   auction_type=AuctionType.buy_now,
   sorting=Sorting.time_left
)
```

## 📝 Notes

- Source repo: https://github.com/dunderrrrrr/tradera_api
- PyPI: https://pypi.org/project/tradera-api/
