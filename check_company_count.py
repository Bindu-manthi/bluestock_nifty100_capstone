import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(DISTINCT company_id) FROM financial_ratios")
print("Distinct companies:", cur.fetchone()[0])

conn.close()