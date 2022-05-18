from scraping_flight_data.flight import Flight
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from re import sub
from decimal import Decimal


def get_flight_indice(flight, dep_time):
    i = 0
    while dep_time[i].text != flight.time_departure:
        i += 1
    return i


def string_to_float(string):
    money = string[0].replace('R', '')
    money = money.replace('.', '')
    money = money.replace(',', '.')
    value = Decimal(sub(r'[^\d.]', '', money))
    return value


def set_price(driver: webdriver, flight: Flight):

    time.sleep(10)
    dep_time = driver.find_elements(By.CSS_SELECTOR, "div[class='dep-time']")
    price = driver.find_elements(By.CSS_SELECTOR, "div[class='flight-price-container -azul'")
    i = get_flight_indice(flight, dep_time)

    p = price[i].text.split("\n")
    p = string_to_float(p)

    Flight.set_price(flight, p)
