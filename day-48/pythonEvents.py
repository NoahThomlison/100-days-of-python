from selenium import webdriver

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
times = driver.find_elements_by_css_selector(".event-widget time")
events = driver.find_elements_by_css_selector(".event-widget .menu a")

eventsDict = {}
for n in range(len(times)):
  eventsDict[n] = {
    "name": events[n].text,
    "time": times[n].text
  }

print(eventsDict) 