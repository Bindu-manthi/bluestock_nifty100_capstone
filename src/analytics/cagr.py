"""
Financial Ratio Engine
Sprint 2 - Day 10
CAGR (Compound Annual Growth Rate)
"""


def calculate_cagr(start_value, end_value, years):
    """
    Calculate CAGR with edge case handling.

    Returns:
        (cagr_value, flag)

    Flags:
        None
        DECLINE_TO_LOSS
        TURNAROUND
        BOTH_NEGATIVE
        ZERO_BASE
        INSUFFICIENT
    """

    if years <= 0:
        return None, "INSUFFICIENT"

    if start_value == 0:
        return None, "ZERO_BASE"

    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    cagr = ((end_value / start_value) ** (1 / years) - 1) * 100

    return round(cagr, 2), None


def revenue_cagr(start_revenue, end_revenue, years):
    return calculate_cagr(start_revenue, end_revenue, years)


def pat_cagr(start_pat, end_pat, years):
    return calculate_cagr(start_pat, end_pat, years)


def eps_cagr(start_eps, end_eps, years):
    return calculate_cagr(start_eps, end_eps, years)