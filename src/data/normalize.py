import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Make sure data/processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Read processed CSVs
X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")

# Initialize scaler
scaler = StandardScaler()

# Normalize (fit on X_train, then transform both X_train and X_test)
X_train_scaled_array = scaler.fit_transform(X_train)
X_test_scaled_array = scaler.transform(X_test)

# Convert NumPy arrays back to DataFrames, preserving original column names
X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled_array, columns=X_test.columns)

# Write resulting normalized sets to CSV
X_train_scaled.to_csv("data/processed/X_train_scaled.csv", index=False)
X_test_scaled.to_csv("data/processed/X_test_scaled.csv", index=False)

print("2 normalized datasets X_train_scaled.csv and X_test_scaled.csv saved to data/processed.")
