import requests
from dotenv import load_dotenv
import os


# to change directory
# cd "C:\Users\maria selciya\weather-skin-app\backend"
# cd C:\Users
# cd C:\Users\maria selciya\weather-skin-app
# .\venv\Scripts\activate
# cd "C:\Users\maria selciya\weather-skin-app\frontend"
# gunicorn -w 4 app:app
# python app.py
# python backend/test_flask.py

# pip install -r global-packages.txt
#reinstall all packages of globalpython 

# Load environment variables from .env file
load_dotenv()

# Define your API key from the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_uv_index(lat, lon):
    """Fetch UV index using OpenWeatherMap's UV Index API"""
    url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data.get('value', 'N/A')  # Extract UV Index value
    else:
        return "N/A"  # Return "N/A" if API request fails




def get_aqi(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            aqi = data['list'][0]['main']['aqi']
            aqi_levels = {
                1: "Good",
                2: "Fair",
                3: "Moderate",
                4: "Poor",
                5: "Very Poor"
            }
            return f"{aqi} ({aqi_levels.get(aqi, 'Unknown')})"
        else:
            print(f"[AQI API] Failed - Status: {response.status_code}")
            return "N/A"
    except Exception as e:
        print("Error fetching AQI:", e)
        return "N/A"



def get_altitude(lat, lon):
    """Fetch altitude using Open-Elevation API"""
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                return data["results"][0]["elevation"]
            else:
                print("[Altitude] No results found in response.")
                return "N/A"
        else:
            print(f"[Altitude API] Failed - Status: {response.status_code}")
            return "N/A"
    except Exception as e:
        print("Error fetching altitude:", e)
        return "N/A"


def get_weather(city_name):
    """Get weather data for a given city"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            lat = data['coord']['lat']
            lon = data['coord']['lon']

            # Fetch external data
            uv_index = get_uv_index(lat, lon)
            aqi = get_aqi(lat, lon)
            altitude = get_altitude(lat, lon)

            celsius_temp = round(data['main']['temp'], 2)
            feels_like_celsius = round(data['main'].get('feels_like', 0), 2)


            weather_data = {
                'city': data['name'],
                'latitude': lat,
                'longitude': lon,
                'temperature': data['main']['temp'],
                'feels_like': data['main'].get('feels_like', 'N/A'),
                #'temperature': celsius_temp,  # 🔴 Updated
                #'feels_like': feels_like_celsius,  # 🔴 Updated
                'pressure': data['main'].get('pressure', 'N/A'),
                'humidity': data['main']['humidity'],
                'visibility': data.get('visibility', 'N/A'),
                'description': data['weather'][0]['description'],
                'uv_index': uv_index,
                'wind_speed': data['wind']['speed'],
                'air_quality': aqi,
                'rain': data.get('rain', {}).get('1h', 0),
                'altitude': altitude
            }

            return weather_data
        else:
            print(f"[Weather API] Failed - Status: {response.status_code}")
            return None
    except Exception as e:
        print("Error fetching weather:", e)
        return None


def skin_advice(weather, skin_condition):
    """Provide skin care advice based on weather and skin condition"""
    temperature = weather['temperature']
    humidity = weather['humidity']
    uv_index = weather['uv_index']
    wind_speed = weather['wind_speed']
    air_quality = weather['air_quality']
    rain = weather['rain']
    altitude = weather['altitude']

    advice = []

    condition_advice = {
        'acne_prone': "Avoid touching your face and use gentle cleansers.",
        'healthy_skin': "Keep up with your skincare routine and stay hydrated.",
        'oily': "Avoid heavy creams and use oil-free moisturizers.",
        'sensitive': "Use fragrance-free products with calming ingredients like aloe vera.",
        'dry': "Use heavier moisturizers, oils, and humectants (like hyaluronic acid).",
        'combination': "Use lightweight moisturizers for oily areas and richer ones for dry areas.",
        'dehydrated': "Drink plenty of water and use hydrating serums.",
        'mature_skin': "Focus on anti-aging products with retinoids and antioxidants.",
        'hyperpigmented_skin': "Use brightening products with vitamin C and niacinamide.",
        'redness_rosacea': "Use calming products and avoid harsh chemicals.",
        'textured': "Use exfoliants like salicylic acid or glycolic acid.",
        'dull_skin': "Use exfoliating masks and brightening serums.",
        'eczema': "Use emollient-rich creams and avoid irritants.",
        'allergy_prone': "Avoid allergens and use soothing, anti-inflammatory products.",
        'sun_damaged': "Use repair creams with retinoids and vitamin C.",
        'uneven_tone': "Use glycolic acid or AHAs to smooth tone.",
        'pimple_prone': "Use non-comedogenic products and avoid heavy makeup.",
        'open_pores': "Use pore-refining toners and clay masks.",
    }

    advice.append(condition_advice.get(skin_condition, "Hydrate, protect, and follow a consistent skincare routine."))

    if temperature > 30:
        advice.append("It's hot! Stay cool, avoid sun, and reapply sunscreen.")
    elif temperature < 10:
        advice.append("Cold weather — use a thick moisturizer and stay hydrated.")
    else:
        advice.append("Mild weather — great for maintaining skin balance.")

    if humidity > 80:
        advice.append("High humidity — oily skin may become shinier.")
    elif humidity < 30:
        advice.append("Low humidity — dry skin needs extra moisture.")

    if uv_index != "N/A" and uv_index > 6:
        advice.append("UV index is high! Use a broad-spectrum SPF 50+.")

    if isinstance(air_quality, str) and air_quality[0].isdigit():
        if int(air_quality[0]) >= 4:
            advice.append("Poor air quality — cleanse thoroughly and use antioxidant serums.")

    if rain > 0:
        advice.append("Rain detected — keep your skin clean and dry when exposed.")

    if isinstance(altitude, (int, float)) and altitude > 2000:
        advice.append("High altitude — hydrate more, use intense moisturizers.")

    return "\n".join(advice)


def main():
    print("🌤️ WELCOME TO THE WEATHER + SKINCARE ADVISOR 🌤️\n")
    city_name = input("Enter your city name: ").strip()
    skin_condition = input("Enter your skin condition (e.g., acne_prone, oily, dry, etc.): ").lower().strip()

    weather_data = get_weather(city_name)

    if weather_data:
        print("\n📍 Location Details:")
        print(f"City: {weather_data['city']}")
        print(f"Latitude/Longitude: {weather_data['latitude']}, {weather_data['longitude']}")
        print(f"Altitude: {weather_data['altitude']} meters")

        print("\n🌡️ Weather Stats:")
        print(f"Temperature: {weather_data['temperature']}°C (Feels like {weather_data['feels_like']}°C)")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Pressure: {weather_data['pressure']} hPa")
        print(f"Visibility: {weather_data['visibility']} meters")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"UV Index: {weather_data['uv_index']}")
        print(f"Air Quality Index: {weather_data['air_quality']}")
        print(f"Rain (last 1h): {weather_data['rain']} mm")
        print(f"Description: {weather_data['description']}")

        print("\n💡 Skin Care Recommendations:")
        advice = skin_advice(weather_data, skin_condition)
        print(advice)
    if not weather_data:
        print("\n❌ Failed to retrieve weather data. Check your city name or API key.")
        return

if __name__ == "__main__":
    main()
