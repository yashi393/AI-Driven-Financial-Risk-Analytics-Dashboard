# 💳 AI-Driven Financial Risk & Investor Behavior Analytics Dashboard

## 📌 Project Overview

This project combines **Data Analytics, Business Intelligence, and Machine Learning** to analyze financial transaction behavior, identify operational risks, and generate AI-powered transaction risk scores.

The solution was developed using **Python, Pandas, Scikit-Learn, Power BI, and DAX** to transform raw transaction data into actionable business insights and executive-level dashboards.

---

## 🎯 Business Problem

Financial institutions process millions of transactions every day. Understanding customer spending patterns, merchant performance, transaction failures, and operational risks is critical for informed decision-making.

The objective of this project was to:

* Analyze customer spending behavior
* Identify high-value merchants
* Monitor transaction failures and refunds
* Evaluate payment method performance
* Predict transaction failure risk using Machine Learning
* Build an executive-ready analytics dashboard

---

## 📊 Dataset Information

| Metric                | Value                  |
| --------------------- | ---------------------- |
| Original Dataset Size | 13+ Million Records    |
| Working Sample Size   | 50,000 Transactions    |
| Time Period           | 2010 - 2019            |
| Domain                | Financial Transactions |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Power BI
* DAX
* GitHub

---

# 🔧 Data Preparation

## Data Cleaning

Performed extensive preprocessing including:

* Missing value handling
* Data type conversions
* Duplicate validation
* Transaction status standardization

Created additional flags:

* Error Flag
* Refund Flag
* Weekend Flag

Generated time-based features:

* Year
* Month
* Month Name
* Quarter
* Weekday
* Hour

---

## Feature Engineering

### Customer Summary Dataset

Generated customer-level metrics:

* Total Transactions
* Total Spend
* Average Transaction Value
* Refund Count
* Failed Transactions
* Customer Activity Level

Customer Segments:

* Low Activity
* Medium Activity
* High Activity

---

### Merchant Summary Dataset

Generated merchant-level metrics:

* Total Revenue
* Total Transactions
* Average Transaction Value
* Refund Count
* Failed Transactions

---

### Monthly KPI Dataset

Created monthly business KPIs:

* Total Transactions
* Total Spend
* Average Transaction Amount
* Refund Transactions
* Failed Transactions

---

# 📈 Power BI Dashboard

The dashboard consists of four business-focused pages.

---

## 1️⃣ Executive Overview

Provides a high-level view of business performance.

### Key Metrics

* Total Transactions
* Total Spend
* Average Transaction Value
* Failed Transactions
* Refund Transactions

### Visualizations

* Monthly Spending Trend
* Monthly Transaction Trend
* Payment Method Distribution

### Dashboard Screenshot

![Executive Overview](https://github.com/yashi393/AI-Driven-Financial-Risk-Analytics-Dashboard/blob/main/screenshots/Executive%20Summary.png?raw=true)

---

## 2️⃣ Customer & Merchant Insights

Analyzes customer behavior and merchant performance.

### Visualizations

* Top Customers by Spend
* Customer Activity Distribution
* Top Merchants by Revenue
* Activity Level vs Spending

### Key Finding

More than 95% of total spending originates from Medium and High Activity customers.

### Dashboard Screenshot

![Customer Merchant Insights](https://github.com/yashi393/AI-Driven-Financial-Risk-Analytics-Dashboard/blob/main/screenshots/Customer%20&%20Merchant%20Insights.png?raw=true)

---

## 3️⃣ Risk & Payment Analytics

Provides operational risk visibility.

### Visualizations

* Transaction Failure Reasons
* Failed vs Successful Transactions
* Refund Analysis
* Payment Method Risk Analysis

### Key Findings

* Insufficient Balance is the most common transaction failure reason.
* Refund transactions represent approximately 5% of all transactions.

### Dashboard Screenshot

![Risk Analytics](https://github.com/yashi393/AI-Driven-Financial-Risk-Analytics-Dashboard/blob/main/screenshots/Risk%20&%20Payment%20Analytics.png?raw=true)

---

## 4️⃣ AI Risk Analytics

Machine Learning-powered transaction risk monitoring.

### Features

* Risk Category Distribution
* Average Risk Score by Payment Method
* Risk Score Trend Analysis
* High-Risk Transaction Monitoring

### Dashboard Screenshot

![AI Risk Analytics](https://github.com/yashi393/AI-Driven-Financial-Risk-Analytics-Dashboard/blob/main/screenshots/AI%20Risk%20Analytics.png?raw=true)

---

# 🤖 Machine Learning Model

## Objective

Predict transaction failure risk and generate transaction-level risk scores.

---

## Target Variable

Transaction Failure

* Successful Transaction = 0
* Failed Transaction = 1

---

## Class Distribution

| Class      | Count  |
| ---------- | ------ |
| Successful | 49,219 |
| Failed     | 781    |

The dataset was highly imbalanced, with only 1.56% failed transactions.

---

## Features Used

### Numerical Features

* Amount
* Hour
* Month
* Quarter
* Weekend Flag

### Categorical Features

* Payment Method
* Weekday
* Merchant Category Code (MCC)
* Merchant State

---

## Model Selection

### Logistic Regression

Chosen because:

* Produces probability outputs
* Generates interpretable risk scores
* Performs well for binary classification problems
* Suitable for business risk analysis

Class imbalance was handled using:

```python
class_weight='balanced'
```

---

## Risk Scoring

Generated transaction-level probabilities using:

```python
risk_score = model.predict_proba(X)[:,1]
```

Transactions were categorized as:

| Risk Score  | Category    |
| ----------- | ----------- |
| 0.00 - 0.30 | Low Risk    |
| 0.30 - 0.70 | Medium Risk |
| 0.70 - 1.00 | High Risk   |

---

## Risk Distribution

| Category    | Count  |
| ----------- | ------ |
| Low Risk    | 9,653  |
| Medium Risk | 37,564 |
| High Risk   | 2,783  |

---

# 📌 Key Business Insights

### Customer Behavior

* Medium and High Activity customers contribute over 95% of total spending.
* Customer spending is concentrated among a relatively small segment of highly active users.

### Merchant Performance

* A small number of merchants contribute a significant portion of overall revenue.
* Merchant concentration highlights potential business dependency risks.

### Operational Risk

* Insufficient Balance is the leading transaction failure reason.
* Swipe transactions account for the largest transaction volume.

### AI Insights

* Machine Learning-generated risk scores enable proactive identification of potentially risky transactions.
* High-risk transaction monitoring can support fraud prevention and operational risk management initiatives.

---

# 🏗️ Project Architecture

Raw Transaction Data

⬇

Data Cleaning & Preprocessing

⬇

Feature Engineering

⬇

Exploratory Data Analysis

⬇

Machine Learning Model

⬇

Risk Score Generation

⬇

Power BI Dashboard

⬇

Business Insights & Decision Support

---

# 📂 Repository Structure

```text
AI-Driven-Financial-Risk-Analytics-Dashboard

│
├── Dashboard
│   └── Financial_Risk_Dashboard.pbix
│
├── Data
│   ├── customer_summary.csv
│   ├── merchant_summary.csv
│   ├── monthly_kpi.csv
│   ├── payment_summary.csv
│   ├── risk_summary.csv
│   └── transaction_risk_predictions.csv
│
├── Notebooks
│   ├── Data_Cleaning.ipynb
│   ├── Feature_Engineering.ipynb
│   └── Risk_Model.ipynb
│
├── Screenshots
│   ├── Executive_Overview.png
│   ├── Customer_Merchant_Insights.png
│   ├── Risk_Analytics.png
│   └── AI_Risk_Analytics.png
│
└── README.md
```

---

# 🚀 Project Highlights

✅ Data Cleaning & Preprocessing

✅ Feature Engineering

✅ Exploratory Data Analysis

✅ Power BI Dashboard Development

✅ DAX Measures

✅ Machine Learning Model

✅ Transaction Risk Scoring

✅ End-to-End Analytics Pipeline

---

## 👤 Author

Yashi Depani

Aspiring Data Analyst | Business Intelligence Enthusiast | Machine Learning Practitioner

Feel free to connect and provide feedback on the project.
