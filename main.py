import time

from scraping.flightstats import flightstats
from scraping.azul import azul
from scraping.gol import gol
from flight import Flight


def print_flights(flights: Flight):
    for i in flights:
        print(f"{i.date}, {i.airplane.company} {i.airplane.airplane_number}, {i.time_departure}, "
              f"{i.time_arrival}, {i.airport_code}, {i.company_name}, {i.airport_name}, "
              f"{i.price}, {i.airplane.model}")


def process_flight(flights):
    for i in flights:
        if i.company_name == "Azul":
            azul.get_flight_price(i)
        elif "Gol" in i.company_name:
            gol.get_flight_price(i)


def get_1d():
    # flights = flightstats.get_flight_info(1, 6)
    # flights += flightstats.get_flight_info(1, 12)
    # flights += flightstats.get_flight_info(1, 18)
    flights = flightstats.get_flight_info(1, 18)
    return flights


def main():
    flights = get_1d()
    process_flight(flights)
    print_flights(flights)


if __name__ == '__main__':
    main()
