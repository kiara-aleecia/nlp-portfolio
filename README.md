# nlp-portfolio
This is a portfolio for Professor Mazidi's 4395 class (spring 2023) where we will be uploading our Human Language Technologies (Natural Language Processing) assignments throughout the semester.

## Intro to NLP
[This document](kam180013portfolio0.pdf) outlines some basic information about NLP and its history as well as my own personal interest in the topic.

[This document](kam180013portfolio1.pdf) describes our first text processing assignment written in Python.

## Assignments
(1) [Text Processing:](employee.py) process and sanitize employee information in a .csv file. This assignment primarily served as a way for the class to get more comfortable with using Python.
  - additional files: [data.csv](data.csv), [employees.pickle](employees.pickle)

(2) [Word Guessing Game:](word_guess_game.py) use a .txt file along with the NLTK library to reveal insights about lexical diversity and statistics for certain parts of speech within the sample. After processing, the 50 most common nouns from the text are used to play a word guessing game.
  - additional files: [anat19.txt](anat19.txt)

(3) [WordNet:](madeamwordnet.ipynb) use the WordNet and SentiWordNet lexical database along with NLTK for sentiment analysis, semantical disambiguation, and linguistic exploration.
  - additional files: [madeamwordnet.ipynb.pdf](madeamwordnet.ipynb.pdf)
  
(4) [Ngrams:](https://github.com/cmn180003/Ngrams) gain experience creating ngrams from text, build a language model from those ngrams, and reflect on the utility of our language model. Create and use bigram and unigram dictionaries from English, French, and Italian to calculate probabilities of each language against test data.
  - additional contributor: [Crystal](https://github.com/cmn180003/)
  
(5) [Sentence Parsing:](MadeamSentenceParsing.pdf) use different methods of parsing on a sentence: "The global pandemic has forced people to adapt and find new ways to support each other." 
  - Parsers: Phrase Structure Grammar (PSG), Dependency, Semantic Role Label (SRL)
  
(6) [WebCrawler:](https://github.com/kiara-aleecia/WebCrawler) build a simple knowledge base for a chatbot after scraping >15 relevant websites for a predetermined topic. Use NLTK and RE for text processing, as well as TF-IDF to calculate and generate relevant sentences for the chatbot. This knowledge base and chatbot will be implemented in a future assignment.
  - additional contributor: [Crystal](https://github.com/cmn180003/)

(7) [Text Classification:](madeamtextclassification.ipynb) find a suitable dataset for text classification and create 3 machine learning models with sklearn. I chose to use an IMDB Reviews dataset to create a binary classification model. Reviews are classified as 0 for negative sentiment and 1 for positive sentiment. The models should be able to predict the correct sentiment label of the review.
  - ML Techniques: Naive Bayes, Logistic Regression, Neural Networks
  - Find the dataset [here](https://www.kaggle.com/datasets/yasserh/imdb-movie-ratings-sentiment-analysis?resource=download).
  - Find the post-analysis [here](4395TextClassificationAnalysis.pdf).

