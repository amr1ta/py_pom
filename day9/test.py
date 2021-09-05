import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver_init(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    url = pytestconfig.getoption("url")
    option = pytestconfig.getoption("option")
    if browser == "chrome":
        if option == "headless":
            options = Options()
            options.headless = True
            driver = BasePage(webdriver.Chrome(ChromeDriverManager().install(), options=options))
        else:
            driver = BasePage(webdriver.Chrome(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.load_url(url)
    yield
    driver.quit()
    

@pytest.mark.usefixtures("driver_init")
class Test_Pages:
    def test_result_found(self):
        home_page = HomePage(self.driver)
        home_page.set_search_query("Design pattern")
        home_page.search()
        result = SearchPage(self.driver)
        assert result.heading_text() == "Design pattern"
