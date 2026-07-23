import sqlite3
import pandas as pd

# =====================================================
# Connect to Database
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
# Company Scorecard Generator
# =====================================================

def generate_scorecard(company_id):

    company_data = (
        ratios_df[ratios_df["company_id"] == company_id]
        .sort_values("year")
    )

    if company_data.empty:
        return None

    latest = company_data.iloc[-1]

    score = 0

    # ROE
    roe = latest["return_on_equity_pct"]
    if roe >= 20:
        score += 3
    elif roe >= 15:
        score += 2
    elif roe >= 10:
        score += 1

    # Net Profit Margin
    npm = latest["net_profit_margin_pct"]
    if npm >= 15:
        score += 3
    elif npm >= 8:
        score += 2
    elif npm >= 5:
        score += 1

    # Debt to Equity
    debt = latest["debt_to_equity"]
    if debt <= 0.5:
        score += 2
    elif debt <= 1:
        score += 1

    # Free Cash Flow
    fcf = latest["free_cash_flow_cr"]
    if fcf > 0:
        score += 2

    # Recommendation
    if score >= 8:
        recommendation = "BUY"
    elif score >= 5:
        recommendation = "HOLD"
    else:
        recommendation = "SELL"

    return {
        "company_id": company_id,
        "roe": roe,
        "net_profit_margin": npm,
        "debt_to_equity": debt,
        "free_cash_flow": fcf,
        "score": score,
        "recommendation": recommendation
    }
# =====================================================
# Generate Scorecards for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

scorecards = []

for company in companies:
    scorecard = generate_scorecard(company)

    if scorecard:
        scorecards.append(scorecard)

# =====================================================
# Save Output
# =====================================================

scorecard_df = pd.DataFrame(scorecards)

output_file = "output/company_scorecards.csv"

scorecard_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Company Scorecard Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(scorecard_df)}")
print(f"Output File         : {output_file}")

print("\nSample Scorecard\n")
print(scorecard_df.iloc[0])