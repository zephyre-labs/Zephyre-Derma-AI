import os
from dotenv import load_dotenv
from weather import get_weather
from live_predict_skin import capture_and_predict
from gemini_api import get_gemini_advice  # 👈 NEW IMPORT
from api.app import app

# Load environment variables
load_dotenv()

def main():
    print("🌟 Welcome to Zephyre: Your Weather-Powered Derma AI")

    # Step 1: Capture Image and Predict Skin Type
    print("\n📸 Capturing image and predicting skin type...")
    skin_type = capture_and_predict()
    if not skin_type:
        print("❌ Failed to predict skin type. Please try again.")
        return

    print(f"🧬 Predicted Skin Type: {skin_type}")

    # Step 2: Get Weather Info
    city = input("\n🏙️ Enter your city name: ").strip()
    weather_info = get_weather(city)

    if weather_info:
        temperature = weather_info.get("temperature")
        humidity = weather_info.get("humidity")
        condition = weather_info.get("description")
        
        print(f"\n🌤️ Weather in {city}:")
        print(f"   Temperature: {temperature}°C")
        print(f"   Humidity   : {humidity}%")
        print(f"   Condition  : {condition}")

        # Step 4: Gemini AI Advice
        print("\n🤖 Generating AI-based skincare advice...")
        gemini_advice = get_gemini_advice(skin_type, condition)
        print("\n📘 Gemini-Powered Skincare Tips:")
        print(gemini_advice)

    else:
        print("❌ Failed to fetch weather data. Check your city name or API settings.")

if __name__ == "__main__":
    main()
