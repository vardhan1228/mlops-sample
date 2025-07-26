# train_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import joblib

# Generate dummy data
X, y = make_classification(n_samples=100, n_features=3, random_state=42)

# Train a simple model
model = LogisticRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'model.joblib')

print("Model saved as model.joblib")
