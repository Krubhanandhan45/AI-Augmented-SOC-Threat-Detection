import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv("features.csv")

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(data)

# Train Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# Save trained model
joblib.dump(model, "isolation_forest_model.pkl")

print("Isolation Forest model trained and saved.")