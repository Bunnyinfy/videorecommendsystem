import requests
import json
import pandas as pd

# API endpoints and their corresponding filenames
api_endpoints = {
    "viewed_posts": "https://api.socialverseapp.com/posts/view?page={page}&page_size=1000",
    "liked_posts": "https://api.socialverseapp.com/posts/like?page={page}&page_size=1000",
    "inspired_posts": "https://api.socialverseapp.com/posts/inspire?page={page}&page_size=1000",
    "rated_posts": "https://api.socialverseapp.com/posts/rating?page={page}&page_size=1000",
    "all_posts": "https://api.socialverseapp.com/posts/summary/get?page={page}&page_size=1000",
    "all_users": "https://api.socialverseapp.com/users/get_all?page={page}&page_size=1000",
}

# Authorization header
headers = {
    "Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
}


def fetch_api_data(endpoint, filename):
    """Fetch data from the API endpoint with pagination and save to file."""
    all_data = []
    page = 1

    while True:
        print(f"Fetching page {page} for {filename}...")
        response = requests.get(endpoint.format(page=page), headers=headers)

        if response.status_code != 200:
            print(f"Error fetching data for {filename}: {response.status_code}")
            break

        data = response.json()

        # Check if data exists
        if not data.get("data"):
            print(f"No more data for {filename}.")
            break

        # Append data
        all_data.extend(data["data"])
        page += 1

    # Save to JSON
    json_filename = f"{filename}.json"
    with open(json_filename, "w") as file:
        json.dump(all_data, file)
    print(f"Saved data to {json_filename}.")

    # Save to CSV
    csv_filename = f"{filename}.csv"
    df = pd.DataFrame(all_data)
    df.to_csv(csv_filename, index=False)
    print(f"Saved data to {csv_filename}.")


# Fetch data for all endpoints
for name, endpoint in api_endpoints.items():
    fetch_api_data(endpoint, name)
