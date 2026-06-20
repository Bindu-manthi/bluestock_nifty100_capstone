def normalize_year(value):
    """
    Convert year formats into standard integer year.
    """

    if value is None:
        return None

    value = str(value).strip()

    if value.startswith("FY"):
        return int("20" + value[-2:])

    if "-" in value:
        return int("20" + value[-2:])

    return int(value)


def normalize_ticker(value):
    """
    Standardize stock ticker format.
    """

    if value is None:
        return None

    value = str(value).strip().upper()

    value = value.replace(".NS", "")

    return value