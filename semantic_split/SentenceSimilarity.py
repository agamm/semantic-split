from typing import List
from sentence_transformers import SentenceTransformer, util

class SentenceTransformersSimilarity():
    def __init__(self, model='all-MiniLM-L6-v2', similarity_threshold=0.2):
        self.model = SentenceTransformer(model)
        self.similarity_threshold = similarity_threshold


    def similarities(self, sentences: List[str]):
        # Encode all sentences 
        embeddings = self.model.encode(sentences)

        # Calculate cosine similarities for neighboring sentences
        similarities = []
        for i in range(1, len(embeddings)):
            sim = util.pytorch_cos_sim(embeddings[i-1], embeddings[i]).item()
            similarities.append(sim)

        return similarities
