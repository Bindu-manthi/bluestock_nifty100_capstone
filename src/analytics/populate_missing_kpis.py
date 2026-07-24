import sqlite3
import pandas as pd
import numpy as np


DB_PATH = "db/nifty100.db"


def extract_percent(value):
    """
    Extract a numeric percentage from text like '10 Years: 18.5%'.
    """
    if value is None:
        return None

    text = str(value)

    if "%" not in text:
        return None

    try:
        pct = text.split(":")[-1].replace("%", "").strip()
        return float(pct)
    except Exception:
        return None


conn = sqlite3.connect(DB_PATH)

analysis = pd.read_sql("SELECT * FROM analysis", conn)
companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

analysis["revenue_cagr"] = analysis["compounded_sales_growth"].apply(extract_percent)
analysis["profit_cagr"] = analysis["compounded_profit_growth"].apply(extract_percent)

analysis = analysis[
    ["company_id", "revenue_cagr", "profit_cagr"]
]

companies = companies[
    ["id", "roce_percentage"]
].rename(columns={"id": "company_id"})

df = ratios.merge(
    analysis,
    on="company_id",
    how="left"
)

df = df.merge(
    companies,
    on="company_id",
    how="left"
)

df["revenue_cagr_5yr"] = df["revenue_cagr"]
df["pat_cagr_5yr"] = df["profit_cagr"]

df["return_on_capital_employed_pct"] = df["roce_percentage"]

df["eps_cagr_5yr"] = np.nan
df["fcf_cagr_5yr"] = np.nan

quality = (
    df["return_on_equity_pct"].fillna(0)
    + df["operating_profit_margin_pct"].fillna(0)
    + df["revenue_cagr_5yr"].fillna(0)
    - df["debt_to_equity"].fillna(0) * 10
)

df["composite_quality_score"] = quality

update_cols = [
    "revenue_cagr_5yr",
    "pat_cagr_5yr",
    "eps_cagr_5yr",
    "fcf_cagr_5yr",
    "return_on_capital_employed_pct",
    "composite_quality_score",
]

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        UPDATE financial_ratios
        SET revenue_cagr_5yr=?,
            pat_cagr_5yr=?,
            eps_cagr_5yr=?,
            fcf_cagr_5yr=?,
            return_on_capital_employed_pct=?,
            composite_quality_score=?
        WHERE id=?
        """,
        (
            row["revenue_cagr_5yr"],
            row["pat_cagr_5yr"],
            row["eps_cagr_5yr"],
            row["fcf_cagr_5yr"],
            row["return_on_capital_employed_pct"],
            row["composite_quality_score"],
            row["id"],
        ),
    )

conn.commit()

print("Updated rows:", len(df))

print("\nNull counts:")
print(df[update_cols].isnull().sum())

conn.close()