import sqlite3
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Open log file
log_file = open("output/ratio_edge_cases.log", "w")

# Connect to database
conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    c.id,
    c.company_name,
    s.broad_sector,
    c.roe_percentage,
    c.roce_percentage,
    f.return_on_equity_pct

FROM companies c

INNER JOIN sectors s
ON c.id = s.company_id

INNER JOIN financial_ratios f
ON c.id = f.company_id

LIMIT 10
""")

rows = cursor.fetchall()

for row in rows:

    company_id = row[0]
    company_name = row[1]
    broad_sector = row[2]

    source_roe = row[3]
    source_roce = row[4]
    calculated_roe = row[5]

    if source_roe is None or calculated_roe is None:
        continue

    difference = abs(source_roe - calculated_roe)

    print("-----------------------------------")
    print(f"Company         : {company_id}")
    print(f"Sector          : {broad_sector}")
    print(f"Source ROE      : {source_roe}")
    print(f"Calculated ROE  : {calculated_roe}")
    print(f"Difference      : {difference:.2f}")

    if difference > 5:
        print("⚠ ROE ANOMALY FOUND")

        log_file.write(
            f"{company_id} | "
            f"{company_name} | "
            f"{broad_sector} | "
            f"Source ROE={source_roe} | "
            f"Calculated ROE={calculated_roe} | "
            f"Difference={difference:.2f}% | "
            f"Category=Formula Difference\n"
        )

log_file.close()
conn.close()

print("\nratio_edge_cases.log generated successfully!")