from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load("model.pkl")

@app.route("/")
def index():
    return "🚀 Flask ML App is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    input_features = data.get("features")

    if not input_features or not isinstance(input_features, list):
        return jsonify({"error": "Invalid input. Provide a list under 'features' key."}), 400

    try:
        prediction = model.predict(np.array(input_features).reshape(1, -1))
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    try:
        test_input = [5.1, 3.5, 1.4, 0.2]
        prediction = model.predict(np.array(test_input).reshape(1, -1))
        return jsonify({"health": "ok", "test_prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"health": "fail", "error": str(e)}), 500

if name == "__main__":
    app.run(host="0.0.0.0", port=5000)
