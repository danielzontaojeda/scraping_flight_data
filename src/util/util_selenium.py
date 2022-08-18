import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium import webdriver

FIREFOX_BINARY_LOCATION = r"C:\Program Files\Mozilla Firefox\firefox.exe"


# def start_browser(url) -> webdriver:
#     options = webdriver.FirefoxOptions()
#     profile = webdriver.FirefoxProfile()
#     profile.set_preference("general.useragent.override", get_useragent())
#     capabilities = teste()
#     options.set_preference("dom.webnotifications.serviceworker.enabled", False)
#     options.set_preference("dom.webnotifications.enabled", False)
#     options.accept_untrusted_certs = True
#     options.binary_location = FIREFOX_BINARY_LOCATION
#     driver = webdriver.Firefox(options=options, capabilities=capabilities, firefox_profile=profile)
#     driver = webdriver.Firefox(options=options)
#     driver.get(url)
#     driver.delete_all_cookies()
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#     driver.execute_script("window.focus();")
#     driver.maximize_window()
#     return driver


def start_browser(url):
    options = uc.ChromeOptions()
    # options.add_argument(f"user-agent={get_useragent()}")
    # options.add_argument("user-data-dir=selenium")
    # options.add_argument("window-size=1920,1080")
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options)
    driver.get(url)
    return driver


def teste():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["acceptSslCerts"] = True
    return capabilities


def get_useragent():
    ua = UserAgent()
    user_agent = ua.chrome
    return user_agent


if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get("https://www.google.com/")
