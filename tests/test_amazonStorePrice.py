# -*- coding: utf-8 -*-
from unittest import TestCase, main
from psnstoreprice import PsnStorePrice


class TestAmazonStorePrice(TestCase):
    def setUp(self):
        self.lib = PsnStorePrice()
        self.urltest = "https://store.playstation.com/#!/it-it/giochi/arslan-the-warriors-of-legend-con-bonus/" \
                       "cid=EP4108-CUSA03866_00-ARSLANWITHBONUS0"

    def test_normalizeurl(self):
        self.assertEqual(self.lib.normalizeurl(self.urltest), self.urltest)

    def test_normalizeprice(self):
        self.assertEqual(self.lib.normalizeprice("€1,00"), 1.00)
        self.assertEqual(self.lib.normalizeprice("$14.08"), 14.08)
        self.assertEqual(self.lib.normalizeprice("£11.00"), 11.00)

    def test_geturl(self):
        self.assertEqual(self.lib.getpage(self.lib.normalizeurl(self.urltest)).find(
            "h1", {"class": "productTitle"}).contents[0], "ARSLAN: THE WARRIORS OF LEGEND con Bonus")

    def test_getprice(self):
        self.assertIsInstance(self.lib.getprice(self.urltest), float)

if __name__ == '__main__':
    main(verbosity=3)
