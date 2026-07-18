# 📈 Nifty100 Analytics Dashboard

A comprehensive financial analytics dashboard built using **Python, Streamlit, SQLite, Pandas, and Plotly** for analyzing Nifty 100 companies. The project provides company insights, financial screening, peer comparison, sector analysis, trend visualization, and report generation through an interactive web dashboard.

---

# 🚀 Features

- Company Financial Profile
- Financial Screener
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Analysis
- Report Generation
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

```
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
│   ├── etl/
│   └── screener/
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

- ROE
- Debt to Equity
- Revenue Growth
- Free Cash Flow
- Market Capitalization
- Net Profit

---

## 🤝 Peer Comparison

Compare companies within the same peer group.

Includes:

- Financial Metrics
- Benchmark Identification
- Radar Chart Comparison

---

## 📈 Trend Analysis

Historical analysis for:

- Sales
- Net Profit
- ROE
- Free Cash Flow

Interactive visualizations help identify long-term performance.

---

## 🏭 Sector Analysis

- Companies by Sector
- Sector-wise Performance
- Average Financial Metrics
- Interactive Charts

---

## 💰 Capital Analysis

Displays available capital-related financial information from the project database.

---

## 📄 Reports

Generate company reports including:

- Financial Summary
- Company Details
- Key Metrics
- ROE Trend
- CSV Download

---

# 🧪 Testing

The project includes automated unit tests.

Run:

```bash
python -m pytest
```

Result:

```
47 passed
```

---

# ▶️ Run Dashboard

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Streamlit

```bash
streamlit run src/dashboard/app.py
```

---

# 📊 Database

SQLite database contains:

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

# ✅ Key Highlights

- Interactive Financial Dashboard
- Financial Ratio Analytics
- Company Screening Engine
- Peer Benchmarking
- Sector Insights
- Trend Visualization
- Report Generation
- SQLite Integration
- Fully Tested Application

---

# 🧪 Test Status

```
47 / 47 Tests Passed
```

---

# 👩‍💻 Developed By

**Bindu Madhavi Manthi**

MCA Graduate

Python Developer | Django | SQL | Data Analytics

---

# 📜 License

This project was developed as part of a Financial Analytics Capstone for educational purposes.