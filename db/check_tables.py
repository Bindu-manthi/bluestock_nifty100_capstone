import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "financial_ratios"
]

for table in tables:
    print(f"\n========== {table.upper()} ==========")

    cursor.execute(f"PRAGMA table_info({table})")

    for column in cursor.fetchall():
        print(column[1])

conn.close()