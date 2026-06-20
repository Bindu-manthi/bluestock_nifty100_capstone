import sys
import os

sys.path.append(os.path.abspath("."))

from src.etl.normaliser import normalize_year, normalize_ticker


def test_fy23():
    assert normalize_year("FY23") == 2023


def test_year_range():
    assert normalize_year("2022-23") == 2023


def test_normal_year():
    assert normalize_year("2024") == 2024


def test_ticker():
    assert normalize_ticker("reliance.ns") == "RELIANCE"


def test_ticker_spaces():
    assert normalize_ticker(" tcs ") == "TCS"