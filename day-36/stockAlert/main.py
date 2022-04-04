import requests
from pandas.tseries.offsets import BDay
from datetime import datetime
from time import sleep #ADDED
import smtplib
apiKey = "CWVX1U22Q7LG2FM5"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "symbol": STOCK_NAME,
    "apikey": apiKey,
    "function":"TIME_SERIES_DAILY"
}


response = requests.get(STOCK_ENDPOINT, params = parameters)
response.raise_for_status()
data = response.json()
today = datetime.today()
day = (f"{today:%d}")
lastBusDay = (today - BDay(2))
day = (f"{lastBusDay:%d}")
month = (f"{lastBusDay:%m}")
yesterdayDate = str(lastBusDay.year) + '-' + str(month) + '-' + str(day)
yesterdayClose = data["Time Series (Daily)"][yesterdayDate]["4. close"]
print(yesterdayClose)

twoDayCloseDate = str(lastBusDay.year) + '-' + str(month) + '-' +  str(int(day)-1)
twoDayClose = data["Time Series (Daily)"][twoDayCloseDate]["4. close"]
print(twoDayClose)

difference = abs(float(yesterdayClose) - float(twoDayClose))
print(difference)

percentDifference = abs(float(yesterdayClose)/float(twoDayClose))
print(percentDifference)

newsApiKey = "8e9013f685234a3db4c05d09bb99970c"
if(percentDifference > 0):
    news_params = {
        "apiKey": newsApiKey,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    topArtices = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: %\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in topArtices]
    formatted_articles = formatted_articles
    my_email = "noahspythonemail@gmail.com"
    my_password = "noahspythonemailpassword"
    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
              from_addr=my_email, 
              to_addrs=my_email, 
              msg=f"{article.encode('ascii', 'ignore')}")
            connection.close()


