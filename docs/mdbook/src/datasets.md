# Datasets
Sugaroid's brains lies in its datasets. It might not make sense and can possibly give wrong
replies if its not trained with the default dataset. Its more like "_Artificially Foolish_"
without a dataset. 

## Prebuilt datasets
Sugaroid uses a few well known datasets which helps to increase the accuracy of natural 
language processing. These are provided and fetched by `nltk` and `spacy`, which are
popular natural language processing libraries used in Python. 

A list of datasets include
* `averaged_perceptron_tagger`
* `punkt`
* `vader_lexicon`

Some of the corpora used by `sugaroid` are
* `stopwords` corpus
* `wordnet` corpus

> **What is corpus?**
> Corpus is a text file which contains useful information which can be precisely extracted
> to get useful information. `stopwords` are words which are commonly used in English speech.
> Most of the time, `stopwords` do not contain important meanings of the statement to the 
> bot. `stopwords` give meaning to robots. Some examples of stopword are `if`, `on`, `is`,
> `are`, etc.

### Wordnet
Wordnet is a collection of arrays of words which have a unique lemma. Some words may be 
used as an exaggeration, or sometimes, the same word is used in superlative, comparative 
tones. At many times, its very useful to ignore such words and depend on the lemma (aka 
root word). Wordnet is a very interesting library that helps to make things simpler.

### Vader Lexicon
Vader Lexicon is a zipped sentiment analyzer which contains many statements with vector 
scores of a respective words. A resultant vector product is take to find out the approximate
sentiment polar score (positive or negative statment). However trained, Vader Lexicon is not
very accurate its terms, but however, it remains one of the best datasets used in sugaroid!

### Punkt
Punkt is a punctuation library used by Sugar to understand mood of a statement, i.e., 
interrogative mood, imperative mood, negation, etc.
