from selenium import webdriver
from selenium.webdriver.common.by import By


def get_flight_details(driver:webdriver, collection):
    for flight in collection:
        date = flight.date.split("/")
        driver.get(f"https://www.flightstats.com/v2/flight-tracker/{flight.airplane.company}/"
                   f"{flight.airplane.airplane_number}?year={date[2]}&month={date[1]}&date={date[0]}")
        details = driver.find_elements(By.CSS_SELECTOR, "h5[class*='exDPyn'")
        flight.set_airplane_model(details[-1].text)

