from scraping_flight_data.src.scraper.gol import scraper
from datetime import timedelta, date

def test_get_flight_list():
    date_search = date.today() + timedelta(days=15)
    assert scraper.get_flight_list(date_search, 'VCP')

