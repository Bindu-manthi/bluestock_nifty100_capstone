# Nifty100 Capstone Project

## Overview

This project implements an ETL and Data Quality Validation pipeline for Nifty100 company data.

## Technologies Used

* Python
* Pandas
* SQLite
* Pytest

## Project Structure

* data/
* db/
* src/
* tests/
* output/

## Data Quality Checks

* DQ-01 Primary Key Validation
* DQ-02 Company-Year Uniqueness
* DQ-03 Foreign Key Validation
* DQ-04 Null Value Check
* DQ-05 Negative Value Check
* DQ-06 Data Type Validation
* DQ-07 Range Validation
* DQ-08 Date Validation

## Database Tables

* companies
* profitandloss
* balancesheet
* cashflow
* analysis
* documents
* prosandcons
* financial_ratios
* peer_groups
* sectors
* stock_prices

## Results

All datasets successfully loaded into SQLite database.

Total Companies: 92

Stock Price Records: 5520

Data Quality Checks: Passed

## Author

Bindu Madhavi Manthi
