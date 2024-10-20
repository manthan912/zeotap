# main.py
import time
import schedule
import weather_api
import db
import processing
import alerting
import config


# Fetch and store weather data for all cities
def fetch_and_store_weather():
    for city in config.CITIES:
        weather_data = weather_api.get_weather_data(city)
        if weather_data:
            db.insert_weather_data(city, weather_data)
            alerting.check_threshold(weather_data)


# Generate daily summary for all cities
def generate_daily_summary():
    for city in config.CITIES:
        summary = processing.get_daily_summary(city)
        print(f"Daily Summary for {city}: {summary}")


def main():
    db.create_weather_table()  # Ensure the weather table exists

    schedule.every(5).minutes.do(fetch_and_store_weather)  # Fetch every 5 minutes
    schedule.every().day.at("23:59").do(generate_daily_summary)  # Generate daily summary at the end of the day

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
