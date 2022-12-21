import requests
import os
from twilio.rest import Client

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": "SFQ442VNAIMF4JDN"

}

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_PARAMS = {
    "apiKey": "d6a0fd6208424303990764739988a502",
    "q": COMPANY_NAME
}

account_sid = "ACfd61e2f33694c0a01346819f1e87a05d"
auth_token = "817fe5e9dc1b5cefd71f115fdabff390"

client = Client(account_sid, auth_token)

request = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
data = request.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_close_price - day_before_yesterday_close_price
percent_change = round((abs(difference) / day_before_yesterday_close_price * 100), 2)

if percent_change > 0:
    request = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    data = request.json()["articles"]
    top_3_news = data[0:3]

    for story in top_3_news:
        message = client.messages \
            .create(
                body=f"TSLA: {'🔽' if difference < 0 else '🔼'} {percent_change}%\n"
                     f"Headline: {story['title']}\n"
                     f"URL: {story['url']}",
                from_='+16692605549',
                to='+447943552608'
        )
