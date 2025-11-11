import os
import pandas as pd
import joblib

# ==== Paths ====
data_path = os.path.join("Data", "creditcard.csv")
model_dir = "models"
model_path = os.path.join(model_dir, "fraude_random_forest.pkl")
scaler_path = os.path.join(model_dir, "scaler.pkl")

# ==== Load model and scaler ====
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    raise FileNotFoundError("Train the model first! Run 'train_model.py'")

rf_model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# ==== Load data ====
df = pd.read_csv(data_path)
X = df.drop(columns=["Class"], errors="ignore")

# ==== Scale features ====
X_scaled = scaler.transform(X)

# ==== Predict ====
predictions = rf_model.predict(X_scaled)

# ==== Show summary ====
print(f"Total transactions: {len(predictions)}")
print(f"Predicted fraud cases: {sum(predictions)}")
print("First 10 predictions:", predictions[:10])
