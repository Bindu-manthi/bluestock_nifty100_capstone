import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM financial_ratios
LIMIT 5
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()