import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
