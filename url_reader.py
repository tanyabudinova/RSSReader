from __future__ import annotations

import requests


class UrlReader:
    def __init__(self, url):
        self.url = url

    def get_content(self) -> bytes | None:
        # Send a GET request to the website
        response = requests.get(self.url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch XML data from {self.url}. Status code: {response.status_code}")
            return None
