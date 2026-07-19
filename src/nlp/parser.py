import os
import re
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "data/raw/analysis.xlsx"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Regex Pattern
pattern = r"(\d+)\s*Year[s]?:?\s*(-?[\d.]+)%"

# ==========================================================
# Parse Function
# ==========================================================

def parse_text(text):
    """
    Extracts:
        Period (Years)
        Percentage Value

    Example:
        '10 Years: 21%' -> (10, 21.0)
        '1 Year: -2%'   -> (1, -2.0)

    Returns:
        tuple(period, value) or None
    """

    if pd.isna(text):
        return None

    text = str(text).strip()

    match = re.search(pattern, text)

    if match:
        period = int(match.group(1))
        value = float(match.group(2))
        return period, value

    return None


# ==========================================================
# Read Excel
# ==========================================================

analysis_df = pd.read_excel(
    INPUT_FILE,
    header=1
)

# ==========================================================
# Metric Mapping
# ==========================================================

metric_columns = {
    "compounded_sales_growth": "Sales CAGR",
    "compounded_profit_growth": "Profit CAGR",
    "stock_price_cagr": "Stock Price CAGR",
    "roe": "ROE"
}

# ==========================================================
# Parse Analysis Data
# ==========================================================

parsed_records = []
failed_records = []

for _, row in analysis_df.iterrows():

    company_id = row["company_id"]

    for column, metric_name in metric_columns.items():

        result = parse_text(row[column])

        if result:

            period, value = result

            parsed_records.append({
                "company_id": company_id,
                "metric_type": metric_name,
                "period_years": period,
                "value_pct": value
            })

        else:

            failed_records.append({
                "company_id": company_id,
                "metric_type": metric_name,
                "original_text": row[column]
            })

# ==========================================================
# Create DataFrames
# ==========================================================

parsed_df = pd.DataFrame(parsed_records)
failed_df = pd.DataFrame(failed_records)

# ==========================================================
# Save Outputs
# ==========================================================

parsed_df.to_csv(
    os.path.join(OUTPUT_FOLDER, "analysis_parsed.csv"),
    index=False
)

failed_df.to_csv(
    os.path.join(OUTPUT_FOLDER, "parse_failures.csv"),
    index=False
)

# ==========================================================
# Summary
# ==========================================================

print("=" * 60)
print("Analysis Parser Completed")
print("=" * 60)

print(f"Total Excel Rows      : {len(analysis_df)}")
print(f"Parsed Records        : {len(parsed_records)}")
print(f"Failed Records        : {len(failed_records)}")

print("\nOutput Files Generated")

print("output/analysis_parsed.csv")
print("output/parse_failures.csv")

print("=" * 60)