# Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

A machine learning project that predicts whether a telecom customer is likely to churn (leave the company), based on their account information, services subscribed, and billing details. Built as an end-to-end project — from data cleaning and exploratory analysis to model training and a live, interactive web app.

**Live App:** [prakhar-customer-churn-prediction.streamlit.app](https://prakhar-customer-churn-prediction-ximn9yvwnskf2klk4azbak.streamlit.app/)

---

## 📝 Overview

Customer churn is one of the most common and costly problems for subscription-based businesses. This project analyzes the Telco Customer Churn dataset (7,043 customers) to understand **why** customers leave, and builds a classification model to **predict** which customers are at risk — so a business could act early to retain them.

---

## ✨ Features

- 🧹 Cleaned and preprocessed a real-world dataset of 7,043 customers, handling missing values and data type issues
- 📊 Performed in-depth exploratory data analysis (EDA) separately on numerical and categorical features
- 🔍 Identified key churn drivers using visualizations (contract type, internet service, payment method, tenure, charges)
- 🔢 Encoded categorical features and trained two classification models (Logistic Regression, Random Forest)
- 📈 Evaluated models using accuracy, precision, recall, F1-score, and confusion matrix
- ⭐ Extracted feature importance to explain which factors matter most for churn
- 🖥️ Built an interactive Streamlit web app for real-time churn prediction
- 🚀 Deployed the app publicly using Streamlit Community Cloud

---

## 📁 Project Structure

```
customer-churn-prediction/
├── churn.csv                          # Raw dataset
├── churn_cleaned.csv                  # Cleaned dataset (output of Part 1)
├── part1_data_cleaning_eda.ipynb      # Data cleaning + exploratory data analysis
├── part2_model_training_testing.ipynb # Feature encoding, model training, evaluation
├── app.py                             # Streamlit web app
├── requirements.txt                   # Python dependencies
├── churn_model.pkl                    # Trained Random Forest model
├── encoders.pkl                       # Saved LabelEncoders for categorical columns
├── columns.pkl                        # Column order expected by the model
└── README.md
```

---

## 📦 Dataset

- **Source:** Telco Customer Churn dataset (IBM Sample Data)
- **Size:** 7,043 customers, 21 columns
- **Target variable:** `Churn` (Yes/No)

**Features include:**
- Demographics: gender, senior citizen status, partner, dependents
- Account info: tenure, contract type, payment method, monthly/total charges
- Services: phone, internet, online security, tech support, streaming TV/movies, etc.

---

## 🔎 Key Insights from EDA

**Overall churn rate: 26.45%** (1,857 out of 7,021 customers, after cleaning)

| Feature | Highest-Risk Category | Churn Rate |
|---|---|---|
| Contract Type | Month-to-month | 42.64% |
| Internet Service | Fiber optic | 41.78% |
| Payment Method | Electronic check | 45.15% |
| Online Security | Without | 41.63% |
| Tech Support | Without | 41.50% |
| Senior Citizen | Yes | 41.63% |

| Numerical Feature | Churned (avg) | Retained (avg) |
|---|---|---|
| Tenure | 18.1 months | 37.6 months |
| Monthly Charges | ₹74.60 | ₹61.34 |
| Total Charges | ₹1,541.38 | ₹2,554.81 |

**Takeaway:** Churn is concentrated among newer, high-paying customers on flexible month-to-month contracts — especially those without add-on services like online security or tech support.

---

## 🤖 Model Training & Results

Two models were trained and compared: **Logistic Regression** and **Random Forest**.

| Metric | Logistic Regression | Random Forest |
|---|---|---|
| Accuracy | ~80% | ~78% |
| Precision | ~0.66 | ~0.62 |
| Recall | ~0.53 | ~0.45 |
| F1-score | ~0.59 | ~0.52 |

**Top predictive features (Random Forest):** Total Charges, Tenure, Monthly Charges, Contract Type, Internet Service Type

The **Random Forest model** was chosen for deployment, since it doesn't require feature scaling — keeping the deployed app simpler.

---

## 📸 Screenshots

> Replace the placeholders below with your own screenshots. Take a screenshot of your running app (Streamlit local or the live link), save it inside a folder called `screenshots/` in your repo, then update the paths below to match.

**App — Input Form**
![App Form](screenshots/app_form.png)

**App — Prediction Result**
![Prediction Result](screenshots/app_result.png)

**EDA — Churn by Contract Type**
![Churn by Contract](screenshots/churn_by_contract.png)

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (Logistic Regression, Random Forest)
- **Model Persistence:** Joblib
- **Web App:** Streamlit
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git, GitHub

---

## ▶️ How to Run Locally

1. Clone this repository
```bash
git clone https://github.com/nitianPRAKHAR/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

4. Open `http://localhost:8501` in your browser

---

## 👤 Author

**Prakhar Bajpai**
B.Tech, Electrical Engineering — National Institute of Technology, Patna
[LinkedIn](https://linkedin.com/in/Prakhar-Bajpai) · [GitHub](https://github.com/nitianPRAKHAR)
