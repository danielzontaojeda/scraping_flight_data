from scraping_flight_data.src.scraper.latam import latam
from scraping_flight_data.src import airport_dict

def test_get_flights():
    d = airport_dict.get_airport_dict_list(['GRU'])
    assert latam.get_flights(d, 15)
