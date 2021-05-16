# Aspect Based Sentiment Analysis through the construction of Auxiliary sentences using BERT

## Citation
* [[1] C. Sun, L. Huang, and X. Qiu, "Utilizing BERT for aspect-based sentiment analysis via constructing auxiliary sentence," arXiv preprint arXiv:1903.09588, 2019.](https://arxiv.org/abs/1903.09588)

## Methodology
For the FYP, it aims to build an Opinion-based intelligent Recommender System, for the first segment, it has to be able to perform sentiment analysis from a text with a given aspect. 
In doing so, we are able to quantify text through the different polarity for each aspect and build a recommender system from it, in the next segment.
Therefore, in this segment, it repeats what the paper published by research published by C. Sun, L. Huang, and X. Qiu[1] has done by converting your text into auxiliary sentences and feed it into the BERT model. However, rather than replicating the paper, we removed conflict polarity from the dataset since it was not needed for my recommender system.
We then validated the results.

### Tasks within this segment
* BERT-Single
* BERT-QA
* BERT-NLI

## Results
For the evaluation, we used Micro-F1 score to evaluate the results since the dataset was rather imbalanced.

Tasks | Micro-F1
--- | --- 
BERT-single| 0.89 |
BERT-QA | 0.92 |
BERT-NLI | 0.92 |

## Dataset used
* Semeval 2014 restaurant reviews