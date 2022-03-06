from twilio.rest import Client
import requests
import os
api_key="YOUR_apikey"
account_sid="your acc_sid"
auth_token="your auth_token"
parameters={
    "lat":13.072090,
    "lon":80.201859,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
report = response.json()
will_rain=False
code=[]
for i in range(0,12):
    code.append(report["hourly"][i]["weather"][0]["id"])
    if code[i]<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its gonna rain",
        from_='Twillio Phone no',
        to='YOUR PHONE NO'
    )
