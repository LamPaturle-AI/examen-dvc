import pandas as pd
from sklearn.model_selection import train_test_split

# Read the raw CSV
df = pd.read_csv("data/raw_data/raw.csv")

# Separate features (X) and target (y)
#    - Drop 'silica_concentrate' from X
#    - Use df["silica_concentrate"] (Series) as y
X = df.drop("silica_concentrate", axis=1)
y = df["silica_concentrate"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Write the resulting splits to CSV
X_train.to_csv("data/processed_data/X_train.csv", index=False)
X_test.to_csv("data/processed_data/X_test.csv", index=False)
y_train.to_csv("data/processed_data/y_train.csv", index=False)
y_test.to_csv("data/processed_data/y_test.csv", index=False)

print("4 datasets X_train.csv, X_test.csv, y_train.csv and y_test.csv saved to data/processed_data.")