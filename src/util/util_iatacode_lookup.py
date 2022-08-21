import airportsdata


def get_city_by_iata(code: str) -> str:
    airports = airportsdata.load("IATA")
    return airports[code]["city"]


if __name__ == "__main__":
    print(get_city_by_iata("FLN"))
    print(get_city_by_iata("CGR"))
    print(get_city_by_iata("PMW"))
