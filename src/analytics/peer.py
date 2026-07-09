import sqlite3
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE = PROJECT_ROOT / "db" / "nifty100.db"

def load_peer_data():

    conn = sqlite3.connect(str(DATABASE))

    query = """
    SELECT
        fr.company_id,
        fr.year,
        fr.return_on_equity_pct,
        fr.debt_to_equity,
        fr.net_profit_margin_pct,
        fr.operating_profit_margin_pct,
        fr.asset_turnover,
        fr.free_cash_flow_cr,
        c.roce_percentage,
        pg.peer_group_name,
        pg.is_benchmark

    FROM financial_ratios fr

    LEFT JOIN companies c
        ON fr.company_id = c.id

    LEFT JOIN peer_groups pg
        ON fr.company_id = pg.company_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def calculate_peer_percentiles(df):

    metrics = [
        "return_on_equity_pct",
        "roce_percentage",
        "net_profit_margin_pct",
        "debt_to_equity",
        "asset_turnover",
        "free_cash_flow_cr"
    ]

    results = []

    grouped = df.dropna(subset=["peer_group_name"]).groupby("peer_group_name")

    for peer_group, group in grouped:

        for metric in metrics:

            if metric not in group.columns:
                continue

            temp = group.copy()

            if metric == "debt_to_equity":
                temp["percentile_rank"] = (
                    1 - temp[metric].rank(pct=True)
                ) * 100
            else:
                temp["percentile_rank"] = (
                    temp[metric].rank(pct=True)
                ) * 100

            temp["metric"] = metric
            temp["value"] = temp[metric]

            results.append(
                temp[
                    [
                        "company_id",
                        "peer_group_name",
                        "metric",
                        "value",
                        "percentile_rank",
                        "year"
                    ]
                ]
            )

    percentile_df = pd.concat(results, ignore_index=True)

    percentile_df = percentile_df.drop_duplicates(
        subset=[
            "company_id",
            "peer_group_name",
            "metric",
            "year"
        ]
    )

    return percentile_df

def save_peer_percentiles(df):

    conn = sqlite3.connect(str(DATABASE))

    df.to_sql(
        "peer_percentiles",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("\npeer_percentiles table saved successfully.")

if __name__ == "__main__":

    df = load_peer_data()

    percentile_df = calculate_peer_percentiles(df)

    save_peer_percentiles(percentile_df)

    print(percentile_df.head())

    print(f"\nRows Saved: {len(percentile_df)}")