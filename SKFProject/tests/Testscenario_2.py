import unittest
from selenium import webdriver
from pages.HomePage import HomePage
from webdriver_manager.chrome import ChromeDriverManager
from locators import *
from selenium.webdriver.common.by import By
from tests.TestBase import TestBase



class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.skfbearingselect.com")

    def test_select_accept_continue(self):
        home = HomePage(self.driver)
        home.select_accept_continue()

    def test_click_image(self):
        home = HomePage(self.driver)
        home.click_image("Single bearing")

    def test_select_dropdown(self):
        home = HomePage(self.driver)
        home.select_dropdown()

    def test_options_displayed(self):
        home = HomePage(self.driver)
        home.options_displayed("Deep groove ball bearings")

    def test_search_box(self):
        home = HomePage(self.driver)
        home.search_box("6203")

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)







