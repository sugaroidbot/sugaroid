---
id: algorithm-cos
title: Cosine Dot Product
---

import useBaseUrl from "@docusaurus/useBaseUrl";

<link rel="stylesheet" href={useBaseUrl("katex.min.css")} />

The Sugaroid AI selectively uses Cosine Dot product for comparing  statements on the ratio of similarity and selects an appropriate  statement stored to the database. 
$$
\vec A.\vec B = ABcos\theta \\
$$

$$
\cos \theta = \frac{\vec A . \vec B}{A.B}
$$


 Words are classified as vectors in this case. Similar words are given  similar but unique vector quantity, such that only equal phrases can  have the common cosine dot product. This vector model was downloaded  from the universal `nltk.wordnet` is a collection of word and their classification

This complex collection of details helped to club similar nouns and  verbs together and provide customised answers, reduce training data and  increasing program logic. Therefore, each data was not to be separately  forced to the sugaroid bot to understand and learn but also learn the  phrases of message input by itself and store it in the SQL Database for  future reference

Cosine Dot product can be accessed within sugaroid by `sugaroid.brain.postprocessors.cosine_similarity`