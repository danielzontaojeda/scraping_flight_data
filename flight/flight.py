from dataclasses import dataclass
from datetime import date, time
from scraping_flight_data.flight.airport import Airport
from scraping_flight_data.flight.airplane import Airplane


@dataclass
class Flight:
	airplane: Airplane
	airport: Airport
	price: float
	date_departure: date
	time_departure: time
	time_arrival: time
	stopover: int
	conections: list[str]
	distance: float 
	yield_pax: float
	duration: int