
from .Splitter import Splitter

import spacy


class SpacySentenceSplitter(Splitter):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def split(self, text: str) -> list[str]:
        doc = self.nlp(text)
        return [str(sent).strip() for sent in doc.sents]
