import sqlite3

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    capex_intensity,
)
conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    p.company_id,
    p.year,
    p.sales,
    p.operating_profit,
    p.other_income,
    p.interest,
    p.net_profit,
    p.eps,
    p.dividend_payout,

    b.equity_capital,
    b.reserves,
    b.borrowings,
    b.investments,
    b.total_assets,

    c.operating_activity,
    c.investing_activity,
    c.financing_activity

FROM profitandloss p

INNER JOIN balancesheet b
ON p.company_id = b.company_id
AND p.year = b.year

INNER JOIN cashflow c
ON p.company_id = c.company_id
AND p.year = c.year
AND (
    c.operating_activity <> 0
    OR c.investing_activity <> 0
    OR c.financing_activity <> 0
)

LIMIT 5
""")
rows = cursor.fetchall()

for row in rows:

    company_id = row[0]
    year = row[1]

    sales = row[2]
    operating_profit = row[3]
    other_income = row[4]
    interest = row[5]
    net_profit = row[6]
    eps = row[7]
    dividend_payout = row[8]

    equity = row[9]
    reserves = row[10]
    borrowings = row[11]
    investments = row[12]
    total_assets = row[13]

    operating_activity = row[14]
    investing_activity = row[15]

    # Calculate KPIs
    npm = net_profit_margin(net_profit, sales)

    opm = operating_profit_margin(
        operating_profit,
        sales
    )

    roe = return_on_equity(
        net_profit,
        equity,
        reserves
    )

    dte = debt_to_equity(
        borrowings,
        equity,
        reserves
    )

    icr = interest_coverage_ratio(
        operating_profit,
        other_income,
        interest
    )

    turnover = asset_turnover(
        sales,
        total_assets
    )

    fcf = free_cash_flow(
        operating_activity,
        investing_activity
    )

    capex, label = capex_intensity(
        investing_activity,
        sales
    )

    print("\n----------------------------")
    print(f"Company : {company_id}")
    print(f"Year    : {year}")
    print(f"Net Profit Margin      : {npm}")
    print(f"Operating Margin       : {opm}")
    print(f"ROE                    : {roe}")
    print(f"Debt to Equity         : {dte}")
    print(f"Interest Coverage      : {icr}")
    print(f"Asset Turnover         : {turnover}")
    print(f"Free Cash Flow         : {fcf}")
    print(f"CapEx Intensity        : {capex}")
    print(f"CapEx Category         : {label}")
conn.close()