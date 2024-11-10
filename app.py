from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from pymongo import MongoClient 
import numpy as np
import base64
import os
from io import BytesIO
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = "/Users/gurpreetsingh/Desktop/Hackathon/asl_digit_classifier.keras"  # or "asl_digit_classifier.h5" if saved in H5 format
model = load_model(model_path)

mongo_uri = "mongodb+srv://hackathon:Geetu1234@cluster0.rfacr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with the MongoDB URI from your teammate
client = MongoClient(mongo_uri)
db = client["hackathon"]  # Replace with the actual database name
collection = db["fs"]

# Function to preprocess and predict
def predict_image(img):
    img = img.resize((64, 64))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return predicted_class

# Define the prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "image" not in data:
        print("No image data provided")
        return jsonify({"error": "No image data provided"}), 400

    # Decode the base64 image
    image_data = data["image"].split(",")[1]  # Remove the base64 prefix
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    print("Image decoded successfully")

    # Predict the class
    predicted_class = predict_image(img)
    print("Prediction successful:", predicted_class)
        # Prepare data to store in MongoDB
    image_record = {
        "image": image_data,  # Store base64 image
        "prediction": int(predicted_class),
    }

    
    # Insert the record into MongoDB
    collection.insert_one(image_record)
    # Return the prediction as JSON
    return jsonify({"prediction": int(predicted_class)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
