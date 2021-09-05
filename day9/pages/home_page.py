from pages.base_page import BasePage
from pages.locators import HomePageLocators

class HomePage(BasePage):

    def set_search_query(self, query):
        self.find_element(*HomePageLocators.SEARCH_CONTAINER).send_keys(query)

    def search(self):
        self.find_element(*HomePageLocators.SEARCH_BUTTON).click()

