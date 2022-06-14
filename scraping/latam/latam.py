import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime, timedelta
from scraping_flight_data.util import data_util
from scraping_flight_data.flight import Flight
from selenium.webdriver.common.by import By
from selenium import webdriver

from util import scraping_util

URL_LATAM = "https://www.latamairlines.com/br/pt"

def get_flight_price(flight: Flight, days:int):
    """Look up price flight and set it in flight object."""
    driver = scraping_util.start_browser(URL_LATAM)
    go_to_price_page(driver, flight, days)
    #if timeoutexception return 0.0 as price
    if close_cookies_window(driver):
        return 0.0
    price = get_price(driver, flight)
    driver.close()
    return price

def go_to_price_page(driver, flight, days):
    """Go to gol webpage that contains flight price."""
    date = datetime.strptime(flight.date, "%d/%m/%Y") + timedelta(days=days)
    date_str = datetime.strftime(date, "%Y-%m-%d")
    driver.get("https://www.latamairlines.com/br/pt/oferta-voos?"
               f"origin={flight.airport_code}&outbound={date_str}T15%3A00%3A00.000Z&"
               "destination=IGU&inbound=null&adt=1&chd=0&inf=0&"
               "trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED")
    time.sleep(30)


def close_cookies_window(driver: webdriver):
    """Close accept cookies window."""
    try:
        WebDriverWait(driver, 120).until(expected_conditions.
        element_to_be_clickable((
        By.CSS_SELECTOR, "button[id='cookies-politics-button']"))).click()
        return False
    except Exception:
        return True



def get_price(driver: webdriver, flight: Flight):
    """Set flight price."""
    flight_list = driver.find_elements(By.CSS_SELECTOR, "li[class='sc-dCVVYJ CEVgB'")
    index = get_flight_index(flight_list, flight)
    if index >= 0:
        flight_price = flight_list[index].text.split("\n")
        flight_price = flight_price[-2]
        flight_price = data_util.string_to_float(flight_price)
    else:
        flight_price = 0.0
    return flight_price


def get_flight_index(flight_list, flight) -> int:
    """Return flight position in flight_list.
    
       Return -1 if flight not found.
    """
    for i, f in enumerate(flight_list):
        flight_details = f.text.split("\n")
        for detail in flight_details:
            if data_util.is_time(detail) and detail == flight.time_departure:
                return i
    return -1

