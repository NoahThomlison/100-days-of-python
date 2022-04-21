from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
score = driver.find_element_by_id("cookies")

items = driver.find_elements_by_css_selector("#store div")


cursorUpgrade = driver.find_element_by_xpath('//*[@id="product0"]')
cursorPrice = driver.find_element_by_id("productPrice0").text

grandmaUpgrade = driver.find_element_by_xpath('//*[@id="product1"]')
grandmaPrice = driver.find_element_by_id('productPrice1').text

for i in range(10000):
  scoreNumber = (score.text.split(" "))
  scoreNumber = int(scoreNumber[0])
  if(scoreNumber > int(cursorPrice)):
    cursorUpgrade.click()
    cursorPrice = driver.find_element_by_id("productPrice0").text
  if(scoreNumber > int(grandmaPrice)):
    grandmaUpgrade.click()
    grandmaPrice = driver.find_element_by_id('productPrice1').text
  print(scoreNumber)
  cookie.click()

