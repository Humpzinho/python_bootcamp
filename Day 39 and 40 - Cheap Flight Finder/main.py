from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import json
from datetime import datetime, timedelta

with open("Day 39 and 40 - Cheap Flight Finder\private_data.json") as file:
    private_data = json.load(file)

date_from = datetime.now().strftime("%d/%m/%Y")
date_to = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")

FLY_FROM_IATA = "RIO"
COUNTRY_SYMBOL = "£"
CURR = "GBP"

data_manager = DataManager()
flight_search = FlightSearch(private_data)
notify_manager = NotificationManager(private_data)

update = False
destination_code = []
sheet_data = data_manager.get_destination_data()

for data in sheet_data:
    if data["iata"] == "":
        destination_code.append(
            flight_search.get_destination_code(data["city"]))
        update = True
    else:
        print(f"Saving IATA Code of {data['city']} from sheet...")
        destination_code.append(data["iata"])

if update == True:
    data_manager.update_sheet(destination_code)

for code, data in zip(destination_code, sheet_data):
    flight = flight_search.check_flights(code, FLY_FROM_IATA, date_from,
                                         date_to, CURR)

    if flight == None:
        print(f"\nNo flights found for: {code}")
        continue

    print(
        f"\n{flight.cityTo}: £{flight.price}, Minimum Required: {COUNTRY_SYMBOL}{data['lowestPrice']}"
    )

    if flight.price < data["lowestPrice"]:

        print(
            f"Low price alert! Only {COUNTRY_SYMBOL}{flight.price} to fly from {flight.cityFrom}-{flight.airportFrom} to {flight.cityTo}-{flight.airportTo}, from {flight.outDate} to {flight.returnDate}."
        )
        if flight.stop_overs > 0:
            print(
                f"Flight has {flight.stop_overs} stop over, via {flight.via_city}."
            )
        notify_manager.send_email(flight)
