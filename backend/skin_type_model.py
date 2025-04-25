from pymongo import MongoClient
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
import cv2
import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import load_model

# Load environment variables from .env
load_dotenv()

# Get the Mongo URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Ensure it exists
if not mongo_uri:
    raise ValueError("❌ MongoDB URI not found. Did you forget to set MONGO_URI in .env?")

# Load your model
model = load_model("skin_type_model.keras")

# Label map for predicted class index
label_map = {
    0: "Normal", 1: "Oily", 2: "Dry", 3: "Combination", 4: "Sensitive",
    5: "Acne Prone", 6: "Dehydrated", 7: "Mature Skin", 8: "Hyperpigmented",
    9: "Redness/Rosacea", 10: "Textured", 11: "Dull", 12: "Eczema",
    13: "Allergy Prone", 14: "Sun Damaged", 15: "Uneven Tone", 16: "Pimple Prone",
    17: "Open Pores", 18: "Healthy Skin"
}

def predict_skin_type(img):
    """Loads an image and predicts skin type."""
    try:
        # Preprocess image
        img = cv2.resize(img, (224, 224))  # Resize to match input size
        img = img / 255.0  # Normalize the image
        img = np.expand_dims(img, axis=0)  # Expand dims for batch size of 1

        # Predict using the model
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)
        predicted_label = label_map.get(predicted_class, "Unknown")

        return predicted_label, np.max(prediction)  # Return predicted label and confidence

    except Exception as e:
        print("Prediction error:", e)
        return None, None

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["skin_data"]
collection = db["predictions"]

# Capture image from webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Press 's' to save and predict
        img_path = "skin_sample.jpg"
        cv2.imwrite(img_path, frame)
        print(f"✅ Image saved to {img_path}")
        
        # Predict skin type
        predicted_label, confidence = predict_skin_type(frame)
        if predicted_label:
            print(f"🧠 Predicted Skin Type: {predicted_label} ({confidence * 100:.2f}% confidence)")

            # Upload to MongoDB
            record = {
                "predicted_label": predicted_label,
                "confidence": float(confidence),
                "timestamp": datetime.now(timezone.utc)
            }

            # Upload record to MongoDB
            insert_result = collection.insert_one(record)

            # Check if insertion was successful
            if insert_result.acknowledged:
                print("Document inserted successfully.")
            else:
                print("Insertion failed.")
    elif key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
