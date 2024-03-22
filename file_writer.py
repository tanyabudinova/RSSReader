import json


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, content):
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(content, json_file, indent=4, ensure_ascii=False)
