# DataChain-Predict: Supply Chain Analytics & GenAI Integration

## 📌 Project Overview
DataChain-Predict is an advanced **supply chain analytics platform** that leverages **data science, visualization, and Generative AI** to provide actionable insights into logistics, sales, and order management.

This project integrates:
- **PostgreSQL** for structured data storage.
- **Power BI** for interactive supply chain analytics.
- **Generative AI (Coming Soon)** for predictive insights.

---

## 🚀 Features
### **🔹 Data Cleaning & Preprocessing**
- Cleans raw supply chain data from **DataCo Smart Supply Chain dataset**.
- Handles **missing values, outliers, and incorrect data types**.
- Computes **new features like delivery delay, profit margin, and risk scores**.

### **🔹 Data Storage (PostgreSQL)**
- Stores structured supply chain data in **PostgreSQL**.
- Supports **fast querying & scalability** for analytics.

### **🔹 Business Intelligence (Power BI/Tableau)**
- Connects **Power BI/Tableau** to PostgreSQL for **interactive dashboards**.
- Visualizes **sales trends, order fulfillment, profit analysis, and delivery delays**.

### **🔹 AI Integration (Coming Soon)**
- Leverages **GenAI** for **predictive risk analysis & demand forecasting**.
- Automates **supply chain decision-making** with **AI-powered recommendations**.

---

## 🔧 Setup Guide
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Saurabh24k/DataChain-Predict.git
cd DataChain-Predict
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Install PostgreSQL (If Not Installed)**
#### **Mac (Homebrew)**
```sh
brew install postgresql
brew services start postgresql
```
#### **Windows**
- Download and install from [PostgreSQL Official Site](https://www.postgresql.org/download/).

### **4️⃣ Restore PostgreSQL Database**
```sh
pg_restore -U supply_admin -d supply_chain data/supply_chain_backup.dump
```
Check if tables exist:
```sql
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM access_logs;
```

### **5️⃣ Connect Power BI**
- Open Power BI → Get Data → **PostgreSQL**
- Use credentials:
  - **Server:** `localhost`
  - **Database:** `supply_chain`
  - **User:** `supply_admin`
  - **Port:** `5432`

Refer to **setup_instructions.md** for detailed steps.

---

## 📊 Power BI Dashboards
- **Key Metrics:** Total Sales, Orders, Profit, Late Deliveries
- **Sales Analysis:** Monthly trends, top-selling categories
- **Delivery Performance:** Average delays, heatmaps

---

## 🤖 AI Features (Upcoming)
- **Demand Forecasting** using GenAI
- **Predictive Order Risk Analysis**
- **Intelligent Supply Chain Optimization**

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 💬 Need Help?
For issues, create an **Issue** on [GitHub](https://github.com/Saurabh24k/DataChain-Predict/issues) or reach out to the contributors.

---

**🚀 Get Started & Transform Your Supply Chain with AI-Driven Insights!**

