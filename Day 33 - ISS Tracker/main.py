import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    (my_lat_lower, my_lat_higher) = (MY_LAT - 5, MY_LAT + 5)
    (my_lng_lower, my_lng_higher) = (MY_LONG - 5, MY_LONG + 5)
    return (my_lat_lower < iss_latitude < my_lat_higher) and (my_lng_lower < iss_longitude < my_lng_higher)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_dark():
    return (sunset <= time_now.hour) or (time_now.hour <= sunrise)


# def sendemail():
#     with smtplib.SMTP("smtp") as connection:
#         connection.starttls()
#         connection.login(user="user", password="password")
#         connection.sendmail(from_addr="email", to_addrs="recipient", msg="Subject: ISS Overhead\n\nISS Overhead!")

#If the ISS is close to my current position

while True:
    if is_iss_overhead():
        if is_dark():
            # sendemail()
            print(f"ISS Overhead at {iss_latitude},{iss_longitude}")

    else:
        print(f"ISS Not Overhead at {iss_latitude},{iss_longitude}")
        if is_dark():
            print(f"It is now Dark, between sunset and sunrise at {time_now.hour}hrs")
        else:
            print(f"It is now Bright, between sunrise and sunset at {time_now.hour}hrs")

    time.sleep(60)


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



