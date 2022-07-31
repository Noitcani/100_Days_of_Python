from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname_field = driver.find_element(By.NAME, 'fName')
lastname_field = driver.find_element(By.NAME, 'lName')
email_field = driver.find_element(By.NAME, 'email')
submit_buttom = driver.find_element(By.XPATH, '/html/body/form/button')

firstname_field.send_keys("FirstNameTest")
lastname_field.send_keys("LastNameTest")
email_field.send_keys("email@test.com")
submit_buttom.click()