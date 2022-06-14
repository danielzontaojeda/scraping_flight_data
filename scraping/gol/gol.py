import time
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from scraping_flight_data.flight import Flight
from scraping_flight_data.util import data_util
from scraping_flight_data.util import scraping_util

URL_GOL = "https://www.voegol.com.br"


def get_flight_price(flight: Flight, days: int):
    """Look up price flight and sets it in flight object."""
    driver = scraping_util.start_browser(URL_GOL)
    go_to_price_page(driver, flight, days)
    price = price_scraper(driver, flight)
    driver.close()
    return price


def go_to_price_page(driver, flight, days):
    """Go to latam webpage that contains flight price"""
    date = datetime.strptime(flight.date, "%d/%m/%Y") + timedelta(days=days)
    date_str = datetime.strftime(date, "%d-%m-%Y")
    driver.get(f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br"
               f"&tipo=DF&de={flight.airport_code}&para=IGU&ida={date_str}&ADT=1&CHD=0&INF=0")
    # Making sure site has enough time to load
    time.sleep(10)


def price_scraper(driver: webdriver, flight: Flight) -> float:
    """Return str with flight price."""
    flight_list = driver.find_elements(By.CSS_SELECTOR,
                                       "div[class='p-select-flight__accordion ng-tns-c148-0 ng-star-inserted']"
                                       )
    i = get_flight_position(flight_list, flight)
    if i >= 0:
        flight_data = flight_list[i].text.split('\n')
        price = data_util.string_to_float(flight_data[-1])
        return price
    else:
        return 0.0


def get_flight_position(flight_list, flight: Flight) -> int:
    """Return the position the flight is in the flight_list."""
    i = 0
    for i, f in enumerate(flight_list):
        origin = f.text.split('\n')
        time_departure = ''
        for element in origin:
            if flight.airport_code in element:
                time_departure = element
                break
        time_departure = time_departure.split('-')
        time_departure = time_departure[1].replace(' ', '')

        if time_departure == flight.time_departure:
            return i
    return -1

