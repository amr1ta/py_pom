import unittest
from pages.page_factory import get_browser_context

class TestTemplate(unittest.TestCase):
    def setUp(self):
        context_driver = get_browser_context('chrome')
        self._driver = context_driver
        self._driver.open("https://en.wikipedia.org/wiki/Main_Page")

    def tearDown(self):
        self._driver.quit()
