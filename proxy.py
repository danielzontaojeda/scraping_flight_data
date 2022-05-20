import requests

# use to parse html text
from lxml.html import fromstring
from itertools import cycle
import traceback


def get_proxies():
    # website to get free proxies
    url = 'https://free-proxy-list.net/'

    response = requests.get(url)

    parser = fromstring(response.text)
    # using a set to avoid duplicate IP entries.
    proxies = set()

    for i in parser.xpath('//tbody/tr')[:200]:

        # Grabbing IP and corresponding PORT
        proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                          i.xpath('.//td[2]/text()')[0]])
        proxies.add(proxy)

    return proxies


def test_proxy(proxy_list):
    # to rotate through the list of IPs
    proxy_pool = cycle(proxy_list)

    # insert the url of the website you want to scrape.
    url = 'https://www.voeazul.com.br/'

    for i in range(1, 201):

        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)

        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy})
            print(response.json())

        except:
            pass
            # One has to try the entire process as most
            # free proxies will get connection errors
            # We will just skip retries.
            print("Skipping.  Connection error")