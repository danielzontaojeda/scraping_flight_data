import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping_flight_data.flight import Flight
from scraping_flight_data.util import data_util


def get_flight_position(flight, flight_list) -> int:
    """Return flight position in flight_list."""
    for i, departure in enumerate(flight_list):
        if departure == flight.time_departure:
            return i
    return -1


def set_price(driver: webdriver, flight: Flight):
    """Set price in flight object."""
    time.sleep(10)
    dep_time = driver.find_elements(By.CSS_SELECTOR, "div[class='dep-time']")
    price = driver.find_elements(By.CSS_SELECTOR, "div[class='flight-price-container -azul'")
    i = get_flight_position(flight, dep_time)

    p = price[i].text.split("\n")
    p = data_util.string_to_float(p[0])

    Flight.set_price(flight, p)
