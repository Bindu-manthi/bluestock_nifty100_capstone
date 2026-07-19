import sqlite3
import pandas as pd

from src.analytics.cagr import revenue_cagr

# --------------------------------------------------
# Load Parsed Analysis Output
# --------------------------------------------------

parsed_df = pd.read_csv("output/analysis_parsed.csv")

print("Parsed Analysis")
print(parsed_df.head())

# --------------------------------------------------
# Load Profit & Loss Data
# --------------------------------------------------

conn = sqlite3.connect("db/nifty100.db")

profit_df = pd.read_sql("""
SELECT
    company_id,
    year,
    sales,
    net_profit,
    eps
FROM profitandloss
""", conn)

conn.close()

print("\nProfit & Loss Data")
print(profit_df.head())

# --------------------------------------------------
# Clean Year Column
# --------------------------------------------------

profit_df["year"] = pd.to_numeric(
    profit_df["year"].astype(str).str.extract(r"(\d{4})")[0],
    errors="coerce"
)

profit_df = profit_df.dropna(subset=["year"])

profit_df["year"] = profit_df["year"].astype(int)

profit_df = profit_df.sort_values(
    ["company_id", "year"]
)

print("\nNormalized Profit Data")
print(profit_df.head())

# --------------------------------------------------
# Validate Sales CAGR
# --------------------------------------------------

results = []

sales_rows = parsed_df[
    parsed_df["metric_type"] == "Sales CAGR"
]

for _, row in sales_rows.iterrows():

    company = row["company_id"]
    years = int(row["period_years"])
    parsed_value = float(row["value_pct"])

    company_data = profit_df[
        profit_df["company_id"] == company
    ].sort_values("year")

    # Need at least (years + 1) observations
    if len(company_data) < years + 1:
        continue

    start_sales = company_data.iloc[-(years + 1)]["sales"]
    end_sales = company_data.iloc[-1]["sales"]

    calculated_value, flag = revenue_cagr(
        start_sales,
        end_sales,
        years
    )

    if calculated_value is None:
        continue

    difference = abs(parsed_value - calculated_value)

    results.append({
        "company_id": company,
        "metric_type": "Sales CAGR",
        "period_years": years,
        "parsed_value": parsed_value,
        "calculated_value": calculated_value,
        "difference": round(difference, 2),
        "status": "REVIEW" if difference > 5 else "OK"
    })

# --------------------------------------------------
# Save Report
# --------------------------------------------------

review_df = pd.DataFrame(results)

review_df.to_csv(
    "output/cagr_divergence_review.csv",
    index=False
)

print("\n===================================")
print("CAGR Validation Completed")
print("===================================")

print(review_df.head())

print(f"\nTotal Records : {len(review_df)}")
print("Output Saved  : output/cagr_divergence_review.csv")