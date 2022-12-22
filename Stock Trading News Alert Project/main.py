import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": os.getenv("STOCK_API_KEY")

}

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_PARAMS = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "q": COMPANY_NAME
}

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

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
                to=os.getenv("PHONE_NUMBER")
            )
