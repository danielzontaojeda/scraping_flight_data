from scraping_flight_data.flight import Flight
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping_flight_data.util.data_util import string_to_float
import time


def get_flight_position(flight, flight_list) -> int:
    """Return flight position in flight_list."""
    i = 0
    while flight_list[i].text != flight.time_departure:
        i += 1
    return i


def set_price(driver: webdriver, flight: Flight):
    """Set price in flight object."""
    time.sleep(10)
    dep_time = driver.find_elements(By.CSS_SELECTOR, "div[class='dep-time']")
    price = driver.find_elements(By.CSS_SELECTOR, "div[class='flight-price-container -azul'")
    i = get_flight_position(flight, dep_time)

    p = price[i].text.split("\n")
    p = string_to_float(p[0])

    Flight.set_price(flight, p)
