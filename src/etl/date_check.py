import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql(
    "SELECT date FROM stock_prices",
    conn
)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

invalid_dates = df[
    df["date"].isna()
]

print("Invalid Dates:")
print(len(invalid_dates))

conn.close()