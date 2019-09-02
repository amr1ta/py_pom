from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
driver.find_element_by_id("searchInput").send_keys("Design pattern")
driver.find_element_by_id("searchButton").click()
print(driver.find_element_by_id("firstHeading").text == "Design pattern")
driver.quit()