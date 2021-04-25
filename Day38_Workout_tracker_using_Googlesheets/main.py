import os

import requests

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]


post_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type":"application/json"
}
query = input("Tell me what exercise you did today")
post_request = {
    "query":query,
    "gender":"female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

post_response = requests.post(url=post_endpoint,json=post_request,headers=headers)
print(post_response.json())