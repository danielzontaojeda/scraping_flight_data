import json
import requests
from bs4 import BeautifulSoup
from scraping_flight_data.src.util import util_datetime
from scraping_flight_data.src.scraper.gol import scraper
from datetime import datetime
from scraping_flight_data.src.flight.airplane import Airplane
from scraping_flight_data.src.flight.airport import Airport
from scraping_flight_data.src.flight.flight import Flight
from scraping_flight_data.src.util import util_iatacode_lookup
from scraping_flight_data.src.util import util_ibge
from scraping_flight_data.src.util import util_distance


def get_airplane(itinerary):
    return Airplane(
        number=itinerary["itineraryPart"]["segments"][0]["flight"]["flightNumber"],
        company_code=itinerary["itineraryPart"]["segments"][0]["flight"]["airlineCode"],
        company_name="GOL",
        capacity=0,
        model=itinerary["itineraryPart"]["segments"][0]["equipment"],
    )


def get_airport(itinerary):
    code = itinerary["itineraryPart"]["segments"][0]["origin"]
    city_name = util_iatacode_lookup.get_city_by_iata(code)
    city_info = util_ibge.get_uf_info(city_name)
    return Airport(
        code=code,
        city_name=city_info["city"],
        state_name=city_info["state"],
        region=city_info["region"],
    )


def get_connections(itinerary):
    segments = itinerary["itineraryPart"]["segments"]
    if itinerary["itineraryPart"]["stops"] == 0:
        return []
    return [
        segment["destination"]
        for segment in segments
        if segment["destination"] != "IGU"
    ]


def get_flight(airport, airplane, itinerary, offers):
    price = float(offers[0]["total"]["alternatives"][0][0]["amount"])
    distance = util_distance.get_distance(airport.city_name)
    return Flight(
        airplane=airplane,
        airport=airport,
        price=price,
        date_departure=datetime.fromisoformat(itinerary["departure"]).date(),
        time_departure=datetime.fromisoformat(itinerary["departure"]).time(),
        time_arrival=datetime.fromisoformat(itinerary["arrival"]).time(),
        stopover=itinerary["itineraryPart"]["stops"],
        connections=get_connections(itinerary),
        distance=distance,
        yield_pax=price / distance,
        duration=itinerary["duration"],
    )


def get_flights_from_airport(itinerary):
    flight_list = []
    for it in itinerary:
        offers = it["brandOffers"]
        airplane = get_airplane(it)
        airport = get_airport(it)
        flight = get_flight(airport, airplane, it, offers)
        flight_list.append(flight)
    return flight_list


def get_flights(list_airport):
    date = util_datetime.date_from_today(30)
    flight_list = []
    for airport in list_airport:
        data_json = scraper.get_flight_list(date, airport)
        itinerary = data_json["response"]["airSearchResults"]["brandedResults"][
            "itineraryPartBrands"
        ][0]
        flights_from_airport = get_flights_from_airport(itinerary)
        flight_list.extend(flights_from_airport)
    return flight_list
