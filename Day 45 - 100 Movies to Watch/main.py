from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_code = response.text
soup = BeautifulSoup(response.text, "lxml")

title_tags = soup.find_all(name="h3", class_="title")
title_list = [tag.getText() for tag in title_tags]
reversed_title_list = title_list[::-1]

print(reversed_title_list)

with open("Top 100 movies.txt", "w", encoding="utf-8") as f:
  for title in reversed_title_list:
    f.write(f"{title}\n")