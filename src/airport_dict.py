from src.file_manager import input
from src.util.util_distance import get_distance
from src.util.util_iatacode_lookup import get_city_by_iata
from src.util.util_ibge import get_uf_info


def get_airport_dict_list(airport_list: list[str]) -> dict:
    airport_dict_list = []
    for airport in airport_list:
        d = {}
        d["airport"] = airport
        d["city_name"] = get_city_by_iata(airport)
        d["distance"] = get_distance(d["city_name"])
        d["uf_info"] = get_uf_info(d["city_name"])
        airport_dict = {airport: d}
        airport_dict_list.append(airport_dict)
    return airport_dict_list


if __name__ == "__main__":
    list_dict_airport = get_airport_dict_list()
    for dict_airport in list_dict_airport:
        for key in dict_airport.keys():
            print(key)
