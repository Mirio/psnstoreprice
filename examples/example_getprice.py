from psnstoreprice import PsnStorePrice

url = "https://store.playstation.com/#!/en-ie/games/earth-defense-force-41-the-shadow-of-new-despair/" \
      "cid=EP4293-CUSA03467_00-EARTHDEFENSEFO41"
pricelib = PsnStorePrice()
print(pricelib.getprice(url))
