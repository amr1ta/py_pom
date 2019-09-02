from pages.base_page import BasePage
from pages.locators import SearchPageLocators

class SearchPage(BasePage):

    def heading_text(self):
        return self.find_element(*SearchPageLocators.HEADING).text