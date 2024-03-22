import argparse
import time
import logging

from app import App
from file_reader import FileReader
from file_writer import FileWriter
from in_memory_link_cache import InMemoryLinkCache
from process_rss_content import ProcessRSSContent
from url_reader import UrlReader

logging.basicConfig(level=logging.DEBUG)
parser = argparse.ArgumentParser(
                    prog='RSSReader',
                    description='Reads')
parser.add_argument('url')
parser.add_argument('-f', '--file_name', default='output.json')
parser.add_argument('-t', '--timeout', type=int, default=10)
if __name__ == '__main__':
    args = parser.parse_args()
    app = App(args.url, args.file_name, args.timeout)
    app.run()
