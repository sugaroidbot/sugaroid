

Jaccard Similarity / sigma similarity uses a simple, but less memory  intensive algorithm to analyze the statements. The equation is given as  follows 

\\[
\theta = \frac {n}{x+y}
\\]


Where n, number of common words in list x and list y, and (x+ y) shows  the union of x and y similarity.

The benefits of using Jaccard similarity is that, sugaroid can implement `can_process` methods in an object with optimal resource usage. There is no need to  use complex cosine dot product for finding similarity in cases there are only one word as list x and list y respectively. This helped to  optimize the sugaroid bot partly

Jaccard Similarity can be accessed by `sugaroid.brain.preprocessors.sigma_similarity`
