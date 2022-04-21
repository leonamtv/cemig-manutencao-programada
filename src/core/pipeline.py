from src.core.city_searcher import search_for_city
from src.core.crawler import crawl_links
from src.core.download_file import get_file
from src.core.process_filtered_data_frame import process_df


def run(city_name, date_to_search=None):
    links_crawled = crawl_links()
    if len(links_crawled) > 0:
        print(process_df(search_for_city(get_file(links_crawled[0]), city_name, date_to_search)))
