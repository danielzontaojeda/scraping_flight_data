from scraping_flight_data.flight import Flight


def main():
    flight_string = ['20/05/2020',
                     'AD 1100',
                     '18:00',
                     '00:00',
                     'VCP',
                     'Azul',
                     'Guarulhos']
    flight = Flight(flight_string)
    flight.set_price('1000,00')
    flight.set_airplane_model('a320')
    print(flight)


if __name__ == "__main__":
    main()