from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the Mongo URI from the environment variable
MONGO_URI = os.getenv("MONGO_URI")


# Debugging: Print the Mongo URI to make sure it is being loaded
print(f"Mongo URI: {MONGO_URI}")  # Should print your Mongo URI

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Access the database (ensure you use your actual database name)
db = client.get_database()

# Helper function to get the database connection
def get_db():
    print(f"Connected to database: {db.name}")  # Debugging statement to check the connection
    return db
