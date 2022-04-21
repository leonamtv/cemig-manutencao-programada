HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                         'Safari/537.3'}

URL_BASE = "https://www.cemig.com.br/atendimento/aviso-de-desligamento-programado/"

PATH_DOWNLOAD = "./downloads/"

FILE_EXTENSION = "xls"
FILE_NAME_SEPARATOR = "_"
FILE_EXTENSION_SEPARATOR = "."
FILE_BASENAME = 'downloaded_sheet'

DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
LINE_BREAK = '\n'
CONTENT_SEPARATOR = '-------------------------------------------------' + LINE_BREAK
END_BULLET = '-'

COLUMN_INI = 'INÍCIO'
COLUMN_FIM = 'FIM'
COLUMN_INI_DT = 'INÍCIO_DT'
COLUMN_FIM_DT = 'FIM_DT'
COLUMN_END = 'ENDEREÇOS'
COLUMN_STA = 'Status'
COLUMN_CID = 'Cidade'


STATUS_UNKNOWN = "Status desconhecido"

DATA_TO_EXCLUDE_IN_NON_NULL = ['nan', 'none', 'null']

NO_CITY_MESSAGE = 'É necessário fornecer o nome de uma cidade!'
