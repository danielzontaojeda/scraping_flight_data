from scraping_flight_data.src.scraper.seatguru import azul_capacity
from scraping_flight_data.src.util import util_iatacode_lookup, util_ibge, util_distance

# TODO: distance, yield_pax
def get_missing_data(flight_dict, capacity_dict):
   flight_dict['capacity'] = azul_capacity.get_capacity_for_model(flight_dict['airplane_model'], capacity_dict)
   flight_dict = get_uf_info(flight_dict)
   flight_dict['distance'] = util_distance.get_distance(flight_dict['city_name'])
   flight_dict['yield_pax'] = flight_dict['price']/flight_dict['distance']
   duration_list = flight_dict['duration_str'].split('h')
   duration = int(duration_list[0])*60 + int(duration_list[1])
   flight_dict['duration'] = duration
   print(flight_dict)
   return flight_dict


def get_uf_info(flight_dict):
   city_name = util_iatacode_lookup.get_city_by_iata(flight_dict['airport_code'])
   uf_dict = util_ibge.get_uf_info(city_name)
   flight_dict['state'] = uf_dict['state']
   flight_dict['region'] = uf_dict['region']
   flight_dict['city_name'] = uf_dict['city']
   return flight_dict
