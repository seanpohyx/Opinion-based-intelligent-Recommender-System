# Opinion-based intelligent Recommender System
This is my Final Year Project(FYP) for academic year 2020/2021 in Nanyang Technological University.

## Abstract
With the recent development of Natural Language Processing (NLP), it is possible to extract sentiments from a text with given aspects. Collaborative Filtering techniques are used to recommend items to generate personalised recommendations based on similar users' preferences. Deep learning has grown popular in recent years for its immense accuracy over massive datasets. 

In this paper, we proposed to design an opinion-based intelligent recommender system utilising deep learning. This system incorporates aspect-based sentiment analysis to understand and quantify text, followed by performing collaborative filtering techniques to build a recommender system. 

For the aspect-based sentiment analysis task, it is executed by converting texts sentences into auxiliary sentences followed by classification training using Bidirectional Encoder Representations from Transformers(BERT) to quantify texts into ratings. For collaborative filtering, it is accomplished using a modified Neural Collaborative Filtering(NCF) that learns the user-item interactions by recognising the relationship between aspects and ratings to provide recommendations to different users. The results are evaluated towards the end and could be used for real-life applications.

## Knowledgements
Special thanks to Dr. Zhaoxia and Dr. Li Fang for their guidance and help throughout this entire FYP period. Without their help, this FYP would be more challenging. 

## Methodology
This FYP is separated into 2 components due to the lack of datasets. 

It consists of:
* [BERT Aspect Based Sentiment Analysis](./BERT-ABSA)
* [Neural Collaborative Filtering (NCF)](./NCF)

## My FYP
* The official Final Year Project Report for this Final Year Project can be also found in the NTU Digital Repository under the following link: 
  [Opinion-based intelligent Recommender System](https://hdl.handle.net/10356/147996)