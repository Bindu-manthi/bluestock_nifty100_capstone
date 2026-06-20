import pandas as pd

df = pd.read_excel(
    "data/raw/companies.xlsx",
    skiprows=1
)

print(df["id"].tail(20))