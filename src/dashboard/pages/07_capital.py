import streamlit as st

st.title("🏦 Capital Allocation")

st.info(
    """
### Capital Allocation Module

This dashboard requires valuation and market capitalization data.

The current SQLite database does not contain:

- Market Capitalization
- EV / EBITDA
- P/E Valuation Dataset
- Capital Allocation Classification

Therefore, the Capital Allocation dashboard cannot be generated from the available data.
"""
)

st.success("✔ Dashboard is working correctly. The page is ready for future valuation data.")