import requests
import smtplib
from datetime import datetime, timezone
import json

#FILL THIS VARIABLES WITH YOUR DATA
with open("Day 33 - ISS Overhead Notifier\ISS Overhead\private_data.json"
          ) as file:
    data = json.load(file)
    MY_LAT = data["my_lat"]
    MY_LNG = data["my_lng"]
    email_sender = data["email_sender"]
    password = data["password"]
    email_reciver = data["email_reciver"]
    smtp = data["smtp"]

    def iss_check():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = int(float(data["iss_position"]["latitude"]))
        iss_longitude = int(float(data["iss_position"]["longitude"]))
        if MY_LAT in range(iss_latitude - 5,
                           iss_latitude + 5) and MY_LNG in range(
                               iss_longitude - 5, iss_longitude + 5):
            return True

    def time_check():
        params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
        response = requests.get(" https://api.sunrise-sunset.org/json",
                                params=params)
        response.raise_for_status()
        data = response.json()
        hour = datetime.now(timezone.utc).hour
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        if hour <= sunrise or hour >= sunset:
            return True


print(f"\nISS Checker: {iss_check()}, Time Checker: {time_check()}")
if not iss_check() and time_check():
    print("\nSending email...")
    with smtplib.SMTP(smtp, 587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(
            from_addr=email_sender,
            to_addrs=email_reciver,
            msg="Subject: Look Up👆🏼\n\nThe ISS is above you in the sky!".encode("utf8"))
        print("\nEmail has been sent.")
else:
	print("\nISS is not close of you, or is not night yet")