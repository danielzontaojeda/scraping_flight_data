import csv
import os

from src.flight import flight

HEADER = [
    "Região",
    "Estado",
    "CidadeOrigem",
    "AERO",
    "DataViagem",
    "Mês",
    "Ano",
    "NúmeroVoo",
    "Equipamento/Avi",
    "CiaAérea",
    "CapacidadeAeronave",
    "Hora Partida",
    "Hora Chegada",
    "Tipo de Trajeto",
    "AeroportoConexão",
    "DistânciaAéreaKM",
    "Preço 30d",
    "Preço 15d",
    "Preço 1d",
    "PreçoMédio",
    "Yield Pax",
]


def is_file_empty(file) -> bool:
    return os.stat(file.name).st_size == 0


def write_file(flights: list[flight.Flight], filename="saida.csv") -> None:
    """Write flight object list into a csv file."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if is_file_empty(file):
            writer.writerow(["sep=,"])
            writer.writerow(HEADER)

        for flight in flights:
            writer.writerow(flight.get_list())
