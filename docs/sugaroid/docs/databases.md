--- 
id: databases
title: Databases
---

Sugaroid uses an `sqlite3`-type database for portability. 
All the responses are explicitly saved and trained on sugaroid.
Sugaroid has two types of training:
1. Supervised training
2. Unsupervised training

## Supervised training
Supervised training is a list of proper responses, most commonly 
collected from the Stanford Question Answering Dataset (Natural)
([SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/) from Stanford NLP, attribution to Rajpurkar & Jia et al. '18). Other 
reponses are manually trained from interactions during testing.
All the responses are saved to `~/.config/sugaroid/sugaroid.db` 
which is opened in read-only mode during production mode to 
prevent people from tampering with the dataset. At local testing, 
it is possible to teach sugaroid a sequel of responses and this 
will appended to the SQL database. Using [Naive Bayers](naive-bayer-classifier) 
algorithm. 

## Unsupervised Training 
Unsupervised training are a community collected dataset. 
The sources of data, are obviously from the community, on its 
hosted [sugaroid.srevinsaju.me](https://sugaroid.srevinsaju.me) 
instance on Microsoft Azure, frontend on AWS. This data are 
also appended to the SQL database like 
[Supervised Training](#supervised-training) but they are saved 
with lesser confidence ( `0.1 * confidence_from_statement` ), as
data from community needs to undergo refining.


