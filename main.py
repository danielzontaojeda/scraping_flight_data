import sys
from time import perf_counter

import airport_dict
from src.file_manager import input, output_excel
from src.scraper.gol import gol
from src.scraper.latam import latam
from airport_dict import get_airport_dict_list

# from src.scraper.azul import azul

sys.path.append("..")


def process_data_azul():
    """
    azul.get_flights changes list_airports
    """
    list_airports = input.get_airport_list()
    flight_list = azul.get_flights(list_airports)
    output_excel.write_file(flight_list)


def process_data_gol(list_airports):
    flight_list = gol.get_flights(list_airports, 30)
    output_excel.write_file(flight_list)


def process_data_latam(list_airports):
    flight_list = latam.get_flights(list_airports, 30)
    output_excel.write_file(flight_list)


def main():
    list_airports = airport_dict.get_airport_dict_list()
    # process_data_azul()
    # process_data_gol(list_airports)
    process_data_latam(list_airports)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Tempo decorrido: {(end - start):.2f} segundos.")
