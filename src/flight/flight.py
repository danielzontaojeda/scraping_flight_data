from dataclasses import dataclass
from datetime import date, time
from src.flight.airport import Airport
from src.flight.airplane import Airplane
from src.util import util_datetime


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

	def get_conection_str(self):
		if self.stopover > 0:
			return "Conexão"
		else:
			return "Direto"


	def get_list(self):
		return[
			self.airport.region,
			self.airport.state_name,
			self.airport.city_name,
			self.airport.code,
			self.date_departure,
			util_datetime.get_month_portuguese(self.date_departure.month),
			self.date_departure.year,
			self.airplane.number,
			self.airplane.model,
			self.airplane.company_name,
			self.airplane.capacity,
			self.time_departure,
			self.time_arrival,
			self.get_conection_str(),
			self.conections,
			self.distance,
			f"{self.price:.2f}",
			0.0,
			0.0,
			f"{self.price:.2f}",
			f"{self.yield_pax:.2f}"
		]

	# def get_list(self):
	# 	return[
	# 		date.today(),
	# 		f"{self.airplane.company_code} {self.airplane.number}",
	# 		self.airplane.capacity,
	# 		self.airplane.model,
	# 		self.airplane.company_name,
	# 		self.airport.code,
	# 		self.airport.city_name,
	# 		self.airport.state_name,
	# 		self.airport.region,
	# 		0.0,
	# 		0.0,
	# 		self.price,
	# 		self.time_departure,
	# 		self.time_arrival,
	# 		self.duration,
	# 		self.stopover,
	# 		self.distance,
	# 		f"{self.yield_pax:.2f}",
	# 	]

