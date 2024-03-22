import json
import logging


class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
                return existing_data
        except FileNotFoundError:
            logging.info("No file to read")
            return []
