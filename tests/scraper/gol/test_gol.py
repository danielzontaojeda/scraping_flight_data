from scraping_flight_data.src.scraper.gol import gol
from scraping_flight_data.src.flight import flight
from scraping_flight_data.src import airport_dict

def test_get_flights():
    d = airport_dict.get_airport_dict_list(['GRU'])
    assert isinstance(gol.get_flights(d, 15), list)
