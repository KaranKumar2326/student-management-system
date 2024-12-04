from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database()

# Helper function to get the database connection
def get_db():
    print(db)
    return db
