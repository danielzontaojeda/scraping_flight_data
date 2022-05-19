import time

from scraping_flight_data.flight import Flight
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


def get_flight_indice(flight_list, flight:Flight):
    i = 0
    for f in flight_list:
        origin = f.text.split('\n')
        time_departure = origin[1].split('-')
        time_departure = time_departure[1].replace(' ','')
        if time_departure == flight.time_departure:
            return i
        else:
            i += 1
    return -1


# def string_to_float(string):
#     money = string.replace('.', '')
#     money = money.replace(',', '.')
#     money = money.replace('R', '')
#     money = money.replace('$', '')
#     money = money.replace(' ', '')
#     return money


def string_to_float(string):
    pattern = "[\d]+[\.]?[0-9]+[,]?[0-9]{2}"
    result = re.search(pattern, string).group().replace('.', '').replace(',', '.')
    return float(result)


def price_scraper(driver: webdriver, flight: Flight):
    flight_list = driver.find_elements(By.CSS_SELECTOR,
                                       "div[class='p-select-flight__accordion ng-tns-c148-0 ng-star-inserted']"
                                       )
    i = get_flight_indice(flight_list, flight)
    flight_data = flight_list[i].text.split('\n')
    price = string_to_float(flight_data[-1])
    return price


def get_flight_price(flight: Flight):
    driver = webdriver.Chrome()
    driver.maximize_window()
    date = flight.date.replace('/', '-')
    driver.get(f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br"
               f"&tipo=DF&de={flight.airport_code}&para=IGU&ida={date}&ADT=1&CHD=0&INF=0")
    time.sleep(10)
    price = price_scraper(driver, flight)
    flight.set_price(price)
