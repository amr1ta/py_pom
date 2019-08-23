import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBase:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.driver_wait = WebDriverWait(self.driver, self.timeout)


    def open_browser(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def find_element(self, *locator):
        return self.driver_wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)





