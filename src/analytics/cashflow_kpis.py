"""
Sprint 2 - Day 11
Cash Flow KPIs
"""


def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow

    Formula:
    Operating Cash Flow + Investing Cash Flow
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    """
    CFO Quality Ratio

    Returns:
        ratio, label
    """
    if pat == 0:
        return None, None

    ratio = cfo / pat

    if ratio > 1:
        label = "High Quality"
    elif ratio >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return round(ratio, 2), label


def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity
    """
    if sales == 0:
        return None, None

    value = abs(investing_activity) / sales * 100

    if value < 3:
        label = "Asset Light"
    elif value <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(value, 2), label


def fcf_conversion_rate(fcf, operating_profit):
    """
    FCF Conversion Rate
    """
    if operating_profit == 0:
        return None

    return round((fcf / operating_profit) * 100, 2)


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Capital Allocation Classification
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    patterns = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed",
    }

    return patterns.get(signs, "Unknown")