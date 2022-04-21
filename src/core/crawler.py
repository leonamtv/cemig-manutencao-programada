from bs4 import BeautifulSoup
from src.env.environment import URL_BASE
from src.core.html_downloader import get_content


def crawl_links():
    html_content = get_content(url=URL_BASE)

    soup = BeautifulSoup(html_content, 'html.parser')

    link_list = [
        element['href']
        for element in soup.findAll('a')
        if element and element['href'] and 'xls' in element['href']
    ]

    return link_list
