from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping_flight_data.flight import Flight
from scraping_flight_data.scraping.flightstats import flightstats_details_page
from scraping_flight_data.util import scraping_util


def get_flightstats_url(date, hour) -> str:
    """ Return url for a date and hour

        hour parameter can be 6, 12 or 18
    """
    return f"https://www.flightstats.com/v2/flight-tracker/arrivals/IGU/" \
           f"?year={date.year}&month={date.month}&date={date.day}&hour={hour}"


def get_flight_info(days, time) -> list[Flight]:
    """Return a collection with flights from day/time."""
    collection = []
    driver = webdriver.Chrome(options=scraping_util.set_browser_options())

    date = datetime.now() + timedelta(days=days)
    driver.get(get_flightstats_url(date, time))
    scraping_util.run_antidetection_script(driver)
    flight_list = driver.find_elements(By.CSS_SELECTOR, "a[class='table__A-sc-1x7nv9w-2 hnJChl']")

    for flights in flight_list:
        flight_string = flights.text.split("\n")
        flight_string.insert(0, str(date.strftime("%d/%m/%Y")))
        flight = Flight(flight_string)
        collection.append(flight)

    flightstats_details_page.get_flight_details(driver, collection)
    driver.close()
    return collection
