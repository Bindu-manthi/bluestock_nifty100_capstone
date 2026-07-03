# Nifty 100 Financial Analytics Capstone

## Project Overview

This project is a Financial Analytics Engine built using Python and SQLite to analyze financial statements of Nifty 100 companies. The project performs ETL, data validation, financial ratio calculations, CAGR analysis, cash flow analytics, and edge case validation.

The project is divided into multiple sprints. Sprint 1 focuses on building the data foundation, while Sprint 2 develops the Financial Ratio Engine.

---

# Technologies Used

- Python 3
- SQLite
- Pandas
- NumPy
- Pytest
- SQL
- VS Code
- Git & GitHub

---

# Project Structure

```text
nifty100_capstone/
│
├── data/
├── db/
│   └── nifty100.db
│
├── output/
│   ├── capital_allocation.csv
│   └── ratio_edge_cases.log
│
├── src/
│   ├── analytics/
│   │   ├── ratios.py
│   │   ├── cagr.py
│   │   ├── cashflow_kpis.py
│   │   ├── populate_financial_ratios.py
│   │   └── ratio_edge_cases.py
│   │
│   ├── etl/
│   └── database/
│
├── tests/
│   ├── analytics/
│   └── etl/
│
├── README.md
└── requirements.txt
```

---

# Sprint 1 — Data Foundation

## Sprint Goal

Build a clean and validated financial database for Nifty 100 companies.

### Tasks Completed

- Environment setup
- Project folder structure
- Python virtual environment
- SQLite database creation
- ETL pipeline development
- Data loading
- Data normalization
- Data validation
- Primary key validation
- Company-Year validation
- SQLite schema creation
- Loading financial statements into database

### Database Tables

- companies
- sectors
- balancesheet
- profitandloss
- cashflow
- stock_prices
- peer_groups
- documents
- prosandcons
- financial_ratios

### Sprint 1 Deliverables

- SQLite database
- ETL pipeline
- Validation scripts
- Automated tests
- GitHub repository

---

# Sprint 2 — Financial Ratio Engine

## Sprint Goal

Develop a Financial Ratio Engine capable of calculating financial KPIs for every company-year.

---

## Profitability Ratios

Implemented:

- Net Profit Margin
- Operating Profit Margin
- Return on Equity (ROE)
- Return on Capital Employed (ROCE)
- Return on Assets (ROA)

---

## Leverage & Efficiency Ratios

Implemented:

- Debt-to-Equity
- Interest Coverage Ratio
- Net Debt
- Asset Turnover

---

## CAGR Engine

Implemented:

- Revenue CAGR
- PAT CAGR
- EPS CAGR

Handled Edge Cases:

- Turnaround
- Decline to Loss
- Both Negative
- Zero Base
- Insufficient Data

---

## Cash Flow KPIs

Implemented:

- Free Cash Flow
- CFO Quality Score
- CapEx Intensity
- FCF Conversion Rate
- Capital Allocation Classification

---

## Database Integration

Successfully integrated analytics with SQLite.

Joined:

- Profit & Loss
- Balance Sheet
- Cash Flow

Generated:

- financial_ratios table

Verified:

- 1184 company-year records

---

## Data Validation

Validated:

- ROE comparison
- ROCE comparison
- Financial sector edge cases
- Duplicate detection
- Ratio anomaly detection

Generated:

```text
output/
    ratio_edge_cases.log
```

---

## Testing

All analytics modules successfully tested.

### Test Summary

```
47 Tests Passed
0 Test Failures
```

Modules Tested

- Ratio Engine
- CAGR Engine
- Cash Flow KPIs
- ETL Normalization
- Data Validation

---

# Outputs

Generated files:

- financial_ratios (SQLite)
- ratio_edge_cases.log
- capital_allocation.csv

---

# Key Features

✔ Automated ETL

✔ SQLite Integration

✔ Financial Ratio Engine

✔ CAGR Analytics

✔ Cash Flow Analytics

✔ Edge Case Detection

✔ Automated Testing

✔ Financial Data Validation

---

# Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 – Data Foundation | ✅ Completed |
| Sprint 2 – Financial Ratio Engine | ✅ Completed |
| Sprint 3 | ⏳ Upcoming |

---

# Future Improvements

- Power BI Dashboard
- Company Screener
- Portfolio Analytics
- Risk Metrics
- Interactive Visualizations

---

# Author

**Bindu Madhavi Manthi**

Python Developer | Data Analyst

GitHub:
https://github.com/Bindu-manthi

