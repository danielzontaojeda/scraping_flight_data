import csv
from scraping_flight_data.flight import flight
import os

HEADER = [
	"Data do vôo",
	"Avião",
	"Capacidade",
	"Modelo",
	"Compania",
	"Aeroporto",
	"Cidade",
	"Estado",
	"Região",
	"Preço 1d",
	"Preço 15d",
	"Preço 30d",
	"Horário de saída",
	"Horário de chegada",
	"Duração em minutos",
	"Conexões",
	"Distância",
	"Yield Pax",
]

def is_file_empty(file):
    return os.stat(file.name).st_size == 0


def write_file(flights: list[flight.Flight]):
    with open("saida.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if is_file_empty(file):
            writer.writerow(["sep=,"])
            writer.writerow(HEADER)

        for flight in flights:
            writer.writerow(flight.get_list())


