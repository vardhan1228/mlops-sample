# app.py
from flask import Flask, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

@app.route('/')
def index():
    return "Welcome to the ML App with Sample Model"

@app.route('/predict', methods=['GET'])
def predict():
    # Use a dummy input to simulate prediction
    sample_input = np.array([[0.5, -1.2, 0.3]])  # 2D input
    prediction = model.predict(sample_input)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
