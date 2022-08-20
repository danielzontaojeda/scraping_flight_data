from scraping_flight_data.src.file_manager import input


def test_get_airport_list():
    assert input.get_airport_list()


def test_get_municipios_json():
    assert input.get_municipios_json()
