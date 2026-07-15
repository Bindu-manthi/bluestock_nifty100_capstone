import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

# Database path
DB_PATH = Path(__file__).resolve().parents[3] / "db" / "nifty100.db"


@st.cache_data(ttl=600)
def run_query(query, params=None):
    """Execute SQL query and return a DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_companies():
    return run_query("""
        SELECT *
        FROM companies
        ORDER BY company_name
    """)


@st.cache_data(ttl=600)
def get_ratios(ticker, year=None):

    if year:
        return run_query("""
            SELECT *
            FROM financial_ratios
            WHERE company_id=?
            AND year=?
        """, (ticker, year))

    return run_query("""
        SELECT *
        FROM financial_ratios
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


@st.cache_data(ttl=600)
def get_pl(ticker):

    return run_query("""
        SELECT *
        FROM profitandloss
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


@st.cache_data(ttl=600)
def get_bs(ticker):

    return run_query("""
        SELECT *
        FROM balancesheet
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


@st.cache_data(ttl=600)
def get_cf(ticker):

    return run_query("""
        SELECT *
        FROM cashflow
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


@st.cache_data(ttl=600)
def get_sectors():

    return run_query("""
        SELECT *
        FROM sectors
    """)


@st.cache_data(ttl=600)
def get_peers(group_name):

    return run_query("""
        SELECT *
        FROM peer_groups
        WHERE peer_group=?
    """, (group_name,))


@st.cache_data(ttl=600)
def get_valuation(ticker):

    return run_query("""
        SELECT *
        FROM financial_ratios
        WHERE company_id=?
        ORDER BY year DESC
        LIMIT 1
    """, (ticker,))