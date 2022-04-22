from tkinter import Button
from turtle import up
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
twitterEmail = "noahspythonemail@gmail.com"
twitterPassword = "noahspythonemailpassword"
upSpeed = 7.5
downSpeed = 75

class InternetSpeedTwitterBot ():
  def __init__(self, driver, upSpeed, downSpeed) -> None:
    self.driver = driver
    self.up = 0
    self.down = 0
    

  def get_internet_speed(self):
    driver.get('https://www.speedtest.net/')
    button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    button.click()
    time.sleep(45)
    self.up = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    self.down = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    print(f'up: {self.up}, down: {self.down}')

    return(self.up, self.down)

  def tweet_at_provider(self):

    print("Test")



bot = InternetSpeedTwitterBot(driver, upSpeed, downSpeed)
# bot.get_internet_speed()
bot.tweet_at_provider()
    
    



# # front end, junior, canada remote jobs
# driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_T=9%2C25170%2C3172%2C25201&f_TPR=r2592000&geoId=101174742&keywords=frontend%20developer&location=Canada&sortBy=R')

# # driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=101174742&keywords=junior%20react%20developer&location=canada')

# signIn = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
# signIn.click()
# email = driver.find_element_by_id("username")
# email.send_keys("noahthomlison@gmail.com")

# password = driver.find_element_by_id("password")
# password.send_keys("noah1917")
# password.send_keys(Keys.ENTER)

# jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# for i in range(len(jobs)):
#   jobs[i].click()
#   time.sleep(1)
  
#   try:
#     driver.find_element_by_css_selector("[aria-label='Dismiss']")
#     apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#     apply_button.click()
#     time.sleep(1)

#     submit_button = driver.find_element_by_css_selector("footer button")
#     if submit_button.get_attribute("aria-label") == "Continue to next step":  
#       time.sleep(1)
#       submit_button.click() 
#       time.sleep(1)
#       submit_button.click() 
#       time.sleep(10)

#       driver.find_element_by_css_selector('[aria-label="Review your application"]').click()
#       time.sleep(1)

#       driver.find_element_by_css_selector('[aria-label="Submit application"]').click()
#       continue
#     else:
#       submit_button.click()  
#   except NoSuchElementException:
#     print("No application button, skipped.")
#     continue
