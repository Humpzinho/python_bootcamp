import requests
import json
from datetime import datetime, timedelta
import smtplib

STOCK = "GOOG"
COMPANY_NAME = "Google"
PERCENTAGE_SENS = 0

with open("Day 36 - Stock Trading News Alert\private_data.json") as file:
    data = json.load(file)
    email_sender = data["email_sender"]
    password = data["password"]
    email_reciver = data["email_reciver"]
    smtp = data["smtp"]

params = {
    "apikey": data["API_KEY"],
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}

today = datetime.now()
today = today.strftime('%Y-%m-%d')

url = "https://www.alphavantage.co/query"
r = requests.get(url, params)
r.raise_for_status()
data_dict = r.json()

keys = list(data_dict["Time Series (Daily)"].keys())

yesterday_data = data_dict["Time Series (Daily)"][keys[0]]
today_data = data_dict["Time Series (Daily)"][keys[1]]

yesterday_close = int(yesterday_data["4. close"].replace(".", ""))
today_close = int(today_data["4. close"].replace(".", ""))

print(yesterday_close, today_close)

percentage = round(abs(today_close - yesterday_close) / yesterday_close * 100)

print(percentage)

if abs(today_close -
       yesterday_close) / yesterday_close * 100 >= PERCENTAGE_SENS:
    if today_close - yesterday_close / yesterday_close * 100 < 0:
        percentage_sym = "Down"
    else:
        percentage_sym = "Up"

    params = {
        "q": COMPANY_NAME,
        "from": today,
        "sortBy": "popularity",
        "apiKey": data["API_KEY_NEWS"],
        "pageSize": "3",
        "language": "pt"
    }
    url = 'https://newsapi.org/v2/everything?'

    data_dict = requests.get(url, params)
    data_dict.raise_for_status()
    data_dict = data_dict.json()

    print(data_dict)

    a1_title = data_dict["articles"][0]["title"]
    a2_title = data_dict["articles"][1]["title"]
    a3_title = data_dict["articles"][2]["title"]

    a1_content = data_dict["articles"][0]["description"]
    a2_content = data_dict["articles"][1]["description"]
    a3_content = data_dict["articles"][2]["description"]

    a1_font = data_dict["articles"][0]["url"]
    a2_font = data_dict["articles"][1]["url"]
    a3_font = data_dict["articles"][2]["url"]

    messages = [{
        "title": a1_title,
        "content": a1_content,
        "link": a1_font
    }, {
        "title": a2_title,
        "content": a2_content,
        "link": a2_font
    }, {
        "title": a3_title,
        "content": a3_content,
        "link": a3_font
    }]

    for msg in messages:
        msga = f"Subject:{STOCK}: {percentage}% {percentage_sym}\n\nHeadline: {msg['title']}\n\nDescription: {msg['content']}\n\nLink: {msg['link']}"
        print("\nSending Email...", msg['title'])
        with smtplib.SMTP(smtp, 587) as connection:
            connection.starttls()
            connection.login(user=email_sender, password=password)
            connection.sendmail(
                from_addr=email_sender,
                to_addrs=email_reciver,
                msg=msga.encode("utf8"))
            print("\nEmail has been sent.\n")
