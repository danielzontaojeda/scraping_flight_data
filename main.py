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
    for flight in flights:
        if "Azul" in flight.company_name:
            # azul.set_flight_price(flight)
            flight.price1d = azul.get_price_future(flight, 1)
            flight.price15d = azul.get_price_future(flight, 15)
            flight.price30d = azul.get_price_future(flight, 30)
        # elif "Gol" in i.company_name:
        #     gol.set_flight_price(i)
        # if "LATAM" in i.company_name:
        #     latam.set_flight_price(i)


def get_flight_list() -> list[Flight]:
    flights = flightstats.get_flight_info(time=6)
    # flights += flightstats.get_flight_info(1, 12)
    # flights += flightstats.get_flight_info(1, 18)
    return flights


def main():
    flights = get_flight_list()
    process_flight(flights)
    output.write_file(flights)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"time spent: {end-start:.2f} seconds")
