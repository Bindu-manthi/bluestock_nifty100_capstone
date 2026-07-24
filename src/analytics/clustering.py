import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


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

def load_latest_ratios():
    """
    Load latest financial ratios for every company.
    """

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
    fr.company_id,
    s.broad_sector,
    fr.return_on_equity_pct,
    fr.debt_to_equity,
    fr.revenue_cagr_5yr,
    fr.fcf_cagr_5yr,
    fr.operating_profit_margin_pct
FROM financial_ratios fr
JOIN (
    SELECT company_id, MAX(id) AS latest_id
    FROM financial_ratios
    GROUP BY company_id
) latest
ON fr.id = latest.latest_id
LEFT JOIN sectors s
ON fr.company_id = s.company_id
ORDER BY fr.company_id;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def prepare_features(df):
    """
    Prepare features for clustering.
    """

    data = df.copy()

    # Sector median imputation
    for feature in FEATURES:
        data[feature] = (
            data.groupby("broad_sector")[feature]
            .transform(lambda x: x.fillna(x.median()))
        )

        # Global median fallback
        median = data[feature].median()

        if pd.isna(median):
            median = 0

        data[feature] = data[feature].fillna(median)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(data[FEATURES])

    return data, scaled

def generate_elbow_curve(scaled):
    """
    Generate elbow curve.
    """

    inertia = []

    ks = range(2, 11)

    for k in ks:
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(scaled)

        inertia.append(model.inertia_)

    plt.figure(figsize=(8,5))

    plt.plot(ks, inertia, marker="o")

    plt.title("KMeans Elbow Curve")

    plt.xlabel("Clusters")

    plt.ylabel("Inertia")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("reports/elbow_plot.png")

    plt.close()


def assign_cluster_names(cluster_means):
    """
    Assign readable cluster names.
    """

    ranking = (
        cluster_means["return_on_equity_pct"]
        + cluster_means["operating_profit_margin_pct"]
        - cluster_means["debt_to_equity"] * 10
    )

    order = ranking.sort_values(ascending=False).index.tolist()

    names = [
        "High-Quality Compounders",
        "Emerging Growth",
        "Defensive Leaders",
        "Value Cyclicals",
        "Turnaround Stories",
    ]

    mapping = {}

    for idx, cluster in enumerate(order):
        mapping[cluster] = names[idx]

    return mapping


def run_clustering(df, scaled):
    """
    Run KMeans clustering.
    """

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(scaled)

    df["cluster_id"] = labels

    distances = model.transform(scaled)

    df["distance_from_centroid"] = distances.min(axis=1)

    cluster_means = (
        df.groupby("cluster_id")[FEATURES]
        .mean()
    )

    name_map = assign_cluster_names(cluster_means)

    df["cluster_name"] = df["cluster_id"].map(name_map)

    return df

if __name__ == "__main__":

    df = load_latest_ratios()

    prepared_df, scaled = prepare_features(df)

    generate_elbow_curve(scaled)

    clustered = run_clustering(
        prepared_df,
        scaled
    )

    output = clustered[
        [
            "company_id",
            "cluster_id",
            "cluster_name",
            "distance_from_centroid",
        ]
    ]

    output.to_csv(
        "output/cluster_labels.csv",
        index=False,
    )

    print()

    print("===================================")
    print("KMeans clustering completed")
    print("===================================")

    print()

    print(output.head())

    print()

    print("Total Companies :", len(output))

    print("Clusters :", output["cluster_id"].nunique())

    print()

    print("Saved : reports/elbow_plot.png")

    print("Saved : output/cluster_labels.csv")