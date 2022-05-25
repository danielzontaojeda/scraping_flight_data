import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from scraping_flight_data.util import data_util
from scraping_flight_data.flight import Flight
from selenium.webdriver.common.by import By
from selenium import webdriver


def close_cookies_window(driver: webdriver):
    """Close accept cookies window."""
    # driver.implicitly_wait(5)
    WebDriverWait(driver, 20).until(expected_conditions.
        element_to_be_clickable((
        By.CSS_SELECTOR, "button[id='cookies-politics-button']"))).click()
    # accept_button = driver.find_element(By.CSS_SELECTOR, "button[id='cookies-politics-button']")
    # accept_button.click()


def get_flight_index(flight_list, flight) -> int:
    for i, f in enumerate(flight_list):
        flight_details = f.text.split("\n")
        for detail in flight_details:
            if data_util.is_time(detail) and detail == flight.time_departure:
                return i
    return -1


def get_price(driver: webdriver, flight: Flight):
    flight_list = driver.find_elements(By.CSS_SELECTOR, "li[class='sc-dCVVYJ CEVgB'")
    index = get_flight_index(flight_list, flight)
    flight_price = flight_list[index].text.split("\n")
    flight_price = flight_price[-2]
    flight_price = data_util.string_to_float(flight_price)
    flight.set_price(flight_price)


def set_flight_price(flight: Flight):
    """Look up price flight and set it in flight object."""

    date_str = flight.date.split('/')
    flight_date = f"{date_str[2]}-{date_str[1]}-{date_str[0]}"
    driver = webdriver.Firefox()
    driver.get("https://www.latamairlines.com/br/pt/oferta-voos?"
               f"origin={flight.airport_code}&outbound={flight_date}T15%3A00%3A00.000Z&"
               "destination=IGU&inbound=null&adt=1&chd=0&inf=0&"
               "trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED")
    driver.maximize_window()
    time.sleep(30)
    close_cookies_window(driver)
    get_price(driver, flight)
    driver.close()
