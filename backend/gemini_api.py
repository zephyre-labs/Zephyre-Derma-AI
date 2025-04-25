# backend/gemini_api.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key missing from environment.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_advice(skin_type: str, weather_condition: str) -> str:
    prompt = (
        f"Give detailed skincare advice for {skin_type} skin in {weather_condition} weather. "
        f"Include cleanser, moisturizer, sunscreen, exfoliation, hydration, and any precautions."
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini error: {e}"
