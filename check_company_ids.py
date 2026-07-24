import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

analysis = pd.read_sql(
    "SELECT DISTINCT company_id FROM analysis ORDER BY company_id",
    conn,
)

ratios = pd.read_sql(
    "SELECT DISTINCT company_id FROM financial_ratios ORDER BY company_id",
    conn,
)

print("Analysis company_id sample:")
print(analysis.head(20))

print("\nFinancial Ratios company_id sample:")
print(ratios.head(20))

common = set(analysis["company_id"]) & set(ratios["company_id"])

print("\nAnalysis companies :", len(analysis))
print("Ratio companies    :", len(ratios))
print("Common company_ids :", len(common))

conn.close()