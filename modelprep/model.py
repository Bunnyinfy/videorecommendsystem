import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import pickle

# Step 1: Create sample viewed_df (data)
data = {
    "user_id": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "post_id": [
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
    ],
    "viewed": [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
}

viewed_df = pd.DataFrame(data)
print(viewed_df.head())

# Step 2: Prepare the data for the Surprise library
reader = Reader(rating_scale=(0, 1))  # Assuming 'viewed' is binary (0 or 1)

# Load the data into Surprise dataset
data = Dataset.load_from_df(viewed_df[["user_id", "post_id", "viewed"]], reader)

# Step 3: Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Step 4: Build the SVD (Singular Value Decomposition) model
model = SVD()

# Step 5: Train the model
model.fit(trainset)

# Step 6: Make predictions and evaluate
predictions = model.test(testset)

# Step 7: Calculate RMSE (Root Mean Squared Error) to evaluate the performance
rmse = accuracy.rmse(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Step 8: Make a prediction for a specific user and item (e.g., user_id = 1, post_id = 10)
user_id = str(1)  # User ID should be a string as per the input data
post_id = str(10)  # Item ID (post) should be a string as per the input data

# Prediction for user 1 and post 10
prediction = model.predict(user_id, post_id)
print(f"Prediction for user {user_id} and post {post_id}: {prediction.est}")


# Step 9: Get top N recommendations for a specific user
def get_top_n(predictions, n=10):
    top_n = {}
    for uid, iid, true_r, est, _ in predictions:
        if uid not in top_n:
            top_n[uid] = []
        top_n[uid].append((iid, est))

    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


top_n_recommendations = get_top_n(predictions, n=5)

# Display top 5 recommendations for each user
for uid, user_ratings in top_n_recommendations.items():
    print(f"Top 5 recommendations for user {uid}:")
    for iid, rating in user_ratings:
        print(f"Post ID: {iid}, Predicted Rating: {rating}")
# Saving the model after training
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
