import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping_flight_data.flight import Flight
from scraping_flight_data.util.data_util import string_to_float
from scraping_flight_data.util.scraping_util import set_browser_options, run_antidetection_script


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


def price_scraper(driver: webdriver, flight: Flight):
    flight_list = driver.find_elements(By.CSS_SELECTOR,
                                       "div[class='p-select-flight__accordion ng-tns-c148-0 ng-star-inserted']"
                                       )
    i = get_flight_indice(flight_list, flight)
    flight_data = flight_list[i].text.split('\n')
    price = string_to_float(flight_data[-1])
    return price


def get_flight_price(flight: Flight):
    driver = webdriver.Chrome(options=set_browser_options())
    driver.maximize_window()
    date = flight.date.replace('/', '-')
    driver.get(f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br"
               f"&tipo=DF&de={flight.airport_code}&para=IGU&ida={date}&ADT=1&CHD=0&INF=0")

    # Making sure site has enough time to load
    time.sleep(3)

    run_antidetection_script(driver)

    price = price_scraper(driver, flight)
    flight.set_price(price)
