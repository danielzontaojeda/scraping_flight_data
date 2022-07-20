import json


def get_airport_list():
    """Return list with airport aita codes from a .txt file"""
    with open("aeroportos_a_pesquisar.txt", "rt") as f:
        return f.readline().split(",")


def get_municipios_json():
    """Return json with brazillian city information from file"""
    with open("municipios.json", "rt", encoding="utf-8") as f:
        return json.load(f)
