from selenium.webdriver.common.by import By

class HomePageLocators():
    SEARCH_CONTAINER = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.ID, "searchButton")

class SearchPageLocators():
    HEADING = (By.ID, "firstHeading")
