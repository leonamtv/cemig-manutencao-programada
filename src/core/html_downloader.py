from urllib.request import urlopen, Request
from src.env.environment import HEADERS


def get_content(url: str):
    request = Request(url=url, headers=HEADERS)
    html = urlopen(request).read()
    return str(html)
