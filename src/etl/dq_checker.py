import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "financial_ratios",
    "peer_groups",
    "sectors",
    "stock_prices"
]

for table in tables:

    df = pd.read_sql(
        f"SELECT * FROM {table}",
        conn
    )

    print(f"\n{table}")
    print(df.dtypes)

conn.close()