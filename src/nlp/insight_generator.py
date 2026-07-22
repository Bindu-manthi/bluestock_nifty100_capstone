import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("db/nifty100.db")

ratios_df = pd.read_sql("""
SELECT *
FROM financial_ratios
""", conn)

conn.close()

print(ratios_df.head())
print(f"\nTotal Records: {len(ratios_df)}")

import sqlite3
import pandas as pd
import os

# =====================================================
# Connect to Database
# =====================================================

conn = sqlite3.connect("db/nifty100.db")

ratios_df = pd.read_sql("""
SELECT *
FROM financial_ratios
""", conn)

conn.close()

os.makedirs("output", exist_ok=True)

# =====================================================
# Generate Financial Insight
# =====================================================

def generate_insight(company_id):

    company_data = (
        ratios_df[ratios_df["company_id"] == company_id]
        .sort_values("year")
    )

    if company_data.empty:
        return None

    latest = company_data.iloc[-1]

    insights = []
    score = 0

    # ROE
    roe = latest["return_on_equity_pct"]

    if roe >= 20:
        insights.append("Excellent profitability with ROE above 20%.")
        score += 2
    elif roe >= 15:
        insights.append("Healthy ROE indicates good shareholder returns.")
        score += 1
    else:
        insights.append("ROE is relatively low.")

    # Debt
    debt = latest["debt_to_equity"]

    if debt <= 0.5:
        insights.append("Low debt indicates a strong capital structure.")
        score += 2
    elif debt <= 1:
        insights.append("Debt level appears manageable.")
        score += 1
    else:
        insights.append("High debt may increase financial risk.")

    # Free Cash Flow
    fcf = latest["free_cash_flow_cr"]

    if fcf > 0:
        insights.append("Positive free cash flow indicates healthy cash generation.")
        score += 2
    else:
        insights.append("Negative free cash flow needs attention.")

    # Net Profit Margin
    npm = latest["net_profit_margin_pct"]

    if npm >= 15:
        insights.append("Profit margins are healthy.")
        score += 2
    elif npm >= 8:
        insights.append("Profit margins are stable.")
        score += 1
    else:
        insights.append("Profit margins are relatively weak.")

    # Overall Rating
    if score >= 7:
        rating = "STRONG"
    elif score >= 4:
        rating = "MODERATE"
    else:
        rating = "WEAK"

    return {
        "company_id": company_id,
        "rating": rating,
        "insights": " ".join(insights)
    }

# =====================================================
# Test with One Company
# =====================================================

# =====================================================
# Generate Insights for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

results = []

for company in companies:
    insight = generate_insight(company)

    if insight is not None:
        results.append(insight)

# =====================================================
# Save Output
# =====================================================

insight_df = pd.DataFrame(results)

output_file = "output/company_insights.csv"

insight_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Financial Insight Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(insight_df)}")
print(f"Output File         : {output_file}")

print("\nSample Insight\n")

print(insight_df.iloc[0])