import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

files = {
    "companies": ("data/raw/companies.xlsx", 1),
    "profitandloss": ("data/raw/profitandloss.xlsx", 1),
    "balancesheet": ("data/raw/balancesheet.xlsx", 1),
    "cashflow": ("data/raw/cashflow.xlsx", 1),
    "analysis": ("data/raw/analysis.xlsx", 1),
    "documents": ("data/raw/documents.xlsx", 0),
    "prosandcons": ("data/raw/prosandcons.xlsx", 0),
    "financial_ratios": ("data/raw/financial_ratios.xlsx", 0),
    "peer_groups": ("data/raw/peer_groups.xlsx", 0),
    "sectors": ("data/raw/sectors.xlsx", 0),
    "stock_prices": ("data/raw/stock_prices.xlsx", 0)
}

for table, (file, skip) in files.items():

    print(f"\nLoading {table}...")

    if table in [
        "companies",
        "profitandloss",
        "balancesheet",
        "cashflow",
        "analysis",
        "documents",
        "prosandcons"
    ]:
        df = pd.read_excel(file, skiprows=1)
    else:
        df = pd.read_excel(file)

    print(f"{table}: {df.shape}")

    df.to_sql(
        table,
        conn,
        if_exists="append",
        index=False
    )

    print(f"{len(df)} rows loaded")

conn.commit()
conn.close()

print("\nDatabase load complete.")