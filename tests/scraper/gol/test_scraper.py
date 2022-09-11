from datetime import timedelta, date

from scraping_flight_data.src.scraper.gol import scraper, get_token


def test_get_flight_list():
    date_search = date.today() + timedelta(days=15)
    token = get_token.get_token()
    assert scraper.get_flight_list(date_search, "VCP", token)
