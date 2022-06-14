import csv
from scraping_flight_data.flight import Flight
import os

HEADER = [
    "Data",
    "Aviao",
    "Hora de saida",
    "Hora de chegada",
    "Aeroporto",
    "Compania",
    "Cidade",
    "Preco_1d",
    "Preco_15d",
    "Preco_30d",
    "Modelo aviao"
]

def is_file_empty(file):
    return os.stat(file.name).st_size == 0


def write_file(flights: list[Flight]):
    with open("saida.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if is_file_empty(file):
            writer.writerow(["sep=,"])
            writer.writerow(HEADER)

        for flight in flights:
            writer.writerow(flight.get_list())
            print(flight)
