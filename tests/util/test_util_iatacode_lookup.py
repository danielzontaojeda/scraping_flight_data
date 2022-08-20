from scraping_flight_data.src.util import util_iatacode_lookup

def test_get_city_by_iata():
    assert util_iatacode_lookup.get_city_by_iata('CWB').lower() == 'curitiba'
    assert util_iatacode_lookup.get_city_by_iata('GIG').lower() == 'rio de janeiro'
    assert util_iatacode_lookup.get_city_by_iata('FLN').lower() == 'florianopolis'
    assert util_iatacode_lookup.get_city_by_iata('CGR').lower() == 'campo grande'
    assert util_iatacode_lookup.get_city_by_iata('PMW').lower() == 'palmas'
