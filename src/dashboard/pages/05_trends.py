import streamlit as st
import plotly.express as px

from utils.db import run_query

st.title("📈 Trend Analysis")

st.write("Analyze historical financial trends for a company.")
# ---------------------------------
# Load Companies
# ---------------------------------

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

st.caption(f"Selected Company: {selected_company}")

# ---------------------------------
# Load Historical Financial Data
# ---------------------------------

trend_data = run_query("""
SELECT
    p.year,
    p.sales,
    p.net_profit,
    f.return_on_equity_pct,
    f.free_cash_flow_cr
FROM profitandloss p
JOIN financial_ratios f
    ON p.company_id = f.company_id
    AND p.year = f.year
WHERE p.company_id = ?
ORDER BY p.year
""", (company_id,))

if trend_data.empty:
    st.warning("No historical financial data available.")
    st.stop()
    trend_data = trend_data.sort_values("year")

st.subheader("Historical Financial Data")

st.dataframe(
    trend_data,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------
# Latest Financial Snapshot
# ---------------------------------

latest = trend_data.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        f"₹ {latest['sales']:,.2f} Cr"
    )

with col2:
    st.metric(
        "Net Profit",
        f"₹ {latest['net_profit']:,.2f} Cr"
    )

with col3:
    st.metric(
        "ROE",
        f"{latest['return_on_equity_pct']:.2f}%"
    )

with col4:
    st.metric(
        "Free Cash Flow",
        f"₹ {latest['free_cash_flow_cr']:,.2f} Cr"
    )


# ---------------------------------
# Revenue Trend
# ---------------------------------

st.subheader("📈 Revenue Trend")

fig = px.line(
    trend_data,
    x="year",
    y="sales",
    markers=True,
    title=f"{selected_company} - Revenue Trend"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Sales (₹ Cr)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------
# Net Profit Trend
# ---------------------------------

st.subheader("💰 Net Profit Trend")

fig = px.line(
    trend_data,
    x="year",
    y="net_profit",
    markers=True,
    title=f"{selected_company} - Net Profit Trend"
)
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Net Profit (₹ Cr)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------
# ROE Trend
# ---------------------------------

st.subheader("📊 Return on Equity (ROE) Trend")

fig = px.line(
    trend_data,
    x="year",
    y="return_on_equity_pct",
    markers=True,
    title=f"{selected_company} - ROE Trend"
)
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="ROE (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------
# Free Cash Flow Trend
# ---------------------------------

st.subheader("💵 Free Cash Flow Trend")

fig = px.line(
    trend_data,
    x="year",
    y="free_cash_flow_cr",
    markers=True,
    title=f"{selected_company} - Free Cash Flow Trend"
)
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Free Cash Flow (₹ Cr)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)