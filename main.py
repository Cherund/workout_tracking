import requests
from datetime import datetime

now = datetime.now()

APP_ID = YOUR_APP_ID
API_KEY = YOUR_API_KEY
exercise_endpoint = YOUR_ENDPOINT
sheet_url = YOUR_SHEET_URL
USER = YOUR_USER
PASSWORD = YOUR_PASSWORD

sheet_auth = (USER, PASSWORD)

nutri_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

query = input('What did you do today?')

body = {
 "query": query,
 "gender": "male",
 "weight_kg": 70,
 "height_cm": 180,
 "age": 28
}

response = requests.post(exercise_endpoint, json=body, headers=nutri_headers)
result = response.json()

for exercise in result['exercises']:
    workout_dict = {
        'workout': {
            'date': now.strftime('%d/%m/%Y'),
            'time': now.strftime('%X'),
            'exercise': exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheet_url, json=workout_dict, auth=sheet_auth)
