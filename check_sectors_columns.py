import sqlite3

conn = sqlite3.connect("db/nifty100.db")

cursor = conn.execute("PRAGMA table_info(sectors)")

for col in cursor.fetchall():
    print(col[1])

conn.close()