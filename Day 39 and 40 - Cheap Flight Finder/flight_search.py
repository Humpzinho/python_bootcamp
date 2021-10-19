import requests
from flight_data import FlightData
import json


class FlightSearch:
    def __init__(self, private_data):
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {"apikey": private_data["search_api_key"]}

    def get_destination_code(self, city_name):
        print(f"Getting destination code for {city_name}")
        location_endpoint = f"https://tequila-api.kiwi.com/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                headers=self.headers,
                                params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, iataCode, fly_from, date_from, date_to, curr):

        params = {
            "fly_from": fly_from,
            "fly_to": iataCode,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": curr
        }

        data = requests.get(url=self.search_endpoint,
                            headers=self.headers,
                            params=params)

        try:
            data = data.json()["data"][0]

        except IndexError:
            params["max_stopovers"] = 2

            data = requests.get(url=self.search_endpoint,
                                headers=self.headers,
                                params=params)
            try:
                data = data.json()["data"][0]
            except IndexError:
                return None
            else:
                with open("Day 39 and 40 - Cheap Flight Finder\data.json",
                          "w") as file:
                    json.dump(data, file, indent=4)

                flight_data = FlightData(
                    price=data["price"],
                    cityFrom=data["route"][0]["cityFrom"],
                    airportFrom=data["route"][0]["flyFrom"],
                    cityTo=data["route"][1]["cityTo"],
                    airportTo=data["route"][1]["flyTo"],
                    outDate=data["route"][0]["local_departure"].split("T")[0],
                    returnDate=data["route"][2]["local_departure"].split(
                        "T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                    link=data["deep_link"])
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                cityFrom=data["route"][0]["cityFrom"],
                airportFrom=data["route"][0]["flyFrom"],
                cityTo=data["route"][0]["cityTo"],
                airportTo=data["route"][0]["flyTo"],
                outDate=data["route"][0]["local_departure"].split("T")[0],
                returnDate=data["route"][1]["local_departure"].split("T")[0],
                link=data["deep_link"])
            return flight_data
