import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql(
    "PRAGMA table_info(profitandloss);",
    conn
)

print(df)

conn.close()