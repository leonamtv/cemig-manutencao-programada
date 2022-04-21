import unicodedata

from src.env.environment import DATE_FORMAT, DATA_TO_EXCLUDE_IN_NON_NULL


def filter_city_name(city_name: str):
    return ''.join(c for c in unicodedata.normalize('NFD', city_name) if unicodedata.category(c) != 'Mn').upper()


def datetime_to_string(date):
    return date.strftime(DATE_FORMAT)


def non_null(data):
    return data and data is not None and str(data).lower() not in DATA_TO_EXCLUDE_IN_NON_NULL
