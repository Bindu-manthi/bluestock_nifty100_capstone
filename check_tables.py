import sqlite3

conn = sqlite3.connect("db/nifty100.db")

cursor = conn.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name
""")

for table in cursor.fetchall():
    print(table[0])

conn.close()