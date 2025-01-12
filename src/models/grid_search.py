import os
import yaml
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import joblib

# Load parameters from params.yaml
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)
n_estimators_list = params["model"]["n_estimators"]
max_depth_list = params["model"]["max_depth"]
learning_rate_list = params["model"]["learning_rate"]
random_state = params["model"]["random_state"]

# Load training data
X_train = pd.read_csv("data/processed/X_train_scaled.csv")
y_train = pd.read_csv("data/processed/y_train.csv")

# Define parameter grid for GradientBoostingRegressor
param_grid = {
    "n_estimators": n_estimators_list,
    "max_depth": max_depth_list,
    "learning_rate": learning_rate_list
}

# Initialize regression model
model = GradientBoostingRegressor(random_state=random_state)

# Set up GridSearchCV
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring="neg_mean_squared_error",  # or "r2", "neg_mean_absolute_error", etc.
    cv=5,              # 5-fold cross-validation
    n_jobs=-1,         # use all available CPU cores
    verbose=1          # print progress messages
)

# Fit grid search on training data
grid_search.fit(X_train, y_train)

# Print best hyperparameters and best score
print("Best parameters:", grid_search.best_params_)
# Note: best_score_ is negative MSE because we used "neg_mean_squared_error"
print("Best MSE:", -grid_search.best_score_)

# Extract best model
best_model = grid_search.best_estimator_

# Make sure models folder exists
os.makedirs("models", exist_ok=True)

# Save best parameters as .pkl file in models folder
joblib.dump(grid_search.best_params_, "models/best_params.pkl")

print("best_params.pkl saved to models.")
