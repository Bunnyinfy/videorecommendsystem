# evaluate_model.py
from surprise.model_selection import cross_validate, GridSearchCV
from surprise import SVD, Dataset, Reader
import pandas as pd
import pickle  # If you save your model in the previous file

# Assuming your data is already prepared as 'viewed_df'
# For example, 'viewed_df' should look like this:
# viewed_df = pd.DataFrame({'user_id': [1, 2, 3, 4, 5], 'post_id': [101, 102, 103, 104, 105], 'viewed': [1, 1, 0, 1, 0]})

viewed_df = pd.DataFrame(
    {
        "user_id": [1, 2, 3, 4, 5],
        "post_id": [101, 102, 103, 104, 105],
        "viewed": [1, 1, 0, 1, 0],
    }
)

# Load the data into Surprise format
reader = Reader(rating_scale=(0, 1))  # Assuming the ratings are binary (0 or 1)
data = Dataset.load_from_df(viewed_df[["user_id", "post_id", "viewed"]], reader)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 1. Model Evaluation - Cross-validation
print("Starting cross-validation...")
cross_validate(model, data, measures=["RMSE", "MAE"], cv=5, verbose=True)

# 2. Hyperparameter Tuning - GridSearchCV
param_grid = {
    "n_factors": [50, 100, 200],
    "n_epochs": [20, 50],
    "lr_all": [0.002, 0.005],
    "reg_all": [0.02, 0.1],
}
grid_search = GridSearchCV(SVD, param_grid, measures=["RMSE"], cv=3)
grid_search.fit(data)

# Get the best parameters and RMSE score
print("Best Parameters:", grid_search.best_params)
print("Best RMSE Score:", grid_search.best_score["RMSE"])
