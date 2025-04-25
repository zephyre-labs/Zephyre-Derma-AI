import os
import pymongo
import gridfs
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get connection string from env
MONGO_URI = os.getenv("MONGODB_URI")

# ✅ Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client["zephyre_db"]  # or "skin_analyzer" depending on context
fs = gridfs.GridFS(db)

# ✅ Upload images from a folder
def upload_images_from_folder(folder_path, label):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as image_file:
                image_id = fs.put(image_file, filename=filename, label=label)
                print(f"✅ Uploaded '{filename}' under label '{label}' with ID: {image_id}")

# ✅ Retrieve image by label and filename
def retrieve_images_by_label(label, filename):
    file_data = fs.find_one({'filename': filename, 'label': label})
    if file_data:
        with open(f"retrieved_{filename}", "wb") as f:
            f.write(file_data.read())
        print(f"✅ Retrieved image as retrieved_{filename}")
    else:
        print("❌ Image not found.")

# ✅ Upload prediction results
from pymongo import MongoClient
from datetime import datetime

def upload_prediction_result(predicted_label, confidence, full_scores):
    prediction_client = MongoClient(MONGO_URI)
    db = prediction_client["skin_analyzer"]
    collection = db["predictions"]

    result_doc = {
        "predicted_label": predicted_label,
        "confidence": round(confidence, 4),
        "scores": {k: round(v, 4) for k, v in full_scores.items()},
        "timestamp": datetime.utcnow()
    }

    collection.insert_one(result_doc)
    print("✅ Prediction result uploaded to MongoDB.")
