from src.file_manager import input
from unidecode import unidecode


def get_uf_info(city_name):
    if city_name == "Porto Alegre":
        return {"state": "Rio Grande do Sul", "region": "Sul", "city": "Porto Alegre"}
    data = input.get_municipios_json()
    for city in data:
        if unidecode(city["nome"]).lower() in unidecode(city_name).lower():
            return {
                "state": city["regiao-imediata"]["regiao-intermediaria"]["UF"]["nome"],
                "region": city["regiao-imediata"]["regiao-intermediaria"]["UF"][
                    "regiao"
                ]["nome"],
                "city": city["nome"],
            }
    raise Exception(f"Could not find {city_name} in ibge database")


if __name__ == "__main__":
    print(get_uf_info("Rio De Janeiro"))
    print(get_uf_info("Rio De janeiro"))
    print(get_uf_info("Rio de Janeiro"))
