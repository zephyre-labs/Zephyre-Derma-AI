import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your API key from the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_aqi(lat, lon):
    """Fetch AQI data using OpenWeatherMap's Air Pollution API"""
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract AQI from response
        aqi = data['list'][0]['main']['aqi']
        return aqi
    else:
        return "N/A"  # Return "N/A" if API request fails

# Example of using get_aqi function
def get_weather(city_name):
    """Fetch weather data and AQI for the given city"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        
        # Get AQI
        aqi = get_aqi(lat, lon)
        
        # Return weather and AQI data
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'uv_index': 'N/A',  # Replace with your UV index API
            'wind_speed': data['wind']['speed'],
            'air_quality_index': aqi,  # AQI
        }
        print(f"weather data for checking is {weather_data}")
        return weather_data
    else:
        return None

# Example of using the get_weather function
city_name = "London"
weather = get_weather(city_name)

if weather:
    print(f"Weather in {weather['city']}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description']}")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
    print(f"Air Quality Index: {weather['air_quality_index']}")
else:
    print("Sorry, could not fetch weather data.")
