from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=101174742&keywords=junior%20react%20developer&location=canada')
# jobList = driver.find_elements_by_css_selector(".jobs-search-results .jobs-search__results-list li")

signIn = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
signIn.click()
email = driver.find_element_by_id("username")
email.send_keys("")

password = driver.find_element_by_id("password")
password.send_keys("")
password.send_keys(Keys.ENTER)

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
applyButton = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
# for job in jobs:

  # applyButton.click()
webdriver.ActionChains(driver).move_to_element(applyButton)
