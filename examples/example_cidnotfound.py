from psnstoreprice import PsnStorePrice

url = "https://store.playstation.com/#!/it-it/giochi/arslan-the-warriors-of-legend-con-bonus/"
pricelib = PsnStorePrice()
pricelib.getpage(pricelib.normalizeurl(url))