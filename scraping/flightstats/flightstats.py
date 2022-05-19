from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from scraping_flight_data.flight import Flight
from scraping_flight_data.scraping.flightstats.flightstats_details_page import get_flight_details
from scraping_flight_data.util.scraping_util import set_browser_options, run_antidetection_script


# hour parameter can be 6, 12 or 18
def get_flightstats_url(date, hour):
    return f"https://www.flightstats.com/v2/flight-tracker/arrivals/IGU/" \
           f"?year={date.year}&month={date.month}&date={date.day}&hour={hour}"


# Returns a collections with flights
def get_flight_info(days, time):
    collection = []
    driver = webdriver.Chrome(options=set_browser_options())

    # Dates for 1, 15 and 30 days from now
    date = datetime.now() + timedelta(days=days)

    driver.get(get_flightstats_url(date, time))

    run_antidetection_script(driver)

    flight_list = driver.find_elements(By.CSS_SELECTOR, "a[class='table__A-sc-1x7nv9w-2 hnJChl']")

    for flights in flight_list:
        flight_string = flights.text.split("\n")
        flight_string.insert(0, str(date.strftime("%d/%m/%Y")))
        flight = Flight(flight_string)
        collection.append(flight)

    get_flight_details(driver, collection)
    driver.close()
    return collection

