from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element_by_name("fName")
firstName.send_keys("Noah")
lastName = driver.find_element_by_name("lName")
lastName.send_keys("Thomlison")
emailAddress = driver.find_element_by_name("email")
emailAddress.send_keys("noahthomlison@gmail.com")

driver.find_element_by_xpath('/html/body/form/button').click()
