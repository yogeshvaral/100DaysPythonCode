import requests
import os
from datetime import date
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ["STOCK_API_KEY"]
}
new_api_parameters = {
    "q": "tesla",
    "from": "2021-03-24",
    "sortBy": "publishedAt",
    "apiKey": os.environ["NEWS_API_KEY"]
}
print(new_api_parameters)
response = requests.get(url=STOCK_URL, params=parameters)
daily_data = response.json()["Time Series (Daily)"]
print(response.json()["Time Series (Daily)"])
today = date.today()
print("Today is: ", today)

# Yesterday date
yesterday = today - timedelta(days=1)
print("Yesterday was: ", yesterday)
day_before_yesterday = today - timedelta(days=2)
print("day_before_yesterday was: ", day_before_yesterday)
print("Get News")
yesterday_close = daily_data[str(yesterday)]["4. close"]
day_before_yesterday_close = daily_data[str(day_before_yesterday)]["4. close"]
print(day_before_yesterday_close, yesterday_close)
percentage_Change = ((float(yesterday_close) - float(day_before_yesterday_close)) / float(
    day_before_yesterday_close)) * 100
print(percentage_Change)
if percentage_Change > 1:
    response = requests.get(url=NEWS_API_URL, params=new_api_parameters)
    print(response.url)
    print(response.json())
    new_data = response.json()
    news_data_slice =  new_data["articles"][:3]
    print(news_data_slice)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
