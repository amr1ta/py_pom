from pages.home_page import HomePage
from pages.search_page import SearchPage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Tests():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.maximize_window()

    def test_result_found(self, querystr):
        home_page = HomePage(self.driver)
        home_page.set_search_query(querystr)
        home_page.search()
        result = SearchPage(self.driver)
        return result.heading_text() == "Design pattern"

    def quit(self):
        self.driver.quit()

t1 = Tests()
print(t1.test_result_found("Design pattern"))
t1.quit()