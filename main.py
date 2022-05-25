import time
from scraping_flight_data.output.excel import output
from flight import Flight
from scraping.azul import azul
from scraping.flightstats import flightstats
from scraping.gol import gol
from scraping_flight_data.scraping.latam import latam


def print_flights(flights: list[Flight]):
    for flight in flights:
        print(flight)


def process_flight(flights: list[Flight]):
    for i in flights:
        if "Azul" in i.company_name:
            time.sleep(60)
            azul.set_flight_price(i)
        elif "Gol" in i.company_name:
            gol.set_flight_price(i)
        elif "LATAM" in i.company_name:
            latam.set_flight_price(i)


def get_1d() -> list[Flight]:
    # flights = flightstats.get_flight_info(2, 6)
    # flights += flightstats.get_flight_info(2, 12)
    # flights += flightstats.get_flight_info(2, 18)
    flights = flightstats.get_flight_info(1, 18)
    return flights


def main():
    start = time.perf_counter()
    flights = get_1d()
    process_flight(flights)
    output.write_file(flights)
    end = time.perf_counter()
    print(f"time spent: {end-start:.2f} seconds")


if __name__ == '__main__':
    main()
