from datetime import datetime

import requests
import os

USER_NAME = "yogeshvaral"
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "graph1"
pixela_endpoints = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoints, json=user_param)
# print(response.text)

graph_end_point = f"{pixela_endpoints}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cyclic Graph",
    "unit": "KM",
    "type": "float",
    "color": "ajisai"

}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoints}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": "20210424",
    "quantity": "3.74"
}

# pixel_creation_response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(pixel_creation_response.text)
today = datetime.now().strftime("%Y%m%d")
print(today)

pixel_update_endpoint = f"{pixela_endpoints}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

pixel_data_update = {
    "quantity": "13.74"
}
# pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_data_update, headers=headers)
#
# print(pixel_update_response.text)

pixel_delete_endpoint = f"{pixela_endpoints}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)

print(pixel_delete_response.text)