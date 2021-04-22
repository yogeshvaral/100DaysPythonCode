import requests
from datetime import datetime
import dateutil.parser
import time
MY_LAT = 18.520430
MY_LNG = 73.856743

parameter = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

yourdate = dateutil.parser.parse(sunrise)

print(yourdate.hour)

print(sunrise,sunset)

def datetime_from_utc_to_local(yourdate):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return yourdate + offset

print(datetime_from_utc_to_local(yourdate).hour,datetime_from_utc_to_local(yourdate))