# alerting.py

THRESHOLD_TEMP = 35  # Example threshold

def check_threshold(weather_data):
    if weather_data['main']['temp'] > THRESHOLD_TEMP:
        print(f"ALERT: Temperature in {weather_data['name']} exceeded {THRESHOLD_TEMP}C!")
        # Implement email or other notification system here
