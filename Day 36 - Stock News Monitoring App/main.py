import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": os.environ.get("ALPHAVANTAGE_API_KEY")
}

stock_api_fetch = requests.get(url="https://www.alphavantage.co/query", params=stock_api_params)
stock_api_fetch.raise_for_status()

full_data = stock_api_fetch.json()["Time Series (Daily)"]
full_data_list = list(stock_api_fetch.json()["Time Series (Daily)"].items())

yesterday_data = full_data_list[0]
day_before_yesterday_data = full_data_list[1]

yesterday_price = float(yesterday_data[1]["4. close"])
day_before_yesterday_price = float(day_before_yesterday_data[1]["4. close"])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
newsapi_param = {
    "qInTitle": "TSLA",
    "from": day_before_yesterday_data[0],
    "sortBy": "popularity",
    "apiKey": os.environ.get("NEWSAPI_KEY"),
    "language": "en",
}

newsapi_fetch = requests.get(url="https://newsapi.org/v2/everything", params=newsapi_param)
newsapi_fetch.raise_for_status()
full_news_data = newsapi_fetch.json()

full_news_list = list(newsapi_fetch.json().items())
articles, article_data = full_news_list[2]

top_3_news = {
    count: {
        "title": article["title"],
        "description": article["description"],
    }
    for count, article in enumerate(article_data[:3])}

tsla_price_change = (yesterday_price - day_before_yesterday_price) / day_before_yesterday_price

if tsla_price_change >= 0.05:
    print(f"TSLA: 🔺{round(tsla_price_change*100,2)}%\n")
    for i in range(0, 3):
        print(f"Headline {i+1}: {top_3_news[i]['title']}")
        print(f"Brief {i+1}: {top_3_news[i]['description']}\n")

if tsla_price_change <= -0.05:
    print(f"TSLA: 🔻{round(tsla_price_change*100,2)}%\n")
    for i in range(0, 3):
        print(f"Headline {i+1}: {top_3_news[i]['title']}")
        print(f"Brief {i+1}: {top_3_news[i]['description']}\n")
