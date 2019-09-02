from pages.base_page import BasePage

class SearchPage(BasePage):
    HEADING = 'firstHeading'

    def heading_text(self):
        return self._driver.find_element_by_id(SearchPage.HEADING).text