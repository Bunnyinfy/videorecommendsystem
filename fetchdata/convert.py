import os
import json
import pandas as pd

# Directories
json_dir = "C:\\Users\\srinivas\\OneDrive\\Desktop\\VideoRecommendSystem\\fetched_data"
csv_dir = "C:\\Users\\srinivas\\OneDrive\\Desktop\\VideoRecommendSystem\\csv_files"

# Ensure directories exist
os.makedirs(json_dir, exist_ok=True)
os.makedirs(csv_dir, exist_ok=True)


# Function to convert JSON to CSV
def convert_json_to_csv(json_filename, csv_filename):
    json_path = os.path.join(json_dir, json_filename)
    csv_path = os.path.join(csv_dir, csv_filename)

    # Load JSON data with explicit encoding
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"Converted {json_filename} to {csv_filename}")


# List of files to convert
file_mapping = {
    "viewed_posts.json": "viewed_posts.csv",
    "liked_posts.json": "liked_posts.csv",
    "inspired_posts.json": "inspired_posts.csv",
    "rated_posts.json": "rated_posts.csv",
    "all_posts.json": "all_posts.csv",
    "all_users.json": "all_users.csv",
}

# Convert each JSON to CSV
for json_file, csv_file in file_mapping.items():
    convert_json_to_csv(json_file, csv_file)

print("All JSON files have been converted to CSV.")
