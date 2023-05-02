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

(8) [ACL Conference Paper Summary:](4395ACLPaperSummary.pdf) summarize, in approximately 2 pages, a paper from the 60th annual Association for Computational Linguistics (ACL) conference
  - Paper used: Exploring and Adapting Chinese GPT to Pinyin Input Method by Tan et. al. 
    - Find it [here](https://aclanthology.org/2022.acl-long.133.pdf)
    
(9) [ChatBot:](https://github.com/kiara-aleecia/StitchyBot) create a chatbot that can discuss a topic and remember things about different users. The project includes various NLP techniques learned over the course of the semester such as text-preprocessing, term frequency measures, information retrieval techniques, etc.
  - additional contributor: [Crystal](https://github.com/cmn180003/)

(10) [Text Classification 2:](madeamtextclassification2.ipynb) find a suitable dataset for text classification and use different machine learning architectures. I chose to use a Genius lyrics dataset to create a song-genre classification model. The models should be able to predict the correct genre tag of the song. The dataset was exceedingly large and difficult to work with on my device, so I only used the first 2500 datapoints.
  - ML Architecture: RNN, CNN, various embedding approaches, etc.
  - Find the dataset [here](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information).

## Final Portfolio Wrap-Up:
An overview of what I learned this semester and potential future endeavors:
  - Technical Skills: Python and use of various Python libraries (NLTK, SpaCy, Pandas, Tensorflow, SKLearn, etc.), text processing, machine learning concepts, further experience with Git version control, and a deeper understanding of linguistics
  - Soft Skills: organization, prioritization, time and project management, flexibility for team and independent work, etc.
  - Conclusion: I believe that after this semester, I have an extensive understanding of the field of NLP and I am excited to continue exploring such an interesting crossroads of linguistics and computer science. If I could do any project, regardless of time or money, I would choose to leverage the current advancements in the field of NLP to progress the current state of language education in the United States. I would particularly focus on ways that we can more effectively teach a second language during early childhood in more schools so that a greater number of children can reap the cognitive benefits of bilingualism.
