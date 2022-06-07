from selenium import webdriver
from fake_useragent import UserAgent


def start_browser() -> webdriver:

    profile = webdriver.FirefoxProfile()
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    options.add_argument('--headless')
    options.accept_untrusted_certs = True
    browser = webdriver.Firefox(firefox_profile=profile,options=options)

    return browser


def set_firefox_options() -> webdriver.FirefoxProfile:
    options = webdriver.FirefoxOptions()
    options.accept_untrusted_certs = True
    options.add_argument('--headless')
    
    return options


def set_browser_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()

    # webdriver options to prevent automation detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    ua = UserAgent()

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

