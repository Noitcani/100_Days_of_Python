# Pre-class Practice

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# chrome_driver_path = "D:/Chrome Driver/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu a")

event_dict = {}
for i in range(len(event_names)):
  event_dict[i] = {
    "times":event_times[i].text, 
    "names":event_names[i].text,
    }

print(event_dict)
driver.quit()


