import traceback
from datetime import datetime, time
import time as t

from scraping_flight_data.src.flight import airport, airplane, flight
from scraping_flight_data.src.scraper.azul import azul_price_page
from scraping_flight_data.src.scraper.seatguru import azul_capacity
from scraping_flight_data.src.util import util_datetime, util_selenium
from scraping_flight_data.src.file_manager import output_excel
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from requests.exceptions import ConnectionError

AZUL_HOMEPAGE = "https://www.voeazul.com.br/"


def select_somente_ida(driver):
    """Select 'somente ida' in webpage."""
    driver.implicitly_wait(20)
    somente_ida = driver.find_elements\
        (By.CSS_SELECTOR,
        "input[name='ControlGroupSearch$SearchMainSearchView$RadioButtonMarketStructure'"
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
    if airport == 'REC':
        airport = 'RECI'
    departure_field.send_keys(airport, Keys.ENTER)


def insert_origin_field(driver):
    """Fill origin field in azul homepage."""
    arrival_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="field-6-destination1"]'))
    )
    arrival_field.clear()
    arrival_field.send_keys('IGU', Keys.ENTER)


def insert_date_field(driver, date):
    date_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="field-7-departure1"]'))
    )
    date_field.send_keys(date.strftime("%d/%m/%Y"), Keys.ENTER)


def click_search_button(driver):
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="searchTicketsButton"]'))
    )
    button.click()


def go_to_price_page(driver, airport, date):
    select_somente_ida(driver)
    fill_fields(driver, airport, date)
    click_search_button(driver)


def create_airport(flight_dict):
    return airport.Airport(
        code= flight_dict['airport_code'],
        city_name= flight_dict['city_name'],
        state_name= flight_dict['state'],
        region= flight_dict['region'],
    )


def create_airplane(flight_dict):
    return airplane.Airplane(
        number= flight_dict['number'],
        company_code= 'AD',
        company_name= 'Azul',
        capacity= flight_dict['capacity'],
        model= flight_dict['airplane_model'],
    )


def create_flight(flight_dict):
    airport = create_airport(flight_dict)
    airplane = create_airplane(flight_dict)
    time_d = flight_dict['departure_time_str'].split(':')
    time_a = flight_dict['arrival_time_str'].split(':')
    if 'stopover_list' not in flight_dict:
        flight_dict['stopover_list'] = []
    return flight.Flight(
        airport= airport,
        airplane= airplane,
        price= flight_dict['price'],
        date_departure= datetime.strptime(flight_dict['departure_date'], "%d-%m-%Y").date(),
        time_departure= time(hour=int(time_d[0]), minute=int(time_d[1])),
        time_arrival=time(hour=int(time_a[0]), minute=int(time_a[1])),
        stopover= flight_dict['stopover_num'],
        stopover_list= flight_dict['stopover_list'],
        distance= flight_dict['distance'],
        yield_pax= flight_dict['yield_pax'],
        duration= flight_dict['duration'],
    )


def get_flights(list_airport):
    date = util_datetime.date_from_today(30)
    capacity_dict = azul_capacity.get_capacity_dict()
    for airport in list_airport:
        print(f'---------------------{airport}-----------------------')
        flight_list = []
        retry = False
        try:
            driver = util_selenium.start_browser(AZUL_HOMEPAGE)
            driver.set_page_load_timeout(10)
            go_to_price_page(driver, airport, date)
            flight_data = azul_price_page.get_flights_data(driver, airport, date, capacity_dict)
            #TODO create custom exception
            if not flight_data: raise EOFError
            for flight_dict in flight_data:
                flight_list.append(create_flight(flight_dict))
        except (IndexError):
            retry = True
            print(traceback.format_exc())
            print(datetime.now())
            print(f"appended {airport}")
            list_airport.append(airport)
        except (ConnectionError, TimeoutException, NoSuchElementException, WebDriverException):
            print(traceback.format_exc())
            print(f"appended {airport}, connection error")
            list_airport.append(airport)
            t.sleep(300)
        except EOFError:
            print(traceback.format_exc())
            print(f'No flights for {airport}')
            t.sleep(300)
        driver.close()
        if not retry:
            output_excel.write_file(flight_list)
            t.sleep(300)


if __name__ == '__main__':
    print(get_flights(['VCP']))
    # get_flights(['GRU'])
    # get_flights(['CWB'])
    # get_flights(['GIG'])

