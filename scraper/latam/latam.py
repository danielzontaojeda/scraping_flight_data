from scraping_flight_data.flight import flight, airplane, airport
from scraping_flight_data.file_manager import input
from scraping_flight_data.scraper.latam import scraper
from datetime import date, timedelta, datetime


def get_flights(list_airport: list[str]) -> list[flight.Flight]:
	#TODO: only getting one airport
	flight_list = []
	for airport in list_airport:
		data_json = scraper.get_flight_list(date_from_today(30), airport)
		info_flights = get_flight_info(data_json)
		flight_list.extend(get_flight_list(info_flights))
	return flight_list


def get_flight_list(info_flights):
	flight_list = []
	for i in range(info_flights['size']):
		# 0 is the number of conections
		flight_airplane = get_airplane(info_flights['itinerary'][i][0])
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
		date_departure = get_date(summary['origin']['departure']),
		time_departure = get_time(summary['origin']['departure']),
		time_arrival = get_time(summary['destination']['arrival']),
		stopover = summary['stopOvers'],
		conections = [],
		distance = 0.0,
		yield_pax = 0.0,
		duration = summary['duration']
	)


def get_date(iso_datetime_str):
	# "2022-08-10T06:15:00"
	iso_format = datetime.fromisoformat(iso_datetime_str)
	return iso_format.date()


def get_time(iso_datetime_str):
	iso_format = datetime.fromisoformat(iso_datetime_str)
	return iso_format.time()


def get_airport(summary):
	uf_info = get_uf_info(summary['origin']['city'])
	return airport.Airport(
		code = summary['origin']['iataCode'],
		city_name = summary['origin']['city'],
		state_name = uf_info['state'],
		region = uf_info['region']
	)


def get_uf_info(city_name):
	if city_name == "Porto Alegre":
		return{
			'state': 'Rio Grande do Sul',
			'region': 'Sul'
		}
	data = input.get_municipios_json()
	for city in data:
		if city['nome'] in city_name:
			return {
				'state': city['regiao-imediata']['regiao-intermediaria']['UF']['nome'],
				'region': city['regiao-imediata']['regiao-intermediaria']['UF']['regiao']['nome']
			}



def get_airplane(itinerary):
	return airplane.Airplane(
		number = itinerary['flight']['flightNumber'],
		company_code = itinerary['flight']['airlineCode'],
		company_name = itinerary['aircraftLeaseText'],
		capacity = 0,
		model = itinerary['equipment']
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


def date_from_today(days: int):
	return date.today()+timedelta(days=days)

