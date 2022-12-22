import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/e489546c3aa1da9d50733832e3a61d12/myWorkouts/workouts"

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY")
}

sheet_headers = {
    "Authorization": os.getenv("SHEETY_KEY")
}

exercise_config = {
    "query": input("What exercises did you do?\n"),
    "gender": "male",
    "weight_kg": 101.6,
    "height_cm": 175.2,
    "age": 33
}


response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_config, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_headers)
print(sheet_response.text)