import streamlit as st
from utils.db import run_query

st.title("🏭 Sector Analysis")
st.write("Analyze companies by sector.")

# ---------------------------------
# Load Sectors
# ---------------------------------

sectors = run_query("""
SELECT DISTINCT broad_sector
FROM sectors
ORDER BY broad_sector
""")

if sectors.empty:
    st.warning("No sectors available.")
    st.stop()

selected_sector = st.selectbox(
    "Select Sector",
    sectors["broad_sector"]
)

# ---------------------------------
# Companies in Selected Sector
# ---------------------------------

sector_companies = run_query("""
SELECT
    c.company_name
FROM companies c
JOIN sectors s
    ON c.id = s.company_id
WHERE s.broad_sector = ?
ORDER BY c.company_name
""", (selected_sector,))

st.subheader(f"Companies in {selected_sector}")

if sector_companies.empty:
    st.warning("No companies available.")
else:
    st.dataframe(
        sector_companies,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------
# Sector KPIs
# ---------------------------------

sector_stats = run_query("""
SELECT
    ROUND(AVG(f.return_on_equity_pct),2) AS avg_roe
FROM financial_ratios f
JOIN sectors s
ON f.company_id = s.company_id
WHERE s.broad_sector = ?
""", (selected_sector,))

sector_de = run_query("""
SELECT
    ROUND(AVG(f.debt_to_equity),2) AS avg_de
FROM financial_ratios f
JOIN sectors s
ON f.company_id = s.company_id
WHERE s.broad_sector = ?
""", (selected_sector,))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Companies",
        len(sector_companies)
    )

with col2:
    st.metric(
        "Average ROE (%)",
        sector_stats.iloc[0]["avg_roe"]
    )

with col3:
    st.metric(
        "Average Debt / Equity",
        sector_de.iloc[0]["avg_de"]
    )

# ---------------------------------
# Company-wise ROE
# ---------------------------------

company_roe = run_query("""
SELECT
    c.company_name,
    ROUND(f.return_on_equity_pct,2) AS ROE,
    f.year
FROM companies c
JOIN financial_ratios f
ON c.id = f.company_id
JOIN sectors s
ON c.id = s.company_id
WHERE s.broad_sector = ?
AND f.year = (
    SELECT MAX(f2.year)
    FROM financial_ratios f2
    WHERE f2.company_id = f.company_id
)
ORDER BY ROE DESC
""", (selected_sector,))

st.subheader("Company-wise ROE")

if company_roe.empty:
    st.info("No ROE data available.")
else:
    st.dataframe(
        company_roe,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------
# Companies Per Sector
# ---------------------------------

sector_count = run_query("""
SELECT
    broad_sector,
    COUNT(*) AS companies
FROM sectors
GROUP BY broad_sector
ORDER BY companies DESC
""")

st.subheader("Companies per Sector")

st.dataframe(
    sector_count,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------
# Companies by Sector Chart
# ---------------------------------

st.subheader("Companies by Sector")

sector_chart = run_query("""
SELECT
    broad_sector,
    COUNT(*) AS companies
FROM sectors
GROUP BY broad_sector
ORDER BY companies DESC
""")

st.bar_chart(
    sector_chart.set_index("broad_sector")
)

# ---------------------------------
# Average ROE by Sector
# ---------------------------------

st.subheader("Average ROE by Sector")

roe_chart = run_query("""
SELECT
    s.broad_sector,
    ROUND(AVG(f.return_on_equity_pct),2) AS avg_roe
FROM sectors s
JOIN financial_ratios f
ON s.company_id = f.company_id
GROUP BY s.broad_sector
ORDER BY avg_roe DESC
""")

st.bar_chart(
    roe_chart.set_index("broad_sector")
)