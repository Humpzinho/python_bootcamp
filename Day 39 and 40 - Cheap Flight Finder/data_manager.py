import requests


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        self.sheety_endpoint = "https://api.sheety.co/1b8b4e59a9cf2a4f1ff62935f4fdecad/flightdeals/prices"
        response_sheet = requests.get(url=self.sheety_endpoint)
        response_sheet.raise_for_status()
        response_sheet = response_sheet.json()
        self.destination_data = response_sheet["prices"]
        return self.destination_data

    def update_sheet(self, city_codes: list):
        print("Updating IATA codes's sheet...")
        for n in range(len(self.destination_data)):

            body = {"price": {"iata": city_codes[n]}}

            response = requests.put(url=f"{self.sheety_endpoint}/{n + 2}",
                                    json=body)

        print(response.text)