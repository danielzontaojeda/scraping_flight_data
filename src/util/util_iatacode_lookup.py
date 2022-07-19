import airportsdata


def get_city_by_iata(code):
    airports = airportsdata.load("IATA")
    return airports[code]["city"]


if __name__ == "__main__":
    print(get_city_by_iata("CWB"))
    print(get_city_by_iata("CGB"))
