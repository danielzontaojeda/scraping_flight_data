import time

from src.flight import airplane
from src.flight import airport, flight
from src.scraper.latam import scraper
from src.scraper.seatguru import latam_capacity
from src.util import util_distance
from src.util import util_ibge, util_datetime


def get_flights(list_airport) -> list:
    """Return list with flights from all airports in list_airport"""
    flight_list = []
    capacity_dict = latam_capacity.get_capacity_dict()
    for airport in list_airport:
        data_json = scraper.get_flight_list(util_datetime.date_from_today(30), airport)
        info_flights = get_flight_info(data_json)
        flight_list.extend(get_flight_list(info_flights, capacity_dict))
        time.sleep(0.5)
    return flight_list


def get_flight_list(info_flights, capacity_dict) -> list:
    """Return list with flights out of info_flights dict.

    capacity_dict has data about airplane capacity.
    It's passed as parameter so multiple api request aren't needed.
    """
    flight_list = []
    destination = ""
    distance = 0
    for i in range(info_flights["size"]):
        flight_airplane = get_airplane(info_flights["itinerary"][i][0], capacity_dict)
        flight_airport = get_airport(info_flights["summary"][i])
        if distance == 0:
            destination = flight_airport.city_name
            distance = util_distance.get_distance(destination)
        flight = get_flight(
            flight_airplane,
            flight_airport,
            info_flights["summary"][i],
            info_flights["itinerary"][i],
            distance,
        )
        flight_list.append(flight)
    return flight_list


def get_flight(airplane, airport, summary, itinerary, distance) -> flight.Flight:
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
        connections=get_connections(itinerary),
        distance=distance,
        yield_pax=price / distance,
        duration=summary["duration"],
    )


def get_connections(itinerary) -> list:
    """Return list with flight connections."""
    if len(itinerary) == 1:
        return None
    return [it["destination"] for it in itinerary if it["destination"] != "IGU"]


def get_airport(summary) -> airport.Airport:
    """Return airport object."""
    uf_info = util_ibge.get_uf_info(summary["origin"]["city"])
    return airport.Airport(
        code=summary["origin"]["iataCode"],
        city_name=summary["origin"]["city"],
        state_name=uf_info["state"],
        region=uf_info["region"],
    )


def get_airplane(itinerary, capacity_dict) -> airplane.Airplane:
    """Return airplane object."""
    model_airplane = itinerary["equipment"]
    return airplane.Airplane(
        number=itinerary["flight"]["flightNumber"],
        company_code=itinerary["flight"]["airlineCode"],
        company_name=itinerary["aircraftLeaseText"],
        capacity=latam_capacity.get_capacity_for_model(model_airplane, capacity_dict),
        model=model_airplane,
    )


def get_flight_info(data_json) -> dict:
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
