from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articleCount = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# articleCount.click()

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# searchGo = driver.find_element_by_id("searchButton").click()