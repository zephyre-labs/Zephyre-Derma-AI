import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")

# Retrieve API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

load_dotenv()  # Loads the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print(f"API Key: {API_KEY}")  # Should print the API key if loaded properly


def test_api(city_name="New York"):
    if not API_KEY:
        print("Error: API key is missing. Check your .env file.")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("✅ API is working!")
        print("Sample Weather Data:", response.json())  # Print API response
    else:
        print("❌ API request failed!")
        print("Status Code:", response.status_code)
        print("Response:", response.json())  # Print error message

# Run the test
test_api()
