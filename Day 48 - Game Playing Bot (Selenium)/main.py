from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.get(GAME_URL)

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
upgrade_dict = {}
end_time_in_seconds = 300
upgrade_list = driver.find_elements(By.CSS_SELECTOR, "div#store div")
upgrade_prices_list = driver.find_elements(By.CSS_SELECTOR, "div#store div b")

def update_dict():
  upgrade_list = driver.find_elements(By.CSS_SELECTOR, "div#store div:not([class*='amount'])")
  upgrade_prices_list = driver.find_elements(By.CSS_SELECTOR, "div#store div b")
  for i in range(len(upgrade_list)-1):    
    upgrade_dict[i] = {"upgrade":upgrade_list[i].get_attribute("id"), "price":int(upgrade_prices_list[i].text.split("- ")[-1].replace(",",""))}
  print("updated dict:", upgrade_dict)

def click_before_buy():
  seconds_to_buy = 5
  buy_cycle_start_time = time.time()
  buy_elapsed_time = 0
  
  while True:
      current_time = time.time()
      buy_elapsed_time = current_time - buy_cycle_start_time
      cookie.click()

      if buy_elapsed_time > seconds_to_buy:
        update_dict()
        buy_stuff()
        break

def buy_stuff():
  money = int(driver.find_element(By.CSS_SELECTOR, "div#money").text.replace(",",""))
  print("money:", money)
  for i in range(len(upgrade_dict)):
    if upgrade_dict[i]["price"] <= money:
      upgrade_id = upgrade_dict[i]["upgrade"]
      print("upgradeID:", upgrade_id)

  upgrade_to_buy = driver.find_element(By.CSS_SELECTOR, f"#{upgrade_id}")
  print("upgrade_buy:", upgrade_to_buy.text)
  upgrade_to_buy.click()

def main():
  start_time = time.time()
  while True:
    current_time = time.time()
    elapsed_time = current_time - start_time  
    click_before_buy()
    print("elapsed time:", elapsed_time)

    if elapsed_time > end_time_in_seconds:
      cps = driver.find_element(By.ID, "cps").text
      print("CPS:", cps)
      break

main()