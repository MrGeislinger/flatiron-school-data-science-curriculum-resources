
# Embeddings

<img src='https://developers.google.com/machine-learning/crash-course/images/linear-relationships.svg' width=100%/>

- Convert words into a vector space
    + Mathematical object
- It's all about closeness
    + Distributional Hypothesis: https://en.wikipedia.org/wiki/Distributional_semantics#Distributional_hypothesis

# Resources

- Kaggle Tutorial:  https://www.kaggle.com/learn/embeddings
- Google Embedding Crash Course: https://developers.google.com/machine-learning/crash-course/embeddings

<img src='https://developers.google.com/machine-learning/crash-course/images/EmbeddingExample3-1.svg' width=60%/>

# Word2Vec

## Skip-Gram Model

We essentially predict the words that will predict the words around it

<img src='https://adventuresinmachinelearning.com/wp-content/uploads/2017/07/Word2Vec-softmax.jpg'/>

- Train the MLP to find the best weights (context) to map word-to-word
- But since words close to another usually contain context, we're _really_ teaching it context in those weights
- Gut check: similar contexted words can be exchanged
    + EX: "A fluffy **dog** is a great pet" <--> "A fluffy **cat** is a great pet"

Each word will have a vector of contexts: the embeddings!

# GloVe - Global Vectors for Word Representation

- Create a matrix of probability of word $w_i$ occurs in **context** of word $w_j$ for whole corpus $P(i | j)$
- For each word, find  vectors when $w_i \cdot w_j = P(i|j)$
- Train to achieve good vectors

<img src='https://cdn-images-1.medium.com/max/800/1*UNtsSilztKXjLG99VXxSQw.png' />

# What Can We Do with Embeddings?

## Genism Library

- `sentences`: dataset to train on
- `size`: how big of a word vector do we want
- `window`: how many words around the target word to train with
- `min_count`: how many times the word shows up in corpus; we don't want words that are rarely used
- `workers`: number of threads (individual task "workers")


```python
from gensim.models import Word2Vec

# Let's assume we have our text corpus already tokenized and stored inside the variable 'data'--the regular text preprocessing steps still need to be handled before training a Word2Vec model!

model = Word2Vec(data, size=100, window=5, min_count=1, workers=4)

model.train(data, total_examples=model.corpus_count)
```

Can also do some interesting (fun) stuff to explore like analogies: https://www.kaggle.com/colinmorris/exploring-embeddings-with-gensim#Exploring-embeddings-with-Gensim

## Visualize with t-SNE (t-Distributed Stochastic Neighbor Embeddings)

Dimensionality reduction (like PCA)

Tries to maintain relative distances (also works for images as well as words)

Can identify relationships and bugs

**Example of t-SNE visualization:** https://www.kaggle.com/colinmorris/visualizing-embeddings-with-t-sne

## Transfer Learning

- Usually embeddings are hundreds of dimensions
- Just use the word embeddings already learned from before!
    + Unless very specific terminology, context will likely carry within language
- Comparable to CNN transfer learning
