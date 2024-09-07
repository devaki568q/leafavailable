from pymongo import MongoClient
import os
from PIL import Image
import base64

# Connect to MongoDB (adjust the URI as needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Replace with your database name
collection = db["img"]  # Replace with your collection name

# Specify the folder containing the images
image_folder_path = r"C:\Users\cuted\OneDrive\Desktop\img"  # Use raw string to avoid escape sequences

# Iterate through each image in the folder
for filename in os.listdir(image_folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):  # Add more formats if needed
        image_path = os.path.join(image_folder_path, filename)
        
        # Open and read the image file
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        
        # Encode the image to base64 (optional)
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        
        # Prepare the document to be inserted into MongoDB
        image_document = {
            "filename": filename,
            "data": encoded_image  # Or use image_data for binary storage
        }
        
        # Insert the document into MongoDB
        collection.insert_one(image_document)
        
        print(f"Uploaded {filename} to MongoDB.")

# Retrieve all images from the collection
for document in collection.find({}):
    filename = document["filename"]
    image_data = document["data"]
    
    # Decode the base64 data (if encoded)
    image_data = base64.b64decode(image_data)
    
    # Save the image to disk
    with open(f"retrieved_{filename}", "wb") as image_file:
        image_file.write(image_data)
    
    print(f"Retrieved {filename} from MongoDB.")
