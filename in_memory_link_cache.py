from link_cache import LinkCache


class InMemoryLinkCache(LinkCache):

    def __init__(self):
        self.links = []

    def add_new_links(self, links):
        self.links.extend(links)

    def contains(self, link):
        return link in self.links
