import pytest
from scraping_flight_data.src.flight import flight
from scraping_flight_data.tests.flight import create_dummy_flight


class TestFlight:
    @pytest.fixture()
    def create_direct_flight(self):
        return create_dummy_flight.get_dummy_flight_no_connections()

    @pytest.fixture()
    def create_connections_flight(self):
        return create_dummy_flight.get_dummy_flight_with_connections()

    def test_get_stopover_str(self, create_direct_flight, create_connections_flight):
        assert isinstance(create_connections_flight, flight.Flight)
        assert isinstance(create_direct_flight, flight.Flight)
        assert create_direct_flight.get_stopover_str() == "Direto"
        assert create_connections_flight.get_stopover_str() == "Conexão"

    def test_format_stopover_string(
        self, create_direct_flight, create_connections_flight
    ):
        assert isinstance(create_connections_flight, flight.Flight)
        assert isinstance(create_direct_flight, flight.Flight)
        assert create_direct_flight.format_stopover_string() == ""
        assert create_connections_flight.format_stopover_string() == "GIG, VCP"
