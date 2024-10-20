# processing.py
import db
from datetime import datetime

# Calculate daily summary (avg, min, max temperatures, and dominant weather)
def get_daily_summary(city):
    connection = db.create_connection()
    cursor = connection.cursor()

    today = datetime.today().strftime('%Y-%m-%d')
    query = f"""
    SELECT 
        AVG(temp) as avg_temp, 
        MAX(temp) as max_temp, 
        MIN(temp) as min_temp, 
        main_weather, COUNT(main_weather) as weather_count 
    FROM weather 
    WHERE DATE(FROM_UNIXTIME(timestamp)) = '{today}' 
    AND city = '{city}' 
    GROUP BY main_weather 
    ORDER BY weather_count DESC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    # Find dominant weather condition
    dominant_weather = result[0][3] if result else None
    summary = {
        "average_temp": result[0][0] if result else None,
        "max_temp": result[0][1] if result else None,
        "min_temp": result[0][2] if result else None,
        "dominant_weather": dominant_weather
    }
    return summary
