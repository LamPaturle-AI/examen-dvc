import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import joblib

# Load the training data
X_train = pd.read_csv("data/processed/X_train_scaled.csv")
y_train = pd.read_csv("data/processed/y_train.csv")

# Define a parameter grid for GradientBoostingRegressor
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10],
    "learning_rate": [0.01, 0.1, 0.2]
}

# Initialize the regression model
model = GradientBoostingRegressor(random_state=42)

# Set up GridSearchCV
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring="neg_mean_squared_error",  # or "r2", "neg_mean_absolute_error", etc.
    cv=5,              # 5-fold cross-validation
    n_jobs=-1,         # use all available CPU cores
    verbose=1          # print progress messages
)

# Fit the grid search on the training data
grid_search.fit(X_train, y_train)

# Print best hyperparameters and best score
print("Best parameters:", grid_search.best_params_)
# Note: best_score_ is negative MSE because we used "neg_mean_squared_error"
print("Best MSE:", -grid_search.best_score_)

# Extract the best model
best_model = grid_search.best_estimator_

# Save the best parameters as a .pkl file
joblib.dump(grid_search.best_params_, "models/best_params.pkl")

print("best_params.pkl saved to models.")
