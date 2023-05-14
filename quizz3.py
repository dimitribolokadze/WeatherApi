import requests
import json
import datetime

api_key = 'cccb7e39abfbe6a058cb1ca4edc0ca3e'
location = 'Tbilisi'
base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'

headers = {'Content-Type': 'application/json'}

response = requests.get(base_url, headers=headers)

weather_data = json.loads(response.text)

if response.status_code == 200:
    if weather_data.get("cod") == "200":
        weather_list = weather_data['list']
        data = {"location": location, "weather_data": []}
        for weather in weather_list:
            date_time = datetime.datetime.fromtimestamp(
                weather['dt']).strftime('%Y-%m-%d %H:%M:%S')
            temp = weather['main']['temp']
            weather_description = weather['weather'][0]['description']
            data["weather_data"].append({
                "date_time": date_time,
                "temperature": temp,
                "description": weather_description
            })
        with open("weather_data.json", "w") as outfile:
            json.dump(data, outfile)
            print("Data written to weather_data.json file")
    else:
        print("Error retrieving weather data:", weather_data.get("message"))
else:
    print("Error connecting to API:", response.status_code, response.reason)
