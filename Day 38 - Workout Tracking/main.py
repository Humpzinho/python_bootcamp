import json
import requests
import pprint
from datetime import datetime

with open("Day 38 - Workout Tracking\private_data.json") as file:
    private_data = json.load(file)

headers = {
    "x-app-id": private_data["app_id"],
    "x-app-key": private_data["app_key"],
    "x-remove-user-id": "0"
}

params = {"query": input("Tell me which exercises do you did: ")}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, headers=headers, json=params)

response = response.json()

sheety_endpoint = f"https://api.sheety.co/d437b5a92b55abd13152c91bce35d30d/myWorkouts/workouts"

for n in range(len(response["exercises"])):

    sheet = {
        "workout": {
            "date":
            datetime.now().strftime("%d/%m/%Y"),
            "time":
            datetime.now().strftime("%H:%M:%S"),
            "exercise":
            response["exercises"][n]["name"].title(),
            "duration":
            str(round(response["exercises"][n]["duration_min"])) + " Minutes",
            "calories":
            str(round(response["exercises"][n]["nf_calories"])) + " Calories"
        }
    }

    headers = {
        "Authorization":
        private_data["bearer"]
    }

    response_sheet = requests.post(url=sheety_endpoint, json=sheet, headers=headers)
    # print(response_sheet.text)
    print("\n", response["exercises"][n]["name"].title(),
          "Added to Google Sheets.")
