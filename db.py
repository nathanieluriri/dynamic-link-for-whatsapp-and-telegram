from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
APPTYPE = os.getenv("APPTYPE")
# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select the database and collection
db = client[f'{APPTYPE}']  # Replace 'mydatabase' with your database name
url_collection = db['SocialLinks']  # Replace 'urlCollection' with your collection name

# Step 3: Insert document with auto-incremented _id
def insert_url_document_for_whatsApp(url):
    try:
        doc = {
            '_id': 'WhatsApp',  # Ensure _id is unique or allow MongoDB to auto-generate
            'url': url
        }
        result = url_collection.insert_one(doc)  # Insert the document
        print(f"Inserted document: {doc}")
        return result.inserted_id  # Return the inserted document ID
    except Exception as e:
        result = url_collection.find_one_and_update(
            {'_id': 'WhatsApp'},                  # Filter: Find document with _id = 'WhatsApp'
            {'$set': {'url': url}},               # Update: Set the 'url' field to the new value
            upsert=True,                          # Create the document if it doesn't exist
            return_document=True                  # Return the updated document
        )  # Insert the document
        print(f"Inserted document: {result}")
        return None
    

def get_url_document_for_whatsApp():
    try:
        # Query for the document using '_id': 'WhatsApp'
        result = url_collection.find_one({'_id': 'WhatsApp'})
        
        # Debugging: Print the result
        print(f"Got document: {result}")
        
        if result:
            return result['url']  # Return the URL field from the document
        return None  # If no document is found, return None
    except Exception as e:
        print(f"Error getting document: {e}")
        return None



# Step 3: Insert document with auto-incremented _id
def insert_url_document_for_telegram(url):
    try:
        doc = {
            '_id': 'telegram',  # Ensure _id is unique or allow MongoDB to auto-generate
            'url': url
        }
        result = url_collection.insert_one(doc)  # Insert the document
        print(f"Inserted document: {doc}")
        return result.inserted_id  # Return the inserted document ID
    except Exception as e:
        result = url_collection.find_one_and_update(
    {'_id': 'telegram'},                  # Filter: Find document with _id = 'WhatsApp'
    {'$set': {'url': url}},               # Update: Set the 'url' field to the new value
    upsert=True,                          # Create the document if it doesn't exist
    return_document=True                  # Return the updated document
) # Insert the document
        print(f"Inserted document: {doc}")
        return None
    

def get_url_document_for_telegram():
    try:
        # Query for the document using '_id': 'WhatsApp'
        result = url_collection.find_one({'_id': 'telegram'})
        
        # Debugging: Print the result
        print(f"Got document: {result}")
        
        if result:
            return result['url']  # Return the URL field from the document
        return None  # If no document is found, return None
    except Exception as e:
        print(f"Error getting document: {e}")
        return None
