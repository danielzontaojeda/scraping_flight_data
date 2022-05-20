from selenium import webdriver
from fake_useragent import UserAgent


def set_browser_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    ua = UserAgent()

    # webdriver options to prevent automation detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")

    # Changes userAgent to prevent detection
    try:
        options.add_argument(f"user-agent={ua.random}")
    except IndexError:
        print("UserAgent error.")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    return options


def run_antidetection_script(driver: webdriver):

    # Sets navigator.webdriver to undefined to prevent detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

