import sqlite3
import pandas as pd

# =====================================================
# Connect Database
# =====================================================

conn = sqlite3.connect("db/nifty100.db")

ratios_df = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

pros_df = pd.read_sql(
    "SELECT * FROM prosandcons",
    conn
)

conn.close()

print("Financial Ratios:", len(ratios_df))
print("Pros & Cons:", len(pros_df))

# =====================================================
# Company Report Generator
# =====================================================

def generate_report(company_id):

    company_data = (
        ratios_df[ratios_df["company_id"] == company_id]
        .sort_values("year")
    )

    if company_data.empty:
        return None

    latest = company_data.iloc[-1]

    pros_data = pros_df[pros_df["company_id"] == company_id]

    if not pros_data.empty:
        pros = pros_data.iloc[0]["pros"]
        cons = pros_data.iloc[0]["cons"]
    else:
        pros = "No major strengths recorded."
        cons = "No major concerns recorded."

    report = f"""
==================================================
Company : {company_id}
==================================================

Financial Summary
-----------------
Net Profit Margin : {latest['net_profit_margin_pct']}%
Operating Margin  : {latest['operating_profit_margin_pct']}%
ROE               : {latest['return_on_equity_pct']}%
Debt/Equity       : {latest['debt_to_equity']}
Free Cash Flow    : {latest['free_cash_flow_cr']} Cr

Pros
----
{pros}

Cons
----
{cons}
"""

    return report

import os

# =====================================================
# Create Output Folder
# =====================================================

os.makedirs("output", exist_ok=True)

# =====================================================
# Generate Reports for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

reports = []

for company in companies:
    report = generate_report(company)

    if report:
        reports.append({
            "company_id": company,
            "report": report
        })

# =====================================================
# Save Reports
# =====================================================

report_df = pd.DataFrame(reports)

output_file = "output/company_reports.csv"

report_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Financial Report Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(report_df)}")
print(f"Output File         : {output_file}")

print("\nSample Report\n")
print(report_df.iloc[0]["report"])