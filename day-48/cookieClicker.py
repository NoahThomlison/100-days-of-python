from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
score = driver.find_element_by_id("cookies")
cursorUpgrade = driver.find_element_by_xpath('//*[@id="product0"]')
grandmaUpgrade = driver.find_element_by_xpath('//*[@id="product1"]')
# farmUpgrade = driver.find_element_by_xpath('//*[@id="product2"]')
# mineUpgrade = driver.find_element_by_xpath('//*[@id="product3"]')
# upgrade1 = driver.find_element_by_xpath('//*[@id="upgrade0"]')
# upgrade2 = driver.find_element_by_xpath('//*[@id="upgrade1"]')
# upgrade3 = driver.find_element_by_xpath('//*[@id="upgrade2"]')
# upgrade4 = driver.find_element_by_xpath('//*[@id="upgrade3"]')
# upgrade5 = driver.find_element_by_xpath('//*[@id="upgrade4"]')

for i in range(10000):
  scoreNumber = (score.text.split(" "))
  # upgrade1.click()
  # upgrade2.click()
  # upgrade3.click()
  # upgrade4.click()
  # upgrade5.click()
  cursorUpgrade.click()
  grandmaUpgrade.click()
  # farmUpgrade.click()
  # mineUpgrade.click()

  # if(scoreNumber[0] > 15)
  # if int(score.text) > 15:
  #   cursorUpgrade.click()
  cookie.click()

