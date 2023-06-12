### Install

1. To use most of the functionality you will need to install some pre-requisists
2. Spacy sm dataset: `python -m spacy download en_core_web_sm`

### Examples

#### Sentence Split by Semantic Similarity

```
    from semantic_split import SimilarSentenceSplitter, SentenceTransformersSimilarity, SpacySentenceSplitter

    text = """
      I dogs are amazing.
      Cats must be the easiest pets around.
      Robots are advanced now with AI.
      Flying in space can only be done by Artificial intelligence."""

    model = SentenceTransformersSimilarity()
    sentence_splitter = SpacySentenceSplitter()
    splitter = SimilarSentenceSplitter(model, sentence_splitter)
    res = splitter.split(text)
```

> **Result**: `[["I dogs are amazing.", "Cats must be the easiest pets around."], ["Robots are advanced now with AI.", "Flying in space can only be done by Artificial intelligence."]]`
