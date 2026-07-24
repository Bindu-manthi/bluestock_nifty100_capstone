import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN revenue_cagr_5yr IS NOT NULL THEN 1 ELSE 0 END) AS revenue_cagr,
    SUM(CASE WHEN pat_cagr_5yr IS NOT NULL THEN 1 ELSE 0 END) AS pat_cagr,
    SUM(CASE WHEN fcf_cagr_5yr IS NOT NULL THEN 1 ELSE 0 END) AS fcf_cagr,
    SUM(CASE WHEN composite_quality_score IS NOT NULL THEN 1 ELSE 0 END) AS quality_score
FROM financial_ratios;
""", conn)

print(df)

conn.close()