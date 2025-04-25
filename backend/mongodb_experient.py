from pymongo import MongoClient

# Replace with your actual connection string
connection_string = "mongodb+srv://lrnmrtbcmndtscntst:eDLhaAz0kPmFc9UB@dermaaicluster.2x6llpd.mongodb.net/?retryWrites=true&w=majority&appName=dermaaiCluster"

try:
    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)

    # Check if the connection was successful by listing databases
    databases = client.list_database_names()

    if databases:
        print("Successfully connected to MongoDB Atlas!")
        print("Databases available:", databases)
    else:
        print("No databases found.")

except Exception as e:
    print("Error connecting to MongoDB Atlas:", e)

# Sample document to insert into your collection
sample_document = {
    "prediction": "oily",
    "confidence_score": 0.85,
    "timestamp": "2025-04-22T12:00:00"
}

# Specify the collection where you want to store data
# List all collections in the 'skin_analysis' database
client = MongoClient(connection_string)

# Define the 'skin_analysis' database
db = client['skin_analysis']

# List all collections in the 'skin_analysis' database
collections = db.list_collection_names()

print("Collections in 'skin_analysis' database:", collections)

from pymongo import MongoClient
from datetime import datetime

# Define the database and collection
db = client['skin_analysis']
collection = db['skin_analysis_results']

# Example prediction data
prediction_data = {
    "user_id": "user123",  # You can track results per user
    "prediction": "oily",  # Skin type prediction
    "confidence_score": 0.85,  # Confidence score of prediction
    "timestamp": datetime.now()  # When the prediction was made
}

# Insert the prediction data into the collection
collection.insert_one(prediction_data)

print("Prediction data stored successfully!")

# List all collections to confirm where the data was stored
collections = db.list_collection_names()
print("Collections in 'skin_analysis' database:", collections)
