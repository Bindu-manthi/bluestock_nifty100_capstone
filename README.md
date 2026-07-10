# Nifty100 Financial Analytics & Stock Screener

## Overview

This project is a financial analytics platform for Nifty 100 companies. It extracts, processes, and analyzes company financial data to generate key financial ratios, stock screeners, peer comparisons, and visual reports.

The project is implemented in multiple sprints, with each sprint adding new analytical capabilities and reporting features.

---

## Sprint Progress

### Sprint 1 – Data Foundation

* Project structure and environment setup
* Data ingestion and normalization
* SQLite database creation
* Data validation pipeline
* ETL workflow

### Sprint 2 – Financial Ratio Engine

* Profitability ratios
* Leverage ratios
* Efficiency ratios
* CAGR calculations
* Cash Flow KPIs
* Financial ratio population
* Edge case validation
* Unit testing

### Sprint 3 – Screener & Peer Engine

* Configurable stock screener
* Six preset screeners
* Composite quality scoring
* Excel screener export
* Peer percentile ranking engine
* SQLite peer percentile storage
* Radar chart generation
* Peer comparison Excel report

---

## Project Structure

```text
nifty100_capstone/
│
├── config/
│   └── screener_config.yaml
│
├── db/
│   └── nifty100.db
│
├── output/
│   ├── screener_output.xlsx
│   └── peer_comparison.xlsx
│
├── reports/
│   └── radar_charts/
│
├── src/
│   ├── analytics/
│   ├── screener/
│   └── etl/
│
├── tests/
│
└── README.md
```

---

## Features

### Data Processing

* Data ingestion
* Data cleaning
* Validation
* SQLite storage

### Financial Analytics

* Profitability ratios
* Leverage ratios
* Efficiency ratios
* CAGR calculations
* Cash Flow KPIs

### Stock Screener

* YAML-based configurable filters
* Six preset screeners
* Composite quality score
* Sector-aware filtering
* Financial sector D/E exception
* Debt-Free Interest Coverage handling

### Peer Analysis

* Peer group identification
* Percentile rankings
* Peer comparison report
* Radar chart visualization

---

## Outputs

### Excel Reports

* `output/screener_output.xlsx`
* `output/peer_comparison.xlsx`

### Database

* `financial_ratios`
* `peer_percentiles`

### Visual Reports

* Radar charts for companies with peer groups
* Saved under `reports/radar_charts/`

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* OpenPyXL
* Matplotlib
* PyYAML
* Pytest

---

## Testing

Run the complete test suite:

```bash
python -m pytest
```

Latest result:

* **47/47 tests passed**

---

## How to Run

Run the Screener Engine:

```bash
python src/screener/engine.py
```

Run Peer Percentile Rankings:

```bash
python src/analytics/peer.py
```

Generate Radar Charts:

```bash
python src/analytics/radar.py
```

Generate Peer Comparison Report:

```bash
python src/analytics/peer_report.py
```

---

## Deliverables

* Financial Ratio Engine
* Stock Screener
* Peer Ranking Engine
* Screener Excel Report
* Peer Comparison Excel Report
* Radar Charts
* SQLite Database
* Automated Test Suite

---

## Test Status

* Unit Tests Passed: **47/47**
* Sprint 1: Completed
* Sprint 2: Completed
* Sprint 3: Completed


# Author

**Bindu Madhavi Manthi**

Python Developer | Data Analyst

GitHub:
https://github.com/Bindu-manthi

