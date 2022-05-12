from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.flightstats.com/v2")

# waits for privacy window to appear
time.sleep(3)

# clicks I Accept
privacySettings = driver.find_element_by_id("onetrust-accept-btn-handler")
privacySettings.click()

#clicks Advanced Search
advancedSearch = driver.find_element_by_class_name("flight-tracker-adv-search-button")
advancedSearch.click()

#inserts IGU at Arrival Airport Field
arrivalAirport = driver.find_element_by_name("arrivalAirport")
arrivalAirport.send_keys("IGU")
time.sleep(1)
arrivalAirport.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
time.sleep(1)

#clicks search
search = driver.find_element_by_class_name("basic-button__Button-sc-3qdr1i-0 kmYwtt")
search.click()