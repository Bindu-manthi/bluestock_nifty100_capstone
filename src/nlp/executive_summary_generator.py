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
# Executive Summary Generator
# =====================================================

def generate_executive_summary(company_id):

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

    score = 0
    highlights = []

    # ROE
    if roe >= 20:
        score += 3
        highlights.append("Strong Return on Equity")
    elif roe >= 15:
        score += 2
        highlights.append("Healthy Return on Equity")

    # Net Profit Margin
    if npm >= 15:
        score += 3
        highlights.append("Healthy Profit Margins")
    elif npm >= 8:
        score += 2

    # Debt
    if debt <= 0.5:
        score += 2
        highlights.append("Low Financial Leverage")
    elif debt <= 1:
        score += 1

    # Free Cash Flow
    if fcf > 0:
        score += 2
        highlights.append("Positive Cash Generation")

    # Rating & Recommendation
    if score >= 8:
        rating = "STRONG"
        recommendation = "BUY"
    elif score >= 5:
        rating = "MODERATE"
        recommendation = "HOLD"
    else:
        rating = "WEAK"
        recommendation = "SELL"

    summary = f"""
Company: {company_id}

Executive Summary
-----------------
{company_id} demonstrates {rating.lower()} financial performance based on profitability, leverage, and cash flow analysis.

Overall Rating: {rating}
Investment Recommendation: {recommendation}

Key Highlights:
"""

    for item in highlights:
        summary += f"\n• {item}"

    return {
        "company_id": company_id,
        "rating": rating,
        "recommendation": recommendation,
        "summary": summary
    }

# =====================================================
# Generate Executive Summaries for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

summaries = []

for company in companies:
    summary = generate_executive_summary(company)

    if summary is not None:
        summaries.append(summary)

# =====================================================
# Save Output
# =====================================================

summary_df = pd.DataFrame(summaries)

output_file = "output/executive_summaries.csv"

summary_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Executive Summary Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(summary_df)}")
print(f"Output File         : {output_file}")

print("\nSample Executive Summary\n")
print(summary_df.iloc[0])