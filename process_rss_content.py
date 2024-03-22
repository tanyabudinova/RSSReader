import xml.etree.ElementTree as ET
from datetime import datetime


class ProcessRSSContent:

    def process(self, content):
        root = ET.fromstring(content)
        items = []
        article = {}
        for item in root.findall('.//item'):
            link = item.find('link')
            if link is not None:
                article['link'] = link.text
            else:
                continue
            title = item.find('title')
            if title is not None:
                article['title'] = title.text
            pub_date = item.find('pubDate')
            if pub_date is not None:
                pubdate_unix = int(datetime.strptime(pub_date.text, "%a, %d %b %Y %H:%M:%S %z").timestamp())
                article['pubDate'] = pubdate_unix
            categories = item.findall('category')
            if categories:
                article['categories'] = [category.text for category in categories]
            description = item.find('description')
            if description is not None:
                article['description'] = description.text
            items.append(article)
            article = {}
        return items
