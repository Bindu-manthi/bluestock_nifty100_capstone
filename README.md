# 📊 Nifty100 Financial Analytics Dashboard

A comprehensive financial analytics project built using **Python, SQLite, Pandas, and Streamlit**. This project analyzes Nifty 100 companies by calculating financial ratios, screening companies based on investment criteria, comparing peers, visualizing trends, and presenting insights through an interactive dashboard.

---

# 🚀 Project Overview

This project was developed in four sprints:

- **Sprint 1:** Data Ingestion & ETL Pipeline
- **Sprint 2:** Financial Ratio & Analytics Engine
- **Sprint 3:** Screener & Peer Comparison Engine
- **Sprint 4:** Interactive Streamlit Dashboard

---

# 📌 Sprint 1 – Data Engineering

### Objectives

- Build ETL pipeline
- Load Nifty100 company data
- Store cleaned data in SQLite
- Normalize financial statements

### Completed

- Company master data
- Profit & Loss data
- Balance Sheet data
- Cash Flow data
- Documents
- Stock Prices
- Peer Groups
- Sectors
- Database validation
- Data cleaning
- Automated ETL pipeline

---

# 📌 Sprint 2 – Financial Analytics Engine

### Objectives

Calculate important financial metrics.

### Implemented KPIs

- Return on Equity (ROE)
- Return on Assets (ROA)
- Debt to Equity
- Operating Profit Margin
- Net Profit Margin
- Interest Coverage
- Asset Turnover
- Free Cash Flow
- Book Value Per Share
- Earnings Per Share (EPS)
- Cash From Operations
- Total Debt
- Revenue CAGR
- Profit CAGR
- EPS CAGR

### Output

- Financial ratios stored in SQLite
- Analytics module completed
- Automated calculations

---

# 📌 Sprint 3 – Screener & Peer Comparison

### Financial Screener

Implemented predefined screeners:

- Quality Compounder
- Growth Stocks
- Value Picks
- Dividend Stocks
- Debt Free Companies
- Custom Filters

### Peer Comparison

Compare companies within the same sector using:

- ROE
- Debt to Equity
- Free Cash Flow
- Operating Margin
- Interest Coverage
- Asset Turnover

### Outputs

- Peer Rankings
- Company Comparison Tables
- Sector-based analysis

---

# 📌 Sprint 4 – Streamlit Dashboard

Built an interactive dashboard using Streamlit.

### Dashboard Pages

### 🏠 Home

- Overall dashboard
- Company statistics
- Summary metrics

### 👤 Company Profile

- Company information
- Financial overview

### 🔍 Screener

- Apply predefined filters
- View screened companies

### 📊 Peer Comparison

- Compare companies
- Benchmark analysis
- Financial metrics

### 📈 Trend Analysis

Historical visualization of

- Revenue
- Net Profit
- ROE
- Free Cash Flow

### 🏭 Sector Analysis

- Sector selection
- Company listing
- Total companies
- Average ROE
- Average Debt/Equity
- Company-wise ROE
- Sector comparison charts

### 📄 Reports

- Financial summary
- Company information
- CSV download

> **Note:** A Valuation page (P/E, P/B, Market Cap, Dividend Yield) was planned, but the current SQLite database does not contain the required valuation tables/columns, so it was not implemented.

---

# 🗂 Project Structure

```text
nifty100_capstone/
│
├── data/
│   └── nifty100.db
│
├── src/
│   ├── analytics/
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── pages/
│   │   │   ├── 01_home.py
│   │   │   ├── 02_profile.py
│   │   │   ├── 03_screener.py
│   │   │   ├── 04_peer_comparison.py
│   │   │   ├── 05_trends.py
│   │   │   ├── 06_sectors.py
│   │   │   ├── 07_capital.py (placeholder)
│   │   │   └── 08_reports.py
│   │   └── utils/
│   │       └── db.py
│   │
│   ├── etl/
│   ├── screener/
│   └── valuation/
│
├── tests/
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

- Python 3.13
- Pandas
- NumPy
- SQLite
- Streamlit
- Matplotlib
- Plotly
- Pytest
- Git
- GitHub

---

# ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd nifty100_capstone
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run src/dashboard/app.py
```

---

# ✅ Running Tests

```bash
python -m pytest
```

Latest Result

```text
47 passed in 2.48s
```

---

# 📊 Database

SQLite database contains:

- companies
- profitandloss
- balancesheet
- cashflow
- financial_ratios
- stock_prices
- sectors
- peer_groups
- peer_percentiles
- prosandcons
- documents
- analysis

---

# ✨ Key Features

- Financial Ratio Calculation
- Automated ETL
- SQLite Database
- Company Screener
- Peer Comparison
- Trend Analysis
- Sector Analytics
- Interactive Dashboard
- CSV Report Download
- Unit Tested Code
- Modular Architecture

---

# 📈 Future Enhancements

- Valuation Module (P/E, P/B, Market Cap)
- Live Stock Price Integration
- Portfolio Tracking
- Watchlist
- PDF Report Export
- Authentication
- Cloud Deployment

---

# 👨‍💻 Author

**Bindu Madhavi Manthi**

**MCA Graduate**

Python Developer | Data Analyst

GitHub: https://github.com/Bindu-manthi



---

# ⭐ Project Status

**Completed**

- ✅ Sprint 1
- ✅ Sprint 2
- ✅ Sprint 3
- ✅ Sprint 4

**All automated tests passing (47/47).**


