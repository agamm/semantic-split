

from typing import List
from .Splitter import Splitter



class SimilarSentenceSplitter(Splitter):

    def __init__(self, similarity_model, sentence_splitter: Splitter):
        self.model = similarity_model
        self.sentence_splitter = sentence_splitter

    def split(self, text: str, group_max_sentences=5) -> List[List[str]]:
        '''
            group_max_sentences: The maximum number of sentences in a group.
        '''
        sentences = self.sentence_splitter.split(text)

        if len(sentences) == 0:
            return []

        
        similarities = self.model.similarities(sentences)

        # The first sentence is always in the first group.
        groups = [[sentences[0]]]

        # Using the group min/max sentences contraints, 
        # group together the rest of the sentences.
        for i in range(1, len(sentences)):
            if len(groups[-1]) >= group_max_sentences:
                groups.append([sentences[i]])
            elif similarities[i-1] >= self.model.similarity_threshold:
                groups[-1].append(sentences[i])
            else:
                groups.append([sentences[i]])

        return groups
