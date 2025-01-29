# **Code Documentation: AI Chatbot Impact Analysis & Data Cleaning**

## **Overview**
This document provides a detailed breakdown of the Python code used throughout the AI chatbot impact analysis and data cleaning process. It covers:
- **Data Import & Inspection**
- **Data Cleaning & Anomaly Fixing**
- **AI-Based Projections for Efficiency Gains**
- **Cost Savings Estimations**
- **Visualizations**

---

## **1. Data Import & Inspection**
```python
import pandas as pd

# Load the dataset
file_path = "customer_support_tickets.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
df.head()
```
**Purpose:**
- Imported the dataset to explore ticket statuses and response times.
- Initial inspection revealed timestamp inconsistencies in resolution times.

---

## **2. Data Cleaning & Fixing Timestamp Anomalies**
```python
# Convert time columns to datetime format
df["First Response Time"] = pd.to_datetime(df["First Response Time"], errors='coerce')
df["Time to Resolution"] = pd.to_datetime(df["Time to Resolution"], errors='coerce')

# Filter out incorrect entries where resolution time is earlier than first response time
df_cleaned = df[df["Time to Resolution"] > df["First Response Time"]]

# Calculate resolution duration in hours
df_cleaned["Resolution Duration"] = (df_cleaned["Time to Resolution"] - df_cleaned["First Response Time"]).dt.total_seconds() / 3600
```
**AI Assistance:** Used AI-powered debugging to quickly detect and correct inconsistent timestamps.

---

## **3. AI-Based Projections for Efficiency Gains**
```python
# Current ticket closure rate
current_closure_rate = (df_cleaned[df_cleaned["Ticket Status"] == "Closed"].shape[0] / len(df_cleaned)) * 100

# Projected AI closure rate (Industry Benchmark: ~67%)
ai_closure_rate = 67

# Resolution Time Improvement (AI speeds up by 50%)
ai_resolution_time = df_cleaned["Resolution Duration"].mean() * 0.5
```
**Purpose:**
- Used industry benchmarks to estimate AI’s impact on resolution rates and response efficiency.

---

## **4. Cost Savings Estimation**
```python
# Assumptions (Industry Benchmarks)
cost_per_human_ticket = 5.00  # $5 per human-handled ticket
cost_per_ai_ticket = 0.60  # AI-handled ticket cost

total_tickets = len(df_cleaned)
current_total_cost = total_tickets * cost_per_human_ticket
ai_tickets_handled = total_tickets * (ai_closure_rate / 100)
ai_total_cost = ai_tickets_handled * cost_per_ai_ticket

cost_savings = current_total_cost - ai_total_cost
```
**Findings:** AI could save approximately **$38,940 per month** in support costs.

---

## **5. Visualizations**
```python
import matplotlib.pyplot as plt

# Closure Rate Comparison
categories = ["Current Closure Rate", "AI Projected Closure Rate"]
values = [current_closure_rate, ai_closure_rate]

plt.figure(figsize=(8, 5))
plt.bar(categories, values)
plt.ylabel("Closure Rate (%)")
plt.title("Current vs. AI Projected Closure Rates")
plt.show()
```
**Purpose:** Created visuals to showcase improvements in efficiency, cost savings, and response time.

---

## **Conclusion**
This documentation highlights how Python and AI-assisted debugging were used to clean, analyze, and project the impact of AI-driven customer support enhancements. It showcases proficiency in **data wrangling, predictive modeling, and visualization techniques**, making it a valuable addition to the portfolio.

