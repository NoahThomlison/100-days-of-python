from asyncio.windows_events import NULL
import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

zillowLink = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.24777324251824%2C%22east%22%3A-122.60919292025261%2C%22south%22%3A49.07717526820971%2C%22north%22%3A49.4231936668977%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A118020%2C%22max%22%3A590099%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A500%2C%22max%22%3A2500%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

response = requests.get(zillowLink, headers=req_headers)
soup = BeautifulSoup(response.content, "html.parser")

listings = []


all_link_elements = soup.select(".list-card a")

dataCards = soup.find_all(class_="list-card-info")
all_price_elements = soup.select(".list-card-heading")

for i in range(8):
  listing = {
  "link": NULL,
  "price": NULL,
  "address": NULL
  }
  link = dataCards[i].find(class_='list-card-link', href=True)
  print(link)
  listing["link"] = link['href']
  listing["price"] = dataCards[i].find(class_='list-card-price').text
  listing["address"] = dataCards[i].find(class_='list-card-addr').text
  listings.append(listing)
  print(listing)
  time.sleep(.5)



chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(listings)):
    driver.get('https://docs.google.com/forms/d/1Jy8UoyIq_HUHvVh037U_6khlfMLGUNqfHk3mbC3MRLg/edit')

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    print(listings[n]['address'])
    print(listings[n]['price'])
    print(listings[n]['link'])

    address.send_keys(listings[n]['address'])
    price.send_keys(listings[n]["price"])
    link.send_keys(listings[n]["link"])
    submit_button.click()

