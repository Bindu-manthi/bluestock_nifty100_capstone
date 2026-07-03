# Sprint 2 Retrospective

## Sprint Goal
Develop a complete Financial Ratio Engine capable of calculating profitability, leverage, efficiency, CAGR, and cash flow KPIs for all companies and validating the results.

## Completed Work
- Implemented profitability ratios (Net Profit Margin, Operating Margin, ROE, ROCE, ROA).
- Implemented leverage and efficiency ratios (Debt-to-Equity, Interest Coverage, Net Debt, Asset Turnover).
- Developed CAGR engine with edge case handling.
- Built cash flow KPI calculations and capital allocation logic.
- Integrated the ratio engine with the SQLite database.
- Validated computed ratios against source values.
- Generated ratio_edge_cases.log for anomaly tracking.
- Successfully passed all 47 unit tests.

## Challenges
- Duplicate cashflow records produced duplicate ratio entries.
- SQL JOIN debugging across multiple tables.
- Differences between source ROE values and calculated ROE required validation.

## Lessons Learned
- Importance of data quality checks before analytics.
- Building reusable analytics functions.
- SQL joins and relational database validation.
- Edge case handling in financial analytics.

## Result
Sprint 2 completed successfully with a working Financial Ratio Engine, automated testing, database integration, and anomaly detection.