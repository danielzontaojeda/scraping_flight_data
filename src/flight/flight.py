from dataclasses import dataclass
from datetime import date, time

from src.flight.airplane import Airplane
from src.flight.airport import Airport
from src.util import util_datetime


@dataclass
class Flight:
    airplane: Airplane
    airport: Airport
    price: float
    date_departure: date
    time_departure: time
    time_arrival: time
    stopover: int
    stopover_list: list[str]
    distance: float
    yield_pax: float
    duration: int

    def get_stopover_str(self) -> str:
        if self.stopover > 0:
            return "Conexão"
        else:
            return "Direto"

    def format_stopover_string(self) -> str:
        """
        Append all airport iata code from stopover_list to
        a string
        """
        if self.stopover_list is None:
            return ""
        string = ""
        for connection in self.stopover_list:
            string += f"{connection}, "
        return string[:-2]

    def get_list(self) -> list:
        return [
            self.airport.region,
            self.airport.state_name,
            self.airport.city_name,
            self.airport.code,
            self.date_departure,
            util_datetime.get_month_portuguese(self.date_departure.month),
            self.date_departure.year,
            self.airplane.number,
            self.airplane.model,
            self.airplane.company_name,
            self.airplane.capacity,
            self.time_departure,
            self.time_arrival,
            self.get_stopover_str(),
            self.format_stopover_string(),
            self.distance,
            f"{self.price:.2f}",
            0.0,
            0.0,
            f"{self.price:.2f}",
            f"{self.yield_pax:.2f}",
        ]
