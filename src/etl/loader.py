import pandas as pd


def load_excel(file_path):
    """
    Load Excel file using row 1 as header.
    """

    return pd.read_excel(file_path, skiprows=1)


if __name__ == "__main__":

    df = load_excel("data/raw/companies.xlsx")

    print(df.head())
    print(df.columns.tolist())