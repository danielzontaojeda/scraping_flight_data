from scraping_flight_data.src.util import util_distance


def test_get_distance():
    assert util_distance.get_distance("Curitiba") > 0
    assert util_distance.get_distance("São Paulo") > 0
    assert util_distance.get_distance("Rio de Janeiro") > 0
    assert util_distance.get_distance("Salvador") > 0
    assert util_distance.get_distance("Manaus") > 0
