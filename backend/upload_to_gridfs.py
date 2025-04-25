from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
mongo_uri = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(mongo_uri)
db = client['weather_skin_db']
fs = gridfs.GridFS(db)

# Save image to GridFS
with open("skin_sample.jpg", "rb") as image_file:
    file_id = fs.put(image_file, filename="skin_sample.jpg")
    print(f"✅ Image uploaded to MongoDB GridFS with file ID: {file_id}")
