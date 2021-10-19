import requests
import json
from twilio.rest import Client

with open("Day 35 - Weather Notify SMS\private_data.json") as file:
    datapv = json.load(file)


params = {
    "lat": datapv["my_lat"],
    "lon": datapv["my_lng"],
    "appid": datapv["my_key"],
    "exclude": "daily,minutely,current"
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                    params=params)
data.raise_for_status()

data = data.json()
will_rain = False

for n in range(12):
    if data["hourly"][n]["weather"][0]["id"] <= 700:
        will_rain = True

if not will_rain:
    body = "It's not rain today."
else:
    body = "Bring an umbrella"
    
client = Client(datapv["account_sid"], datapv["auth_token"]) 
    
message = client.messages.create(  
                            messaging_service_sid=data["message_sid"], 
                            body=body,      
                            to=data["number"]
                        ) 

print(message.sid)