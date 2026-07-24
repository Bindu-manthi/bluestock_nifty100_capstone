import sqlite3
import pandas as pd
import os

db_path = "data/nifty100.db"

print("Database exists:", os.path.exists(db_path))
print("Absolute path:", os.path.abspath(db_path))

conn = sqlite3.connect(db_path)

tables = pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""", conn)

print("\nTables in database:\n")
print(tables)

conn.close()