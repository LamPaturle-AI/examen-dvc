import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

# Make sure data/processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load parameters
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)
test_size = params["split"]["test_size"]
random_state = params["split"]["random_state"]

# Read raw CSV
df = pd.read_csv("data/raw/raw.csv")

# Drop 'date' column if present
if 'date' in df.columns:
    df = df.drop("date", axis=1)

# Separate features (X) and target (y)
#    - Drop 'silica_concentrate' from X
#    - Use df["silica_concentrate"] (Series) as y
X = df.drop("silica_concentrate", axis=1)
y = df["silica_concentrate"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Write resulting splits to CSV
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("4 datasets X_train.csv, X_test.csv, y_train.csv and y_test.csv saved to data/processed.")
