from scraping_flight_data.flight import Flight
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scraping_flight_data.scraping.azul import azul_prices_page
import time


def insert_departure_field(driver, flight):
    time.sleep(.4)
    departure_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='origin1'")
    departure_field[1].clear()
    departure_field[1].send_keys(flight.airport_code, Keys.ENTER)


def insert_origin_field(driver):
    time.sleep(.4)
    arrival_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='destination1'")
    arrival_field[1].clear()
    arrival_field[1].send_keys('IGU', Keys.ENTER)


def insert_date_field(driver, flight):
    time.sleep(.4)
    date_field = driver.find_elements(By.CSS_SELECTOR, "input[id*='departure1'")
    date_field[1].send_keys(flight.date)


def go_to_price_page(driver, flight):

    # Selects 'somente ida' tab
    driver.implicitly_wait(5)
    somente_ida = driver.find_elements(By.CSS_SELECTOR,
                                       "input[name='ControlGroupSearch$SearchMainSearchView$RadioButtonMarketStructure'"
                                       )
    button = somente_ida[1]
    driver.execute_script("arguments[0].click();", button)

    # Insert fields
    insert_departure_field(driver, flight)
    insert_origin_field(driver)
    insert_date_field(driver, flight)
    time.sleep(.4)

    # Clicks search button
    driver.implicitly_wait(5)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[id='searchTicketsButton'")
    search_button.click()


def get_flight_price(flight: Flight):

    options = webdriver.ChromeOptions()
    # webdriver options to prevent automation detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.voeazul.com.br/")

    # Sets navigator.webdriver to undefined to prevent detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    print(driver.execute_script("return navigator.userAgent;"))

    go_to_price_page(driver, flight)
    azul_prices_page.set_price(driver, flight)


