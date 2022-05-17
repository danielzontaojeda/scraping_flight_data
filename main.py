from scraping import flightstats
from flight import Flight


def print_flights(flights: Flight):
    for i in flights:
        print(f"{i.date}, {i.airplane.company} {i.airplane.airplane_number}, {i.time_departure}, "
              f"{i.time_arrival}, {i.airport_code}, {i.company_name}, {i.airport_name}")


def process_flight(flights):
    for i in flights:
        if i.company_name == "Azul":
            azul.get_flight_price(i)
            break #TODO


def main():
    # How many days from now, Time(6, 12 or 18)
    flights = flightstats.get_flight_info(1, 18)
    print_flights(flights)
    process_flight(flights)


if __name__ == '__main__':
    main()
