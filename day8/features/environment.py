from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


def before_all(context):
    browser = context.config.userdata['browser']
    if browser == "chrome":
        driver = BasePage(webdriver.Chrome(ChromeDriverManager().install()))
    context.driver = driver
    context.homepage_url = context.config.userdata['homepage_url']
    
def after_all(context):
    context.driver.quit()