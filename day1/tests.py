from pages import HomePage
from pages import SearchPage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

home_page = HomePage(driver)
home_page.set_search_query("Design pattern")
home_page.search()
result = SearchPage(driver)
print(result.heading_text() == "Design pattern")

driver.quit()
