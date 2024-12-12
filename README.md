
# Video Recommendation System

A **Video Recommendation System** built using the **Surprise** library, **Streamlit** for interactive deployment and **flask** for api implementation. The system provides personalized video recommendations based on user viewing history. It leverages collaborative filtering using the Singular Value Decomposition (SVD) algorithm.

## Features:
- **User-Based Recommendations**: Suggests posts that a user is likely to interact with based on their past interactions and similarities with other users.
- **CSV Upload**: Users can upload their own CSV data containing user interactions (user_id, post_id, viewed).
- **Model Training & Prediction**: The system can either load an existing model or train a new model using the uploaded data.

---

## Requirements

To run the project, you'll need the following libraries:

- `streamlit` — for building the web interface.
- `pandas` — for data manipulation and analysis.
- `surprise` — for building and evaluating the recommendation model.
- `pickle` — for saving and loading the trained model.
- `flask` - api implementation
  
You can install the required libraries using:

```bash
pip install streamlit pandas surprise
```

---

## Project Structure

The project is structured as follows:

```
/video-recommendation-system
│
├── /modelprep
│   └── model.py          # Model training and saving script
│
├── /recsys
│   ├── /Lib              # Virtual environment libraries
│   └── /site-packages    # Installed packages
│
├── app.py                # Streamlit app to interact with users
├── model.pkl             # Pre-trained model (if available)
├── data.csv              # Sample data (optional)
└── README.md             # Project documentation
```

---

## CSV Data Format

The CSV file used for the recommendation system should contain the following columns:

- **user_id**: A unique identifier for each user.
- **post_id**: A unique identifier for each post (video/content).
- **viewed**: A binary value (0 or 1) indicating whether the user has viewed the post (`1` for viewed, `0` for not viewed).
- **mood**

### Example Data (`data.csv`):

```csv
user_id,post_id,viewed,mood
1,101,1,happy
1,102,0,sad
1,103,1,joy
2,101,0,sad
2,102,1,joy
2,103,1,sad
3,101,1,happy
3,103,0,joy
```

---

## How to Run the Application

1. **Train a Model or Load an Existing Model**:
   - The app allows you to either train a new model using the uploaded data or load a pre-trained model.
   
2. **Upload Your CSV Data**:
   - Use the Streamlit interface to upload a CSV file containing `user_id`, `post_id`, and `viewed` columns.
   
3. **Get Recommendations**:
   - After uploading the data and training the model, input the **User ID** to get personalized recommendations.

4. **Streamlit Interface**:
   - Run the Streamlit app with the following command:
   
   ```bash
   streamlit run app.py
   ```

---

## Code Explanation

### 1. **Model Training (model.py)**

In the `model.py` file, the model is trained using the **SVD (Singular Value Decomposition)** algorithm from the **Surprise** library.

#### Key Steps:
- Load the data from a CSV file.
- Preprocess the data to extract necessary columns (`user_id`, `post_id`, `viewed`).
- Train the model using the **SVD** algorithm.
- Save the trained model to a `model.pkl` file.



### 2. **Streamlit (app.py)**

The `app.py` file builds an interactive interface using **Streamlit**. Users can upload their data, train the model, and get recommendations.

#### Key Steps:
- Upload a CSV file containing user interaction data.
- Load or train the recommendation model.
- Provide a user ID to get video post recommendations.
- Display the top 5 recommended posts.

## Evaluation & Tuning

You can evaluate and tune the model by using different algorithms or tuning hyperparameters. The **Surprise** library offers tools like **GridSearchCV** for hyperparameter tuning and cross-validation for model evaluation.

For instance, to fine-tune the SVD model, you can adjust parameters like the number of factors (`n_factors`), learning rate (`lr_all`), and regularization (`reg_all`).

---

## Future Enhancements

- **Hybrid Recommendation**: Combine collaborative filtering with content-based filtering for more accurate recommendations.
- **Scalability**: Improve model scalability for larger datasets.
- **Model Evaluation Metrics**: Implement additional evaluation metrics like **F1-Score**, **Precision**, and **Recall**.

---
Here is a clear, step-by-step documentation of the approach, model architecture, and key decisions made during development, along with the implementation of the three API endpoints you requested.

---

# **Step-by-Step Documentation for the Video Recommendation System**

## **Approach**

1. **Data Collection**:
   The first step involves gathering user interaction data. The data should contain:
   - `user_id`: A unique identifier for each user.
   - `post_id`: A unique identifier for each post (e.g., a video or piece of content).
   - `viewed`: A binary value (0 or 1) indicating whether the user has interacted with the post.

   The data is loaded into a DataFrame using pandas, and the interaction information is used to create a user-item interaction matrix for the recommendation system.

2. **Data Preprocessing**:
   - The interaction data is processed into a format that can be fed into the **Surprise** library, which is used for building collaborative filtering models.
   - The data is then split into training and test sets.

3. **Model Architecture**:
   - **Collaborative Filtering**: The model used is based on **Singular Value Decomposition (SVD)**, a matrix factorization technique. SVD decomposes the interaction matrix into latent factors that can predict missing interactions (ratings).
   - The **Surprise** library provides a built-in SVD implementation that works well with collaborative filtering tasks.
   - The model is trained using the user-item interaction data and is saved using the **pickle** library for later use.

4. **Recommendation Generation**:
   - The model makes predictions for unseen posts (posts that the user has not interacted with yet) based on learned latent factors.
   - The top N recommendations are generated by sorting the predicted ratings in descending order.

5. **Deployment with Streamlit**:
   - The Streamlit app provides a simple interface where users can upload CSV data, train the recommendation model, and view personalized recommendations.

---

## **Key Decisions Made During Development**

1. **Collaborative Filtering**: Collaborative filtering was chosen because it doesn't require additional information about posts (e.g., content metadata) and can generate recommendations purely based on user interactions.
   
2. **SVD (Singular Value Decomposition)**: SVD was selected as the algorithm for matrix factorization because it's widely used in collaborative filtering tasks and provides efficient recommendations with relatively small datasets.

3. **User-Based Recommendations**: Recommendations are based on users' past interactions, ensuring that the system gives personalized content based on users' historical data.

4. **Model Storage**: The trained model is saved using **pickle** to avoid retraining the model every time the system is used, making it more efficient.

---

## **API Implementation**

We'll be using **Flask** for creating the API. Below is the code to implement the API endpoints you requested:

### **1. Install Necessary Packages**

First, you need to install the required packages:

```bash
pip install flask pandas surprise pickle-mixin
```

### **2. API Code Implementation**


---

## **API Endpoints**

### **1. Recommendations based on username, category_id, and mood**

**URL**: `http://localhost:5000/feed?username=your_username&category_id=category_id_user_want_to_see&mood=user_current_mood`

**Parameters**:
- `username`: The username of the user requesting recommendations.
- `category_id`: The ID of the category the user is interested in.
- `mood`: The mood of the user (optional).

**Example**:

```http
GET http://localhost:5000/feed?username=johndoe&category_id=2&mood=happy
```

### **2. Recommendations based on username and category_id**

**URL**: `http://localhost:5000/feed?username=your_username&category_id=category_id_user_want_to_see`

**Parameters**:
- `username`: The username of the user requesting recommendations.
- `category_id`: The ID of the category the user is interested in.

**Example**:

```http
GET http://localhost:5000/feed?username=johndoe&category_id=2
```

### **3. Recommendations based on username only**

**URL**: `http://localhost:5000/feed?username=your_username`

**Parameters**:
- `username`: The username of the user requesting recommendations.

**Example**:

```http
GET http://localhost:5000/feed?username=johndoe
```

---

## **Conclusion**

This documentation provides a clear explanation of the approach, model architecture, key decisions made during the development, and details of the three API endpoints for generating video post recommendations.

- **Collaborative Filtering** and **SVD** were used to build the recommendation system.
- Three API endpoints were created to provide personalized recommendations for users based on their username, category, and mood.
  
These endpoints can be used for delivering personalized content recommendations to users in different scenarios.



---
