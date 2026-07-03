import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    company_id,
    year,
    return_on_equity_pct,
    debt_to_equity
FROM financial_ratios
WHERE return_on_equity_pct > 15
AND debt_to_equity < 1
LIMIT 20;
""")

rows = cursor.fetchall()

print("Companies matching screener:\n")

for row in rows:
    print(row)

conn.close()