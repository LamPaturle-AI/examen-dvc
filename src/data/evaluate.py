import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import json
import joblib

# Load trained model
model_path = "models/gbr_model.pkl"
model = joblib.load(model_path)

# Load test data
X_test = pd.read_csv("data/processed/X_test_scaled.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

# Make predictions
y_pred = model.predict(X_test)

# Make sure 'data/processed' folder exists
os.makedirs("data/processed", exist_ok=True)

# Write predictions to CSV
prediction_df = pd.DataFrame({"prediction": y_pred})
prediction_csv_path = "data/processed/prediction.csv"
prediction_df.to_csv(prediction_csv_path, index=False)
print(f"prediction.csv saved to data/processed")

# Calculate evaluation metrics
mse = mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test, y_pred)

# Make sure metrics folder exists
os.makedirs("metrics", exist_ok=True)

# Save metrics to JSON
scores_path = "metrics/scores.json"
results = {
        "mse": mse,
        "mae": mae,
        "r2": r2
    }

with open(scores_path, "w") as f:
    json.dump(results, f, indent=4)

print(f"scores.json saved to metrics.")
