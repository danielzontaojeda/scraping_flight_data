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


	def get_list(self):
		return[
			date.today(),
			f"{self.airplane.company_code} {self.airplane.number}",
			self.airplane.capacity,
			self.airplane.model,
			self.airplane.company_name,
			self.airport.code,
			self.airport.city_name,
			self.airport.state_name,
			self.airport.region,
			0.0,
			0.0,
			self.price,
			self.time_departure,
			self.time_arrival,
			self.duration,
			self.stopover,
			self.distance,
			self.yield_pax,
		]