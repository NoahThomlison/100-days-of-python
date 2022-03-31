import smtplib
import datetime as dt
import random

my_email = "noahspythonemail@gmail.com"
my_password = "noahspythonemailpassword"
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

with open("quotes.txt") as data:
  quotes = (data.read())
  quotesArray = quotes.split('\n')

now = dt.datetime.now()
day = now.weekday()
dayString = weekDays[day]

if dayString == "Wednesday":
  quote_to_send = (random.choice(quotesArray))
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
      from_addr=my_email, 
      to_addrs=my_email, 
      msg=f"Subject:Hello\n\n{quote_to_send}")
    connection.close()
