import streamlit as st
from utils.db import run_query

st.title("📊 Stock Screener")
st.write("Filter companies based on financial metrics.")

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.header("🔍 Screening Filters")

# ---------------------------------
# Filters
# ---------------------------------

roe_min = st.sidebar.slider(
    "Minimum ROE (%)",
    min_value=0,
    max_value=50,
    value=15
)

de_max = st.sidebar.slider(
    "Maximum Debt to Equity",
    min_value=0.0,
    max_value=5.0,
    value=1.0,
    step=0.1
)

fcf_min = st.sidebar.number_input(
    "Minimum Free Cash Flow (Cr)",
    min_value=0.0,
    value=0.0,
    step=100.0
)

opm_min = st.sidebar.slider(
    "Minimum Operating Profit Margin (%)",
    min_value=0,
    max_value=100,
    value=10
)

icr_min = st.sidebar.slider(
    "Minimum Interest Coverage",
    min_value=0,
    max_value=100,
    value=3
)

asset_turnover_min = st.sidebar.slider(
    "Minimum Asset Turnover",
    min_value=0.0,
    max_value=5.0,
    value=0.5,
    step=0.1
)

# ---------------------------------
# SQL Query
# ---------------------------------

query = """
SELECT
    c.company_name,
    f.company_id,
    f.year,
    f.return_on_equity_pct,
    f.debt_to_equity,
    f.free_cash_flow_cr,
    f.operating_profit_margin_pct,
    f.interest_coverage,
    f.asset_turnover
FROM financial_ratios f
JOIN companies c
ON f.company_id = c.id
WHERE
    f.year = (
        SELECT MAX(fr.year)
        FROM financial_ratios fr
        WHERE fr.company_id = f.company_id
    )
    AND f.return_on_equity_pct >= ?
    AND f.debt_to_equity <= ?
    AND f.free_cash_flow_cr >= ?
    AND f.operating_profit_margin_pct >= ?
    AND f.interest_coverage >= ?
    AND f.asset_turnover >= ?
ORDER BY
    f.return_on_equity_pct DESC
"""

# ---------------------------------
# Execute Query
# ---------------------------------

result = run_query(
    query,
    (
        roe_min,
        de_max,
        fcf_min,
        opm_min,
        icr_min,
        asset_turnover_min
    )
)

# ---------------------------------
# Results
# ---------------------------------

st.subheader(f"📈 Companies Found: {len(result)}")

st.dataframe(
    result,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------
# CSV Download
# ---------------------------------

csv = result.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Results as CSV",
    data=csv,
    file_name="screener_results.csv",
    mime="text/csv"
)