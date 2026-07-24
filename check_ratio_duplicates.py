import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    year,
    COUNT(*) AS cnt
FROM financial_ratios
GROUP BY company_id, year
HAVING COUNT(*) > 1
ORDER BY cnt DESC, company_id;
""", conn)

print(df)

conn.close()