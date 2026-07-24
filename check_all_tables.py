import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""", conn)

print("Tables:\n")
print(tables)

for table in tables["name"]:
    print(f"\n===== {table} =====")
    cols = pd.read_sql(f"PRAGMA table_info({table});", conn)
    print(cols[["name", "type"]])

conn.close()