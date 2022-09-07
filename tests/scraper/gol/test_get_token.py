from scraping_flight_data.src.scraper.gol import get_token


def test_get_token():
    assert get_token.get_token()
