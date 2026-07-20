import sqlite3
import pandas as pd
import os

# =====================================================
# Connect to Database
# =====================================================

conn = sqlite3.connect("db/nifty100.db")

# Load Financial Ratios
ratios_df = pd.read_sql("""
SELECT *
FROM financial_ratios
""", conn)

# Load Pros & Cons
pros_df = pd.read_sql("""
SELECT *
FROM prosandcons
""", conn)

conn.close()

# =====================================================
# Create Output Folder
# =====================================================

os.makedirs("output", exist_ok=True)

# =====================================================
# Narrative Generator Function
# =====================================================

def generate_narrative(company_id):
    ratio_data = (
        ratios_df[ratios_df["company_id"] == company_id]
        .sort_values("year")
    )

    if ratio_data.empty:
        return None

    latest = ratio_data.iloc[-1]

    pros_data = pros_df[pros_df["company_id"] == company_id]

    if not pros_data.empty:
        pros = pros_data.iloc[0]["pros"]
        cons = pros_data.iloc[0]["cons"]
    else:
        pros = "No major strengths recorded."
        cons = "No major concerns recorded."

    narrative = f"""{company_id} demonstrates a notable financial profile.

Net Profit Margin: {latest['net_profit_margin_pct']}%

Operating Profit Margin: {latest['operating_profit_margin_pct']}%

Return on Equity: {latest['return_on_equity_pct']}%

Debt to Equity: {latest['debt_to_equity']}

Free Cash Flow: {latest['free_cash_flow_cr']} Cr

Pros:
{pros}

Cons:
{cons}
"""

    return narrative


# =====================================================
# Generate Narratives for All Companies
# =====================================================

companies = sorted(ratios_df["company_id"].unique())

narratives = []

for company in companies:
    text = generate_narrative(company)

    if text:
        narratives.append({
            "company_id": company,
            "narrative": text
        })

# =====================================================
# Save Output
# =====================================================

narrative_df = pd.DataFrame(narratives)

output_file = "output/company_narratives.csv"

narrative_df.to_csv(output_file, index=False)

# =====================================================
# Display Summary
# =====================================================

print("=" * 60)
print("Narrative Generation Completed")
print("=" * 60)

print(f"Companies Processed : {len(narrative_df)}")
print(f"Output File         : {output_file}")

print("\nSample Narrative\n")

print(narrative_df.iloc[0]["narrative"])