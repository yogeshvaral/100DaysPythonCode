import requests
MY_LAT = 18.520430
MY_LNG = 73.856743
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_KEY = "2624eb685fa4459c28e605246c612203"
parameters = {
"lat" : MY_LAT,
"lon": MY_LNG,
"exclude":"current,minutely,daily",
"appid":MY_KEY

}
response = requests.get(url=OWM_ENDPOINT,params=parameters)

weather_data = response.json()
weather_data_slice = weather_data["hourly"][:12]
for hour_data in weather_data_slice:
    if hour_data["weather"][0]["id"] < 900:
        print("bring Umbrella")