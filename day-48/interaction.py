from selenium import webdriver

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articleCount = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]').text
print(articleCount)