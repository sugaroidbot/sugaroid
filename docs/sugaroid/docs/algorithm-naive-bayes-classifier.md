---
id: naive-bayer-classifier
title: Naive Bayers Classifiers
---

[Naive Bayers Classifiers][bayers-wiki] is the most 
prominent algorithm used in Sugaroid. Most responses
are classified with Naive Bayers Classifiers. Naive Bayes 
Algorithm is a linear and scalable algorithm which can guess the
most appropriate answer based on statistical probability

Sugaroid uses Naive Bayers Algorithm on a list of responses
saved as a portable SQL database; the most probable reponses 
are then filtered out using summation algorithm. Naive Bayers 
Classifiers is a light weight algorithm which uses less CPU load,
but has high memory usage. Using `mysql` instead of `sqlite3`
can however, considerably decrease memory usage sacrificing 
portability

[bayers-wiki]: https://en.wikipedia.org/wiki/Naive_Bayes_classifier


