"""
Financial Ratio Engine
Sprint 2 - Day 8
Profitability Ratio Functions
"""


def net_profit_margin(net_profit, sales):
    """
    Calculate Net Profit Margin (%)

    Formula:
    Net Profit Margin = (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Calculate Operating Profit Margin (%)

    Formula:
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (operating_profit / sales) * 100


def check_opm(calculated_opm, source_opm):
    """
    Compare calculated OPM with source OPM.

    Returns True if the difference is greater than 1%.
    """
    if calculated_opm is None or source_opm is None:
        return False

    return abs(calculated_opm - source_opm) > 1


def return_on_equity(net_profit, equity_capital, reserves):
    """
    Calculate Return on Equity (ROE)

    Formula:
    ROE = Net Profit / (Equity Capital + Reserves) * 100
    """
    capital = equity_capital + reserves

    if capital <= 0:
        return None

    return (net_profit / capital) * 100


def return_on_capital_employed(
    ebit,
    equity_capital,
    reserves,
    borrowings
):
    """
    Calculate Return on Capital Employed (ROCE)

    Formula:
    ROCE = EBIT / (Equity + Reserves + Borrowings) * 100
    """
    capital_employed = equity_capital + reserves + borrowings

    if capital_employed <= 0:
        return None

    return (ebit / capital_employed) * 100


def return_on_assets(net_profit, total_assets):
    """
    Calculate Return on Assets (ROA)

    Formula:
    ROA = Net Profit / Total Assets * 100
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


# Day 9 - Leverage & Efficiency Ratios


def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Calculate Debt-to-Equity Ratio

    Formula:
    Borrowings / (Equity Capital + Reserves)

    Rules:
    - If borrowings = 0, return 0
    - If equity + reserves <= 0, return None
    """
    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return borrowings / equity


def high_leverage_flag(debt_to_equity_ratio, sector):
    """
    Returns True if:
    - Debt-to-Equity > 5
    - Company is NOT in Financials sector
    """
    if debt_to_equity_ratio is None:
        return False

    if sector.lower() == "financials":
        return False

    return debt_to_equity_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    """
    Calculate Interest Coverage Ratio (ICR)

    Formula:
    (Operating Profit + Other Income) / Interest

    Rule:
    - Return None if interest = 0
    """
    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def interest_coverage_label(interest):
    """
    Return 'Debt Free' when interest expense is zero.
    """
    if interest == 0:
        return "Debt Free"

    return None


def net_debt(borrowings, investments):
    """
    Net Debt = Borrowings - Investments
    """
    return borrowings - investments


def asset_turnover(sales, total_assets):
    """
    Asset Turnover = Sales / Total Assets

    Rule:
    - Return None if total_assets = 0
    """
    if total_assets == 0:
        return None

    return sales / total_assets