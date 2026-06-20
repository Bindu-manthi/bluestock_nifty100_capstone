import pandas as pd

from src.etl.validator import (
    check_primary_key,
    check_company_year_uniqueness
)


def test_pk_unique():

    df = pd.DataFrame({
        "id": [1, 2, 3]
    })

    assert len(
        check_primary_key(df, "id")
    ) == 0


def test_pk_duplicate():

    df = pd.DataFrame({
        "id": [1, 1, 2]
    })

    assert len(
        check_primary_key(df, "id")
    ) > 0


def test_company_year_unique():

    df = pd.DataFrame({
        "company_id": ["ABB"],
        "year": ["2023"]
    })

    assert len(
        check_company_year_uniqueness(df)
    ) == 0