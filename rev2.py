import gridfs
from pymongo import MongoClient
from PIL import Image
import io

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Access GridFS
fs = gridfs.GridFS(db)

# Fetch the image by filename
filename = 'med.jpg'  # Replace with your image filename
grid_out = fs.find_one({'filename': filename})

if grid_out is None:
    print(f"File '{filename}' not found in GridFS.")
else:
    # Convert the file to an image
    image = Image.open(io.BytesIO(grid_out.read()))

    # Display the image
    image.show()

    # Optionally, save the image locally
    image.save("output_image.jpg")

# Close the MongoDB connection
client.close()
