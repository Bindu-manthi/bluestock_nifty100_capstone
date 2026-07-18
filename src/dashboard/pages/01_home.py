import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add dashboard folder to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from utils.db import run_query

st.title("🏠 Home Dashboard")
st.caption("Interactive financial analytics dashboard for Nifty 100 companies.")
st.write("Welcome to the Nifty 100 Analytics Dashboard")

# ---------------------------------
# Sidebar
# ---------------------------------

selected_year = st.sidebar.selectbox(
    "Select Financial Year",
    ["2019", "2020", "2021", "2022", "2023", "2024"],
    index=5
)

st.sidebar.success(f"Selected Year: {selected_year}")

# ---------------------------------
# KPI Queries
# ---------------------------------

total_companies = run_query("""
SELECT COUNT(*) AS total
FROM companies
""")

average_roe = run_query("""
SELECT AVG(return_on_equity_pct) AS avg_roe
FROM financial_ratios
""")

avg_npm = run_query("""
SELECT AVG(net_profit_margin_pct) AS avg_npm
FROM financial_ratios
""")

avg_opm = run_query("""
SELECT AVG(operating_profit_margin_pct) AS avg_opm
FROM financial_ratios
""")

avg_de = run_query("""
SELECT AVG(debt_to_equity) AS avg_de
FROM financial_ratios
""")

debt_free = run_query("""
SELECT COUNT(DISTINCT company_id) AS debt_free
FROM financial_ratios
WHERE total_debt_cr = 0
""")

# ---------------------------------
# Safe Function
# ---------------------------------

def safe_metric(value):
    if value is None:
        return "N/A"
    try:
        if str(value) == "nan":
            return "N/A"
        return round(float(value), 2)
    except:
        return value

# ---------------------------------
# KPI Cards
# ---------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Companies", int(total_companies.iloc[0]["total"]))

with col2:
    st.metric(
        "Average ROE (%)",
        safe_metric(average_roe.iloc[0]["avg_roe"])
    )

with col3:
    st.metric(
        "Average Net Profit Margin (%)",
        safe_metric(avg_npm.iloc[0]["avg_npm"])
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Average Operating Profit Margin (%)",
        safe_metric(avg_opm.iloc[0]["avg_opm"])
    )

with col5:
    st.metric(
        "Average Debt to Equity",
        safe_metric(avg_de.iloc[0]["avg_de"])
    )

with col6:
    st.metric(
        "Debt-Free Companies",
        int(debt_free.iloc[0]["debt_free"])
    )

# ---------------------------------
# Sector Breakdown
# ---------------------------------

sector_df = run_query("""
SELECT
    broad_sector,
    COUNT(company_id) AS company_count
FROM sectors
GROUP BY broad_sector
ORDER BY company_count DESC
""")

st.subheader("📊 Sector Breakdown")

fig = px.pie(
    sector_df,
    names="broad_sector",
    values="company_count",
    hole=0.5,
    title="Companies by Broad Sector"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------
# Top 5 Companies
# ---------------------------------

top_companies = run_query("""
SELECT
    c.company_name,
    f.return_on_equity_pct,
    s.broad_sector
FROM companies c
JOIN financial_ratios f
    ON c.id = f.company_id
JOIN sectors s
    ON c.id = s.company_id
WHERE f.return_on_equity_pct IS NOT NULL
ORDER BY f.return_on_equity_pct DESC
LIMIT 5
""")

st.subheader("🏆 Top 5 Companies (Latest ROE)")

if top_companies.empty:
    st.info("No company data available.")
else:
    st.dataframe(
        top_companies,
        use_container_width=True,
        hide_index=True
    )