import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping_flight_data.src.scraper.azul import external_apis_caller
from selenium.common.exceptions import TimeoutException


def get_flights_data(driver, airport, date, capacity_dict):
    time.sleep(10)
    flight_data = []
    try:
        elements = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, 'div[class*="flight-item"]')
            )
        )
    except TimeoutException:
        element = driver.find_element(By.CSS_SELECTOR, 'div[id="tbl-depart-flights"]')
        if "Desculpe" in element.text:
            return []
        else:
            raise TimeoutException
    # elements = driver.find_elements(By.CSS_SELECTOR, 'div[class*="flight-item"]')
    for element in elements:
        flight_dict = get_flight_dict(element, airport, date)
        if flight_dict:
            if flight_dict["stopover_num"] > 0:
                get_data_stopover_menu(flight_dict, element)
            else:
                get_data_airplane(flight_dict, element)
            flight_dict = external_apis_caller.get_missing_data(
                flight_dict, capacity_dict
            )
            flight_data.append(flight_dict)
    return flight_data


def get_data_airplane(flight_dict, element):
    details = scrape_data_stopover(element)
    pattern = r"\(.*?\sA?(\d+)\s?.*?\)"
    match = re.search(pattern, details[0].text)
    flight_dict["airplane_model"] = match.group(1)


def get_data_stopover_menu(flight_dict, element):
    details = scrape_data_stopover(element)
    get_data_details(flight_dict, details)
    return flight_dict


def scrape_data_stopover(element):
    button = WebDriverWait(element, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//div[@class='flight-segments']"))
    )
    button.click()
    details = WebDriverWait(element, 20).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='station']"))
    )
    return details


def get_data_details(flight_dict, details):
    """
    Get stopover info and airplane model from flight details page and
    adds into details_info dict.
    """
    # pattern = r'\(.*?((\d+)?\w+).*\).*\((.*)\)'
    pattern = r"^.*?\(.*?(\w+\s?\w+\s?\w+).*\).*\((.*)\).*$"
    stopover_list = []
    airplane_model = ""
    for detail in details:
        string = detail.text
        string = string.replace("\n", " ")
        print(string)
        match = re.search(pattern, string)
        if match.group(2) != "IGU":
            stopover_list.append(match.group(2))
        airplane_model = match.group(1)
    flight_dict["stopover_list"] = stopover_list
    flight_dict["airplane_model"] = airplane_model


def price_string_to_float(string):
    string = string.replace(".", "")
    string = string.replace(",", ".")
    return float(string)


def get_flight_dict(element, airport, date):
    string = element.text
    string = string.replace("\n", " ")
    match = get_data_from_element(string)
    if not match:
        # TODO: do logs.
        return None
    stopover_num = 0 if match.group(4) == "" else int(match.group(4))
    return {
        "number": int(match.group(1)),
        "departure_time_str": match.group(2),
        "arrival_time_str": match.group(3),
        "stopover_num": stopover_num,
        "duration_str": match.group(5),
        "price": price_string_to_float(match.group(6)),
        "airport_code": airport,
        "departure_date": date.strftime("%d-%m-%Y"),
    }


def get_data_from_element(string):
    """
    Return flight number, departure time, arrival time,
    number of stopover and flight price from string in match object.
    """
    pattern = r"(\d{4}).*?(\d{2}:\d{2}).*?(\d{2}:\d{2}).*?\d{4}\s(\d?).*?Duração:\s(\d{2}h\d{2}).*R\$\s?((\d?\.?\d{3}\,\d{2}))"
    return re.search(pattern, string)
