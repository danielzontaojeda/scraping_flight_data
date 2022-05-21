import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping_flight_data.flight import Flight
from scraping_flight_data.util import data_util
from scraping_flight_data.util import scraping_util


def get_flight_position(flight_list, flight: Flight) -> int:
    """Return the position the flight is in the flight_list."""
    i = 0
    for f in flight_list:
        origin = f.text.split('\n')
        time_departure = ''
        # time_departure = origin[1].split('-')
        # try:
        #     time_departure = time_departure[1].replace(' ', '')
        # # We get an index error when there is a promotion
        # except IndexError:
        # TODO: see if this works when there is no promotion
        for element in origin:
            if flight.airport_code in element:
                time_departure = element
                break
        time_departure = time_departure.split('-')
        time_departure = time_departure[1].replace(' ', '')

        if time_departure == flight.time_departure:
            return i
        else:
            i += 1
    return -1


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


def set_flight_price(flight: Flight):
    """Look up price flight and sets it in flight object."""
    driver = webdriver.Chrome(options=scraping_util.set_browser_options())
    driver.maximize_window()
    date = flight.date.replace('/', '-')
    driver.get(f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br"
               f"&tipo=DF&de={flight.airport_code}&para=IGU&ida={date}&ADT=1&CHD=0&INF=0")

    # Making sure site has enough time to load
    time.sleep(10)

    scraping_util.run_antidetection_script(driver)

    price = price_scraper(driver, flight)
    flight.set_price(price)
