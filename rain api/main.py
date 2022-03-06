from twilio.rest import Client
import requests
import os
api_key="a0d680c1352f007f28539ecf7c0d4527"
account_sid="ACa20f58eb052f680b4ec397edbc1d6ae9"
auth_token="05c0551007a19d93a915d39de087d93e"
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
        from_='+19362463180',
        to='+918754280344'
    )

#api_key=os.environ.get("OWM_API_KEY")
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

# print(message.sid)