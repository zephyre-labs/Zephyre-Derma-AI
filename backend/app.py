from flask import Flask, request, jsonify
from flask_cors import CORS  # This will allow requests from other origins (your frontend)

from PIL import Image
import numpy as np
import base64
import io
import os
from keras.models import load_model  # ✅ This was missing!

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load model
model_path = os.path.join(os.path.dirname(__file__), "skin_type_model.keras")
model = load_model(model_path, compile=False)
# Your custom modules
from rule_based_bot import skin_type_suggestions
from weather import get_weather

# Flask app
app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "http://127.0.0.1:5500"}})


# Labels for skin types
LABELS = [
    'normal', 'oily', 'dry', 'combination', 'sensitive', 'acne_prone',
    'dehydrated', 'mature_skin', 'hyperpigmented_skin', 'redness_rosacea',
    'textured', 'dull_skin', 'eczema', 'allergy_prone', 'sun_damaged',
    'uneven_tone', 'pimple_prone', 'open_pores', 'healthy_skin'
]

# Prediction function
def predict_skin_type(image_array):
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)[0]
    max_index = np.argmax(predictions)
    return LABELS[max_index], round(float(predictions[max_index]) * 100, 2)

# Route
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        image_data = data.get('image')
        city = data.get('city', 'Chennai')

        if not image_data:
            return jsonify({"status": "error", "message": "Image not provided"}), 400

        img_bytes = base64.b64decode(image_data.split(',')[1])
        img = Image.open(io.BytesIO(img_bytes)).resize((224, 224))
        img_array = np.array(img) / 255.0

        label, confidence = predict_skin_type(img_array)
        weather = get_weather(city) or "humid"
        advice = get_rule_based_suggestion(label)

        return jsonify({
            "status": "success",
            "skin_type": label,
            "confidence": confidence,
            "weather": weather,  # 👈 ADD THIS
            "derma_advice": advice
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
print("🔥 Flask server is running at http://localhost:5000/analyze")

# Production server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')