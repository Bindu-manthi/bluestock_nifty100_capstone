import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql(
    "SELECT * FROM stock_prices",
    conn
)

invalid_prices = df[
    (df["open_price"] <= 0)
    | (df["high_price"] <= 0)
    | (df["low_price"] <= 0)
    | (df["close_price"] <= 0)
]

print("Invalid Stock Prices:")
print(len(invalid_prices))

conn.close()