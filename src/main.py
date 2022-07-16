from src.file_manager import output_excel
from src.file_manager import input
from src.scraper.latam import latam
from time import perf_counter

import sys
sys.path.append("..")

def main():
	list_airports = input.get_airport_list()
	flight_list = latam.get_flights(list_airports)	
	output_excel.write_file(flight_list)


if __name__ == "__main__":
	start = perf_counter()
	main()
	end = perf_counter()
	print(f"Tempo decorrido: {(end - start):.2f} segundos.")