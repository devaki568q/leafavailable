import gridfs
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Access GridFS
fs = gridfs.GridFS(db)

# Specify the directory containing images
image_folder_path = r"C:\Users\cuted\Desktop\img"  # Replace with your folder path

# Iterate over all files in the folder
for filename in os.listdir(image_folder_path):
    file_path = os.path.join(image_folder_path, filename)

    # Check if the file is an image (by extension)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        with open(file_path, "rb") as f:
            fs.put(f, filename=filename)
            print(f"File '{filename}' has been uploaded to GridFS.")

# Close the MongoDB connection
client.close()
