import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "output"


def export_screeners(results_dict):
    OUTPUT_DIR.mkdir(exist_ok=True)

    output_file = OUTPUT_DIR / "screener_output.xlsx"

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for preset_name, df in results_dict.items():
            df.to_excel(
                writer,
                sheet_name=preset_name[:31],
                index=False
            )

    print(f"\nExcel exported successfully!")
    print(f"Location: {output_file}")