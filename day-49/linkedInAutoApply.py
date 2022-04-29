from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
linkedInPassword = ""
linkedInEmail = "@gmail.com"

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

jobType = int(input("What job would you like to apply for? Front end (1), full stack (2), or react (3) "))
answer = input("Would you like to only apply to quick apply jobs? (y/n) ")

if(jobType == 1):
  # front end, junior, canada remote jobs
  driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_JT=F&f_T=9%2C3172%2C25170%2C25201&f_TPR=r2592000&f_WT=2&geoId=101174742&keywords=frontend%20developer&  location=Canada&sortBy=R')

elif(jobType == 2):
  # # full stack, junior, canada remote jobs
  driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_T=9%2C25170%2C3172%2C25201&f_TPR=r2592000&f_WT=2&geoId=101174742&keywords=full%20stack%20developer& location=Canada&sortBy=R')

elif(jobType == 3):
  # # react, junior, canada remote jobs
  driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_T=9%2C25170%2C3172%2C25201&f_TPR=r2592000&f_WT=2&geoId=101174742&keywords=react%20developer&  location=Canada&sortBy=R')

if(answer == "y"):
  quickApplyOnly = True
else:
  quickApplyOnly = False

signIn = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
signIn.click()
email = driver.find_element(By.ID, "username")
email.send_keys(linkedInEmail)

password = driver.find_element(By.ID, "password")
password.send_keys(linkedInPassword)
password.send_keys(Keys.ENTER)
time.sleep(3)

jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
# try:
#   pages = driver.find_elements(By.CSS_SELECTOR, '.artdeco-pagination__pages li')
# except NoSuchElementException:
#   print("no pages")
#   pages = driver.find_element(By.CSS_SELECTOR, '.artdeco-pagination__pages li')

print(f'Quick Apply Only: {quickApplyOnly}')
# for page in pages:
print(len(jobs))
for i in range(len(jobs)):
  jobs[i].click()
  time.sleep(1)
  try:
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Dismiss']")
    apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
    apply_button.click()
    time.sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
    if submit_button.get_attribute("aria-label") == "Continue to next step":  
      if quickApplyOnly:
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[aria-label='Dismiss']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[data-control-name='discard_application_confirm_btn']").click()  
        print("Complex application, skipped.")
        continue
      else:
        print("Complex Application you have 30 seconds to complete it")
        time.sleep(30)
    else:
      print("Applied")
      submit_button.click()  
      driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="post-apply-modal"] button').click()
  except NoSuchElementException:
    print("No application button, skipped.")
    continue
  # page.click()

