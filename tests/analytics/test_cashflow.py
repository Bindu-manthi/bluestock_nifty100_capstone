from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern,
)


# 1. Free Cash Flow
def test_free_cash_flow():
    assert free_cash_flow(500, -150) == 350


# 2. CFO Quality - High Quality
def test_cfo_quality_high():
    ratio, label = cfo_quality_score(1200, 1000)

    assert ratio == 1.2
    assert label == "High Quality"


# 3. CFO Quality - Moderate
def test_cfo_quality_moderate():
    ratio, label = cfo_quality_score(700, 1000)

    assert ratio == 0.7
    assert label == "Moderate"


# 4. CFO Quality - Accrual Risk
def test_cfo_quality_low():
    ratio, label = cfo_quality_score(300, 1000)

    assert ratio == 0.3
    assert label == "Accrual Risk"


# 5. PAT = 0
def test_cfo_quality_zero_pat():
    ratio, label = cfo_quality_score(1000, 0)

    assert ratio is None
    assert label is None


# 6. CapEx Intensity
def test_capex_intensity():
    value, label = capex_intensity(-50, 2000)

    assert value == 2.5
    assert label == "Asset Light"


# 7. FCF Conversion
def test_fcf_conversion():
    assert fcf_conversion_rate(300, 600) == 50


# 8. Zero Operating Profit
def test_fcf_conversion_zero():
    assert fcf_conversion_rate(300, 0) is None


# 9. Capital Allocation Pattern
def test_capital_allocation():
    assert (
        capital_allocation_pattern(100, -50, -25)
        == "Reinvestor"
    )


# 10. Distress Pattern
def test_distress():
    assert (
        capital_allocation_pattern(-100, 50, 100)
        == "Distress Signal"
    )