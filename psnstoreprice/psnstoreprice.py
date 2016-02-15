from psnstoreprice.exception import CidNotFound, UrlNotPsn, PageNotFound
from bs4 import BeautifulSoup
from time import sleep
from webkit_server import Client


class PsnStorePrice:

    def normalizeurl(self, url):
        """
        clean the url and check if all element required is present

        :param url(string): PSN store url

        :return: string(url cleaned)

        """
        if "store.playstation.com" in url:
            if "cid=" in url:
                return url
            else:
                raise CidNotFound("Please check the url, it doesn't not contain the cid code")
        else:
            raise UrlNotPsn("Please check the url, it doesn't contain www.amazon*")

    def normalizeprice(self, price):
        """
        remove the currenty from price

        :param price(string): price tag find on amazon store

        :return: float(price cleaned)

        """
        listreplace = ["$", "£", "€"]
        for replacestring in listreplace:
            price = price.replace(replacestring, "")
        return float(price.replace(",", "."))

    def getpage(self, url, sleep_time=5):
        """
        Get the page and raise if status_code is not equal to 200

        :param url(string): normalized(url)

        :param sleep_time(int): Time to wait until take the data (default 5s)

        :return: bs4(html)
        """

        req = Client()
        req.visit(url=url)
        sleep(sleep_time)
        resp = req.body()
        if req.status_code() == 200:
            body_content = BeautifulSoup(resp, "html.parser")
            if body_content.find("h1", {"class": "productTitle"}) is not None:
                return body_content
            else:
                return self.getpage(url=url, sleep_time=int(sleep_time+1))
        else:
            raise PageNotFound("Page not found, please check url")

    def getprice(self, url, sleep_time=5):
        """
        Find the price on AmazonStore starting from URL

        :param url(string): url

        :param sleep_time(int): Time to wait until take the data (default 5s)

        :return: float(price cleaned)
        """
        body_content = self.getpage(self.normalizeurl(url), sleep_time=sleep_time)
        return self.normalizeprice(body_content.find_all("div", {"class": "price"})[-1].contents[0])
