from abc import ABC, abstractmethod
from typing import List


class Splitter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def split(self, text: str) -> List[str]:
        pass
