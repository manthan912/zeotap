# weather_api.py
import requests
import config

def get_weather_data(city):
    url = f"{config.API_URL}?q={city}&appid={config.OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
