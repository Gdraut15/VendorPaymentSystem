from config.db_config import create_connection

try:
    conn = create_connection()
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)

