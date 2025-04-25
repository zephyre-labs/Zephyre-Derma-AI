from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv
import os
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
mongo_uri = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(mongo_uri)
db = client['weather_skin_db']
fs = gridfs.GridFS(db)

# Find the image in GridFS
image = fs.find_one({"filename": "skin_sample.jpg"})
if image:
    # Read the file content into memory
    image_data = image.read()
    # Process image_data in memory (e.g., pass it to a function, display it, etc.)
    print("✅ Image loaded successfully into memory.")
else:
    print("⚠ No image found.")
