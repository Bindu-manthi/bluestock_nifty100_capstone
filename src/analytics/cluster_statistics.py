import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt

import pandas as pd


DB_PATH = "db/nifty100.db"

OUTPUT_DIR = Path("output")
REPORT_DIR = Path("reports")

OUTPUT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)


FEATURES = [
    "return_on_equity_pct",
    "debt_to_equity",
    "revenue_cagr_5yr",
    "fcf_cagr_5yr",
    "operating_profit_margin_pct",
]

LIMITS = {
    "return_on_equity_pct": (-100, 100),
    "debt_to_equity": (0, 20),
    "revenue_cagr_5yr": (-100, 200),
    "fcf_cagr_5yr": (-100, 300),
    "operating_profit_margin_pct": (-100, 100),
}


def load_data():
    """
    Load latest ratios and cluster labels.
    """

    conn = sqlite3.connect(DB_PATH)

    ratios = pd.read_sql(
        """
        SELECT *
        FROM financial_ratios
        WHERE id IN
        (
            SELECT MAX(id)
            FROM financial_ratios
            GROUP BY company_id
        )
        """,
        conn,
    )

    conn.close()

    clusters = pd.read_csv(
        "output/cluster_labels.csv"
    )

    df = ratios.merge(
        clusters,
        on="company_id",
        how="inner",
    )

    return df

def sanitize_metrics(df):
    """
    Remove unrealistic values from the analytics layer only.
    The database is NOT modified.
    """

    df = df.copy()

    for column, (lower, upper) in LIMITS.items():

        if column not in df.columns:
            continue

        df.loc[
            (df[column] < lower) |
            (df[column] > upper),
            column
        ] = pd.NA

        median = df[column].median()

        if pd.isna(median):
            median = 0

        df[column] = df[column].fillna(median)

    return df

def cluster_profile(df):
    """
    Generate cluster statistics.
    """

    mean_profile = (
        df.groupby("cluster_name")[FEATURES]
        .mean()
        .round(2)
    )

    median_profile = (
        df.groupby("cluster_name")[FEATURES]
        .median()
        .round(2)
    )

    company_count = (
        df.groupby("cluster_name")
        .size()
        .to_frame("companies")
    )

    print()

    print("=" * 60)

    print("COMPANY COUNT")

    print("=" * 60)

    print(company_count)

    print()

    print("=" * 60)

    print("MEAN PROFILE")

    print("=" * 60)

    print(mean_profile)

    print()

    print("=" * 60)

    print("MEDIAN PROFILE")

    print("=" * 60)

    print(median_profile)

    return mean_profile, median_profile

def generate_correlation_heatmap(df):
    """
    Generate correlation matrix and heatmap.
    """

    corr = df[FEATURES].corr()

    print()
    print("=" * 60)
    print("CORRELATION MATRIX")
    print("=" * 60)
    print(corr.round(2))

    fig, ax = plt.subplots(figsize=(8, 6))

    image = ax.imshow(corr.values)

    ax.set_xticks(range(len(FEATURES)))
    ax.set_yticks(range(len(FEATURES)))

    ax.set_xticklabels(FEATURES, rotation=45, ha="right")
    ax.set_yticklabels(FEATURES)

    for i in range(len(FEATURES)):
        for j in range(len(FEATURES)):
            ax.text(
                j,
                i,
                f"{corr.iloc[i, j]:.2f}",
                ha="center",
                va="center",
                fontsize=8,
            )

    plt.colorbar(image)

    plt.title("Financial KPI Correlation")

    plt.tight_layout()

    output_file = REPORT_DIR / "correlation_heatmap.png"

    plt.savefig(output_file, dpi=300)

    plt.close()

    print()
    print(f"Heatmap saved -> {output_file}")


def generate_outlier_report(df):
    """
    Generate a report of rows containing values outside the configured limits.
    """

    outliers = pd.DataFrame()

    for column, (lower, upper) in LIMITS.items():
        if column not in df.columns:
            continue

        temp = df[
            (df[column] < lower) |
            (df[column] > upper)
        ].copy()

        if not temp.empty:
            temp["outlier_metric"] = column
            outliers = pd.concat([outliers, temp], ignore_index=True)

    output_file = OUTPUT_DIR / "outlier_report.csv"
    outliers.to_csv(output_file, index=False)

    print()
    print("=" * 60)
    print("OUTLIER REPORT")
    print("=" * 60)
    print(f"Rows Found : {len(outliers)}")
    print(f"Saved -> {output_file}")


def generate_portfolio_statistics(df):
    """
    Generate overall portfolio statistics.
    """

    stats = (
        df[FEATURES]
        .describe()
        .round(2)
        .T
    )

    output_file = OUTPUT_DIR / "portfolio_stats.csv"

    stats.to_csv(output_file)

    print()
    print("=" * 60)
    print("PORTFOLIO STATISTICS")
    print("=" * 60)
    print(stats)

    print()
    print(f"Saved -> {output_file}")


if __name__ == "__main__":

    df = load_data()

    raw_df = df.copy()

    df = sanitize_metrics(df)

    cluster_profile(df)

    generate_correlation_heatmap(df)

    generate_outlier_report(raw_df)

    generate_portfolio_statistics(df)