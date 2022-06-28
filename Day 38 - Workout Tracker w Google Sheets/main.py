import requests
import datetime as dt
import os

# Export Environ Var for
## NUTRITIONIX_APP_ID = Nutritionix app id
## NUTRITIONIX_API_KEY = Nutritionix API key
## SHEETY_AUTH = Sheety Auth Token
## SHEETY_EP = Sheety Endpoint

NUTRITIONIX_HEADER = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
    "Content-Type": "application/json",
}

NUTRITIONIX_EXERCISE_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_HEADER = {
    "Authorization": os.environ.get("SHEETY_AUTH"),
    "Content-Type": "application/json",
}

# User info
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 170
AGE = 30

# User input, post, and response from Nutritionix API (POST)
user_exercise_input = input("Tell me which exercises you did:  ")

nutritionix_exercise_params = {
    "query": user_exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_post = requests.post(url=NUTRITIONIX_EXERCISE_EP,
                              json=nutritionix_exercise_params,
                              headers=NUTRITIONIX_HEADER)

# Creating row and adding in info using Sheety API (POST)
for count, exercise in enumerate(exercise_post.json()["exercises"]):
    sheety_params = {
        "workout":{
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise_post.json()["exercises"][count]["name"].title(),
            "duration": exercise_post.json()["exercises"][count]["duration_min"],
            "calories": exercise_post.json()["exercises"][count]["nf_calories"],
        }
    }

    sheety_post = requests.post(url=os.environ.get("SHEETY_EP"),
                                json=sheety_params,
                                headers=SHEETY_HEADER)

