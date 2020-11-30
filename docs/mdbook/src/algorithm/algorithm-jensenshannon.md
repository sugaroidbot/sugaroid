
import useBaseUrl from "@docusaurus/useBaseUrl";

<link rel="stylesheet" href={useBaseUrl("katex.min.css")} />

The [Jensen Shannon Distance](https://en.wikipedia.org/wiki/Jensen–Shannon_divergence) is the last and the complex algorithm used inside `sugaroid` bot. The equation for finding Jensen Shannon Distance is not directly  used within
$$
D(M || Q) = \sum M(i) . \log \frac {M(i)}{Q(i)} \\
$$
$$
JSD (M || Q) = \frac 12\sum ( \log(\frac {M(i)}{\frac12M(i) + Q(i)}) +  \log(\frac{Q(i)}{\frac 12 M(i) + Q(i)}))
$$
 This being a complex and CPU intensive process, is handled  systematically by a Natural Language Processing library with Industrial  Processing support, viz, SpaCy. The [SpaCy](https://github.com/srevinsaju/sugaroid/blob/430dd87fa8fd4831fc1b717676d5e8923146d020/spacy.io) library handles this effectively by loading data from `en_core_web_sm` and `en_core_web_lg`

The difference between `sm` and `lg` is that, `en_core_web_sm` is collection of all the word in the dictionary with vectors only  and weighs 7.5 MB. The `en_core_web_lg` weighs 880 MB, and has data for `tensors` too. This dataset is more efficient because, the data so obtained has  tensor data and this helps to correctly measure Jensen Shannon Distance.

The JSD is internally implemented in an `nlp` object called `LanguageProcessor` and handles most of the complex conversations inside `sugaroid.brain.utils.LanguageProcessor` is a signed class with two methods `tokenize` and `similarity` The `similarity` method return the resultant net vector displacement of the given vectors.