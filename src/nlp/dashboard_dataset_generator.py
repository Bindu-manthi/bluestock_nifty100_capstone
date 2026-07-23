import sqlite3
import pandas as pd

# =====================================================
# Connect Database
# =====================================================

conn = sqlite3.connect("db/nifty100.db")

ratios_df = pd.read_sql("""
SELECT *
FROM financial_ratios
""", conn)

conn.close()

import os

os.makedirs("output", exist_ok=True)

# =====================================================
# Dashboard Dataset Generator
# =====================================================

def generate_dashboard_record(company_id):

    company_data = (
        ratios_df[ratios_df["company_id"] == company_id]
        .sort_values("year")
    )

    if company_data.empty:
        return None

    latest = company_data.iloc[-1]

    roe = latest["return_on_equity_pct"]
    npm = latest["net_profit_margin_pct"]
    debt = latest["debt_to_equity"]
    fcf = latest["free_cash_flow_cr"]

    # Financial Score
    score = 0

    if roe >= 20:
        score += 3
    elif roe >= 15:
        score += 2
    elif roe >= 10:
        score += 1

    if npm >= 15:
        score += 3
    elif npm >= 8:
        score += 2
    elif npm >= 5:
        score += 1

    if debt <= 0.5:
        score += 2
    elif debt <= 1:
        score += 1

    if fcf > 0:
        score += 2

    # Recommendation
    if score >= 8:
        recommendation = "BUY"
    elif score >= 5:
        recommendation = "HOLD"
    else:
        recommendation = "SELL"

    # Financial Rating
    if score >= 8:
        rating = "STRONG"
    elif score >= 5:
        rating = "MODERATE"
    else:
        rating = "WEAK"

    return {
        "company_id": company_id,
        "roe": roe,
        "net_profit_margin": npm,
        "debt_to_equity": debt,
        "free_cash_flow": fcf,
        "score": score,
        "recommendation": recommendation,
        "rating": rating
    }

# =====================================================
# Generate Dashboard Dataset for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

dashboard_records = []

for company in companies:
    record = generate_dashboard_record(company)

    if record is not None:
        dashboard_records.append(record)

# =====================================================
# Save Output
# =====================================================

dashboard_df = pd.DataFrame(dashboard_records)

output_file = "output/dashboard_dataset.csv"

dashboard_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Dashboard Dataset Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(dashboard_df)}")
print(f"Output File         : {output_file}")

print("\nSample Dashboard Record\n")
print(dashboard_df.iloc[0])