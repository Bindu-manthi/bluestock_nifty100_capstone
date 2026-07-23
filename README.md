# 📈 NIFTY100 Financial Intelligence Platform

A comprehensive financial intelligence platform built using **Python, Streamlit, SQLite, Pandas, Plotly, and SQLAlchemy** for analyzing NIFTY100 companies. The platform provides financial analytics, company screening, peer comparison, trend analysis, sector insights, automated reporting, and NLP-based financial intelligence through an interactive dashboard.

---

# 🚀 Features

- Company Financial Profile
- Financial Screener
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Analysis
- Report Generation
- Financial Ratio Analytics
- Executive Summary Generation
- Company Scorecards
- Dashboard Dataset Generation
- NLP-based Financial Narratives
- Interactive Charts
- SQLite Database Integration
- CSV Export Support

---

# 🛠 Tech Stack

- Python 3.13
- Streamlit
- Pandas
- Plotly
- SQLite
- SQLAlchemy
- OpenPyXL
- Pytest

---

# 📂 Project Structure

```text
nifty100_capstone/
│
├── data/
│
├── db/
│   └── nifty100.db
│
├── output/
│
├── src/
│   ├── analytics/
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── pages/
│   │   │   ├── 01_home.py
│   │   │   ├── 02_profile.py
│   │   │   ├── 03_screener.py
│   │   │   ├── 04_peers.py
│   │   │   ├── 05_trends.py
│   │   │   ├── 06_sectors.py
│   │   │   ├── 07_capital.py
│   │   │   └── 08_reports.py
│   │   └── utils/
│   │       └── db.py
│   │
│   ├── analytics/
│   ├── etl/
│   ├── screener/
│   └── nlp/
│
├── tests/
│
├── requirements.txt
├── README.md
└── run_pipeline.py
```

---

# 📊 Dashboard Modules

## 🏠 Home

- Project Overview
- Database Summary
- KPI Cards
- Company Statistics

---

## 👤 Company Profile

- Company Information
- Financial Overview
- ROE Trend
- Business Summary

---

## 🔍 Financial Screener

Filter companies using financial metrics like:

- Return on Equity (ROE)
- Debt to Equity Ratio
- Revenue Growth
- Free Cash Flow
- Market Capitalization
- Net Profit

---

## 🤝 Peer Comparison

Compare companies within the same peer group.

Includes:

- Financial Metrics
- Peer Benchmarking
- Comparative Analysis

---

## 📈 Trend Analysis

Historical analysis for:

- Revenue
- Net Profit
- ROE
- Free Cash Flow

Interactive visualizations help identify long-term business performance.

---

## 🏭 Sector Analysis

- Companies by Sector
- Sector-wise Performance
- Average Financial Metrics
- Interactive Charts

---

## 💰 Capital Analysis

Displays capital allocation and capital structure information using financial database records.

---

## 📄 Reports

Generate company reports including:

- Financial Summary
- Company Details
- Key Financial Metrics
- ROE Trend
- CSV Export

---

# 🚀 Project Development Timeline

## ✅ Sprint 1 – Data Foundation (Days 1–7)

### Goal

Build a reliable financial database by loading, validating, and storing NIFTY100 financial statements.

### Completed

- Python project setup
- Virtual environment configuration
- Excel data ingestion
- Data normalization
- SQLite schema creation
- ETL pipeline
- Data validation framework

### Deliverables

- SQLite Database
- ETL Modules
- Data Validation Engine

---

## ✅ Sprint 2 – Financial Ratio Engine (Days 8–14)

### Goal

Develop a financial analytics engine capable of calculating key financial ratios and KPIs.

### Completed

- Profitability Ratios
- Liquidity Ratios
- Leverage Ratios
- Efficiency Ratios
- CAGR Engine
- Cash Flow KPI Engine
- Financial Ratio Population

### Deliverables

- 50+ Financial KPIs
- Financial Ratio Engine
- Automated KPI Calculations

---

## ✅ Sprint 3 – Financial Screener & Peer Comparison (Days 15–21)

### Goal

Develop intelligent company screening and peer comparison capabilities.

### Completed

- Financial Screener Engine
- Preset Screeners
- Custom Filters
- Peer Ranking Engine
- Benchmark Analysis

### Deliverables

- Company Screening Engine
- Peer Comparison Module
- Percentile Ranking System

---

## ✅ Sprint 4 – Dashboard & Visualization (Days 22–28)

### Goal

Build an interactive Streamlit dashboard for financial analysis and visualization.

### Completed

- Home Dashboard
- Company Profile Page
- Financial Screener UI
- Peer Comparison Dashboard
- Trend Analysis
- Sector Analysis
- Capital Analysis
- Report Module

### Deliverables

- Interactive Dashboard
- Data Visualizations
- CSV Export Support

---

## ✅ Sprint 5 – NLP Financial Intelligence (Days 29–35)

### Goal

Generate automated financial narratives, reports, scorecards, and executive summaries using NLP and rule-based analytics.

### Completed

- Financial Data Parser
- CAGR Validation Engine
- Company Narrative Generator
- Financial Insight Generator
- Company Report Generator
- Company Scorecard Generator
- Dashboard Dataset Generator
- Executive Summary Generator

### Deliverables

- Company Narratives
- Financial Insights
- Company Reports
- Investment Scorecards
- Dashboard Dataset
- Executive Summaries

---

# 📊 Database

SQLite database includes:

- companies
- stock_prices
- balancesheet
- profitandloss
- cashflow
- financial_ratios
- peer_groups
- peer_percentiles
- sectors
- analysis
- documents

---

# 📁 Generated Outputs

```text
output/
├── analysis_parsed.csv
├── parse_failures.csv
├── cagr_divergence_review.csv
├── company_narratives.csv
├── company_insights.csv
├── company_reports.csv
├── company_scorecards.csv
├── dashboard_dataset.csv
└── executive_summaries.csv
```

---

# 🧪 Testing

Run the automated test suite:

```bash
python -m pytest
```

### Result

```text
47 / 47 Tests Passed
```

---

# ▶️ Run the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit dashboard:

```bash
streamlit run src/dashboard/app.py
```

---

# ✅ Key Highlights

- Interactive Financial Intelligence Dashboard
- Automated ETL Pipeline
- SQLite Database Integration
- Financial Ratio Analytics (50+ KPIs)
- Financial Screening Engine
- Peer Benchmarking
- Sector Performance Analysis
- Trend Visualization
- Company Report Generation
- NLP-based Financial Narratives
- Financial Insight Generation
- Executive Summary Generation
- Investment Recommendation Engine
- Dashboard-ready Dataset Generation
- CSV Export Support
- Fully Tested Application (47/47 Tests Passed)

---

# 👩‍💻 Developed By

**Bindu Madhavi Manthi**

MCA Graduate

Python Developer | Django | SQL | Data Analytics

---

# 📜 License

This project was developed as part of a **Financial Analytics Capstone Project** for educational and learning purposes.