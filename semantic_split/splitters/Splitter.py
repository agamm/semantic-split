from abc import ABC, abstractmethod


class Splitter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def split(self, text: str) -> list[str]:
        pass
