from datetime import time, date

from scraping_flight_data.src.file_manager import add_prices
from scraping_flight_data.src.flight import flight, airport, airplane

airport_flight = airport.Airport(
    city_name='Curitiba',
    state_name='Paraná',
    region='Sul',
    code='CWB'
)

airplane1 = airplane.Airplane(
    capacity=144,
    number=3065,
    company_name='LATAM AIRLINES BRASIL',
    company_code='LATAM',
    model='319'
)

airplane2 = airplane.Airplane(
    capacity=144,
    number=3293,
    company_name='LATAM AIRLINES BRASIL',
    company_code='LATAM',
    model='319'
)

def get_time_from_string(string: str) -> time:
    string = string.split(':')
    return time(hour=int(string[0]), minute=int(string[1]), second=int(string[2]))


def get_date_from_string(d: str) -> date:
     d = d.split('/')
     return date(int(d[2]), int(d[1]), int(d[0]))

flight1 = flight.Flight(
    airport=airport_flight,
    airplane=airplane1,
    yield_pax=2.16,
    duration='duration',
    distance=534,
    stopover=0,
    stopover_list=None,
    date_departure= get_date_from_string('23/08/2022'),
    price=6000.69,
    time_departure= get_time_from_string('15:15:00'),
    time_arrival= get_time_from_string('23:20:00'),
)
flight2 = flight.Flight(
    airport=airport_flight,
    airplane=airplane2,
    yield_pax=2.16,
    duration='duration',
    distance=534,
    stopover=2,
    stopover_list=['GIG, VCP'],
    date_departure= get_date_from_string('23/08/2022'),
    price=5000.69,
    time_departure= get_time_from_string('16:15:00'),
    time_arrival= get_time_from_string('23:20:00'),
)

def get_dummy_flight_no_connections():
    return flight1

def get_dummy_flight_with_connections():
    return flight2


