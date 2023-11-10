# Semantic-Split

![semantic-split-tests](https://github.com/agamm/semantic-split/actions/workflows/python-package.yml/badge.svg)

A Python library to chunk/group your text based on semantic similarity - ideal for pre-processing data for Language Models or Vector Databases. Leverages [SentenceTransformers](https://github.com/UKPLab/sentence-transformers) and [spaCy](https://github.com/explosion/spaCy).

## Why?

1. **Better Context:** Providing more relevant context to your prompts enhances the LLM's performance ([arXiv:2005.14165](https://arxiv.org/abs/2005.14165) [cs.CL]). Semantic-Split groups related sentences together, ensuring your prompts have relevant context.

2. **Improved Results:** Short, precise prompts often yield the best results from LLMs ([arXiv:2004.04906](https://arxiv.org/abs/2004.04906) [cs.CL]). By grouping semantically similar sentences, Semantic-Split helps you craft such efficient prompts.

3. **Cost Savings:** LLMs like GPT-4 charge costs per token and have a token limit (e.g., 8K tokens). With Semantic-Split, you can make your prompts shorter and more meaningful, leading to potential cost savings.

**Real world example**:

Imagine you're building an application where users ask questions about articles:

- A. We want to only add parts in the artcile that are relevant to our query (for better results).
- B. We want to be able to query the article quickly (pre-processing).

1. We want to pre-process the article - so each query is fast (point B). So we split it into semantic chunks using `semantic-split` and store it in a [Vector DB](https://unzip.dev/0x014-vector-databases/?ref=github-semantic-split) as embeddings.
2. Each time the user asks something we calculate the embedding for their question and find the top 3 similar chunks in our Vector DB.
3. We add those 3 chunks to our pompt, to get better results for our user's questions.

As you can see, in part `1`, which involves semantic sentence splitting (grouping), is crucial. If we don't split or group the sentences semantically, we risk losing essential information. This can diminish the effectiveness of our Vector DB in identifying the most suitable chunks. Consequently, we may end up with poorer context for our prompts, negatively impacting the quality of our responses.

## Install

`python -m spacy download en_core_web_sm`  
`pip install semantic-split`

You might need to have CUDA for the `SentenceSimilarity` an easy fix is to install it via pytorch:
`pip install torch` if you have a GPU.
or (this requires python 3.8 for some reason)
`pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html` if you don't.
or `conda install cudatoolkit`

## Development

1. To use most of the functionality you will need to install some pre-requisists
2. Spacy sm dataset: `python -m spacy download en_core_web_sm`
3. `poetry install`
4. See examples

## ✂️ Splitters

### 1. Semantic Similarity

### Input

```
  I dogs are amazing.
  Cats must be the easiest pets around.
  Robots are advanced now with AI.
  Flying in space can only be done by Artificial intelligence.
```

### Output

`[ ["I dogs are amazing.", "Cats must be the easiest pets around."], `  
`["Robots are advanced now with AI.", "Flying in space can only be done by Artificial intelligence."] ]`

### Code

```python
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

## Tests

`poetry run pytest`
