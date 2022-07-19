import json


def get_airport_list():
    with open("aeroportos_a_pesquisar.txt", "rt") as f:
        return f.readline().split(",")


def get_municipios_json():
    with open("municipios.json", "rt", encoding="utf-8") as f:
        return json.load(f)
