import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("SECTORS TABLE COLUMNS\n")

cursor.execute("PRAGMA table_info(sectors)")

for column in cursor.fetchall():
    print(column[1])

conn.close()