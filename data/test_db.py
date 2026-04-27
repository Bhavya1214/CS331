from db import get_connection

try:
    conn = get_connection()
    print("✅ Connected successfully")
except Exception as e:
    print("❌ Error:", e)