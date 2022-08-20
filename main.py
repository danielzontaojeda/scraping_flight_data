import sys
from time import perf_counter

from src import airport_dict
from src.file_manager import input, output_excel, add_prices
from src.scraper.gol import gol
from src.scraper.latam import latam
# from src.scraper.azul import azul


def process_data_azul():
    """
    azul.get_flights changes list_airports
    """
    list_airports = input.get_airport_list()
    flight_list = azul.get_flights(list_airports)
    output_excel.write_file(flight_list)


def webscrape_gol(list_airports):
    flight_list = gol.get_flights(list_airports, 30)
    output_excel.write_file(flight_list)
    flight_list = gol.get_flights(list_airports, 15)
    add_prices.insert_price(flight_list, 15)
    flight_list = gol.get_flights(list_airports, 1)
    add_prices.insert_price(flight_list, 1)


def webscrape_latam(list_airports):
    flight_list = latam.get_flights(list_airports, 30)
    output_excel.write_file(flight_list)
    flight_list = latam.get_flights(list_airports, 15)
    add_prices.insert_price(flight_list, 15)
    flight_list = latam.get_flights(list_airports, 1)
    add_prices.insert_price(flight_list, 1)


def main():
    list_airports = input.get_airport_list()
    list_airports_dict = airport_dict.get_airport_dict_list(list_airports)
    # process_data_azul()
    webscrape_gol(list_airports_dict)
    webscrape_latam(list_airports_dict)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Tempo decorrido: {(end - start):.2f} segundos.")
