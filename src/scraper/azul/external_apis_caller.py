from scraping_flight_data.src.scraper.seatguru import azul_capacity
from scraping_flight_data.src.util import (
    util_get_logger,
)

LOGGER = util_get_logger.get_logger(__name__)


def get_missing_data(flight_dict, capacity_dict, airport_dict):
    flight_dict["capacity"] = azul_capacity.get_capacity_for_model(
        flight_dict["airplane_model"], capacity_dict
    )
    flight_dict = get_uf_info(flight_dict, airport_dict)
    flight_dict["distance"] = airport_dict[flight_dict["airport_code"]]["distance"]
    flight_dict["yield_pax"] = flight_dict["price"] / flight_dict["distance"]
    duration_list = flight_dict["duration_str"].split("h")
    duration = int(duration_list[0]) * 60 + int(duration_list[1])
    flight_dict["duration"] = duration
    LOGGER.info(flight_dict)
    return flight_dict


def get_uf_info(flight_dict, airport_dict):
    uf_dict = airport_dict[flight_dict["airport_code"]]["uf_info"]
    flight_dict["state"] = uf_dict["state"]
    flight_dict["region"] = uf_dict["region"]
    flight_dict["city_name"] = uf_dict["city"]
    return flight_dict
