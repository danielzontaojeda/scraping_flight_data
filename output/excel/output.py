import csv
from scraping_flight_data.flight import Flight

HEADER = [
    "Data",
    "Avião",
    "Hora de saída",
    "Hora de chegada",
    "Aeroporto",
    "Compania",
    "Cidade",
    "Preço",
    "Modelo avião"
]


def write_file(flights: list[Flight]):
    with open("saida.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sep=,"])
        writer.writerow(HEADER)
        for flight in flights:
            writer.writerow(flight.get_list())
