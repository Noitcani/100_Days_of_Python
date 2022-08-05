from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Import twitter creds from .env
load_dotenv()
TWITTER_USER = environ["TWITTER_USER"]
TWITTER_PW = environ["TWITTER_PW"]

# Globals
TARGET_SPEED_DOWNLOAD = 500.0
TARGET_SPEED_UPLOAD = 500.0
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"

class InternetSpeedTwitterBot():
  def get_internet_speed(self):
    print("Getting Internet Speed...")
    # Start Driver
    driver.get(SPEED_TEST_URL)
    print("Navigating to Speed Test Site...")
    sleep(1)

    # Start test
    start_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="start speed test - connection type multi"]')
    start_button.click()
    print("Starting Speed Test...")
    test_start_time = time.time()
    previous_second = 0
    while True:
      test_elapsed_time = time.time() - test_start_time
      rounded_test_elapsed_time = int(test_elapsed_time)
      
      test_complete_popup = driver.find_element(By.CSS_SELECTOR, 'div[data-view-cid="view46"] div[role="alertdialog"]')
      try:
        pop_up_exist = test_complete_popup.get_attribute("style")
        if pop_up_exist == "display: block;":
          print(f"\n Speed Test Completed after {rounded_test_elapsed_time} seconds")
          break
      
      except:
        pass

      else:
        if rounded_test_elapsed_time > previous_second:
          print(f"Running speed test, {rounded_test_elapsed_time} seconds has passed.", end = "\r")
        previous_second = rounded_test_elapsed_time

    popup_x_button = driver.find_element(By.CSS_SELECTOR, 'div[data-view-cid="view46"] div[role="alertdialog"] a[title="Dismiss"]')
    popup_x_button.click()

    download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    print("Download Speed:", download_speed)

    upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    print("Upload Speed:", upload_speed)

    internet_speeds = {
      "Download Speed": float(download_speed),
      "Upload Speed": float(upload_speed),
    }

    return (internet_speeds)
  
  def tweet_at_provider(self, internet_speeds):
    tweet_message = ""
    if (internet_speeds["Download Speed"] < TARGET_SPEED_DOWNLOAD):
      tweet_message += f"My Download Speed is {internet_speeds['Download Speed']}mb/s when I'm paying for {TARGET_SPEED_DOWNLOAD}mb/s \n\n"
      print("Tweeting at Provider...Download Speed Sucks")

    if  (internet_speeds["Upload Speed"] < TARGET_SPEED_UPLOAD):
      tweet_message += f"My Upload Speed is {internet_speeds['Upload Speed']}mb/s when I'm paying for {TARGET_SPEED_UPLOAD}mb/s \n\n"
      print("Tweeting at Provider...Upload Speed Sucks")

    elif (internet_speeds["Download Speed"] >= TARGET_SPEED_DOWNLOAD) and (internet_speeds["Upload Speed"] >= TARGET_SPEED_UPLOAD):
      print("My Internet Speed ok")

    driver.get(TWITTER_LOGIN_URL)
    sleep(3)
    username_field = driver.find_element(By.NAME, "text")
    username_field.send_keys(TWITTER_USER)

    submit_username_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    submit_username_button.click()
    sleep(3)

    pw_field = driver.find_element(By.NAME, "password")
    pw_field.send_keys(TWITTER_PW)

    submit_login_button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')
    submit_login_button.click()
    sleep(5)

    tweet_field = driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
    tweet_field.send_keys(tweet_message)
    sleep(2)
    tweet_send_button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
    tweet_send_button.click()

bot1 = InternetSpeedTwitterBot()
internet_speeds = bot1.get_internet_speed()
# internet_speeds = {
#   "Download Speed": 100.0,
#   "Upload Speed": 100.0,
# }
bot1.tweet_at_provider(internet_speeds)

