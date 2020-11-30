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


![Naive Bayers Algorithm](https://wikimedia.org/api/rest_v1/media/math/render/svg/1eaed580cf7c29f044a9e517f1cd4a7dd69c4b1f)
> **Source**: Wikipedia

The lesser complex version of the Naive Bayers Classifier is used
explicitly in Sugaroid for deriving the responses. The 
equation used, is given below

import useBaseUrl from "@docusaurus/useBaseUrl";

<link rel="stylesheet" href={useBaseUrl("katex.min.css")} />



$$
p(D|C) = \Pi_i p(\omega_i | C )
$$

where `p` is the Probability, `D|C` is the conditional probability. 

[bayers-wiki]: https://en.wikipedia.org/wiki/Naive_Bayes_classifier


