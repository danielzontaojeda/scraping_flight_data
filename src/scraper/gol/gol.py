import json
import requests
from bs4 import BeautifulSoup
from scraping_flight_data.src.util import util_datetime
from scraping_flight_data.src.scraper.gol import scraper
from datetime import datetime

def get_flights(list_airport):
    airport = list_airport[0]
    date = util_datetime.date_from_today(30)
    # date_str = datetime.strftime(date, "%d-%m-%Y")
    data_json = scraper.get_flight_list(date, airport)
    print(data_json['response']['airSearchResults']['brandedResults']['itineraryPartBrands'][0])
