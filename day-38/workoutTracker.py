from pydoc import resolve
import requests

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
