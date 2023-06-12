from semantic_split import SentenceTransformersSimilarity


def test_basic_usage():

    sentence0 = "I love dogs." 
    sentence1 = "I love cats."

    model = SentenceTransformersSimilarity()
    similarities = model.similarities([sentence0, sentence1])

    assert similarities[0] - 0.7728430 < 0.0001

