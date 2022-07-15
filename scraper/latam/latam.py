from scraping_flight_data.flight import flight, airplane, airport
from scraping_flight_data.scraper.latam import scraper
from scraping_flight_data.util import util_ibge, util_datetime
from scraping_flight_data.scraper.seatguru import latam_capacity


def get_flights(list_airport: list[str]) -> list[flight.Flight]:
	flight_list = []
	capacity_dict = latam_capacity.get_capacity_dict()
	for airport in list_airport:
		data_json = scraper.get_flight_list(util_datetime.date_from_today(30), airport)
		info_flights = get_flight_info(data_json)
		flight_list.extend(get_flight_list(info_flights, capacity_dict))
	return flight_list


def get_flight_list(info_flights, capacity_dict):
	flight_list = []
	for i in range(info_flights['size']):
		# 0 is the number of conections
		flight_airplane = get_airplane(info_flights['itinerary'][i][0], capacity_dict)
		flight_airport = get_airport(info_flights['summary'][i])
		flight = get_flight(flight_airplane, flight_airport,
					info_flights['summary'][i], info_flights['itinerary'][i] )
		flight_list.append(flight)
	return flight_list


def get_flight(airplane, airport, summary, itinerary):
	return flight.Flight(
		airplane = airplane,
		airport = airport,
		price = summary['lowestPrice']['amount'],
		date_departure = util_datetime.get_date_from_isoformat(summary['origin']['departure']),
		time_departure = util_datetime.get_time_from_isoformat(summary['origin']['departure']),
		time_arrival = util_datetime.get_time_from_isoformat(summary['destination']['arrival']),
		stopover = summary['stopOvers'],
		conections = [],
		distance = 0.0,
		yield_pax = 0.0,
		duration = summary['duration']
	)


def get_airport(summary):
	uf_info = util_ibge.get_uf_info(summary['origin']['city'])
	return airport.Airport(
		code = summary['origin']['iataCode'],
		city_name = summary['origin']['city'],
		state_name = uf_info['state'],
		region = uf_info['region']
	)


def get_airplane(itinerary, capacity_dict):
	model_airplane = itinerary['equipment']
	return airplane.Airplane(
		number = itinerary['flight']['flightNumber'],
		company_code = itinerary['flight']['airlineCode'],
		company_name = itinerary['aircraftLeaseText'],
		capacity = latam_capacity.get_capacity_for_model(model_airplane, capacity_dict),
		model = model_airplane
	)
	
	
def get_flight_info(data_json):
	summary_list = []
	itinerary_list = []
	for data in data_json:
		summary = data['summary']
		summary_list.append(summary)
		itinerary = data['itinerary']
		itinerary_list.append(itinerary)
	return {
		'summary': summary_list,
		'itinerary': itinerary_list,
		'size': len(summary_list)
	}

