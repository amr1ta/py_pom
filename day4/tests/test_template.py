import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self._driver = BasePage(webdriver.Chrome(
            ChromeDriverManager().install()))
        self._driver.open("https://en.wikipedia.org/wiki/Main_Page")

    def tearDown(self):
        self._driver.quit()
