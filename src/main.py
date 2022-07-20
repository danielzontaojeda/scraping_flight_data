import sys
from time import perf_counter

from src.file_manager import input
from src.file_manager import output_excel
from src.scraper.gol import gol
from src.scraper.latam import latam

sys.path.append("..")


def main():
    list_airports = input.get_airport_list()
    flight_list = gol.get_flights(list_airports)
    flight_list.extend(latam.get_flights(list_airports))
    output_excel.write_file(flight_list)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Tempo decorrido: {(end - start):.2f} segundos.")
