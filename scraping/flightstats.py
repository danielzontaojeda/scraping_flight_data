from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from scraping_flight_data.flight import Flight


# hour parameter can be 6, 12 or 18
def get_flightstats_url(date, hour):
    return f"https://www.flightstats.com/v2/flight-tracker/arrivals/IGU/" \
           f"?year={date.year}&month={date.month}&date={date.day}&hour={hour}"


def close_flightstats_privacy_message(driver):
    try:
        driver.implicitly_wait(4)
        accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
    except NoSuchElementException:
        print("close_flightstats_privacy_message couldn't find the element")


def get_flight_info(days, time):
    collection = []
    driver = webdriver.Chrome()

    # Dates for 1, 15 and 30 days from now
    date = datetime.now() + timedelta(days=days)

    driver.get(get_flightstats_url(date, time))

    # close_flightstats_privacy_message(driver)
    flight_list = driver.find_elements(By.CSS_SELECTOR, "a[class='table__A-sc-1x7nv9w-2 hnJChl']")

    for flights in flight_list:
        flight_string = flights.text.split("\n")
        flight_string.insert(0, str(date.strftime("%d/%m/%Y")))
        flight = Flight(flight_string)

        collection.append(flight)

    driver.close()
    return collection

