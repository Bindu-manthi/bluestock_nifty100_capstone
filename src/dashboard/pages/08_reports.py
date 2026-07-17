import streamlit as st
from utils.db import run_query
st.title("📄 Reports")

st.write("Generate and view company reports.")
companies = run_query("""
SELECT
    company_name,
    id
FROM companies
ORDER BY company_name
""")

selected_company = st.selectbox(
    "Select Company",
    companies["company_name"]
)

company_id = companies.loc[
    companies["company_name"] == selected_company,
    "id"
].iloc[0]

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

st.dataframe(
    company_info,
    use_container_width=True,
    hide_index=True
)

financial_summary = run_query("""
SELECT
    year,
    return_on_equity_pct,
    debt_to_equity,
    free_cash_flow_cr
FROM financial_ratios
WHERE company_id = ?
ORDER BY year DESC
LIMIT 10
""", (company_id,))


st.subheader("Financial Summary")

if financial_summary.empty:
    st.warning("No data available.")
else:
    st.dataframe(
        financial_summary,
        use_container_width=True,
        hide_index=True
    )
    
csv = financial_summary.to_csv(index=False).encode("utf-8")

st.subheader("Summary Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Records",
    len(financial_summary)
)

col2.metric(
    "Latest ROE",
    financial_summary.iloc[0]["return_on_equity_pct"]
)

col3.metric(
    "Latest Debt/Equity",
    financial_summary.iloc[0]["debt_to_equity"]
)

st.subheader("ROE Trend")

chart = financial_summary.copy()

chart = chart.sort_values("year")

st.line_chart(
    chart.set_index("year")["return_on_equity_pct"]
)

st.download_button(
    label="📥 Download Financial Summary (CSV)",
    data=csv,
    file_name=f"{selected_company}_financial_summary.csv",
    mime="text/csv"
)