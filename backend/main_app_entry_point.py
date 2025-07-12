import os
from dotenv import load_dotenv
from weather import get_weather
from live_predict_skin import capture_and_predict
from rule_based_bot import get_rule_based_suggestion


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
        print("\n🤖 Generating skincare tips to make it glow ...")
        advice = get_rule_based_suggestion(skin_type)
        print(advice)

    else:
        print("❌ Failed to fetch weather data. Check your city name or API settings.")

if __name__ == "__main__":
    main()
