import streamlit as st
from utils.db import run_query

st.title("📄 Reports")
st.write("Generate and view company reports.")

# ---------------------------------
# Company List
# ---------------------------------

companies = run_query("""
SELECT
    company_name,
    id
FROM companies
ORDER BY company_name
""")

if companies.empty:
    st.warning("No companies found.")
    st.stop()

selected_company = st.selectbox(
    "Select Company",
    companies["company_name"]
)

company_id = companies.loc[
    companies["company_name"] == selected_company,
    "id"
].iloc[0]

# ---------------------------------
# Company Information
# ---------------------------------

company_info = run_query("""
SELECT
    c.company_name,
    s.broad_sector
FROM companies c
LEFT JOIN sectors s
ON c.id = s.company_id
WHERE c.id = ?
""", (company_id,))

st.subheader("Company Information")

if company_info.empty:
    st.info("No company information available.")
else:
    st.dataframe(
        company_info,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------
# Financial Summary
# ---------------------------------

financial_summary = run_query("""
SELECT
    year,
    MAX(return_on_equity_pct) AS return_on_equity_pct,
    MAX(debt_to_equity) AS debt_to_equity,
    MAX(free_cash_flow_cr) AS free_cash_flow_cr
FROM financial_ratios
WHERE company_id = ?
GROUP BY year
ORDER BY year DESC
LIMIT 10
""", (company_id,))

st.subheader("Financial Summary")

if financial_summary.empty:

    st.warning("No financial data available.")

else:

    st.dataframe(
        financial_summary,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------
    # Summary Statistics
    # -----------------------------

    st.subheader("Summary Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Records",
        len(financial_summary)
    )

    col2.metric(
        "Latest ROE",
        round(float(financial_summary.iloc[0]["return_on_equity_pct"]), 2)
    )

    col3.metric(
        "Latest Debt / Equity",
        round(float(financial_summary.iloc[0]["debt_to_equity"]), 2)
    )

    # -----------------------------
    # ROE Trend
    # -----------------------------

    st.subheader("ROE Trend")

    chart = financial_summary.sort_values("year")

    st.line_chart(
        chart.set_index("year")["return_on_equity_pct"]
    )

    # -----------------------------
    # CSV Download
    # -----------------------------

    csv = financial_summary.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Financial Summary (CSV)",
        data=csv,
        file_name=f"{selected_company}_financial_summary.csv",
        mime="text/csv"
    )