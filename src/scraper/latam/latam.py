import time

from scraping_flight_data.src.util import util_get_logger
from src.flight import airplane, airport, flight
from src.scraper.latam import scraper
from src.scraper.seatguru import latam_capacity
from src.util import util_datetime

LOGGER = util_get_logger.get_logger(__name__)

def get_flights(list_dict_airport: list[dict], days: int) -> list:
    """Return list with flights from all airports in list_airport"""
    flight_list = []
    capacity_dict = latam_capacity.get_capacity_dict()
    for dict_airport in list_dict_airport:
        for airport in dict_airport.keys():
            airport_info = dict_airport[airport]
            data_json = scraper.get_flight_list(
                util_datetime.date_from_today(days), airport
            )
            info_flights = get_flight_info(data_json)
            flight_list.extend(
                get_flight_list(info_flights, capacity_dict, airport_info)
            )
            time.sleep(10)
    return flight_list


def get_flight_list(
    info_flights: dict, capacity_dict: dict, airport_info: dict
) -> list:
    """Return list with flights out of info_flights dict."""
    flight_list = []
    destination = ""
    distance = 0
    for i in range(info_flights["size"]):
        flight_airplane = get_airplane(info_flights["itinerary"][i][0], capacity_dict)
        flight_airport = get_airport(info_flights["summary"][i], airport_info)
        if distance == 0:
            destination = flight_airport.city_name
            distance = airport_info["distance"]
        flight = get_flight(
            flight_airplane,
            flight_airport,
            info_flights["summary"][i],
            info_flights["itinerary"][i],
            distance,
        )
        LOGGER.info(f'created flight: {flight}')
        flight_list.append(flight)
    return flight_list


def get_flight(
    airplane: airplane.Airplane,
    airport: airport.Airport,
    summary: dict,
    itinerary: dict,
    distance: int,
) -> flight.Flight:
    """Return flight object."""
    price = summary["lowestPrice"]["amount"]
    return flight.Flight(
        airplane=airplane,
        airport=airport,
        price=price,
        date_departure=util_datetime.get_date_from_isoformat(
            summary["origin"]["departure"]
        ),
        time_departure=util_datetime.get_time_from_isoformat(
            summary["origin"]["departure"]
        ),
        time_arrival=util_datetime.get_time_from_isoformat(
            summary["destination"]["arrival"]
        ),
        stopover=summary["stopOvers"],
        stopover_list=get_connections(itinerary),
        distance=distance,
        yield_pax=price / distance,
        duration=summary["duration"],
    )


def get_connections(itinerary: dict) -> list:
    """Return list with flight connections."""
    if len(itinerary) == 1:
        return None
    return [it["destination"] for it in itinerary if it["destination"] != "IGU"]


def get_airport(summary: dict, airport_info: dict) -> airport.Airport:
    """Return airport object."""
    uf_info = airport_info["uf_info"]
    return airport.Airport(
        code=summary["origin"]["iataCode"],
        city_name=uf_info["city"],
        state_name=uf_info["state"],
        region=uf_info["region"],
    )


def get_airplane(itinerary: dict, capacity_dict: dict) -> airplane.Airplane:
    """Return airplane object."""
    model_airplane = itinerary["equipment"]
    return airplane.Airplane(
        number=itinerary["flight"]["flightNumber"],
        company_code=itinerary["flight"]["airlineCode"],
        company_name=itinerary["aircraftLeaseText"],
        capacity=latam_capacity.get_capacity_for_model(model_airplane, capacity_dict),
        model=model_airplane,
    )


def get_flight_info(data_json: list) -> dict:
    """Return dict with data parsed from data_json."""
    summary_list = []
    itinerary_list = []
    for data in data_json:
        summary = data["summary"]
        summary_list.append(summary)
        itinerary = data["itinerary"]
        itinerary_list.append(itinerary)
    return {
        "summary": summary_list,
        "itinerary": itinerary_list,
        "size": len(summary_list),
    }
