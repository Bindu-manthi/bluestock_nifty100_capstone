from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    check_opm,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
)


# 1. Net Profit Margin - Normal Case
def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10


# 2. Net Profit Margin - Sales = 0
def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


# 3. Operating Profit Margin
def test_operating_profit_margin():
    assert operating_profit_margin(200, 1000) == 20


# 4. OPM Cross-check Mismatch
def test_check_opm():
    assert check_opm(20, 18) is True


# 5. Return on Equity - Normal Case
def test_return_on_equity():
    assert return_on_equity(100, 200, 300) == 20


# 6. Return on Equity - Negative Equity
def test_return_on_equity_negative():
    assert return_on_equity(100, -200, 100) is None


# 7. Return on Capital Employed
def test_return_on_capital_employed():
    assert return_on_capital_employed(150, 200, 300, 500) == 15


# 8. Return on Assets
def test_return_on_assets():
    assert return_on_assets(100, 1000) == 10


# Day 9 Tests


from src.analytics.ratios import (
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    interest_coverage_label,
    net_debt,
    asset_turnover,
)


def test_debt_to_equity():
    assert debt_to_equity(200, 100, 100) == 1


def test_debt_to_equity_debt_free():
    assert debt_to_equity(0, 100, 100) == 0


def test_debt_to_equity_negative_equity():
    assert debt_to_equity(100, -200, 100) is None


def test_high_leverage_flag():
    assert high_leverage_flag(6.5, "Technology") is True


def test_high_leverage_financials():
    assert high_leverage_flag(8.0, "Financials") is False


def test_interest_coverage_ratio():
    assert interest_coverage_ratio(400, 100, 50) == 10


def test_interest_coverage_zero_interest():
    assert interest_coverage_ratio(400, 100, 0) is None


def test_interest_coverage_label():
    assert interest_coverage_label(0) == "Debt Free"


def test_net_debt():
    assert net_debt(1000, 250) == 750


def test_asset_turnover():
    assert asset_turnover(5000, 2500) == 2


def test_asset_turnover_zero_assets():
    assert asset_turnover(1000, 0) is None