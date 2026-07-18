import streamlit as st
import plotly.express as px

from utils.db import (
    run_query,
    get_companies,
    get_ratios,
    get_pl,
    get_bs,
    get_cf,
)

st.title("🏢 Company Profile")

# -----------------------------
# Company Selection
# -----------------------------

companies = get_companies()

selected_company = st.selectbox(
    "Select Company",
    companies["company_name"].tolist()
)

company = companies[
    companies["company_name"] == selected_company
].iloc[0]

ticker = company["id"]

# -----------------------------
# Load Financial Data
# -----------------------------

ratios = get_ratios(ticker)
pl = get_pl(ticker)
bs = get_bs(ticker)
cf = get_cf(ticker)

latest_ratio = ratios.iloc[-1] if not ratios.empty else None
latest_pl = pl.iloc[-1] if not pl.empty else None
latest_cf = cf.iloc[-1] if not cf.empty else None

# -----------------------------
# Company Details
# -----------------------------

st.subheader(company["company_name"])
st.write(company["about_company"])

st.divider()

st.subheader("📌 Company Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Ticker", ticker)

with col2:
    st.metric("Book Value", round(company["book_value"], 2))

with col3:
    st.metric("ROE (%)", round(company["roe_percentage"], 2))

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("ROCE (%)", round(company["roce_percentage"], 2))

with col5:
    if latest_ratio is not None:
        st.metric(
            "Net Profit Margin (%)",
            round(latest_ratio["net_profit_margin_pct"], 2)
        )
    else:
        st.metric("Net Profit Margin (%)", "N/A")

with col6:
    if latest_ratio is not None:
        st.metric(
            "Debt / Equity",
            round(latest_ratio["debt_to_equity"], 2)
        )
    else:
        st.metric("Debt / Equity", "N/A")

# -----------------------------
# Financial KPI Cards
# -----------------------------

st.divider()

st.subheader("📊 Financial KPIs")

k1, k2, k3 = st.columns(3)

with k1:
    if latest_ratio is not None:
        st.metric(
            "Net Profit Margin",
            round(latest_ratio["net_profit_margin_pct"], 2)
        )

with k2:
    if latest_ratio is not None:
        st.metric(
            "Debt to Equity",
            round(latest_ratio["debt_to_equity"], 2)
        )

with k3:
    if latest_ratio is not None:
        st.metric(
            "Free Cash Flow (Cr)",
            round(latest_ratio["free_cash_flow_cr"], 2)
        )

# -----------------------------
# Revenue vs Net Profit
# -----------------------------

if not pl.empty:

    st.divider()

    st.subheader("📈 Revenue vs Net Profit")

    fig = px.bar(
        pl,
        x="year",
        y=["sales", "net_profit"],
        barmode="group",
        title="Revenue vs Net Profit"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROE Trend
# -----------------------------

if not ratios.empty:
    

    st.divider()

    st.subheader("📉 ROE Trend")

    fig = px.line(
        ratios,
        x="year",
        y="return_on_equity_pct",
        markers=True,
        title="Return on Equity Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Pros & Cons
# -----------------------------

pros_cons = run_query(
    """
    SELECT pros, cons
    FROM prosandcons
    WHERE company_id = ?
    """,
    (ticker,)
)

st.divider()

st.subheader("✅ Pros & ❌ Cons")

if not pros_cons.empty:

    left, right = st.columns(2)

    with left:
        st.success("Pros")
        st.write(pros_cons.iloc[0]["pros"])

    with right:
        st.error("Cons")
        st.write(pros_cons.iloc[0]["cons"])

else:
    st.info("No Pros & Cons available.")