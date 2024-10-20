import sqlite3
from sqlite3 import Error
import config

# Create a connection to SQLite
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(config.DB_PATH)  # This creates a file `weather.db`
    except Error as e:
        print(f"Error: '{e}'")
    return connection

# Create the weather table if it doesn't exist
def create_weather_table():
    query = """
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        main_weather TEXT,
        temp REAL,
        feels_like REAL,
        timestamp INTEGER
    );
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

# Insert new weather data
def insert_weather_data(city, weather_data):
    query = "INSERT INTO weather (city, main_weather, temp, feels_like, timestamp) VALUES (?, ?, ?, ?, ?)"
    values = (city, weather_data['weather'][0]['main'], weather_data['main']['temp'], weather_data['main']['feels_like'], weather_data['dt'])
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()