import requests
import time
import os

from os import path
from src.env.environment import FILE_EXTENSION
from src.env.environment import FILE_NAME_SEPARATOR
from src.env.environment import FILE_EXTENSION_SEPARATOR
from src.env.environment import FILE_BASENAME
from src.env.environment import PATH_DOWNLOAD


def generate_name_from_timestamp(basename: str):
    stripped_timestamp = str(time.time()).split(FILE_EXTENSION_SEPARATOR)[0]
    return f"{basename}{FILE_NAME_SEPARATOR}{stripped_timestamp}{FILE_EXTENSION_SEPARATOR}{FILE_EXTENSION}"


def get_file(url: str):
    if not path.exists(PATH_DOWNLOAD):
        os.makedirs(PATH_DOWNLOAD)
    file_name = generate_name_from_timestamp(FILE_BASENAME)
    file_path = path.join(PATH_DOWNLOAD, file_name)
    response = requests.get(url)
    file_to_write = None
    try:
        file_to_write = open(file_path, 'wb')
        file_to_write.write(response.content)
    except IOError:
        print('Error while writing file')
    finally:
        file_to_write.close()

    return file_path

