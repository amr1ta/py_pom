from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'

    def set_search_query(self, query):
        self._driver.find_element_by_id(HomePage.SEARCH_CONTAINER).send_keys(query)

    def search(self):
        self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).click()