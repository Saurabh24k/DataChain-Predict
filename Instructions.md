# Power BI Setup Instructions for Supply Chain Analysis

## 📌 Step 1: Clone the GitHub Repository

To access the project files, follow these steps:

1. Open **Command Prompt (Windows)** or **Terminal (Mac/Linux)**.
2. Run the following command to clone the repository:
   ```sh
   git clone https://github.com/Saurabh24k/DataChain-Predict.git
   ```
3. Navigate into the project directory:
   ```sh
   cd DataChain-Predict
   ```
4. The cleaned data files are located in the **`data/`** folder:
   - `Cleaned_Orders.csv`
   - `Cleaned_Access_Logs.csv`
   - `supply_chain_backup.dump` (PostgreSQL database backup)

---

## 📌 Step 2: Install PostgreSQL (If Not Installed)

Power BI connects to **PostgreSQL** as a data source, so you need to have PostgreSQL installed.

### **Windows Users:**
1. Download PostgreSQL from [PostgreSQL Official Site](https://www.postgresql.org/download/).
2. Install it and set up a **superuser account** (`supply_admin`).
3. Make sure **pgAdmin** is installed for managing the database.


---

## 📌 Step 3: Restore the PostgreSQL Database

To use the existing database backup, restore it with the following command:
```sh
pg_restore -U supply_admin -d supply_chain data/supply_chain_backup.dump
```

After restoring, verify the data using:
```sql
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM access_logs;
```
If the table counts match the expected values, your setup is correct.

---

## 📌 Step 4: Install Power BI PostgreSQL Connector

To connect Power BI to PostgreSQL, install the **ODBC Driver**:
1. **Download PostgreSQL ODBC Driver** from [PostgreSQL ODBC Downloads](https://www.postgresql.org/ftp/odbc/versions/).
2. Install the driver and restart your computer.

---

## 📌 Step 5: Connect Power BI to PostgreSQL

1. Open **Power BI Desktop**.
2. Click **Home** → **Get Data** → **More...**.
3. In the search bar, type **PostgreSQL** and select it.
4. Click **Connect** and enter the following credentials:
   - **Server:** `localhost`
   - **Database:** `supply_chain`
   - **Username:** `supply_admin`
   - **Password:** `your_password`
   - **Port:** `5432`
5. Click **OK** and select the tables (`orders` and `access_logs`).
6. Load the data into Power BI.

---

## 📌 Step 6: Create Power BI Dashboards

### **1️⃣ Key Metrics Dashboard**
- **Total Sales** → `SUM(Sales)`
- **Total Orders** → `COUNT(DISTINCT order_id)`
- **Total Profit** → `SUM(order_profit_per_order)`
- **Late Delivery Rate** → `AVG(late_delivery_risk_score)`

**Chart Type:** Scorecards & Summary Tiles

### **2️⃣ Sales & Profit Analysis**
- **Profitability by Product Category**
- **Top 10 Most Profitable Products**
- **Sales Trend Over Time**

**Chart Type:** Bar Chart, Line Chart

### **3️⃣ Delivery Performance**
- **Average Delivery Delay per Region**
- **Late Delivery Risk Heatmap**

**Chart Type:** Heatmap & Boxplot

---

## 📌 Step 7: Publish & Share the Dashboard

1. Save the Power BI file.
2. Click **Publish** → **Power BI Service**.
3. Share the report link with the me.

---

## ✅ You’re Done!
Your Power BI dashboard should now be fully functional. If you run into any issues, check PostgreSQL connection settings or refresh the data source in Power BI.

Let me know once you complete these steps! 🚀

