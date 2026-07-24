import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    company_id,
    year,
    return_on_equity_pct,
    operating_profit_margin_pct
FROM financial_ratios
WHERE
    ABS(return_on_equity_pct) > 200
    OR ABS(operating_profit_margin_pct) > 200
ORDER BY company_id;
"""

df = pd.read_sql(query, conn)

conn.close()

print(df)
print("\nRows:", len(df))