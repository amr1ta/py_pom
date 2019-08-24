from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


def get_browser_context(browser):
    if browser == "chrome":
        return BasePage(webdriver.Chrome(ChromeDriverManager().install()))
