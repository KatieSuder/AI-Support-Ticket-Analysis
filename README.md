# **AI Chatbot Impact on Customer Support - Data Analysis & Visualization**

## **Project Overview**
This project analyzes **customer support ticket data** to evaluate the potential impact of **AI chatbots** on **resolution rates, response times, customer satisfaction, and cost savings**. The analysis includes **data cleaning, AI-driven projections, and visualizations** to support decision-making for AI adoption in customer support.

## **Key Findings**
- **AI chatbots could improve ticket closure rates** from **33% to ~67%**.
- **AI reduces resolution time** from **7.59 hours to ~3.80 hours**.
- **Projected cost savings:** ~$38,940 per month.
- **Customer satisfaction score projected to increase** from **2.99 to 3.44**.

## **Table of Contents**
- [Data Analysis Process](#data-analysis-process)
- [Technologies Used](#technologies-used)
- [Project Files](#project-files)
- [How to Run the Analysis](#how-to-run-the-analysis)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)

---

## **Data Analysis Process**
### **1. Data Cleaning & Preparation**
- Converted timestamps to **datetime format**.
- Identified and **removed invalid timestamps** where resolution time was before response time.
- Calculated **ticket resolution duration** in hours.

### **2. AI Projections**
- Applied **industry benchmarks** for AI chatbot performance.
- **Closure rate increase:** From **33% → 67%**.
- **Time reduction:** AI reduces resolution time by **50%**.

### **3. Cost Savings Analysis**
- Assumed **$5 per human-handled ticket** and **$0.60 per AI-handled ticket**.
- AI-driven support estimated to save **~$38,940 per month**.

### **4. Visualizations & Insights**
- **Bar charts comparing current vs. AI closure rates, resolution times, and cost savings.**

---

## **Technologies Used**
- **Python (pandas, matplotlib)** for data cleaning and analysis.
- **GitHub** for project hosting and documentation.
- **Tableau / Power BI (Optional)** for interactive dashboards.

---

## **Project Files**
- 📄 [Data Analysis Breakdown](./data_analysis_breakdown.md) – **Step-by-step analysis & code.**
- 📊 [Visuals & Charts](./visuals/) – **Graphs & insights.**
- 📜 [Python Code for Analysis](./ai_chatbot_code.py) – **Data cleaning & projections.**

---

## **How to Run the Analysis**
1. Clone this repository:
   ```sh
   git clone https://github.com/katiesuder/AI-Support-Ticket-Analysis.git
   ```
2. Install dependencies:
   ```sh
   pip install pandas matplotlib
   ```
3. Run the Jupyter Notebook or Python script to reproduce the findings.

---

## **Visualizations**
| **Metric**           | **Current** | **Projected (AI Chatbots)** |
|---------------------|------------|------------------------|
| Closure Rate       | 33%        | 67%                    |
| Resolution Time    | 7.59 hrs   | 3.80 hrs               |
| Cost Per Month    | $42,345    | $3,404                 |
| Cost Savings       | -          | $38,940                |
| Customer Satisfaction | 2.99    | 3.44                    |

Here are key insights from our analysis:

### **1. Closure Rate Comparison**
📊 AI chatbots are projected to **double the closure rate** from 33% to 67%.
![Closure Rate](./visuals/closure_rate_comparison.png)

### **2. Impact of AI on Resolution Time**
⏳ AI is expected to **cut resolution time in half**.
![Resolution Time](./visuals/resolution_time_comparison.png)

### **3. Estimated Cost Savings**
💰 AI-driven support could save **~$38,940 per month**.
![Cost Savings](./visuals/cost_savings_comparison.png)

---

## **Conclusion**
AI chatbots have the potential to **transform customer support operations** by improving **efficiency, cost-effectiveness, and customer satisfaction**. This analysis provides **data-driven insights** to support AI adoption in customer service teams.

**Next Steps:**
- Deploy **a pilot AI chatbot program**.
- Measure **real-world AI vs. human support performance**.
- Optimize **chatbot efficiency based on feedback**.

---

### **🚀 Connect & Collaborate**
For questions, feel free to reach out via **GitHub Issues** or **LinkedIn**!

---

