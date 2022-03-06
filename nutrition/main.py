import requests
from datetime import datetime
APP_ID="7b5daf81"
API_KEY="0d8e02d625b2bb533d22cb61a588971b"
exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
update_endpoint="https://api.sheety.co/5c56768738290a1d36c796265960587f/workoutTracking/workouts"

sheety_endpoint=""
headers={
   "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
cal_config={

 "query":input("Tell me which exercices you did:"),
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response=requests.post(url=exercise_endpoint,json=cal_config,headers=headers)
calories=response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for excercise in calories["exercises"]:
     sheet_inputs={
       "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":excercise["name"].title(),
            "duration":excercise["duration_min"],
            "calories":excercise["nf_calories"],
        }
     }
     sheet_response=requests.post(url=update_endpoint,json=sheet_inputs)
     print(sheet_response.text)