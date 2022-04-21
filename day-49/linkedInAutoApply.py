from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=101174742&keywords=junior%20react%20developer&location=canada')

signIn = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
signIn.click()
email = driver.find_element_by_id("username")
email.send_keys("")

password = driver.find_element_by_id("password")
password.send_keys("")
password.send_keys(Keys.ENTER)

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

for i in range(len(jobs)):
  jobs[i].click()
  time.sleep(1)
  
  try:
    apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
    apply_button.click()
    time.sleep(1)

    submit_button = driver.find_element_by_css_selector("footer button")
    if submit_button.get_attribute("aria-label") == "Continue to next step":  
      time.sleep(1)
      driver.find_element_by_css_selector("[aria-label='Dismiss']").click()
      time.sleep(1)
      driver.find_element_by_css_selector("[data-control-name='discard_application_confirm_btn']").click()  
      print("Complex application, skipped.")
      continue
    else:
      submit_button.click()  
  except NoSuchElementException:
    print("No application button, skipped.")
    continue
