# House-Price-Prediction-System-End-to-End-Machine-Learning-Project-
This repository contains a data  project, including datasets, preprocessing, EDA, visualizations, and insights using Python.
# 🏠 House Price Prediction System (End-to-End Machine Learning Project)

## 📌 Project Overview

This project builds a complete **Machine Learning system** that predicts house prices based on property characteristics such as area, number of bedrooms, bathrooms, location, property type, and property age.

The system demonstrates a full **Data Science workflow** including:

* Data collection and preprocessing
* Exploratory data analysis
* Feature engineering
* Model training and evaluation
* Model serialization
* Deployment using a simple Flask web application

The final application allows users to enter house details through a web interface and receive an estimated house price.

---

# 🎯 Business Problem

Real estate companies and buyers often struggle to estimate fair property prices. Manual valuation is slow and subjective.

This system uses **machine learning to automatically predict house prices**, helping:

* Real estate companies
* Property investors
* Home buyers
* Market analysts

make faster and more data-driven decisions.

---

# 🧠 Machine Learning Workflow

The system follows the standard **Data Science lifecycle**:

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Saving
8. Deployment with Web Interface

---

# 📊 Dataset

The dataset contains property information used to predict house prices.

### Example Features

| Feature       | Description                  |
| ------------- | ---------------------------- |
| Area          | Size of the house (sq ft)    |
| Bedrooms      | Number of bedrooms           |
| Bathrooms     | Number of bathrooms          |
| Age           | Age of the property          |
| Location      | Rural / Suburb / City Center |
| Property_Type | Apartment / House / Villa    |
| Price         | Target variable              |

---

# 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Deployment

* Flask

### Model Storage

* Joblib

---

# 📈 Exploratory Data Analysis

EDA was performed to understand relationships between variables.

Key analyses include:

* Price distribution visualization
* Correlation heatmap
* Feature relationships

These insights help identify important predictors for house price.

---

# ⚙️ Data Preprocessing

The following preprocessing steps were applied:

* Handling missing values
* Encoding categorical variables using **LabelEncoder**
* Removing unnecessary columns
* Feature selection
* Train-test split

---

# 🤖 Model Training

A **Linear Regression model** was used for price prediction.

### Training Steps

1. Split dataset into training and testing data
2. Train model using training data
3. Generate predictions
4. Evaluate model performance

---

# 📊 Model Evaluation

Model performance was evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics measure prediction accuracy and model reliability.

---

# 💾 Model Saving

The trained model and encoders were saved using **Joblib**:

* `house_price_model.pkl`
* `location_encoder.pkl`
* `property_encoder.pkl`

This allows the model to be reused during deployment.

---

# 🌐 Web Application

A simple **Flask web interface** allows users to input property details and get price predictions.

### Features

* Input house details
* Send data to ML model
* Display predicted price instantly

---

# 📁 Project Structure

```
house_price_prediction_project
│
├── house_prices.csv
├── notebook.ipynb
├── house_price_model.pkl
├── location_encoder.pkl
├── property_encoder.pkl
├── app.py
│
├── templates
│     └── index.html
│
└── README.md
```

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask joblib
```

---

## 3️⃣ Train the Model

Run the Jupyter notebook:

```
notebook.ipynb
```

This will generate the trained model files.

---

## 4️⃣ Run the Web Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

# 📷 Application Interface

Users enter property details and the system predicts the estimated house price.

---

# 🔮 Future Improvements

Possible improvements include:

* Using advanced models (Random Forest, XGBoost)
* Adding feature scaling and pipelines
* Deploying using **Streamlit**
* Hosting on **AWS / Render / Heroku**
* Adding real-time property datasets
* Building a full dashboard for market analysis

---

# 👨‍💻 Author

**Ranganathan**

Data Analytics / Data Science Enthusiast
Focused on building practical machine learning systems.

---
