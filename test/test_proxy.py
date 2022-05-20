from scraping_flight_data.proxy import get_proxies, test_proxy


def main():
    proxy_list = get_proxies()
    test_proxy(proxy_list)


if __name__ == '__main__':
    main()
