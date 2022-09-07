import time as t
import traceback
from datetime import datetime, time

from requests.exceptions import ConnectionError
from scraping_flight_data.src.file_manager import output_excel, add_prices
from scraping_flight_data.src.flight import airport, airplane, flight
from scraping_flight_data.src.scraper.azul import azul_price_page
from scraping_flight_data.src.scraper.azul.NoFlightException import NoFlightException
from scraping_flight_data.src.scraper.seatguru import azul_capacity
from scraping_flight_data.src.util import util_get_logger, util_datetime, util_selenium
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

AZUL_HOMEPAGE = "https://www.voeazul.com.br/"
SLEEP_TIME = 300
LOGGER = util_get_logger.get_logger(__name__)


def select_somente_ida(driver):
    """Select 'somente ida' in webpage."""
    driver.implicitly_wait(20)
    somente_ida = driver.find_elements(
        By.CSS_SELECTOR,
        "input[name='ControlGroupSearch$SearchMainSearchView$RadioButtonMarketStructure'",
    )
    button = somente_ida[1]
    driver.execute_script("arguments[0].click();", button)


def fill_fields(driver, airport, date):
    """Fill fields with flight information."""
    insert_departure_field(driver, airport)
    insert_origin_field(driver)
    insert_date_field(driver, date)


def insert_departure_field(driver, airport):
    """Fill departure field in azul homepage."""
    t.sleep(4)
    departure_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="field-5-origin1"]'))
    )
    departure_field.clear()
    if airport == "REC":
        airport = "RECI"
    departure_field.send_keys(airport, Keys.ENTER)


def insert_origin_field(driver):
    """Fill origin field in azul homepage."""
    arrival_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="field-6-destination1"]'))
    )
    arrival_field.clear()
    arrival_field.send_keys("IGU", Keys.ENTER)


def insert_date_field(driver, date):
    date_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="field-7-departure1"]'))
    )
    date_field.send_keys(date.strftime("%d/%m/%Y"), Keys.ENTER)


def click_search_button(driver):
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[id="searchTicketsButton"]')
        )
    )
    button.click()


def go_to_price_page(driver, airport, date):
    select_somente_ida(driver)
    fill_fields(driver, airport, date)
    click_search_button(driver)


def create_airport(flight_dict):
    return airport.Airport(
        code=flight_dict["airport_code"],
        city_name=flight_dict["city_name"],
        state_name=flight_dict["state"],
        region=flight_dict["region"],
    )


def create_airplane(flight_dict):
    return airplane.Airplane(
        number=flight_dict["number"],
        company_code="AD",
        company_name="Azul",
        capacity=flight_dict["capacity"],
        model=flight_dict["airplane_model"],
    )


def create_flight(flight_dict):
    airport = create_airport(flight_dict)
    airplane = create_airplane(flight_dict)
    time_d = flight_dict["departure_time_str"].split(":")
    time_a = flight_dict["arrival_time_str"].split(":")
    if "stopover_list" not in flight_dict:
        flight_dict["stopover_list"] = []
    return flight.Flight(
        airport=airport,
        airplane=airplane,
        price=flight_dict["price"],
        date_departure=datetime.strptime(
            flight_dict["departure_date"], "%d-%m-%Y"
        ).date(),
        time_departure=time(hour=int(time_d[0]), minute=int(time_d[1])),
        time_arrival=time(hour=int(time_a[0]), minute=int(time_a[1])),
        stopover=flight_dict["stopover_num"],
        stopover_list=flight_dict["stopover_list"],
        distance=flight_dict["distance"],
        yield_pax=flight_dict["yield_pax"],
        duration=flight_dict["duration"],
    )


def error_handler(error, airport, list_airport: list[str] = None, sleep=False):
    LOGGER.error(error)
    if "NoFlightException" in error:
        LOGGER.info(f"No flights for {airport}")
    else:
        list_airport.append(airport)
        LOGGER.info(f"appended {airport}")
    if sleep:
        t.sleep(SLEEP_TIME)


def get_flights(list_airport: list[str], days):
    date = util_datetime.date_from_today(days)
    capacity_dict = azul_capacity.get_capacity_dict()
    for airport in list_airport:
        LOGGER.info(f"---------------------{airport}-----------------------")
        flight_list = []
        try:
            driver = util_selenium.start_browser(AZUL_HOMEPAGE)
            go_to_price_page(driver, airport, date)
            flight_data = azul_price_page.get_flights_data(
                driver, airport, date, capacity_dict
            )
            if not flight_data:
                raise NoFlightException
            for flight_dict in flight_data:
                flight_list.append(create_flight(flight_dict))
                LOGGER.info(f'flight created: {flight_list[-1]}')
        except IndexError:
            # Sometimes mobile site is loaded. In that case we try again without waiting.
            error_handler(traceback.format_exc(), airport, list_airport, sleep=False)
            driver.close()
            continue
        except (ConnectionError, TimeoutException, NoSuchElementException):
            error_handler(traceback.format_exc(), airport, list_airport, sleep=True)
        except WebDriverException:
            error_handler(traceback.format_exc(), airport, list_airport, sleep=True)
            continue  # Can't close driver when WebDriverException occurs.
        except NoFlightException:
            error_handler(traceback.format_exc(), airport, sleep=True)
        driver.close()
        if days == 30:
            output_excel.write_file(flight_list)
        else:
            add_prices.insert_price(flight_list, days)
        t.sleep(SLEEP_TIME)


if __name__ == "__main__":
    print(get_flights(["ERM", "GRU"], 31))
    # get_flights(['GRU'])
    # get_flights(['CWB'])
    # get_flights(['GIG'])
