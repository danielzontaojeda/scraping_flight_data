import time
from datetime import datetime

from scraping_flight_data.src.flight import airplane, airport, flight
from scraping_flight_data.src.scraper.gol import scraper
from scraping_flight_data.src.scraper.seatguru import gol_capacity
from scraping_flight_data.src.util import util_datetime, util_get_logger
from scraping_flight_data.src.scraper.gol import get_token

LOGGER = util_get_logger.get_logger(__name__)

def get_flights(list_dict_airport: list[dict], days: int) -> list[flight.Flight]:
    """Return list with flights from all airports in list_airport."""
    date = util_datetime.date_from_today(days)
    flight_list = []
    capacity_dict = gol_capacity.get_capacity_dict()
    token = get_token.get_token()
    LOGGER.info(f'token = {token}')
    for dict_airport in list_dict_airport:
        for airport in dict_airport.keys():
            data_json = scraper.get_flight_list(date, airport, token)
            itinerary = data_json["response"]["airSearchResults"]["brandedResults"][
                "itineraryPartBrands"
            ][0]
            flights_from_airport = get_flights_from_airport(
                itinerary, capacity_dict, dict_airport, airport
            )
            flight_list.extend(flights_from_airport)
            time.sleep(10)
    return flight_list


def get_flights_from_airport(
    itinerary: dict, capacity_dict: dict, dict_airport: dict, airport_code: str
) -> list[flight.Flight]:
    """Get flight information out of itinerary json."""
    flight_list = []
    for it in itinerary:
        offers = it["brandOffers"]
        airplane = get_airplane(it, capacity_dict)
        airport = get_airport(it, airport_code, dict_airport)
        flight = get_flight(airport, airplane, it, offers, dict_airport)
        LOGGER.info(f'created flight: {flight}')
        flight_list.append(flight)
    return flight_list


def get_airplane(itinerary: dict, capacity_dict: dict) -> airplane.Airplane:
    """Return Airplane object."""
    model = itinerary["itineraryPart"]["segments"][0]["equipment"]
    return airplane.Airplane(
        number=itinerary["itineraryPart"]["segments"][0]["flight"]["flightNumber"],
        company_code=itinerary["itineraryPart"]["segments"][0]["flight"]["airlineCode"],
        company_name="GOL",
        capacity=gol_capacity.get_capacity_for_model(model, capacity_dict),
        model=model,
    )


def get_airport(
    itinerary: dict, airport_code: str, dict_airport: dict
) -> airport.Airport:
    """Return Airport object."""
    code = itinerary["itineraryPart"]["segments"][0]["origin"]
    city_name = dict_airport[airport_code]["city_name"]
    city_info = dict_airport[airport_code]["uf_info"]
    return airport.Airport(
        code=code,
        city_name=city_info["city"],
        state_name=city_info["state"],
        region=city_info["region"],
    )


def get_flight(
    airport: airport.Airport,
    airplane: airplane.Airplane,
    itinerary: dict,
    offers: list,
    dict_airport: dict,
) -> flight.Flight:
    """Return flight object."""
    price = float(offers[0]["total"]["alternatives"][0][0]["amount"])
    distance = dict_airport[airport.code]["distance"]
    return flight.Flight(
        airplane=airplane,
        airport=airport,
        price=price,
        date_departure=datetime.fromisoformat(itinerary["departure"]).date(),
        time_departure=datetime.fromisoformat(itinerary["departure"]).time(),
        time_arrival=datetime.fromisoformat(itinerary["arrival"]).time(),
        stopover=itinerary["itineraryPart"]["stops"],
        stopover_list=get_stopover_list(itinerary),
        distance=distance,
        yield_pax=price / distance,
        duration=itinerary["duration"],
    )


def get_stopover_list(itinerary: dict) -> list:
    """Return list of flight stopovers."""
    segments = itinerary["itineraryPart"]["segments"]
    if itinerary["itineraryPart"]["stops"] == 0:
        return []
    return [
        segment["destination"]
        for segment in segments
        if segment["destination"] != "IGU"
    ]
