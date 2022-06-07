import csv
from scraping_flight_data.flight import Flight

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


def write_file(flights: list[Flight]):
    with open("saida.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell == 0:
            writer.writerow(["sep=,"])
            writer.writerow(HEADER)

        for flight in flights:
            writer.writerow(flight.get_list())
            print(flight)
