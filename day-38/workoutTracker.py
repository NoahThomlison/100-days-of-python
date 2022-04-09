from pydoc import resolve
import requests
from datetime import datetime

nutrition_ix_key = "70c7984e84b34028a06cb2bfa58921da"
nutrition_ix_APP_ID ="4ae3f135"
nutrition_ix_exerciseUrl = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("What exercises would you like to record? ")

HEADERS = {
  "x-app-id": nutrition_ix_APP_ID,
  "x-app-key": nutrition_ix_key,
  "x-remote-user-id": "0"
}

exerciseParams = {
 "query":exercise,
 "gender":"male",
 "weight_kg":86,
 "height_cm":182.88,
 "age":33
}
# url=pixel_creation_endpoint, json=pixel_params, headers=headers
response = requests.post(url=nutrition_ix_exerciseUrl, json=exerciseParams, headers=HEADERS)
response.raise_for_status()
exerciseData = response.json()
print(exerciseData)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
exercise = exerciseData["exercises"][0]['name']
duration = exerciseData["exercises"][0]['duration_min']
calories = exerciseData["exercises"][0]['nf_calories']
print(exercise, duration, calories)

sheetlyURL = 'https://api.sheety.co/fb24b170d5576eb361cf6c5aa9b91d83/myWorkouts100DaysOfPython/workouts'

# sheetly post
sheetly_body = {
  "workout": {
    "date": today_date,
    "time": now_time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
  }
}
response = requests.post(url=sheetlyURL, json=sheetly_body, auth=("noah", "123456789"))
