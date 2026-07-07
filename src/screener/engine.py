import sqlite3
import pandas as pd
import yaml
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE = PROJECT_ROOT / "db" / "nifty100.db"
CONFIG_FILE = PROJECT_ROOT / "config" / "screener_config.yaml"

def load_ratios():
    conn = sqlite3.connect(str(DATABASE))

    query = """
    SELECT
        fr.*,
        c.roce_percentage,
        s.broad_sector
    FROM financial_ratios fr

    LEFT JOIN companies c
        ON fr.company_id = c.id

    LEFT JOIN sectors s
        ON fr.company_id = s.company_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def load_config():
    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)
    return config

def apply_filters(df, filters):
    filtered = df.copy()

    # Handle Interest Coverage
    if "interest_coverage" in filtered.columns:
        filtered["interest_coverage"] = (
            filtered["interest_coverage"]
            .replace("Debt Free", np.inf)
        )

        filtered["interest_coverage"] = pd.to_numeric(
            filtered["interest_coverage"],
            errors="coerce"
        )

    # Apply filters
    for key, value in filters.items():

        # Minimum filters
        if key.endswith("_min"):
            column = key.replace("_min", "")

            if column in filtered.columns:
                filtered = filtered[
                    filtered[column] >= value
                ]

        # Maximum filters
        elif key.endswith("_max"):
            column = key.replace("_max", "")

            # Skip D/E filter for Financial sector
            if column == "debt_to_equity" and "broad_sector" in filtered.columns:

                financials = filtered[
                    filtered["broad_sector"] == "Financials"
                ]

                others = filtered[
                    filtered["broad_sector"] != "Financials"
                ]

                if column in others.columns:
                    others = others[
                        others[column] <= value
                    ]

                filtered = pd.concat(
                    [financials, others],
                    ignore_index=True
                )

            elif column in filtered.columns:

                filtered = filtered[
                    filtered[column] <= value
                ]

    # Temporary Composite Score
    filtered["composite_quality_score"] = (
        filtered["return_on_equity_pct"].fillna(0) * 0.50 +
        filtered["roce_percentage"].fillna(0) * 0.30 +
        filtered["net_profit_margin_pct"].fillna(0) * 0.20
    )

    # Sort
    filtered = filtered.sort_values(
        by="composite_quality_score",
        ascending=False
    )

    return filtered

def run_preset(df, config, preset_name):

    if preset_name not in config:
        raise ValueError(f"Preset '{preset_name}' not found.")

    filters = config[preset_name]

    result = apply_filters(df, filters)

    return result


if __name__ == "__main__":

    df = load_ratios()
    config = load_config()

    print("\n========== PRESET TEST RESULTS ==========\n")

    for preset in config.keys():

        result = run_preset(df, config, preset)

        print(f"{preset:<25} {len(result)} companies")