import streamlit as st
import plotly.express as px

from utils.db import run_query

st.title("👥 Peer Comparison")

st.write("Compare companies within the same peer group.")

# ---------------------------------
# Load Peer Groups
# ---------------------------------

peer_groups = run_query("""
SELECT DISTINCT peer_group_name
FROM peer_groups
ORDER BY peer_group_name
""")

selected_group = st.selectbox(
    "Select Peer Group",
    peer_groups["peer_group_name"]
)

# ---------------------------------
# Load Companies
# ---------------------------------

companies = run_query("""
SELECT
    c.company_name,
    p.company_id
FROM peer_groups p
JOIN companies c
ON p.company_id = c.id
WHERE p.peer_group_name = ?
ORDER BY c.company_name
""", (selected_group,))

st.subheader("Companies in this Peer Group")

if companies.empty:
    st.warning("No companies found in this peer group.")
else:
    st.dataframe(
        companies,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------
# Peer Comparison Metrics
# ---------------------------------

comparison = run_query("""  
SELECT
    c.company_name,
    p.is_benchmark,
    f.return_on_equity_pct,
    f.debt_to_equity,
    f.free_cash_flow_cr,
    f.operating_profit_margin_pct,
    f.interest_coverage,
    f.asset_turnover
FROM peer_groups p
JOIN companies c
    ON p.company_id = c.id
JOIN financial_ratios f
    ON p.company_id = f.company_id
WHERE
    p.peer_group_name = ?
    AND f.year = (
        SELECT MAX(fr.year)
        FROM financial_ratios fr
        WHERE fr.company_id = f.company_id
    )
ORDER BY
    p.is_benchmark DESC,
    f.return_on_equity_pct DESC
""", (selected_group,))

comparison["Benchmark"] = comparison["is_benchmark"].map({
    1: "⭐ Benchmark",
    0: ""
})

comparison = comparison[
    [
        "company_name",
        "Benchmark",
        "return_on_equity_pct",
        "debt_to_equity",
        "free_cash_flow_cr",
        "operating_profit_margin_pct",
        "interest_coverage",
        "asset_turnover"
    ]
]

st.subheader("📊 Financial Comparison")

if comparison.empty:
    st.warning("No financial comparison data available.")
else:
    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )



# ---------------------------------
# Radar Chart
# ---------------------------------

if (
    not comparison.empty
    and len(comparison) >= 2
):

    radar_df = comparison.melt(
        id_vars="company_name",
        value_vars=[
            "return_on_equity_pct",
            "debt_to_equity",
            "operating_profit_margin_pct",
            "interest_coverage",
            "asset_turnover"
        ],
        var_name="Metric",
        value_name="Value"
    )

    fig = px.line_polar(
        radar_df,
        r="Value",
        theta="Metric",
        color="company_name",
        line_close=True
    )

    st.subheader("📈 Peer Radar Comparison")

    st.plotly_chart(
        fig,
        use_container_width=True
    )

