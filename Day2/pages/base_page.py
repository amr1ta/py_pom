# Base Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self._driver = driver
        self._timeout = 10
        self._driver_wait = WebDriverWait(self._driver, self._timeout)

    # Add Explicit Wait to find_element API
    def find_element(self, *locator):
        return self._driver_wait.until(EC.visibility_of_element_located(locator))