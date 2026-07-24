import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    COUNT(*) AS cnt
FROM sectors
GROUP BY company_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC;
""", conn)

print(df)

conn.close()