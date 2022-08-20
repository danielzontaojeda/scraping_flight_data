from src import airport_dict


def test_get_airport_dict_list():
    assert airport_dict.get_airport_dict_list(['GRU', 'GIG', 'VCP'])
