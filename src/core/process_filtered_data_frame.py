from src.core.util import datetime_to_string, non_null
from src.env.environment import CONTENT_SEPARATOR
from src.env.environment import END_BULLET
from src.env.environment import LINE_BREAK
from src.env.environment import COLUMN_INI
from src.env.environment import COLUMN_FIM
from src.env.environment import COLUMN_STA
from src.env.environment import COLUMN_END
from src.env.environment import STATUS_UNKNOWN
from src.env.environment import NOTHING_FOUND_MESSAGE


def process_df(df):
    content: str = ''
    for ini, fim, end, sta in zip(df[COLUMN_INI], df[COLUMN_FIM], df[COLUMN_END], df[COLUMN_STA]):
        process_address(end)
        content += f"Início: {datetime_to_string(ini)} - Fim: {datetime_to_string(fim)}{LINE_BREAK}"\
                   f"{LINE_BREAK}Endereços:{LINE_BREAK}{process_address(end)}{LINE_BREAK}"\
                   f"{LINE_BREAK}Status: {process_status(sta)}{LINE_BREAK}"\
                   f"{LINE_BREAK}{CONTENT_SEPARATOR}"
    if content == '':
        content = NOTHING_FOUND_MESSAGE
    return content


def process_address(end: str):
    addresses_split = end.split(LINE_BREAK)
    addresses_formatted = [f"{END_BULLET} {address.lstrip()}" for address in addresses_split]
    return f"{LINE_BREAK}".join(addresses_formatted)


def process_status(status: str):
    return status if non_null(status) else STATUS_UNKNOWN
