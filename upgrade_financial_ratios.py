import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

columns = [
    ("revenue_cagr_5yr", "REAL"),
    ("pat_cagr_5yr", "REAL"),
    ("eps_cagr_5yr", "REAL"),
    ("fcf_cagr_5yr", "REAL"),
    ("return_on_capital_employed_pct", "REAL"),
    ("composite_quality_score", "REAL"),
]

existing = {
    row[1]
    for row in cur.execute("PRAGMA table_info(financial_ratios)")
}

for column, dtype in columns:
    if column not in existing:
        cur.execute(
            f"ALTER TABLE financial_ratios ADD COLUMN {column} {dtype}"
        )
        print(f"Added {column}")
    else:
        print(f"{column} already exists")

conn.commit()
conn.close()

print("Schema upgrade complete.")