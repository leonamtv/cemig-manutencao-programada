import datetime

import pandas as pd

from os import path

from src.core.util import filter_city_name
from src.env.environment import COLUMN_CID
from src.env.environment import COLUMN_INI
from src.env.environment import COLUMN_FIM
from src.env.environment import COLUMN_INI_DT
from src.env.environment import COLUMN_FIM_DT


def search_for_city(file_path: str, city_name: str, date_to_search: datetime.datetime = None):
    if not path.exists(file_path):
        raise IOError
    if not file_path :
        raise Exception('Undefined file path')
    df = pd.read_excel(file_path)
    new_header = df.iloc[1]
    df = df[2:]
    df.columns = new_header
    df_filtered_by_city = df.loc[df[COLUMN_CID] == filter_city_name(city_name)]
    df_filtered = df_filtered_by_city.copy()
    if date_to_search:
        date_to_search_dt = date_to_search.date()
        df_filtered[COLUMN_INI] = pd.to_datetime(df_filtered[COLUMN_INI])
        df_filtered[COLUMN_FIM] = pd.to_datetime(df_filtered[COLUMN_FIM])
        df_filtered[COLUMN_INI_DT] = df_filtered[COLUMN_INI].dt.date
        df_filtered[COLUMN_FIM_DT] = df_filtered[COLUMN_FIM].dt.date
        df_filtered = df_filtered.loc[df_filtered[COLUMN_INI_DT] <= date_to_search_dt]\
                                 .loc[date_to_search_dt <= df_filtered[COLUMN_FIM_DT]]
    return df_filtered
