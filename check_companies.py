import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("COMPANIES TABLE COLUMNS\n")

cursor.execute("PRAGMA table_info(companies)")

for column in cursor.fetchall():
    print(column[1])

conn.close()