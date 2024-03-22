import time
import logging

from file_reader import FileReader
from file_writer import FileWriter
from in_memory_link_cache import InMemoryLinkCache
from process_rss_content import ProcessRSSContent
from url_reader import UrlReader


class App:

    def __init__(self, url, file_name, timeout):
        self.url_reader = UrlReader(url)
        self.processor = ProcessRSSContent()
        self.links_cache = InMemoryLinkCache()
        self.file_reader = FileReader(file_name)
        self.init_cache()
        self.file_writer = FileWriter(file_name)
        self.timeout = timeout

    def init_cache(self):
        existing_content = self.file_reader.read()
        links = [entry['link'] for entry in existing_content]
        self.links_cache.add_new_links(links)

    def run(self):
        while True:
            content = self.url_reader.get_content()
            if content is None:
                continue
            items = self.processor.process(content)
            new_items = [item for item in items if not self.links_cache.contains(item['link'])]
            for item in new_items:
                self.links_cache.add_new_links([item['link']])
            if new_items:
                logging.info("Writing new things")
                existing_content = self.file_reader.read()
                existing_content.extend(new_items)
                self.file_writer.write(existing_content)
            else:
                logging.info("No new data")

            time.sleep(self.timeout)
