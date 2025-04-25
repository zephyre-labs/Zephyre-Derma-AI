from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Mongo URI from the .env file
MONGO_URI = os.getenv('MONGO_URI')

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Access the database and collection
db = client['your_database_name']  # Replace with your database name
collection = db['your_collection_name']  # Replace with your collection name

# Query all documents in the collection
documents = collection.find()

# Check if documents exist and print them
if collection.count_documents({}) > 0:
    for doc in documents:
        print(doc)
else:
    print("No documents found in the collection.")
