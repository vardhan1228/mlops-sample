from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import joblib

# ✅ Fix: total = 3, informative + redundant + repeated <= 3
X, y = make_classification(
    n_samples=100,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=42
)

model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.joblib')
print("✅ Model saved as model.joblib")
