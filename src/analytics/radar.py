import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE = PROJECT_ROOT / "db" / "nifty100.db"

REPORT_DIR = PROJECT_ROOT / "reports" / "radar_charts"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

def load_peer_data():

    conn = sqlite3.connect(str(DATABASE))

    query = """
    SELECT
        fr.company_id,
        fr.return_on_equity_pct,
        fr.net_profit_margin_pct,
        fr.asset_turnover,
        fr.free_cash_flow_cr,
        c.roce_percentage,
        pg.peer_group_name

    FROM financial_ratios fr

    LEFT JOIN companies c
        ON fr.company_id = c.id

    LEFT JOIN peer_groups pg
        ON fr.company_id = pg.company_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def create_radar_chart(df, company_id):

    company = df[df["company_id"] == company_id]

    if company.empty:
        print(f"{company_id} not found.")
        return

    peer_group = company["peer_group_name"].iloc[0]

    if pd.isna(peer_group):
        print(f"{company_id} has no peer group assigned.")
        return

    peer_df = df[df["peer_group_name"] == peer_group]

    metrics = [
        "return_on_equity_pct",
        "roce_percentage",
        "net_profit_margin_pct",
        "asset_turnover",
        "free_cash_flow_cr"
    ]

    company_values = (
        company[metrics]
        .mean()
        .fillna(0)
        .tolist()
    )

    peer_values = (
        peer_df[metrics]
        .mean()
        .fillna(0)
        .tolist()
    )

    labels = [
        "ROE",
        "ROCE",
        "NPM",
        "Asset Turnover",
        "FCF"
    ]

    angles = np.linspace(
        0,
        2 * np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    company_values += company_values[:1]
    peer_values += peer_values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(
        figsize=(7, 7),
        subplot_kw=dict(polar=True)
    )

    ax.plot(
        angles,
        company_values,
        linewidth=2,
        label=company_id
    )

    ax.fill(
        angles,
        company_values,
        alpha=0.25
    )

    ax.plot(
        angles,
        peer_values,
        linestyle="--",
        linewidth=2,
        label="Peer Average"
    )

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_title(f"{company_id} vs {peer_group}")

    ax.legend(loc="upper right")

    filename = REPORT_DIR / f"{company_id}_radar.png"

    plt.savefig(filename, dpi=300)

    plt.close()

    print(f"Saved: {filename}")

if __name__ == "__main__":

    df = load_peer_data()

    companies = (
        df["company_id"]
        .dropna()
        .unique()
    )

    count = 0

    for company in companies:

        try:
            create_radar_chart(df, company)
            count += 1

        except Exception as e:
            print(f"Skipped {company}: {e}")

    print(f"\nTotal radar charts generated: {count}")