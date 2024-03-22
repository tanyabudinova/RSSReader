from abc import ABC, abstractmethod


class LinkCache(ABC):

    @abstractmethod
    def add_new_links(self, links: list[str]):
        pass

    @abstractmethod
    def contains(self, link):
        pass
