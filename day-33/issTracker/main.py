import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 49 # Your latitude
MY_LONG = -123 # Your longitude
Offset = 100
MY_LAT_UPPER = MY_LAT + Offset
MY_LAT_LOWER = MY_LAT - Offset
MY_LONG_UPPER = MY_LONG + Offset
MY_LONG_LOWER = MY_LONG - Offset

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": 49,
    "lng": -123,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.utcnow()

noISS = True
while noISS == True:
    print("Trackinnngggg")
    time.sleep(60)
    if(time_now.hour < sunrise and time_now.hour > sunset):
        if(iss_latitude < (MY_LAT_UPPER) and iss_latitude > (MY_LAT_LOWER) and iss_longitude < (MY_LONG_UPPER) and iss_longitude > (MY_LONG_LOWER)):
            my_email = "noahspythonemail@gmail.com"
            my_password = "noahspythonemailpassword"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                  from_addr=my_email, 
                  to_addrs=my_email, 
                  msg=f"Subject:ISS ALERT!!!\n\nThe ISS is close")
                connection.close()
            noISS = False
    