import pandas as pd


def check_primary_key(df, column):
    """
    DQ-01:
    Check primary key uniqueness.
    """

    duplicates = df[df[column].duplicated()]

    return duplicates


def check_company_year_uniqueness(df):
    """
    DQ-02:
    Check company_id + year uniqueness.
    """

    duplicates = df[
        df.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    return duplicates


def check_foreign_key(
    child_df,
    parent_df,
    child_column,
    parent_column
):
    """
    DQ-03:
    Foreign Key Integrity
    """

    errors = child_df[
        ~child_df[child_column].isin(
            parent_df[parent_column]
        )
    ]

    return errors


if __name__ == "__main__":

    # Load profit and loss data
    df = pd.read_excel(
        "data/raw/profitandloss.xlsx",
        skiprows=1
    )

    # Load companies data
    companies_df = pd.read_excel(
        "data/raw/companies.xlsx",
        skiprows=1
    )

    # DQ-01
    pk_errors = check_primary_key(
        df,
        "id"
    )

    # DQ-02
    company_year_errors = (
        check_company_year_uniqueness(df)
    )

    # DQ-03
    fk_errors = check_foreign_key(
        df,
        companies_df,
        "company_id",
        "id"
    )
    print("\nSample FK Errors:")
    print(
    fk_errors[
        ["company_id"]
    ]
    .drop_duplicates()
    .head(20)
)

    print("PK Errors:")
    print(len(pk_errors))

    print("\nFK Errors:")
    print(len(fk_errors))

    print("\nCompany-Year Errors:")
    print(len(company_year_errors))

    if len(company_year_errors) > 0:
        print(
            company_year_errors[
                ["id", "company_id", "year"]
            ]
            .sort_values(
                ["company_id", "year"]
            )
        )

    failures = []

    # DQ-02 failures
    unique_errors = company_year_errors[
        ["company_id", "year"]
    ].drop_duplicates()

    for _, row in unique_errors.iterrows():

        failures.append({
            "rule_id": "DQ-02",
            "severity": "CRITICAL",
            "table_name": "profitandloss",
            "company_id": row["company_id"],
            "year": row["year"],
            "message": "Duplicate company-year record"
        })

    # DQ-03 failures
    for _, row in fk_errors.iterrows():

        failures.append({
            "rule_id": "DQ-03",
            "severity": "CRITICAL",
            "table_name": "profitandloss",
            "company_id": row["company_id"],
            "year": row["year"],
            "message": "Foreign key violation"
        })

    failures_df = pd.DataFrame(failures)

    failures_df.to_csv(
        "output/validation_failures.csv",
        index=False
    )

    print("\nValidation file created.")