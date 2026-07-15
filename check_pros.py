import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql_query("SELECT * FROM prosandcons LIMIT 5", conn)

print(df)
print(df.columns.tolist())

conn.close()