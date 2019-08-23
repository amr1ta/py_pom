from selenium import webdriver
from locators import Locators
from tests.TestBase import TestBase

class HomePage(TestBase):

    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def load_page(self):
        self.open_browser("https://www.skfbearingselect.com")


    def select_accept_continue (self):
        if self.driver.find_element(*Locators.BTN_ACCEPT).is_displayed():
            self.driver.find_element(*Locators.BTN_ACCEPT).click()

    def click_image(self,image_text):
        self.driver.find_element_by_text(image_text).click()

    def select_dropdown(self):
        self.driver.find_element(*Locators.SELECT_BEARING_TYPE).click()

    def options_displayed(self,option):
        opts_list = self.driver.find_elements(*Locators.OPTIONS_BEARING_TYPE)
        for opt in opts_list:
            if (opt.text == option):
                opt.click()


    def search_box(self,value):
        self.driver.find_element(*Locators.SEARCH_DESIGNATION).send_keys(value)





