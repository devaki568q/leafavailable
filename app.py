from flask import Flask, render_template, request, send_file
import gridfs
from pymongo import MongoClient
from PIL import Image
import io

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Access GridFS
fs = gridfs.GridFS(db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_image', methods=['POST'])
def fetch_image():
    filename = request.form['filename']
    grid_out = fs.find_one({'filename': filename})

    if grid_out is None:
        return f"File '{filename}' not found in GridFS."

    image = Image.open(io.BytesIO(grid_out.read()))
    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg', as_attachment=False, attachment_filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
