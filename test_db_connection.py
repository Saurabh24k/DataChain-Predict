import psycopg2

try:
    conn = psycopg2.connect(
        dbname="supply_chain",
        user="supply_admin",
        password="your_password",
        host="localhost",
        port="5432"
    )
    print("✅ Connected to PostgreSQL successfully!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")

