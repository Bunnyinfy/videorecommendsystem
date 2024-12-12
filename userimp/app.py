from flask import Flask, request, jsonify
import pandas as pd
import pickle
from surprise import SVD, Reader, Dataset
from surprise.model_selection import train_test_split

app = Flask(__name__)

# Load the trained model (if saved)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Sample data to simulate user interaction (you can replace it with actual data or a database)
df = pd.read_csv("app.csv")  # Assuming 'data.csv' contains user interaction data


# Function to generate recommendations
def get_recommendations(user_id, category_id=None, mood=None, top_n=10):
    # Filter data based on category_id and mood (optional)
    if category_id:
        df_filtered = df[df["category_id"] == category_id]
    else:
        df_filtered = df

    if mood:
        df_filtered = df_filtered[df_filtered["mood"] == mood]

    all_posts = df_filtered["post_id"].unique()
    unseen_posts = [
        post
        for post in all_posts
        if post not in df_filtered[df_filtered["user_id"] == user_id]["post_id"].values
    ]

    predictions = []
    for post in unseen_posts:
        pred = model.predict(user_id, post)
        predictions.append((post, pred.est))

    # Sort predictions by estimated rating and return top N posts
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:top_n]


# API Endpoint 1: Recommendations based on username, category_id, and mood
@app.route("/feed", methods=["GET"])
def feed():
    username = request.args.get("username")
    category_id = request.args.get("category_id", type=int)
    mood = request.args.get("mood")

    # Find user_id based on username (simulating a mapping to user_id, you can replace it with real data)
    user_id = df[df["username"] == username]["user_id"].values[0]  # Example

    # Get recommendations
    top_recommendations = get_recommendations(user_id, category_id, mood)

    # Format response
    recommendations = [
        {"post_id": post, "predicted_rating": rating}
        for post, rating in top_recommendations
    ]
    return jsonify(recommendations)


# API Endpoint 2: Recommendations based on username and category_id
@app.route("/feed", methods=["GET"])
def feed_category():
    username = request.args.get("username")
    category_id = request.args.get("category_id", type=int)

    # Find user_id based on username
    user_id = df[df["username"] == username]["user_id"].values[0]

    # Get recommendations
    top_recommendations = get_recommendations(user_id, category_id=category_id)

    # Format response
    recommendations = [
        {"post_id": post, "predicted_rating": rating}
        for post, rating in top_recommendations
    ]
    return jsonify(recommendations)


# API Endpoint 3: Recommendations based on username only
@app.route("/feed", methods=["GET"])
def feed_user():
    username = request.args.get("username")

    # Find user_id based on username
    user_id = df[df["username"] == username]["user_id"].values[0]

    # Get recommendations
    top_recommendations = get_recommendations(user_id)

    # Format response
    recommendations = [
        {"post_id": post, "predicted_rating": rating}
        for post, rating in top_recommendations
    ]
    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
