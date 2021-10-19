import requests
import json
import datetime

with open("Day 37 - Habit Tracking\private_data.json") as file:
    private_data = json.load(file)

pixela_endpoint = "https://pixe.la/v1/users"

date = datetime.datetime.now()
date = date.strftime('%Y%m%d')

#CREATE A USER
# user_params = {
#     "token": private_data["token"],
#     "username": private_data["username"],
#     "agreeTermsOfService": private_data["agreeTermsOfService"],
#     "notMinor": private_data["notMinor"]
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#CREATE A GRAPH
graph_endpoint = f"{pixela_endpoint}/{private_data['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": private_data["token"].encode("utf-8")}

# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers)
# print(response.text)

#CREATE A PIXEL
params = {"date": date, "quantity": "500"}

# response = requests.post(
#     url=f"{graph_endpoint}/{graph_config['id']}",
#     json=params,
#     headers=headers)
# print(response.text)

#UPATE A PIXEL
DATE = date
# response = requests.put(url=f"{graph_endpoint}/{graph_config['id']}/{DATE}",
#                         json=params,
#                         headers=headers)

# print(response.text)

#DELETE A PIXEL

response = requests.delete(url=f"{graph_endpoint}/{graph_config['id']}/{DATE}", headers=headers)
print(response.text)


