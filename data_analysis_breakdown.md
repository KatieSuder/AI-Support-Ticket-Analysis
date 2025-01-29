Step-by-Step Breakdown: AI Chatbot Data Analysis & Visualization

1. Data Import & Inspection

Goal: Load the dataset and understand its structure.

import pandas as pd

# Load the dataset
file_path = "customer_support_tickets.csv"
df = pd.read_csv(file_path)

# Display the first few rows
df.head()

Findings:

The dataset contains customer support ticket details.

Key columns include "Ticket Status," "First Response Time," "Time to Resolution," and "Customer Satisfaction Rating."

2. Identifying Data Anomalies & Cleaning

Goal: Fix issues like incorrect timestamps.

# Convert timestamps to datetime
df["First Response Time"] = pd.to_datetime(df["First Response Time"], errors='coerce')
df["Time to Resolution"] = pd.to_datetime(df["Time to Resolution"], errors='coerce')

# Remove rows where resolution time is earlier than response time
df_cleaned = df[df["Time to Resolution"] > df["First Response Time"]]

Findings:

Some resolution times were recorded incorrectly (e.g., before first response time).

Cleaning these errors ensured accurate calculations.

3. Calculating Resolution Metrics

Goal: Determine ticket resolution rates and average resolution time.

# Calculate ticket closure rate
closed_tickets = df_cleaned[df_cleaned["Ticket Status"] == "Closed"].shape[0]
total_tickets = len(df_cleaned)
current_closure_rate = (closed_tickets / total_tickets) * 100

# Compute average resolution time in hours
df_cleaned["Resolution Duration"] = (df_cleaned["Time to Resolution"] - df_cleaned["First Response Time"]).dt.total_seconds() / 3600
average_resolution_time = df_cleaned["Resolution Duration"].mean()

Findings:

Current Closure Rate: ~33%

Average Resolution Time: ~7.59 hours

4. Applying AI Projections

Goal: Estimate AI’s impact on support efficiency.

# AI Industry Benchmarks
ai_closure_rate = 67  # AI increases closure rate to ~67%
ai_resolution_time = average_resolution_time * 0.5  # AI reduces resolution time by 50%

Findings:

Projected AI Closure Rate: ~67%

Projected AI Resolution Time: ~3.80 hours

5. Cost Savings Analysis

Goal: Estimate potential cost reduction from AI implementation.

# Assumed costs
cost_per_human_ticket = 5.00  # $5 per human-handled ticket
cost_per_ai_ticket = 0.60  # AI-handled ticket cost

# Current vs. AI-based costs
current_total_cost = total_tickets * cost_per_human_ticket
ai_tickets_handled = total_tickets * (ai_closure_rate / 100)
ai_total_cost = ai_tickets_handled * cost_per_ai_ticket
cost_savings = current_total_cost - ai_total_cost

Findings:

Current Support Costs: ~$42,345 per month

Projected AI Costs: ~$3,404 per month

Estimated Savings: ~$38,940 per month

6. Customer Satisfaction Projection

Goal: Estimate customer satisfaction improvements using AI.

# Current average satisfaction score
average_satisfaction = df_cleaned["Customer Satisfaction Rating"].dropna().mean()

# AI projected satisfaction improvement (~15% increase)
ai_satisfaction_rate = round((average_satisfaction * 1.15), 2)

Findings:

Current Satisfaction Score: ~2.99

Projected AI Satisfaction Score: ~3.44

7. Data Visualizations

Closure Rate Comparison

import matplotlib.pyplot as plt

categories = ["Current Closure Rate", "AI Projected Closure Rate"]
values = [current_closure_rate, ai_closure_rate]

plt.figure(figsize=(8, 5))
plt.bar(categories, values)
plt.ylabel("Closure Rate (%)")
plt.title("Current vs. AI Projected Closure Rates")
plt.show()

Insights:

AI implementation is projected to double the closure rate.

Resolution Time Reduction

categories_time = ["Current Resolution Time", "AI Projected Resolution Time"]
values_time = [average_resolution_time, ai_resolution_time]

plt.figure(figsize=(8, 5))
plt.bar(categories_time, values_time, color=["red", "green"])
plt.ylabel("Resolution Time (Hours)")
plt.title("Impact of AI on Resolution Time")
plt.show()

Insights:

AI is projected to cut resolution time in half.

Cost Savings Breakdown

categories_cost = ["Current Cost", "Projected AI Cost", "Estimated Savings"]
values_cost = [current_total_cost, ai_total_cost, cost_savings]

plt.figure(figsize=(8, 5))
plt.bar(categories_cost, values_cost, color=["red", "green", "blue"])
plt.ylabel("Total Cost ($)")
plt.title("Estimated Cost Savings with AI Implementation")
plt.show()

Insights:

AI-driven support is estimated to save ~$38,940 per month.

Conclusion: Impact of AI on Customer Support

Key Takeaways:

✅ AI improves ticket resolution rate from ~33% to ~67%✅ AI reduces resolution time from 7.59 hours to ~3.80 hours✅ Estimated savings of ~$38,940 per month in support costs✅ Projected satisfaction score increase from ~2.99 to ~3.44

Final Thoughts:

This breakdown showcases a complete data analytics workflow, combining:

Data cleaning & anomaly detection

AI-driven efficiency projections

Cost-benefit analysis

Data visualization storytelling

This project highlights real-world problem-solving skills and AI’s potential in business operations, making it a strong portfolio piece for tech and analytics roles.