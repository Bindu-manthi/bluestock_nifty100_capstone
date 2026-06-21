import pandas as pd

df = pd.read_excel(
    "data/raw/stock_prices.xlsx"
)

print(df.columns.tolist())
print(df.head())