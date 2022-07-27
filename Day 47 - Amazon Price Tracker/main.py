from email.header import Header
import requests
import lxml
from bs4 import BeautifulSoup
from os import environ
import dotenv
import smtplib

dotenv.load_dotenv()

# Set-up
## env Variables
USER_AGENT = environ["USER_AGENT"]
ACCEPT_LANGUAGE = environ["ACCEPT_LANGUAGE"]
SENDING_EMAIL = environ["SENDING_EMAIL"]
EMAIL_PW = environ["EMAIL_PW"]

HEADER = {
  "User-Agent": USER_AGENT,
  "Accept-Language": ACCEPT_LANGUAGE,
  }

URL_OF_PRODUCT_TO_TRACK = "https://www.amazon.com/Ninja-NJ601AMZ-Professional-1000-Watt-Dishwasher-Safe/dp/B098RD17LG/ref=sr_1_1?crid=3RFS5GQ4RYJ33&keywords=blender&qid=1658935474&sprefix=blen%2Caps%2C354&sr=8-1"

TARGET_PRICE = 100.0


# Webscrape for Price
response = requests.get(url= URL_OF_PRODUCT_TO_TRACK, headers=HEADER)

soup = BeautifulSoup(response.text, "lxml")

product_name = soup.select_one("#productTitle").getText()
price = soup.select_one("span[class~=a-offscreen]").getText()

price_as_float = float(price.strip("$"))
print(price_as_float)

# Check against Target Price, and send email

message = f"Subject: Price hit on {product_name} \n\n {product_name} has fallen below target price of ${TARGET_PRICE} and is now at ${price_as_float}"

if price_as_float < TARGET_PRICE:
  with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=SENDING_EMAIL, password=EMAIL_PW)
    connection.sendmail(from_addr=SENDING_EMAIL, 
						to_addrs=SENDING_EMAIL, 
						msg=message)