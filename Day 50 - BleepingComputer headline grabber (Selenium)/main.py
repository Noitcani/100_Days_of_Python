from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

bleepingcom_url = "https://www.bleepingcomputer.com/"
TODAY_DATE = datetime.now().strftime("%B").upper() + datetime.now().strftime(" %d, %Y")
file_to_write_to = "bleepingcomarticles.md"

driver.get(bleepingcom_url)
list_of_article_categories = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_category'] span:nth-child(1) a")
list_of_article_headlines = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_text'] h4 a")
list_of_article_descriptors = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_text'] p")
list_of_article_dates = driver.find_elements(By.CSS_SELECTOR, "[class='bc_news_date']")
next_page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next Page"]')

def update_all_elements():
  global list_of_article_categories, list_of_article_headlines, list_of_article_descriptors, list_of_article_dates, next_page_button
  print("Updating elements to new page...")
  list_of_article_categories = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_category'] span:nth-child(1) a")
  list_of_article_headlines = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_text'] h4 a")
  list_of_article_descriptors = driver.find_elements(By.CSS_SELECTOR, "[class='bc_latest_news_text'] p")
  list_of_article_dates = driver.find_elements(By.CSS_SELECTOR, "[class='bc_news_date']")
  next_page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next Page"]')

def page_has_todays_news_check():
  print("Running Date Check on Page...")
  page_has_todays_news = False
  for date in list_of_article_dates:
    if date.text == TODAY_DATE:
      page_has_todays_news = True
  return page_has_todays_news

def prepend_line(file_to_write_to, todays_entry):
    print("Writing to DB...")
    # define name of temporary dummy file
    dummy_file = file_to_write_to + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_to_write_to, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(todays_entry + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)

    # remove original file
    os.remove(file_to_write_to)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_to_write_to)


def main():

  print("Starting App...")
  todays_entry = f"# {TODAY_DATE}\n\n"

  if not os.path.exists(file_to_write_to):
    with open(file_to_write_to, 'w') as f:
      pass

  with open(file_to_write_to, 'r') as f:
    if todays_entry in f.read():
      print(f"Already Updated for Today, {TODAY_DATE}...")
      quit()
    else:
      pass
    
  while True:
    if page_has_todays_news_check() == True:
      print("This page has today's articles. Processing...")
      for i in range(len(list_of_article_categories)):
        if list_of_article_categories[i].text != "DEALS":
          article_and_link = "[" + list_of_article_headlines[i].text + "](" + list_of_article_headlines[i].get_attribute("href") + ")"
          todays_entry += f"## {i+1}. {article_and_link} \n -{list_of_article_descriptors[i].text}\n\n"
      next_page_button.click()
      sleep(2)
      update_all_elements()
      
    else:
      print("No more articles from Today. Writing to DB...")
      prepend_line(file_to_write_to, todays_entry)
      driver.quit()
      break

main()