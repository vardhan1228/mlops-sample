from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    model = None
    print(f"❌ Failed to load model: {e}")

@app.route("/")
def index():
    return "Welcome to the Flask ML App  vardhan🎉"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Example input: /predict?f1=5.1&f2=3.5&f3=1.4&f4=0.2
        features = [
            float(request.args.get("f1")),
            float(request.args.get("f2")),
            float(request.args.get("f3")),
            float(request.args.get("f4"))
        ]
        prediction = model.predict([features])[0]
        return jsonify({
            "input": features,
            "prediction": int(prediction)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/health")
def health():
    if model:
        return "OK", 200
    return "Model not loaded", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
