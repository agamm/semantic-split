import pytest
from utls import load_testdata
from semantic_split import SentenceTransformersSimilarity, \
    SimilarSentenceSplitter, SpacySentenceSplitter


splitter = None

# Loading Spacy and The SentenceTransformer takes time, so we do it once for all tests.
@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    global splitter
    model = SentenceTransformersSimilarity()
    sentence_splitter = SpacySentenceSplitter()
    splitter = SimilarSentenceSplitter(similarity_model = model, 
                                       sentence_splitter=sentence_splitter)
    yield  # this is where the testing happens


def test_two_similar_sentences():

    text = """I love dogs. I love cats."""
    res = splitter.split(text)

    assert res == [["I love dogs.", "I love cats."]]

def test_similar_sentences():

    text = """I dogs are amazing. 
    Cats must be the easiest pets around. 
    Robots are advanced now with AI. 
    Flying in space can only be done by Artificial intelligence."""

    res = splitter.split(text)

    assert res == [
        ["I dogs are amazing.", 
         "Cats must be the easiest pets around."], 
        ["Robots are advanced now with AI.", 
         "Flying in space can only be done by Artificial intelligence."]]

def test_different_sentences():

    text = """I love dogs. He has flowers at home."""
    res = splitter.split(text)

    print(res)

    assert res[0][0] == 'I love dogs.'
    assert res[1][0] == 'He has flowers at home.'
    assert res == [['I love dogs.'], ['He has flowers at home.']]


def test_5th_sentences():
    text = load_testdata('sentences.txt')
    res = splitter.split(text)

    assert len(res) == 5


def test_max_group_sentences():
    text = load_testdata('sentences.txt')
    res = splitter.split(text, group_max_sentences=1)
    
    assert len(res) == 20

