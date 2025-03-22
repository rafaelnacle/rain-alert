import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

parameters = {
    "lat": -23.663345,
    "lon": -52.604435,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_='',
        body='Hoje vai chover, lembre-se de trazer um ☂️',
        to=''
    )