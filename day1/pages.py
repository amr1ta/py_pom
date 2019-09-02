class BasePage():
    def __init__(self, driver):
        self._driver = driver

class HomePage(BasePage):
    # locators
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'

    def set_search_query(self, query):
        self._driver.find_element_by_id(HomePage.SEARCH_CONTAINER).send_keys(query)

    def search(self):
        self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).click()

class SearchPage(BasePage):
    # locators
    HEADING = 'firstHeading'

    def heading_text(self):
        return self._driver.find_element_by_id(SearchPage.HEADING).text