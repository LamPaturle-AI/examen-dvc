import os
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Load training data
X_train = pd.read_csv("data/processed/X_train_scaled.csv")
y_train = pd.read_csv("data/processed/y_train.csv")

# Load best hyperparameters from best_params.pkl
params_path = "models/best_params.pkl"
best_params = joblib.load(params_path)

# Create GradientBoostingRegressor with best parameters
gbr = GradientBoostingRegressor(random_state=42, **best_params)

# Fit model on training data
gbr.fit(X_train, y_train)

# Make sure models folder exists
os.makedirs("models", exist_ok=True)

# Save trained model
joblib.dump(gbr, "models/gbr_model.pkl")

print("Trained Gradient Boosting model saved to models.")
