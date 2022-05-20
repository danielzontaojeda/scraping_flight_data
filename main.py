from scraping.flightstats import flightstats
from scraping.azul import azul
from scraping.gol import gol
from scraping_flight_data.scraping.latam import latam
from flight import Flight


def print_flights(flights: list[Flight]):
    for i in flights:
        print(i)


def process_flight(flights):
    for i in flights:
        if i.company_name == "Azul":
            azul.set_flight_price(i)
        elif "Gol" in i.company_name:
            gol.set_flight_price(i)
        elif "LATAM" in i.company_name(i):
            latam.set_flight_price(i)


def get_1d() -> list[Flight]:
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
