from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from os import environ
from dotenv import load_dotenv

load_dotenv()
LI_USERNAME = environ["LI_USERNAME"]
LI_PASSWORD = environ["LI_PASSWORD"]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

linkedin_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver.get(linkedin_url)
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
time.sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys(LI_USERNAME)
pw_field = driver.find_element(By.ID, "password")
pw_field.send_keys(LI_PASSWORD)
login_submit = driver.find_element(By.CSS_SELECTOR, "button[data-litms-control-urn='login-submit']")
login_submit.click()
time.sleep(2)

job_listing_list = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

# for job in job_listing_list:
#   print(job.get_attribute("data-job-id"))

job_listing_list[0].click()
time.sleep(2)

easy_apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
easy_apply_button.click()
time.sleep(2)

phone_number_field = driver.find_element(By.CSS_SELECTOR, "input[name*='phoneNumber']")
phone_number_field.send_keys("123456789")

next_step_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_step_button.click()
time.sleep(2)

next_step_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_step_button.click()
time.sleep(2)