import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scraping_flight_data.flight import Flight
from scraping_flight_data.scraping.azul import azul_prices_page
from scraping_flight_data.util import scraping_util


def insert_departure_field(driver, flight):
    """Fill departure field in azul homepage."""
    time.sleep(.4)
    departure_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='origin1'")
    departure_field[1].clear()
    departure_field[1].send_keys(flight.airport_code, Keys.ENTER)


def insert_origin_field(driver):
    """Fill origin field in azul homepage."""
    time.sleep(.4)
    arrival_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='destination1'")
    arrival_field[1].clear()
    arrival_field[1].send_keys('IGU', Keys.ENTER)


def insert_date_field(driver, flight):
    """Fill date field in azul homepage."""
    time.sleep(.4)
    date_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='departure1'")
    date_field[1].send_keys(flight.date)


def set_currency_real(driver):
    """Set currency to real."""
    usd_button = driver.find_element(By.CSS_SELECTOR, "i[class='TCSS__icon TCSS__icon--usa'")
    usd_button.click()
    time.sleep(2)
    br_button = driver.find_element(By.CSS_SELECTOR, "i[class='TCSS__icon TCSS__icon--brazil'")
    br_button.click()


def fill_fields(driver, flight):
    """Fill fields with flight information."""
    insert_departure_field(driver, flight)
    time.sleep(5)
    insert_origin_field(driver)
    time.sleep(5)
    insert_date_field(driver, flight)
    time.sleep(5)
    time.sleep(.4)


def click_search_button(driver):
    """Click search button."""
    time.sleep(5)
    driver.implicitly_wait(5)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[id='searchTicketsButton'")
    search_button.click()


def select_somente_ida(driver):
    """Select 'somente ida' in webpage."""
    driver.implicitly_wait(5)
    somente_ida = driver.find_elements\
        (By.CSS_SELECTOR,
        "input[name='ControlGroupSearch$SearchMainSearchView$RadioButtonMarketStructure'"
        )
    button = somente_ida[1]
    driver.execute_script("arguments[0].click();", button)


def go_to_price_page(driver, flight):
    """Fill flight details in azul homepage and click in search.

        It's necessary to change currency use set_currency_real()
        if using vpn or proxy
    """
    select_somente_ida(driver)
    fill_fields(driver, flight)
    click_search_button(driver)


def set_flight_price(flight: Flight):
    """Look up price flight and set it in flight object."""

    driver = webdriver.Firefox()
    driver.get("https://www.voeazul.com.br/")
    driver.maximize_window()

    scraping_util.run_antidetection_script(driver)

    go_to_price_page(driver, flight)
    azul_prices_page.set_price1d(driver, flight)
    driver.close()

