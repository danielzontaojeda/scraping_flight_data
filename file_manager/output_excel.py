import csv
from scraping_flight_data.flight import flight
import os

HEADER = [
	"Data do voo",
	"Aviao",
	"Capacidade",
	"Modelo",
	"Compania",
	"Codigo do Aeroporto",
	"Cidade",
	"Estado",
	"Regiao",
	"Preco 1d",
	"Preco 15d",
	"Preco 30d",
	"Horario de saida",
	"Horario de chegada",
	"Duracao em minutos",
	"Conexoes",
	"Distancia",
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
            writer.writerow(get_list(flight))


def get_list(flight):
	return[
		flight.date_departure,
		f"{flight.airplane.company_code} {flight.airplane.number}",
		flight.airplane.capacity,
		flight.airplane.model,
		flight.airplane.company_name,
		flight.airport.code,
		flight.airport.city_name,
		flight.airport.state_name,
		flight.airport.region,
		0.0,
		0.0,
		flight.price,
		flight.time_departure,
		flight.time_arrival,
		flight.duration,
		flight.stopover,
		flight.distance,
		flight.yield_pax,
	]
