from time import perf_counter

from src import airport_dict
from src.file_manager import input, output_excel, add_prices
from src.scraper.azul import azul
from src.scraper.gol import gol
from src.scraper.latam import latam
from src.util import util_get_logger, post_scraping

LOGGER = util_get_logger.get_logger(__name__)


def webscrape_azul():
    list_airports = input.get_airport_list()
    azul.get_flights(list_airports, 30)
    azul.get_flights(list_airports, 15)
    # azul.get_flights(list_airports, 1)


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
    webscrape_azul(list_airports_dict)
    webscrape_gol(list_airports_dict)
    webscrape_latam(list_airports_dict)
    post_scraping.create_csv_backup()
    post_scraping.delete_old_backup()
    post_scraping.delete_old_log()


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    LOGGER.info("Script ran succesfully.")
    LOGGER.info(f"Elapsed time: {(end - start):.2f} seconds.")
