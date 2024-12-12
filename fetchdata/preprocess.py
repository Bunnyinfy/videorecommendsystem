import os
import pandas as pd

# Directories
csv_dir = "C:\\Users\\srinivas\\OneDrive\\Desktop\\VideoRecommendSystem\\csv_files"
preprocessed_dir = (
    "C:\\Users\\srinivas\\OneDrive\\Desktop\\VideoRecommendSystem\\preprocessed_data"
)

# Ensure the preprocessed directory exists
os.makedirs(preprocessed_dir, exist_ok=True)


# Function to preprocess data
def preprocess_data(csv_path, output_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Drop duplicates if any
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("unknown")

    # Convert categorical columns to numeric (if applicable)
    for col in df.select_dtypes(include=["object"]).columns:
        if df[col].nunique() < 50:  # Convert only for columns with fewer unique values
            df[col] = df[col].astype("category").cat.codes

    # Save the preprocessed file
    df.to_csv(output_path, index=False)
    print(f"Preprocessed {os.path.basename(csv_path)} and saved to {output_path}")


# List of CSV files to preprocess
csv_files = [
    "viewed_posts.csv",
    "liked_posts.csv",
    "inspired_posts.csv",
    "rated_posts.csv",
    "all_posts.csv",
    "all_users.csv",
]

# Preprocess each file
for file in csv_files:
    csv_path = os.path.join(csv_dir, file)
    preprocessed_path = os.path.join(preprocessed_dir, f"preprocessed_{file}")
    preprocess_data(csv_path, preprocessed_path)

print("All files have been preprocessed and saved!")
